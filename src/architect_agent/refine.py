"""Built-in refine loop — critique the per-aspect design, feed findings back, converge.

The Architect owns its own quality loop (like the Analyst's refinement of below-threshold
requirements). Deterministic critique produces precise findings; this loop acts on them:

  design -> critique -> reconcile ownership -> re-critique   (bounded)
                                     -> still failing -> escalate (open issues)

Ownership reconciliation is the main content fix after inflation: when several aspects each
DEFINE the same entity, one must OWN it and the rest CONSUME it. The owner is adjudicated by
an LLM (which aspect's scope the entity belongs to); the losers are then deterministically
stripped of the entity and given it under `consumes`. Deterministic strip after a single
judgement — no oscillation.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from . import critique as critique_mod
from .aspect_design import (AspectDesign, components_by_aspect, consumes_by_aspect,
                            design_aspects, interfaces_by_aspect)
from .client import AgentClient, LLMError

ADJUDICATOR_AGENT = "architect_ownership_adjudicator"
INTERFACE_ADJUDICATOR_AGENT = "architect_interface_adjudicator"
MAX_ROUNDS = 2


@dataclass
class RefineResult:
    designs: list[AspectDesign]
    rounds: int
    open_issues: list[str] = field(default_factory=list)
    critique: critique_mod.Critique | None = None


def _glossary_def(package: dict, name: str) -> str:
    for t in package.get("glossary", []):
        if t["name"] == name:
            return t.get("definition", "")
    return ""


def reconcile_ownership(designs: list[AspectDesign], package: dict,
                        client: AgentClient) -> int:
    """Resolve every 'entity defined in >1 aspect' conflict: adjudicate one owner, strip it
    from the others (moving it to their `consumes`). Returns the number of conflicts fixed."""
    cb = {d.branch: {c["name"] for c in d.components} for d in designs}
    violations = critique_mod.ownership_violations({a: s for a, s in cb.items()})
    by_branch = {d.branch: d for d in designs}
    fixed = 0
    for f in violations:
        entity = f.subjects[0]
        claimants = [d for d in designs if any(c["name"] == entity for c in d.components)]
        payload = json.dumps({
            "entity": {"name": entity, "definition": _glossary_def(package, entity)},
            "aspects": [{"name": d.branch, "scope": d.scope} for d in claimants],
        })
        try:
            out = client.complete_json(ADJUDICATOR_AGENT, payload)
            owner = out.get("owner")
        except LLMError:
            owner = None
        if owner not in {d.branch for d in claimants}:
            owner = claimants[0].branch   # deterministic fallback: first claimant owns
        for d in claimants:
            if d.branch != owner:
                d.components = [c for c in d.components if c["name"] != entity]
                if not any(x.get("concern") == entity for x in d.consumes):
                    d.consumes.append({"concern": entity, "why": f"owned by {owner}"})
        fixed += 1
    return fixed


def _iface_purpose(designs: list[AspectDesign], name: str) -> str:
    for d in designs:
        for i in d.interfaces:
            if i.get("name") == name:
                return i.get("purpose", "")
    return ""


def _merge_interface(designs: list[AspectDesign], keep: str, drop: str) -> None:
    """Rename `drop` -> `keep` across all designs; union operations (by name) and consumers."""
    for d in designs:
        kept = next((i for i in d.interfaces if i.get("name") == keep), None)
        rest: list[dict] = []
        for i in d.interfaces:
            if i.get("name") == drop:
                if kept is None:
                    i["name"] = keep
                    kept = i
                    rest.append(i)
                else:
                    ops = {o.get("name"): o for o in kept.get("operations", [])}
                    for o in i.get("operations", []):
                        ops.setdefault(o.get("name"), o)
                    kept["operations"] = list(ops.values())
                    kept["consumers"] = sorted(set(kept.get("consumers", [])) | set(i.get("consumers", [])))
            else:
                rest.append(i)
        d.interfaces = rest


def reconcile_interfaces(designs: list[AspectDesign], package: dict,
                         client: AgentClient) -> set[tuple[str, str]]:
    """Adjudicate each near-duplicate interface pair by PURPOSE. Merge the true duplicates
    (Auth vs Auth) into one; record the false positives (Authentication vs Authorization) so
    they are NOT reported to a human. Returns the set of pairs confirmed DISTINCT."""
    crit = _run_critique(designs, package)
    dups = [f for f in crit.findings if f.kind == "near_duplicate_interface"]
    distinct: set[tuple[str, str]] = set()
    for f in dups:
        a, b = f.subjects
        payload = json.dumps({"a": {"name": a, "purpose": _iface_purpose(designs, a)},
                              "b": {"name": b, "purpose": _iface_purpose(designs, b)}})
        try:
            out = client.complete_json(INTERFACE_ADJUDICATOR_AGENT, payload)
        except LLMError:
            distinct.add(tuple(sorted((a, b))))   # can't confirm a merge -> don't force one
            continue
        if out.get("same") is True:
            keep = out.get("canonical") if out.get("canonical") in (a, b) else a
            _merge_interface(designs, keep, b if keep == a else a)
        else:
            distinct.add(tuple(sorted((a, b))))
    return distinct


def _run_critique(designs: list[AspectDesign], package: dict) -> critique_mod.Critique:
    glossary = [t["name"] for t in package.get("glossary", [])]
    return critique_mod.critique_design(
        interfaces_by_aspect=interfaces_by_aspect(designs),
        components_by_aspect=components_by_aspect(designs),
        consumes_by_aspect=consumes_by_aspect(designs),
        glossary_terms=glossary)


def refine(package: dict, client: AgentClient | None = None,
           max_rounds: int = MAX_ROUNDS) -> RefineResult:
    """Design the aspects, then critique-and-reconcile until clean or the round budget runs
    out. Remaining errors after the budget become open issues for a human."""
    client = client or AgentClient()
    designs = design_aspects(package, client)

    rounds = 0
    crit = _run_critique(designs, package)
    while rounds < max_rounds and not crit.clean:
        reconcile_ownership(designs, package, client)
        rounds += 1
        crit = _run_critique(designs, package)

    # Adjudicate near-duplicate interfaces: merge true dups, drop false positives (so a pair
    # like Authentication/Authorization never dead-ends as an open issue).
    distinct = reconcile_interfaces(designs, package, client)
    crit = _run_critique(designs, package)
    # Self-assessment: did the Architect finish its job? Flag owned entities with no attributes
    # (undefined data model), empty interfaces, and dangling attribute types. The ERROR-level
    # ones (entities with no fields) become handover open issues, so the Planner/human sees the
    # Architect's own unfinished work instead of it leaking downstream as a fabricated requirement.
    glossary_terms = [t.get("name") for t in package.get("glossary", [])
                      if isinstance(t, dict) and t.get("name")]
    crit.findings.extend(critique_mod.completeness_findings(designs, glossary_terms))
    open_issues = [f.reason for f in crit.findings
                   if f.severity == "error"
                   and not (f.kind == "near_duplicate_interface"
                            and tuple(sorted(f.subjects)) in distinct)]
    return RefineResult(designs=designs, rounds=rounds, open_issues=open_issues, critique=crit)
