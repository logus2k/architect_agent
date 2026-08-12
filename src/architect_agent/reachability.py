"""Architect ENDPOINT-REACHABILITY review — deterministic, advisory.

`design_judge` checks design coherence; the coverage check confirms a requirement is *present* in
some concept. Neither asks the harder question the Reservation case exposed: can every behavioural
requirement actually be ACTED ON — is there a callable OPERATION for it, and will that operation be
REACHABLE (routed to an endpoint) in the built app?

Two failure modes this catches, both kind-agnostic (the concept's `kind` label is advisory, never the
authority — routability follows CONTENT, i.e. whether a concept exports operations):

  1. OPERATION ON A NON-SERVICE CONCEPT — a concept exports FUNCTIONS (operations) but is typed
     `entity`, so a router that gates on kind=="service" silently drops them. This is exactly the
     Reservation case: `submit_reservation` lived on the `reservation` entity and was never routed.
     The Builder now routes by function-export (not by kind), so these ARE reachable — but the review
     SURFACES them so the mis-typing is visible at design time instead of only showing up as a dead UI.

  2. ASPECT WITH NO OPERATIONS — an aspect has requirements but designs only data (components/
     entities) and NO interface/operation anywhere. Any behavioural requirement in it is unreachable:
     there is no operation to call. Flagged for confirmation (a purely-informational aspect is fine).

Deterministic (no model, no regex): reads the handover's `code_contract` + `by_aspect`. ADVISORY, not
a gate. Emitted in the handover as `reachability_review`.
"""

from __future__ import annotations


def _operations(concept: dict) -> list[dict]:
    """The concept's OPERATIONS — function exports with a symbol. Class exports (data models) are not
    operations and are never routed."""
    return [e for e in (concept.get("exports") or [])
            if e.get("kind") == "function" and e.get("symbol")]


def run(handover: dict) -> dict:
    """Reachability verdict over the code_contract. Returns a report; never raises."""
    contract = handover.get("code_contract") or {}
    by_aspect = handover.get("by_aspect") or {}

    routes: list[str] = []                       # every operation the Builder will route
    non_service_ops: list[dict] = []             # operations carried by a non-service concept
    op_req_ids: set[str] = set()                 # req_ids carried by any operation-bearing concept
    for key, v in contract.items():
        ops = _operations(v)
        if not ops:
            continue
        op_req_ids |= set(v.get("req_ids") or [])
        for e in ops:
            routes.append(f"/{key}/{e['symbol']}")
            if v.get("kind") != "service":
                non_service_ops.append({"path": f"/{key}/{e['symbol']}",
                                        "concept": key, "kind": v.get("kind")})

    # Aspect actionability: an aspect can act iff one of its requirements is carried by an
    # operation-bearing concept. req_ids are attached aspect-granularly, so this is aspect-level.
    aspects: dict[str, dict] = {}
    no_operation_aspects: list[str] = []
    for name, a in by_aspect.items():
        reqs = set(a.get("req_ids") or [])
        has_ops = bool(reqs & op_req_ids)
        aspects[name] = {"requirements": len(reqs), "has_operations": has_ops}
        if reqs and not has_ops:
            no_operation_aspects.append(name)

    # Every function export is routed by the Builder (kind-agnostic), so nothing is unroutable by
    # construction; the review still reports non-service operations so the mis-typing is visible, and
    # flags aspects that design no operation at all.
    reachable = not no_operation_aspects
    return {
        "reachable": reachable,
        "routes": len(routes),
        "operations_on_non_service_concepts": non_service_ops,
        "aspects": aspects,
        "aspects_without_operations": sorted(no_operation_aspects),
        "note": ("Advisory. `operations_on_non_service_concepts` are reachable (the Builder routes by "
                 "function-export, not by kind) but reveal a concept that owns operations yet is typed "
                 "as data. `aspects_without_operations` design no callable operation — confirm none of "
                 "their requirements need a user-triggered action, else the aspect needs an interface."),
    }
