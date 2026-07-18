"""Generation stages — requirements in, model elements out.

Every stage follows the same shape:

    requirements (filtered by class)
      -> agent call, one requirement per call, with the authoritative name list
      -> mint returned intents into the registry
      -> structured stage output

The registry is what makes independent stateless calls agree with each other. A
stage never invents an identifier: it proposes an *intent* ("GPU cluster") and the
registry decides the name. Stage N+1 receives those names and is told to reuse them
verbatim. This is the mechanism that replaces the shared conversational context the
house pattern deliberately does not have.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

from .client import AgentClient, LLMError
from .symbols import Kind, Symbol, SymbolRegistry

#: Matches the requirements lab (`src/reqqa/jobs.py:48`). Borrowed, not tuned here.
WORKERS = 8

CLASSES = ("functional", "structural", "interface", "behavioral", "constraint", "allocation")


class ClassificationError(RuntimeError):
    """A requirement could not be classified. Fatal by policy: an unclassified
    requirement would silently vanish from the architecture, which in an INCOSE
    context is an untraceable coverage hole."""


@dataclass
class Requirement:
    """One gate-accepted requirement from the reqqa scorecard."""

    req_id: str
    text: str
    provenance: dict = field(default_factory=dict)
    lineage: dict = field(default_factory=dict)
    classes: list[str] = field(default_factory=list)
    confidence: float | None = None

    @classmethod
    def from_scorecard_entry(cls, entry: dict) -> "Requirement":
        return cls(req_id=entry["req_id"], text=entry["text"],
                   provenance=entry.get("provenance", {}),
                   lineage=entry.get("lineage", {}))


def load_scorecard(path_or_dict) -> list[Requirement]:
    """Read the Analyst Agent's scorecard. Only gate-accepted, non-duplicate
    requirements are present by the time it reaches us — reqqa filters them —
    but `duplicate_of` is re-checked because trusting an upstream invariant you
    can cheaply verify is how coverage holes appear."""
    data = path_or_dict
    if not isinstance(data, dict):
        with open(path_or_dict) as fh:
            data = json.load(fh)
    out = []
    for entry in data.get("requirements", []):
        if (entry.get("lineage") or {}).get("duplicate_of"):
            continue
        out.append(Requirement.from_scorecard_entry(entry))
    return out


# -- classification ------------------------------------------------------------

def classify(reqs: list[Requirement], client: AgentClient,
             workers: int = WORKERS) -> list[Requirement]:
    """Assign architectural classes. Per-item and order-independent, so it
    parallelises without the consistency risk that generation carries."""

    def one(req: Requirement) -> Requirement:
        data = client.complete_json(
            "architect_classifier",
            json.dumps({"req_id": req.req_id, "text": req.text}))
        classes = [c for c in data.get("classes", []) if c in CLASSES]
        if not classes:
            raise ClassificationError(
                f"{req.req_id} produced no valid class (got {data.get('classes')!r}). "
                "Refusing to drop it silently.")
        req.classes = classes
        req.confidence = data.get("confidence")
        return req

    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(one, reqs))


def _of_class(reqs: list[Requirement], cls: str) -> list[Requirement]:
    return [r for r in reqs if cls in r.classes]


# -- stages --------------------------------------------------------------------

@dataclass
class StageOutput:
    """What one generation stage produced, already reconciled with the registry."""

    symbols: list[Symbol] = field(default_factory=list)
    records: list[dict] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)


def _context(reg: SymbolRegistry, kinds: list[Kind] | None = None, limit: int = 120) -> str:
    block = reg.as_prompt_block(kinds=kinds, limit=limit)
    return f"KNOWN ELEMENTS\n{block}\n" if block else "KNOWN ELEMENTS\n(none yet)\n"


def _ask(client: AgentClient, agent: str, req: Requirement, reg: SymbolRegistry,
         kinds: list[Kind] | None = None) -> dict:
    payload = (f"{_context(reg, kinds)}\n"
               f"REQUIREMENT {req.req_id}: {req.text}")
    return client.complete_json(agent, payload)


def decompose(reqs: list[Requirement], reg: SymbolRegistry, client: AgentClient) -> StageOutput:
    """Functional decomposition → `action def`."""
    out = StageOutput()
    for req in _of_class(reqs, "functional"):
        data = _ask(client, "architect_decompose", req, reg, [Kind.ACTION_DEF])
        for fn in data.get("functions", []):
            if not fn.get("intent"):
                continue
            sym = reg.mint(fn["intent"], Kind.ACTION_DEF, req_id=req.req_id,
                           description=fn.get("description", ""))
            out.symbols.append(sym)
            out.records.append({"req_id": req.req_id, "name": sym.name,
                                "description": sym.description,
                                "parent": fn.get("parent")})
    return out


def logical(reqs: list[Requirement], reg: SymbolRegistry, client: AgentClient) -> StageOutput:
    """Logical components → `part def` plus a usage for each."""
    out = StageOutput()
    for req in _of_class(reqs, "structural"):
        data = _ask(client, "architect_logical", req, reg, [Kind.PART_DEF])
        for comp in data.get("components", []):
            if not comp.get("intent"):
                continue
            definition = reg.mint(comp["intent"], Kind.PART_DEF, req_id=req.req_id,
                                  description=comp.get("description", ""))
            usage = reg.mint(comp["intent"], Kind.PART_USAGE, req_id=req.req_id)
            attrs = []
            for a in comp.get("attributes", []):
                if not a.get("intent"):
                    continue
                asym = reg.mint(a["intent"], Kind.ATTRIBUTE, req_id=req.req_id,
                                parent=definition.name)
                attrs.append({"name": asym.name, "type": _scalar(a.get("type"))})
            out.symbols += [definition, usage]
            out.records.append({"req_id": req.req_id, "def": definition.name,
                                "usage": usage.name, "attributes": attrs,
                                "description": definition.description})
    return out


def interfaces(reqs: list[Requirement], reg: SymbolRegistry, client: AgentClient) -> StageOutput:
    """Interfaces → `port def` + `interface def`.

    An interface definition needs both ends. Where the model names an end that is
    not a registered component, the interface is still emitted but the end is
    dropped to `unresolved` — an interface with a dangling reference will not
    resolve, and losing the whole interface loses more information than losing
    one end.
    """
    out = StageOutput()
    for req in _of_class(reqs, "interface"):
        data = _ask(client, "architect_interface", req, reg, [Kind.PART_USAGE])
        out.unresolved += [f"{req.req_id}: {u}" for u in data.get("unresolved", [])]
        for iface in data.get("interfaces", []):
            if not iface.get("intent"):
                continue
            port = reg.mint(f"{iface['intent']} port", Kind.PORT_DEF, req_id=req.req_id)
            sym = reg.mint(iface["intent"], Kind.INTERFACE_DEF, req_id=req.req_id,
                           description=iface.get("description", ""))
            attrs = []
            for a in iface.get("attributes", []):
                if a.get("intent"):
                    attrs.append({"name": _identifier(a["intent"]),
                                  "type": _scalar(a.get("type"))})
            ends = []
            for role in ("supplier", "consumer"):
                name = iface.get(role)
                if name in reg:
                    ends.append({"role": role, "element": name})
                elif name:
                    out.unresolved.append(
                        f"{req.req_id}: interface {sym.name} names unknown {role} {name!r}")
            out.symbols += [port, sym]
            out.records.append({"req_id": req.req_id, "name": sym.name,
                                "port": port.name, "attributes": attrs,
                                "ends": ends, "description": sym.description})
    return out


def behavior(reqs: list[Requirement], reg: SymbolRegistry, client: AgentClient) -> StageOutput:
    """Lifecycle → `state def` with states and transitions.

    States are minted as registry symbols so they are globally unique, but they are
    emitted *inside* the state definition, so their names only need to be unique
    within it. Registering them anyway keeps traceability uniform.
    """
    out = StageOutput()
    for req in _of_class(reqs, "behavioral"):
        data = _ask(client, "architect_behavior", req, reg, [Kind.PART_USAGE])
        for machine in data.get("state_machines", []):
            if not machine.get("intent"):
                continue
            sym = reg.mint(machine["intent"], Kind.STATE_DEF, req_id=req.req_id,
                           description=machine.get("subject", ""))
            states, seen = [], {}
            for st in machine.get("states", []):
                if not st:
                    continue
                ident = _identifier(st)
                if ident not in seen:
                    seen[ident] = True
                    states.append(ident)
            transitions = []
            for tr in machine.get("transitions", []):
                src, dst = tr.get("from"), tr.get("to")
                if not src or not dst:
                    continue
                si, di = _identifier(src), _identifier(dst)
                # A transition to or from an undeclared state will not resolve.
                if si in seen and di in seen:
                    transitions.append({"from": si, "to": di,
                                        "trigger": tr.get("trigger", "")})
                else:
                    out.unresolved.append(
                        f"{req.req_id}: transition {si}->{di} references an undeclared state")
            out.symbols.append(sym)
            out.records.append({"req_id": req.req_id, "name": sym.name,
                                "subject": machine.get("subject", ""),
                                "states": states, "transitions": transitions})
    return out


def constraints(reqs: list[Requirement], reg: SymbolRegistry, client: AgentClient) -> StageOutput:
    """Measurable constraints → `constraint def`."""
    out = StageOutput()
    for req in _of_class(reqs, "constraint"):
        data = _ask(client, "architect_constraint", req, reg, [Kind.PART_DEF])
        out.unresolved += [f"{req.req_id}: {u}" for u in data.get("unquantified", [])]
        for con in data.get("constraints", []):
            if not con.get("intent"):
                continue
            sym = reg.mint(con["intent"], Kind.CONSTRAINT_DEF, req_id=req.req_id,
                           description=con.get("description", ""))
            # Constraint parameters are scoped to the constraint body, so they are
            # NOT minted through the registry: the registry exists for cross-artifact
            # consistency, and renaming these would break the model's own expression,
            # which references them by the names it chose.
            params = []
            for p in con.get("parameters", []):
                if p.get("intent"):
                    params.append({"name": _identifier(p["intent"]),
                                   "type": _scalar(p.get("type"), default="Real")})
            out.symbols.append(sym)
            out.records.append({"req_id": req.req_id, "name": sym.name,
                                "expression": con.get("expression", ""),
                                "parameters": params,
                                "category": con.get("category", "performance"),
                                "description": sym.description})
    return out


def allocations(reqs: list[Requirement], reg: SymbolRegistry, client: AgentClient) -> StageOutput:
    """Function → component allocation. Only names already in the registry are
    accepted; a hallucinated endpoint becomes an unresolved note rather than an
    allocation that will not compile."""
    out = StageOutput()
    for req in _of_class(reqs, "allocation"):
        data = _ask(client, "architect_allocation", req, reg,
                    [Kind.ACTION_DEF, Kind.PART_USAGE])
        out.unresolved += [f"{req.req_id}: {u}" for u in data.get("unallocated", [])]
        for alloc in data.get("allocations", []):
            fn, comp = alloc.get("function"), alloc.get("component")
            if fn in reg and comp in reg:
                out.records.append({"req_id": req.req_id, "function": fn,
                                    "component": comp,
                                    "rationale": alloc.get("rationale", "")})
            else:
                out.unresolved.append(
                    f"{req.req_id}: allocation references unknown element(s) "
                    f"{fn!r} -> {comp!r}")
    return out


def verification(reqs: list[Requirement], reg: SymbolRegistry,
                 client: AgentClient, workers: int = WORKERS) -> StageOutput:
    """Requirement → verification method. Per-requirement and independent."""
    out = StageOutput()

    def one(req: Requirement) -> list[dict]:
        data = _ask(client, "architect_verification", req, reg)
        return [{"req_id": req.req_id, **v} for v in data.get("verifications", [])]

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for recs in ex.map(one, reqs):
            out.records += recs
    return out


def _identifier(raw: str) -> str:
    """Sanitise a model-proposed name into a legal, non-reserved SysML identifier.
    Used only for constraint-local parameters; global names come from the registry."""
    import re as _re
    from .symbols import RESERVED as _RESERVED
    ident = _re.sub(r"[^0-9a-zA-Z_]+", "_", raw.strip()).strip("_") or "param"
    if ident[0].isdigit():
        ident = "p_" + ident
    if ident.lower() in _RESERVED:
        ident += "Param"
    return ident


_SCALARS = {"Integer", "String", "Real", "Boolean"}


def _scalar(value: str | None, default: str = "String") -> str:
    """Coerce a model-proposed type to a ScalarValues type. Anything unrecognised
    falls back rather than emitting an unresolvable reference — the validator would
    reject it, and a wrong-but-valid type is easier to spot than a build failure."""
    return value if value in _SCALARS else default
