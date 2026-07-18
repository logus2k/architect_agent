"""The Architect Agent pipeline — implementation.md §3, steps 1-7.

    load -> classify -> generate -> assemble -> VALIDATE -> render -> package

Validation is a blocking gate and sits *before* rendering: an invalid model cannot
be resolved into a diagram, so drawing precedes nothing. Nothing partial is
published — a failed gate raises and writes no package.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from . import emit, sysml
from .client import AgentClient
from .generate import (Requirement, StageOutput, allocations, classify, constraints,
                       decompose, load_scorecard, logical, verification)
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


def run(scorecard: str | Path | dict, out_dir: str | Path, *,
        package_name: str = "Architecture",
        client: AgentClient | None = None,
        review_diagrams: bool = False) -> ArchitectureResult:
    """Execute the full pipeline. Returns only on success."""
    client = client or AgentClient()
    out_dir = Path(out_dir)
    reg = SymbolRegistry()
    open_issues: list[str] = []

    # Step 1-2 — load and classify.
    reqs = load_scorecard(scorecard)
    if not reqs:
        raise GateFailure("scorecard contained no requirements")
    reqs = classify(reqs, client)
    for r in reqs:
        if r.confidence is not None and r.confidence < 0.5:
            open_issues.append(
                f"{r.req_id} classified with low confidence ({r.confidence}): {r.classes}")

    # Step 3 — generate. Order matters: logical architecture mints the component
    # names that allocation later binds to, so it must run first.
    logical_out = logical(reqs, reg, client)
    functions_out = decompose(reqs, reg, client)
    constraints_out = constraints(reqs, reg, client)
    allocs_out = allocations(reqs, reg, client)
    verify_out = verification(reqs, reg, client)
    for stage in (constraints_out, allocs_out):
        open_issues += stage.unresolved

    # Step 4 — assemble.
    model = emit.emit_model(package_name, reg, logical=logical_out,
                            functions=functions_out, constraint_defs=constraints_out,
                            allocs=allocs_out)

    # Step 5 — validate (blocking).
    result = sysml.validate(model)
    if not result.valid:
        # Regeneration is not implemented: with names owned by the registry and
        # emission deterministic, a failure here is a defect in the emitter or a
        # bad model-proposed expression, and re-running produces identical output.
        # Retrying would only hide it. See implementation.md §3 Step 5.
        raise GateFailure(
            f"model failed validation ({len(result.errors)} errors, no partial output "
            f"written):\n" + "\n".join(f"  - {e}" for e in result.errors[:10]))

    # Step 6 — render. Non-fatal: the model is already known good.
    diagrams: dict[str, bytes] = {}
    png_path = out_dir / "diagrams" / "logical_architecture.png"
    png_path.parent.mkdir(parents=True, exist_ok=True)
    render = sysml.validate(model, render_png=png_path)
    if render.render_error:
        open_issues.append(f"diagram render failed: {render.render_error}")

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
        "traceability.md": emit.traceability_md(reg),
        "interfaces.md": "# Interfaces\n\n_Interface modelling is not yet implemented._\n",
        "behavior.md": "# Behavior\n\n_Behaviour modelling is not yet implemented._\n",
    }
    artifacts["ADD.md"] = _add(package_name, reqs, reg, open_issues, artifacts)

    emit.write_package(out_dir, model=model, artifacts=artifacts, diagrams=diagrams)
    reg.save(out_dir / "symbols.json")

    return ArchitectureResult(package_dir=out_dir, model=model, registry=reg,
                              requirements=reqs, validation=result,
                              open_issues=open_issues, diagram_review=review)


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
              "", "## 5. Interfaces", "", "_Not yet implemented._",
              "", "## 6. Behavior", "", "_Not yet implemented._",
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
              "- Interface and behaviour modelling are not implemented; those "
              "sections are empty regardless of the requirements.",
              "- Diagram review, where present, is advisory: it does not gate the build.",
              "- Element names are assigned by the symbol registry, not by the model, "
              "so they are stable across regeneration.", ""]
    return "\n".join(lines)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Generate an MBSE architecture package.")
    ap.add_argument("scorecard", help="reqqa scorecard JSON")
    ap.add_argument("-o", "--out", default="architecture", help="output directory")
    ap.add_argument("-p", "--package", default="Architecture", help="SysML package name")
    ap.add_argument("--review", action="store_true", help="advisory vision review")
    args = ap.parse_args()
    try:
        res = run(args.scorecard, args.out, package_name=args.package,
                  review_diagrams=args.review)
    except GateFailure as e:
        print(f"FAILED: {e}")
        return 1
    print(f"wrote {res.package_dir} — {len(res.registry)} elements, "
          f"{len(res.requirements)} requirements, {len(res.open_issues)} open issues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
