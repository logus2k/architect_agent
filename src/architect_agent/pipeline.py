"""The Architect Agent pipeline — implementation.md §3, steps 1-7.

    load -> classify -> generate -> assemble -> VALIDATE -> render -> package

Validation is a blocking gate and sits *before* rendering: an invalid model cannot
be resolved into a diagram, so drawing precedes nothing. Nothing partial is
published — a failed gate raises and writes no package.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path

from . import emit, handover, sysml
from .client import AgentClient
from . import judge as judge_mod
from .generate import (Requirement, StageOutput, allocations, behavior, classify,
                       constraints, decompose, interfaces, load_package, logical,
                       verification)
from .symbols import SymbolRegistry

#: Borrowed from the requirements lab's refine gate (`max_iters=3`); never tuned
#: for this pipeline. See implementation.md §3 Step 5.
MAX_REGENERATION_ATTEMPTS = 3


class GateFailure(RuntimeError):
    """The model did not validate within the attempt budget. Deliberately fatal:
    publishing an invalid architecture is worse than failing the run."""


@dataclass
class ArchitectureResult:
    package_dir: Path
    model: str
    registry: SymbolRegistry
    requirements: list[Requirement]
    validation: sysml.ValidationResult
    open_issues: list[str] = field(default_factory=list)
    diagram_review: dict | None = None
    judge_verdicts: list = field(default_factory=list)


#: Where architecture packages are published. A bind-mounted directory, so the
#: Planner can read a package without the Architect exposing a service. Keyed by
#: the Analyst project id, which is also the Planner's project key.
PUBLISH_ROOT = Path(os.environ.get("ARCHITECT_DATA_DIR", "data")) / "architecture"


def publish_path(project_id: str) -> Path:
    """Stable location for a project's architecture package."""
    return PUBLISH_ROOT / project_id


