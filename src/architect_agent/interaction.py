"""Architect INTERACTION binding — bind the Product agent's UX actions to real contract operations.

The Product spec declares, per screen, structured `actions` ({kind, entity}) and, per journey, the flow
and the entities it must `create`. This module BINDS each action to the code-contract operation that
realizes it (matched by CRUD kind + entity), yielding the concrete ENDPOINT the Builder must wire a control
to — turning "the storefront should let you add to cart" from an improvised guess into a checked contract.

Authority: the Architect does NOT invent operations. Where an action has no realizing operation it is
recorded as a GAP (surfaced for the Planner/human to resolve), never silently created — keeping the
pipeline's requirement-traceability intact. A journey whose `creates` entity has no bound create action is
flagged too: that is precisely the "no entity created through the UI" failure, caught at design time.

Deterministic and domain-neutral: matches on the CRUD verb (create/list/view/update/delete) and lexical,
singularised entity-token overlap between the action's entity and the operation name — no domain
vocabulary, no new operations.
"""

from __future__ import annotations

# CRUD verb tuples (mirror builder.contract_scaffold — kept local so the architect stays self-contained).
_CREATE = ("create", "add", "register", "submit", "new", "insert", "upload", "save", "store", "post",
           "generate", "make", "build", "place", "checkout", "purchase", "book", "pay")
_GET = ("get", "fetch", "retrieve", "find", "show", "read", "lookup", "resolve")
_LIST = ("list", "browse", "all", "search", "query", "index", "view")
_UPDATE = ("update", "edit", "modify", "confirm", "cancel", "approve", "reject", "set", "change",
           "associate", "assign", "toggle", "switch", "activate", "deactivate", "publish")
_DELETE = ("delete", "remove", "discard", "clear", "unregister", "revoke")

#: An action's declared kind -> the contract CRUD verb(s) that can realize it. `navigate` needs no operation.
_KIND_VERBS = {"create": {"create"}, "update": {"update"}, "delete": {"delete"},
               "list": {"list"}, "search": {"list"}, "view": {"get"}, "navigate": set()}

_STOP = {"the", "a", "an", "to", "of", "for", "by", "and", "id", "list", "all", "new", "my", "your"}


def _verb(symbol: str) -> str | None:
    head = (symbol or "").split("_")[0].lower()
    for verbs, kind in ((_CREATE, "create"), (_GET, "get"), (_LIST, "list"),
                        (_UPDATE, "update"), (_DELETE, "delete")):
        if head in verbs:
            return kind
    return None


def _sing(tok: str) -> str:
    """Crude singularisation so product/products and category/categories match (lexical, matching only)."""
    if len(tok) > 3 and tok.endswith("ies"):
        return tok[:-3] + "y"
    if len(tok) > 2 and tok.endswith("s") and not tok.endswith("ss"):
        return tok[:-1]
    return tok


def _tokens(s: str) -> set:
    return {_sing(t) for t in (s or "").lower().replace("-", "_").split("_")
            if t and t not in _STOP}


def _op_index(code_contract: dict) -> list[dict]:
    ops = []
    for key, v in (code_contract or {}).items():
        for e in (v.get("exports") or []):
            if e.get("kind") == "function" and e.get("symbol"):
                sym = e["symbol"]
                ops.append({"concept": key, "symbol": sym, "verb": _verb(sym),
                            "endpoint": f"/{key}/{sym}", "tokens": _tokens(sym)})
    return ops


def _bind_action(action: dict, ops: list[dict]) -> dict:
    kind = (action.get("kind") or "").lower()
    if kind == "navigate":
        return {"bound": True, "navigate": True}
    verbs = _KIND_VERBS.get(kind, set())
    ent = _tokens(action.get("entity"))
    scored = sorted(((len(ent & o["tokens"]), o) for o in ops if o["verb"] in verbs),
                    key=lambda x: x[0], reverse=True)
    if scored and scored[0][0] > 0:
        o = scored[0][1]
        return {"bound": True, "operation": o["symbol"], "endpoint": o["endpoint"], "concept": o["concept"]}
    return {"bound": False, "reason": f"no {kind or '?'} operation realizing entity '{action.get('entity')}'"}


def run(handover: dict, product_spec: dict | None) -> dict:
    """Bind every screen action to a contract operation and check journey create-coverage. Attaches
    `action_bindings`, `gaps`, and `journeys` to the returned review (also written onto the handover).
    Advisory to the run (never fails it); the DATA is what the Builder consumes to wire controls."""
    spec = product_spec or {}
    ops = _op_index(handover.get("code_contract") or {})
    bindings, gaps = [], []
    for s in (spec.get("screens") or []):
        for a in (s.get("actions") or []):
            if not isinstance(a, dict):
                continue
            res = _bind_action(a, ops)
            rec = {"screen": s.get("id"), "action": a.get("id"), "kind": a.get("kind"),
                   "entity": a.get("entity"), **res}
            bindings.append(rec)
            if not res.get("bound"):
                gaps.append(rec)

    by = {(b["screen"], b["action"]): b for b in bindings}

    def _entity_has_bound_create(ent: str, flow: list) -> bool:
        et = _tokens(ent)
        for f in flow:
            if not isinstance(f, dict):
                continue
            b = by.get((f.get("screen"), f.get("action")))
            if b and b.get("bound") and b.get("kind") == "create" and (et & _tokens(b.get("entity"))):
                return True
        return False

    journeys = []
    for j in (spec.get("journeys") or []):
        flow = j.get("flow") or []
        creates = j.get("creates") or []
        # PER-ENTITY coverage: EVERY entity the journey must create needs its own bound create action in the
        # flow (an "any create is bound" check would mask a second, unrealised create — e.g. cart bound, order
        # not). An unrealised create is exactly the "no entity created through the UI" failure, caught here.
        unrealised = [e for e in creates if not _entity_has_bound_create(e, flow)]
        journeys.append({"id": j.get("id"), "creates": creates,
                         "creates_all_bound": (not unrealised) if creates else None,
                         "unrealised_creates": unrealised})
        if unrealised:
            gaps.append({"journey": j.get("id"),
                         "reason": f"journey creates {unrealised} but no bound create action realises them"})

    review = {"action_bindings": bindings, "gaps": gaps, "journeys": journeys,
              "_reviewed": {"actions": len(bindings), "bound": sum(1 for b in bindings if b.get("bound")),
                            "gaps": len(gaps), "operations": len(ops)}}
    handover["interaction_review"] = review
    return review
