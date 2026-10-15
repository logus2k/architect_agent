"""Planner handover from the per-aspect design.

Supersedes the old per-requirement `handover.py`. Structured by ASPECT (the Architect now
designs per aspect), but STILL keyed by `req_id` under `by_requirement` so the Planner's
existing reader (`planner_agent/src/planner/architecture.py`) joins unchanged. Adds
`by_aspect` (the natural unit for Planner epics) and the critique's open issues.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from . import capabilities
from .aspect_design import AspectDesign

CONTRACT_VERSION = "2.0"   # aspect-structured; SysML dropped


def _module(name: str) -> str:
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name)
    return re.sub(r"_+", "_", s).lower().strip("_")


# Backend-obligation stems: if an uncovered requirement's text contains a word starting with one of
# these, it DEMANDS server-side work and may NOT be treated as a non-backend deferral (fail-closed).
# Pure UI/display/infra requirements (no such verb) are legitimately deferrable. Deterministic and
# lexical — a keyword list, not a semantic judgement — so the deferral decision never drifts.
_BACKEND_STEMS = (
    "process", "stor", "validat", "persist", "email", "sav", "delet", "updat", "creat",
    "authent", "authoriz", "generat", "comput", "calculat", "send", "sent", "record", "retriev",
    "fetch", "confirm", "cancel", "submit", "regist", "upload", "download", "encrypt", "schedul",
    "notif", "payment", "charg", "invoic", "export", "aggregat", "assign", "approv", "reject",
    "publish", "archiv", "return", "quer", "verif", "hash", "token", "log",
)


def _demands_backend(text: str) -> bool:
    """True if the requirement text contains a backend-obligation verb (word-prefix match, no regex)."""
    words = "".join(c if c.isalnum() else " " for c in (text or "").lower()).split()
    return any(w.startswith(stem) for w in words for stem in _BACKEND_STEMS)


def _norm_type(t: str) -> str:
    """Normalize a declared type to Python-native syntax so opencode/pydantic accept it. Converts
    C#/Java generics (`List<Category>`) and typing forms (`Optional[Item]`, `List[X]`, `Dict[K,V]`)
    to `list[Category]`, `Item | None`, `list[X]`, `dict[K, V]`. Deterministic string ops, no regex."""
    if not isinstance(t, str) or not t.strip():
        return t
    t = t.strip().replace("<", "[").replace(">", "]")
    for a, b in (("List[", "list["), ("Dict[", "dict["), ("Set[", "set["),
                 ("Tuple[", "tuple["), ("FrozenSet[", "frozenset[")):
        t = t.replace(a, b)
    for opt in ("Optional[", "optional["):
        if t.startswith(opt) and t.endswith("]"):
            t = t[len(opt):-1].strip() + " | None"
            break
    return t


def _derive_code_contract(by_aspect: dict) -> dict:
    """The Architect's STABLE CODE CONTRACT — one canonical concept per name, its kind, and its
    public exports (symbols + signatures) — derived deterministically from the components (entities)
    and interfaces (services) already designed. This is the Architect's responsibility: the Builder
    IMPLEMENTS against this contract (maps each concept to ONE module, generates exactly these
    exports, imports by these names) instead of a per-task model INVENTING structure and names —
    which is what produced the module/package collisions and the import/export name drift.

    Stack-agnostic on purpose: it names concepts, kinds and symbols, not file paths. The Builder's
    frame maps (kind, concept) -> a concrete module path deterministically, so structure is decided
    once and the same concept never lands in two places."""
    # All component names are the "types" that count as concepts — a signature/attribute referencing
    # one of them is a cross-module DEPENDENCY the Builder must import.
    comp_names = {c["name"] for a in by_aspect.values() for c in (a.get("components") or [])
                  if c.get("name")}
    contract: dict[str, dict] = {}

    def _attach_reqs(key: str, req_ids: list) -> None:
        # A concept realizes the requirements of the aspect(s) that produced it. This is what makes
        # traceability MEASURABLE: an aspect the model silently dropped (produced no component/
        # interface) contributes no concept, so its req_ids appear in NO concept -> uncovered. This
        # is aspect-granular and derived deterministically (no model self-tagging to drift).
        if req_ids:
            cur = contract[key].setdefault("req_ids", [])
            for r in req_ids:
                if r not in cur:
                    cur.append(r)

    for a in by_aspect.values():
        areqs = a.get("req_ids") or []
        for c in (a.get("components") or []):
            name = c.get("name")
            if not name:
                continue
            key = _module(name)
            fields = [{"name": at.get("name"), "type": _norm_type(at.get("type"))}
                      for at in (c.get("attributes") or []) if at.get("name")]
            deps = {_module(f["type"]) for f in fields if f["type"] in comp_names} - {key}
            contract.setdefault(key, {
                "concept": name, "kind": "entity",
                "exports": [{"symbol": name, "kind": "class", "fields": fields}],
                "depends_on": sorted(deps)})
            _attach_reqs(key, areqs)
        for i in (a.get("interfaces") or []):
            iname = i.get("name") or ""
            svc = iname[:-len("Interface")] if iname.endswith("Interface") else iname
            if not svc:
                continue
            key = _module(svc)
            ops, deps = [], set()
            for o in (i.get("operations") or []):
                if not o.get("name"):
                    continue
                inputs = [{"name": p.get("name"), "type": _norm_type(p.get("type"))}
                          for p in (o.get("inputs") or []) if p.get("name")]
                ret = _norm_type(o.get("returns"))
                deps |= {_module(p["type"]) for p in inputs if p["type"] in comp_names}
                if ret in comp_names:
                    deps.add(_module(ret))
                ops.append({"symbol": _module(o["name"]), "kind": "function",
                            "inputs": inputs, "returns": ret})
            deps.discard(key)
            if key in contract:                     # concept already an entity — attach service ops
                contract[key].setdefault("exports", []).extend(ops)
                contract[key]["depends_on"] = sorted(set(contract[key].get("depends_on", [])) | deps)
            else:
                contract[key] = {"concept": svc, "kind": "service", "exports": ops,
                                 "depends_on": sorted(deps)}
            _attach_reqs(key, areqs)
    return contract


def build(designs: list[AspectDesign], *, package: dict,
          tree_nodes: list[dict] | None = None,
          open_issues: list[str] | None = None,
          product_spec: dict | None = None) -> dict:
    """Assemble the aspect-structured handover.

    `tree_nodes`: the Analyst tree's [{req_id, branch, tags}] — used to key elements back to
    requirements. Falls back to the package's own tree.
    `product_spec`: the Product agent's spec (surfaces/screens) — the AUTHORITATIVE signal for whether
    the app needs environment-provided authentication (a surface requiring a signed-in user), independent
    of whether the design emitted an auth verb.
    """
    nodes = tree_nodes or package.get("tree", {}).get("nodes", [])
    reqs_by_branch: dict[str, list[str]] = {}
    branch_by_req: dict[str, str] = {}
    tags_by_req: dict[str, list[str]] = {}
    for n in nodes:
        branch_by_req[n["req_id"]] = n.get("branch")
        tags_by_req[n["req_id"]] = n.get("tags", [])
        reqs_by_branch.setdefault(n.get("branch"), []).append(n["req_id"])

    by_aspect = {}
    components_global = []
    for d in designs:
        by_aspect[d.branch] = {
            "scope": d.scope,
            "req_ids": reqs_by_branch.get(d.branch, []),
            "components": d.components,
            "functions": d.functions,
            "interfaces": d.interfaces,
            "consumes": d.consumes,
        }
        for c in d.components:
            components_global.append({"name": c["name"], "owner_aspect": d.branch,
                                      "suggested_module": _module(c["name"]),
                                      "attributes": c.get("attributes", [])})

    # Cross-aspect resolution: a requirement in one aspect often USES an entity OWNED by
    # another (a public menu display consumes Menu). The owning aspect defines that entity's
    # fields; we surface them here so the Planner sees the schema even when the requirement's
    # own branch doesn't own it — otherwise the Planner asks for fields the Architect already
    # modelled elsewhere. `consumes[].concern` names the entity (or a cross-cutting tag).
    comp_by_name = {c["name"]: c for c in components_global}         # name -> {name, attributes, ...}
    resp_by_name: dict[str, str] = {}
    for d in designs:
        for c in d.components:
            if c.get("name"):
                resp_by_name.setdefault(c["name"], c.get("responsibility", ""))

    # req_id -> its aspect's elements, so the Planner joins on req_id as before.
    by_requirement = {}
    design_by_branch = {d.branch: d for d in designs}
    for req_id, branch in branch_by_req.items():
        d = design_by_branch.get(branch)
        if not d:
            continue
        own_names = {c["name"] for c in d.components if c.get("name")}
        # Entities this aspect CONSUMES from other aspects — resolve each to its owning
        # component (with the real attributes) so the requirement carries that schema too.
        consumed = []
        for con in (d.consumes or []):
            name = con.get("concern")
            gc = comp_by_name.get(name)
            if gc and name not in own_names:
                consumed.append({"name": gc["name"],
                                 "suggested_module": gc["suggested_module"],
                                 "responsibility": resp_by_name.get(name, ""),
                                 "attributes": gc.get("attributes", []),
                                 "consumed": True})
        # Per the handover contract (sdk/how_to.md §3), by_requirement elements are OBJECTS,
        # not bare names — the Planner's reader joins on `.name` / `.suggested_module` /
        # `.responsibility` / `.supplier` / `.consumer`. Emitting strings crashes it.
        by_requirement[req_id] = {
            "aspect": branch,
            "tags": tags_by_req.get(req_id, []),
            "components": [{"name": c["name"],
                            "suggested_module": _module(c["name"]),
                            "responsibility": c.get("responsibility", ""),
                            "attributes": c.get("attributes", [])} for c in d.components]
                          + consumed,
            "functions": [{"name": f["name"]} for f in d.functions],
            "interfaces": [{"name": i["name"],
                            "supplier": branch,
                            "consumer": ", ".join(i.get("consumers", []) or [])}
                           for i in d.interfaces],
        }

    code_contract = _derive_code_contract(by_aspect)

    # ENVIRONMENT-PROVIDED CAPABILITIES (deterministic invariant): authentication is provided by the
    # shared oauth2-proxy, so the app builds NONE of it — strip any app-implemented auth operations the
    # designer emitted (login/sign_in/validate_session/...), regardless of naming. Generic + measured to
    # not touch domain nouns. The wiring obligation is recorded for the deploy/backend stages.
    code_contract, _removed_auth = capabilities.strip_app_auth(code_contract)
    _auth_obligation = capabilities.auth_obligation(_removed_auth, product_spec=product_spec)

    # APPLIED CONSTRAINTS: carry the Analyst's per-requirement non-functional constraints onto the
    # concept that realizes them, so the Builder sees them verbatim (they were previously dropped).
    constr_by_req = {r["req_id"]: (r.get("constraints") or [])
                     for r in package.get("requirements", []) if r.get("req_id")}
    for v in code_contract.values():
        ac = []
        for rid in (v.get("req_ids") or []):
            for c in constr_by_req.get(rid, []):
                if c not in ac:
                    ac.append(c)
        if ac:
            v["applied_constraints"] = ac

    # COMPLETENESS GATE (traceability): every requirement must be realized by some contract concept
    # OR verifiably deferred. `req_ids` are attached to concepts deterministically from the aspect
    # that produced them, so a requirement is UNCOVERED exactly when its aspect produced no concept
    # (the "silently dropped design" failure). Uncovered requirements are error-level and make the
    # handover NOT architect_ready — an incomplete design never ships to the Builder as if complete.
    texts = {r["req_id"]: r.get("text", "") for r in package.get("requirements", []) if r.get("req_id")}
    all_reqs = list(texts)
    covered = set()
    for v in code_contract.values():
        covered |= set(v.get("req_ids") or [])
    # Split the not-realized requirements: a legitimate DEFERRAL (pure UI/display/infra — no backend
    # verb) is acceptable and counts as handled; a real GAP (uncovered AND demands backend work) is an
    # error that blocks the handover. Fail-closed: anything ambiguous demands backend -> a real gap.
    uncovered = [r for r in all_reqs if r not in covered]
    deferred = [{"req_id": r, "target": "frontend_or_infra", "text": texts[r]}
                for r in uncovered if not _demands_backend(texts[r])]
    real_gaps = [r for r in uncovered if _demands_backend(texts[r])]
    # Open issues are STRUCTURED — the Planner filters them by the requirement they
    # touch, and a bare sentence carries no such handle. One unmodeled-requirement
    # issue names MANY requirements, so it carries `req_ids` (all of them) alongside
    # `req_id` (the first), rather than being flattened into prose the consumer has
    # to parse back out.
    issues = list(open_issues or [])
    if real_gaps:
        issues.append({
            "kind": "unmodeled_requirement",
            "severity": "error",
            "reason": (f"{len(real_gaps)} backend requirement(s) not realized by any "
                       f"contract concept: {real_gaps[:12]}"),
            "req_ids": list(real_gaps),
            "req_id": real_gaps[0],
            "subjects": list(real_gaps[:12]),
        })
    manifest = package.get("manifest", {})
    architect_ready = bool(manifest.get("architect_ready", False)) and not real_gaps
    traceability = {"total": len(all_reqs), "covered_by_concept": len(covered),
                    "deferred": len(deferred), "real_gaps": real_gaps,
                    "traceable": not real_gaps}
    return {
        "contract_version": CONTRACT_VERSION,
        "source_package": {
            "project_id": manifest.get("project_id"),
            "project_name": manifest.get("project_name"),
            "architect_ready": architect_ready,
            "requirements_received": len(package.get("requirements", [])),
            "aspects": len(designs),
        },
        "by_aspect": by_aspect,
        "by_requirement": by_requirement,
        "components": components_global,
        # STABLE CODE CONTRACT (concept -> kind + public exports). The Builder implements against
        # this instead of inventing structure/names — preventing collisions and import/export drift.
        "code_contract": code_contract,
        # Capabilities the ENVIRONMENT provides (app builds nothing; the pipeline wires them).
        "environment_capabilities": [_auth_obligation] if _auth_obligation else [],
        "deferred_concerns": deferred,
        "traceability": traceability,
        "open_issues": issues,
    }


def write(doc: dict, root: str | Path) -> Path:
    path = Path(root) / "planner_handover.json"
    path.write_text(json.dumps(doc, indent=2) + "\n")
    return path