def run(scorecard: str | Path | dict, out_dir: str | Path | None = None, *,
        package_name: str = "Architecture",
        client: AgentClient | None = None,
        review_diagrams: bool = False,
        require_ready: bool = False,
        limit: int | None = None) -> ArchitectureResult:
    """Execute the full pipeline. Returns only on success.

    `require_ready` enforces the Analyst's `manifest.architect_ready` flag. It
    defaults to False because no package sets it today (the release gate is not
    built upstream), so demanding it would block every run. Turn it on once the
    Analyst's sign-off state machine exists.
    """
    client = client or AgentClient()
    reg = SymbolRegistry()
    open_issues: list[str] = []

    # Step 1-2 — load and classify.
    reqs, manifest = load_package(scorecard)
    if not reqs:
        raise GateFailure("package contained no requirements")
    # Default to the published location keyed by project id, so consumers have a
    # path they can predict rather than one that has to be communicated.
    out_dir = Path(out_dir) if out_dir else publish_path(
        manifest.get("project_id") or "unknown")
    if manifest:
        ready = manifest.get("architect_ready")
        blockers = manifest.get("blockers") or []
        if require_ready and not ready:
            raise GateFailure("package is not architect_ready: " + "; ".join(blockers))
        if not ready:
            open_issues.append(
                "Analyst package is not architect_ready ("
                + (manifest.get("release_status") or "unknown") + "): "
                + "; ".join(blockers[:3]))
    if limit:
        reqs = reqs[:limit]

    # Requirements the Analyst has flagged for a human, or rewritten, are still
    # modelled — but never silently. Consuming an unapproved or reworded
    # requirement without saying so is how an architecture ends up traceable to
    # text nobody signed off.
    pending = [r.req_id for r in reqs if r.status == "needs_human"]
    if pending:
        open_issues.append(
            f"{len(pending)} requirement(s) awaiting human approval were modelled "
            f"anyway: {', '.join(pending[:8])}"
            + (" ..." if len(pending) > 8 else ""))
    refined = [r.req_id for r in reqs if r.text_changed]
    if refined:
        open_issues.append(
            f"{len(refined)} requirement(s) were refined upstream; the architecture "
            f"derives from the rewritten text, not the source document wording: "
            + ", ".join(refined[:8]) + (" ..." if len(refined) > 8 else ""))
    reqs = classify(reqs, client)
    for r in reqs:
        if r.confidence is not None and r.confidence < 0.5:
            open_issues.append(
                f"{r.req_id} classified with low confidence ({r.confidence}): {r.classes}")

    # Step 3 — generate. Order matters: logical architecture mints the component
    # names that allocation later binds to, so it must run first.
    logical_out = logical(reqs, reg, client)
    functions_out = decompose(reqs, reg, client)
    interfaces_out = interfaces(reqs, reg, client)
    behavior_out = behavior(reqs, reg, client)
    constraints_out = constraints(reqs, reg, client)
    allocs_out = allocations(reqs, reg, client)
    verify_out = verification(reqs, reg, client)
    for stage in (interfaces_out, behavior_out, constraints_out, allocs_out):
        open_issues += stage.unresolved

    # Step 4 — assemble.
    model = emit.emit_model(package_name, reg, logical=logical_out,
                            functions=functions_out, constraint_defs=constraints_out,
                            allocs=allocs_out, interfaces_out=interfaces_out,
                            behavior_out=behavior_out)

    # Step 5+6 — validate (blocking) AND render, in ONE JVM call. The Java tool
    # only renders when the model is valid, so passing render_png here is safe and
    # avoids a second ~1.7s standard-library load. An invalid model still writes no
    # diagram and fails the gate below.
    diagrams: dict[str, bytes] = {}
    png_path = out_dir / "diagrams" / "logical_architecture.png"
    png_path.parent.mkdir(parents=True, exist_ok=True)
    result = sysml.validate(model, render_png=png_path)
    if not result.valid:
        # Regeneration is not implemented: with names owned by the registry and
        # emission deterministic, a failure here is a defect in the emitter or a
        # bad model-proposed expression, and re-running produces identical output.
        # Retrying would only hide it. See implementation.md §3 Step 5.
        raise GateFailure(
            f"model failed validation ({len(result.errors)} errors, no partial output "
            f"written):\n" + "\n".join(f"  - {e}" for e in result.errors[:10]))
    if result.render_error:
        open_issues.append(f"diagram render failed: {result.render_error}")

    # Semantic review: the validator proved the model resolves, not that it means
    # the right thing. Judge first; anything wrong or undecided goes to a human.
    verdicts = judge_mod.review(reqs, constraints_out=constraints_out,
                                allocs_out=allocs_out, behavior_out=behavior_out,
                                client=client)
    open_issues += judge_mod.escalations(verdicts)

    review = None
    if review_diagrams and png_path.exists():
        from .vision_review import review_diagram
        try:
            rev = review_diagram(png_path, f"the logical architecture of {package_name}")
            review = {"matches": rev.matches, "reason": rev.reason}
            issue = rev.as_open_issue("logical architecture")
            if issue:
                open_issues.append(issue)
        except Exception as e:  # advisory only — never fails the run
            open_issues.append(f"diagram review unavailable: {e}")

    # Step 7 — package.
    artifacts = {
        "functional_decomposition.md": emit.functional_decomposition_md(functions_out),
        "logical_architecture.md": emit.logical_architecture_md(logical_out),
        "constraints.md": emit.constraints_md(constraints_out),
        "allocations.md": emit.allocations_md(allocs_out),
        "verification_plan.md": emit.verification_plan_md(verify_out),
        "traceability.md": emit.traceability_md(reg, reqs),
        "interfaces.md": emit.interfaces_md(interfaces_out),
        "behavior.md": emit.behavior_md(behavior_out),
    }
    artifacts["ADD.md"] = _add(package_name, reqs, reg, open_issues, artifacts)

    emit.write_package(out_dir, model=model, artifacts=artifacts, diagrams=diagrams)
    reg.save(out_dir / "symbols.json")

    # Requirement-keyed index for the Planner (sdk/how_to.md). Published alongside
    # the model so the Planner never has to parse SysML.
    handover_doc = handover.build(
        reqs=reqs, reg=reg, manifest=manifest, logical_out=logical_out,
        functions_out=functions_out, interfaces_out=interfaces_out,
        constraints_out=constraints_out, allocs_out=allocs_out,
        behavior_out=behavior_out, verdicts=verdicts)
    handover.write(handover_doc, out_dir)

    return ArchitectureResult(package_dir=out_dir, model=model, registry=reg,
                              requirements=reqs, validation=result,
                              open_issues=open_issues, diagram_review=review,
                              judge_verdicts=verdicts)


