"""Planner handover — a requirement-keyed index of the architecture.

The Planner plans from requirements, not from SysML, and should not have to parse
`.sysml` to find out what the system is made of. So the architecture is republished
keyed by `req_id`: the field the Planner already carries in `traces_to`.

What this deliberately does not do: decide tasks, sizing, languages, file layout or
build order. Those are the Planner's. This says only what exists and what bounds it.

Contract documented in `sdk/how_to.md`.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from .generate import Requirement, StageOutput
from .judge import Verdict
from .symbols import Kind, SymbolRegistry

CONTRACT_VERSION = "1.0"


def _snake(name: str) -> str:
    """'MatchingService' -> 'matching_service'. A convenience for the Planner's file
    naming; the authoritative field is the component name itself."""
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name)
    return re.sub(r"_+", "_", s).lower().strip("_")


def _bucket(index: dict, req_id: str, key: str) -> list:
    return index.setdefault(req_id, {}).setdefault(key, [])


def build(*, reqs: list[Requirement], reg: SymbolRegistry, manifest: dict,
          logical_out: StageOutput, functions_out: StageOutput,
          interfaces_out: StageOutput, constraints_out: StageOutput,
          allocs_out: StageOutput, behavior_out: StageOutput | None = None,
          verdicts: list[Verdict] | None = None) -> dict:
    """Assemble the handover document. Pure data assembly — no LLM calls."""
    by_req: dict[str, dict] = {}

    # Routing labels, with provenance. The Analyst documents `classes[]` as never
    # empty, but packages whose `classify:run` was not executed carry `classes: []`
    # throughout — observed on 386/386 for this project, and independently reported
    # by the Planner. Where that happens the Architect's fallback classifier fills
    # them, so downstream routing has a signal either way; `classified_by` says
    # which, because analyst-supplied labels and our fallback are not equivalent
    # evidence.
    for req in reqs:
        if req.classes:
            entry = by_req.setdefault(req.req_id, {})
            entry["classes"] = list(req.classes)
            entry["classified_by"] = req.classified_by

    for rec in logical_out.records:
        _bucket(by_req, rec["req_id"], "components").append({
            "name": rec["def"],
            "usage": rec["usage"],
            "responsibility": rec.get("description", ""),
            "attributes": rec.get("attributes") or [],
        })

    for rec in functions_out.records:
        _bucket(by_req, rec["req_id"], "functions").append({
            "name": rec["name"],
            "description": rec.get("description", ""),
        })

    for rec in interfaces_out.records:
        ends = {e["role"]: e["element"] for e in rec.get("ends") or []}
        _bucket(by_req, rec["req_id"], "interfaces").append({
            "name": rec["name"],
            "supplier": ends.get("supplier"),
            "consumer": ends.get("consumer"),
            "description": rec.get("description", ""),
        })

    for rec in constraints_out.records:
        # Only expressions that survived emission are quotable as acceptance
        # criteria; a body the emitter replaced with `true` asserts nothing.
        expr = (rec.get("expression") or "").strip()
        _bucket(by_req, rec["req_id"], "constraints").append({
            "name": rec["name"],
            "expression": expr or None,
            "category": rec.get("category", ""),
            "description": rec.get("description", ""),
        })

    for rec in allocs_out.records:
        _bucket(by_req, rec["req_id"], "allocations").append({
            "function": rec["function"],
            "component": rec["component"],
            "rationale": rec.get("rationale", ""),
        })

    for rec in (behavior_out.records if behavior_out else []):
        _bucket(by_req, rec["req_id"], "state_machines").append({
            "name": rec["name"],
            "states": rec.get("states") or [],
            "transitions": rec.get("transitions") or [],
        })

    # Every component once, so the same element is named identically wherever the
    # Planner meets it.
    components = []
    for name in reg.names(Kind.PART_DEF):
        sym = reg.get(name)
        usage = next((u for u in reg.names(Kind.PART_USAGE)
                      if reg.get(u).intent_key == sym.intent_key), None)
        components.append({
            "name": name,
            "usage": usage,
            "suggested_module": _snake(name),
            "responsibility": sym.description,
            "req_ids": list(sym.req_ids),
        })

    # Dependency edges come from declared interfaces only — never inferred. Absent
    # means no interface was modelled, not that no dependency exists.
    depends_on, seen_edges = [], set()
    for rec in interfaces_out.records:
        ends = {e["role"]: e["element"] for e in rec.get("ends") or []}
        src, dst = ends.get("consumer"), ends.get("supplier")
        if src and dst and src != dst and (src, dst) not in seen_edges:
            seen_edges.add((src, dst))
            depends_on.append({"from": src, "to": dst, "via": rec["name"]})

    open_issues = []
    for stage, kind in ((constraints_out, "unquantified_constraint"),
                        (interfaces_out, "unresolved_interface"),
                        (allocs_out, "unallocated")):
        for note in stage.unresolved:
            req_id, _, detail = note.partition(": ")
            open_issues.append({"kind": kind, "req_id": req_id.strip(),
                                "detail": detail.strip() or note})
    for v in (verdicts or []):
        if v.needs_human:
            open_issues.append({
                "kind": "semantic_defect" if v.verdict == "wrong" else "needs_review",
                "req_id": v.req_id, "element": v.element,
                "detail": v.reason, "suggested_fix": v.suggested_fix,
            })

    modelled = {r.req_id for r in reqs} & set(by_req)
    return {
        "contract_version": CONTRACT_VERSION,
        "source_package": {
            "project_id": manifest.get("project_id"),
            "project_name": manifest.get("project_name"),
            "run_id": manifest.get("run_id"),
            # Mirrored verbatim: the Planner must branch on this, not on data
            # being present. No package sets it true today.
            "architect_ready": manifest.get("architect_ready", False),
            "release_status": manifest.get("release_status"),
            "requirements_received": len(reqs),
            "requirements_modelled": len(modelled),
        },
        "classification": {
            "from_analyst": sum(1 for r in reqs if r.classified_by == "analyst"),
            "from_architect_fallback": sum(1 for r in reqs if r.classified_by == "architect"),
            "unclassified": sum(1 for r in reqs if not r.classes),
        },
        "by_requirement": by_req,
        "components": components,
        "depends_on": depends_on,
        "open_issues": open_issues,
    }


def write(doc: dict, root: str | Path) -> Path:
    path = Path(root) / "planner_handover.json"
    path.write_text(json.dumps(doc, indent=2) + "\n")
    return path