def _add(package: str, reqs: list[Requirement], reg: SymbolRegistry,
         open_issues: list[str], artifacts: dict[str, str]) -> str:
    """Architecture Definition Document (technical_architecture.md §8.8).

    Assembled deterministically from the other artifacts. It introduces no new
    architectural content — that is the rule the section states, and generating
    prose here with an LLM would quietly break it.
    """
    by_class: dict[str, int] = {}
    for r in reqs:
        for c in r.classes:
            by_class[c] = by_class.get(c, 0) + 1

    lines = [
        f"# Architecture Definition Document — {package}", "",
        "## 1. Introduction", "",
        f"This document describes the architecture of {package}, derived from "
        f"{len(reqs)} INCOSE-validated requirements supplied by the Analyst Agent. "
        "It is generated from the architecture artifacts and introduces no content "
        "of its own.", "",
        "## 2. Requirements Summary", "",
        f"- Requirements consumed: **{len(reqs)}**",
    ]
    for cls, n in sorted(by_class.items()):
        lines.append(f"- Classified `{cls}`: {n}")
    sources = sorted({(r.provenance or {}).get("source_file", "") for r in reqs} - {""})
    if sources:
        lines += ["", "Source documents:"] + [f"- `{s}`" for s in sources]

    lines += ["", "## 3. Functional Architecture", "",
              artifacts["functional_decomposition.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 4. Logical Architecture", "",
              artifacts["logical_architecture.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 5. Interfaces", "",
              artifacts["interfaces.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 6. Behavior", "",
              artifacts["behavior.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 7. Constraints", "",
              artifacts["constraints.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 8. Allocation", "",
              artifacts["allocations.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 9. Verification Approach", "",
              artifacts["verification_plan.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 10. Traceability", "",
              artifacts["traceability.md"].split("\n", 2)[2].strip() or "_None._",
              "", "## 11. Assumptions and Open Issues", ""]
    if open_issues:
        lines += [f"- {i}" for i in open_issues]
    else:
        lines.append("_No open issues recorded._")
    lines += ["", "### Known limitations of this generator", "",
              "- Semantic review is performed by a judge agent; anything it marks "
              "wrong or cannot decide is listed above for human sign-off. An empty "
              "list means the judge approved, not that a human did.",
              "- Diagram review, where present, is advisory: it does not gate the build.",
              "- Element names are assigned by the symbol registry, not by the model, "
              "so they are stable across regeneration.", ""]
    return "\n".join(lines)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Generate an MBSE architecture package.")
    ap.add_argument("scorecard", help="reqqa scorecard JSON")
    ap.add_argument("-o", "--out", default=None,
                    help="output directory (default: data/architecture/<project_id>)")
    ap.add_argument("-p", "--package", default="Architecture", help="SysML package name")
    ap.add_argument("--review", action="store_true", help="advisory vision review")
    ap.add_argument("--limit", type=int, default=None,
                    help="model only the first N requirements")
    args = ap.parse_args()
    try:
        res = run(args.scorecard, args.out, package_name=args.package,
                  review_diagrams=args.review, limit=args.limit)
    except GateFailure as e:
        print(f"FAILED: {e}")
        return 1
    from . import judge as _j
    counts = _j.summary(res.judge_verdicts)
    print(f"wrote {res.package_dir} — {len(res.registry)} elements, "
          f"{len(res.requirements)} requirements, {len(res.open_issues)} open issues")
    print(f"judge: {counts['ok']} ok, {counts['wrong']} wrong, "
          f"{counts['uncertain']} uncertain"
          + (" -> HUMAN REVIEW REQUIRED" if counts['wrong'] or counts['uncertain'] else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
