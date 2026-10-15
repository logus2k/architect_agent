"""Architect RUNTIME-SCOPE gate — 'should this requirement become a runtime operation at all?'

The design/proportionality judges ask whether the design is sound and no more complex than needed.
Neither asks a prior question: does a requirement even describe behaviour the RUNNING APPLICATION
performs? A requirement can be perfectly real yet belong to a DIFFERENT realization surface — the
CI/CD pipeline ("perform a license-compliance scan during the build"), the build artifact ("the
container image shall not include TensorFlow"), or a dependency policy ("use components licensed under
MIT/Apache"). When the aspect designer treats such a requirement as functional, it fabricates a runtime
service with endpoints (`POST /compliance/verify_license_compliance`) that no store ever feeds — a
HOLLOW endpoint that can only ever return "unknown"/"not found". Removing the runtime crash on such an
endpoint is not a fix; the endpoint should never have been synthesized.

So we classify each requirement's REALIZATION SURFACE with a judge (semantic — the discriminator is the
sentence's SUBJECT: the running app vs the build/CI/deploy/dependency layer; not a string match), then
DECIDE IN CODE: a code-contract concept whose requirements are ALL non-runtime yields NO runtime
operations. Fail-OPEN — a requirement we cannot confidently classify counts as runtime, so a real
feature is never dropped; only a concept whose every requirement is CONFIRMED non-runtime is stripped.
The stripped requirements are recorded (never silently lost) under `non_runtime_concerns` so a later
build/CI/deploy stage can own them.

Measured 17/17 on the real Shoes-Store requirement set (the three build/CI/dependency requirements
separated from the fourteen runtime ones, keeping infra-SOUNDING but genuinely-runtime reqs — Redis
sessions, ensemble retrieval, local AI inference).

SCOPE_SYSTEM_PROMPT below is the source of truth; registered as `architect_scope_judge` in
agent_server (create/update via the admin API POST/PUT /admin/api/agents).
"""

from __future__ import annotations

SCOPE_AGENT = "architect_scope_judge"

#: The surfaces the judge may return. Exactly one is the runtime application; the rest are non-runtime
#: realization surfaces that must NOT become runtime operations. Kept in code so the decision never
#: depends on free-text the model invents.
_RUNTIME = "runtime_app"
_NON_RUNTIME = {"build_or_ci", "packaging_or_deploy", "dependency_policy"}
_VALID = {_RUNTIME, *_NON_RUNTIME}

SCOPE_SYSTEM_PROMPT = """\
You classify ONE software requirement by its REALIZATION SURFACE: WHO performs it, and WHERE.

Ask: does the RUNNING APPLICATION perform this behaviour at runtime for an end-user or client (an API call, a screen, storing/searching/displaying data, processing a payment, sending a notification)? Or is the requirement about something OTHER than the running app's runtime behaviour?

Surfaces:
- runtime_app        : the deployed application performs this at runtime for a user/client. Yields an API/UI operation.
- build_or_ci        : performed by the CI/CD pipeline or the BUILD process (a scan, a test, a check run DURING the build), not by the running app.
- packaging_or_deploy: a constraint on the built ARTIFACT or its deployment/runtime platform (the container image must/mustn't contain X; use engine Y for sessions/cache). Not an app feature.
- dependency_policy  : a constraint on WHICH components/libraries/licenses may be used. Not an app feature.

Decide by the SUBJECT of the sentence (who acts): "the system/user/customer" doing something with data at runtime => runtime_app. "The CI/CD pipeline", "the build process", "the production container image", "components licensed under..." => the non-runtime surfaces. When a requirement describes a runtime capability that merely NAMES an infrastructure technology (e.g. "use Redis to manage session data", "serve embeddings via TEI", "perform local AI inference"), the running app still performs it => runtime_app.

Output ONLY JSON: {"surface":"runtime_app|build_or_ci|packaging_or_deploy|dependency_policy","why":"<short>"}
No commentary, no markdown fences."""


def classify_requirements(req_text_by_id: dict[str, str], client) -> dict[str, str]:
    """Classify each requirement's realization surface (batch=1 — the measured-accurate mode). Returns
    {req_id: surface}. FAIL-OPEN: any requirement that errors or returns an unknown surface is treated
    as `runtime_app`, so a real feature is never dropped on a flaky classification."""
    out: dict[str, str] = {}
    for rid, text in (req_text_by_id or {}).items():
        if not (text or "").strip():
            out[rid] = _RUNTIME
            continue
        try:
            raw = client.complete_json(SCOPE_AGENT, f"REQUIREMENT:\n{text}")
            surface = str((raw or {}).get("surface", "")).strip().lower()
        except Exception:                                   # noqa: BLE001 — fail open, keep the feature
            surface = _RUNTIME
        out[rid] = surface if surface in _VALID else _RUNTIME
    return out


def _dependants(code_contract: dict, key: str) -> set[str]:
    """Concepts (other than `key`) that declare a dependency on `key`."""
    return {k for k, v in code_contract.items()
            if k != key and key in (v.get("depends_on") or [])}


def filter_contract(code_contract: dict, surfaces: dict[str, str]) -> dict:
    """Strip runtime operations from concepts whose requirements are ALL non-runtime. Mutates
    `code_contract` in place; returns a review record. A concept is stripped only when it has req_ids,
    every one is CONFIRMED non-runtime, and (for full removal) nothing else depends on it."""
    dropped_ops: list[dict] = []
    dropped_concepts: list[str] = []
    for key in list(code_contract.keys()):
        v = code_contract[key]
        reqids = v.get("req_ids") or []
        if not reqids:
            continue                                        # unattributed — keep (fail-open)
        req_surfaces = [surfaces.get(r, _RUNTIME) for r in reqids]
        if not all(s in _NON_RUNTIME for s in req_surfaces):
            continue                                        # any runtime req -> a runtime concept, keep
        fns = [e for e in (v.get("exports") or []) if e.get("kind") == "function" and e.get("symbol")]
        if fns:
            v["exports"] = [e for e in v["exports"] if e.get("kind") != "function"]
            dropped_ops.append({"concept": key, "operations": [e["symbol"] for e in fns],
                                "req_ids": reqids, "surfaces": sorted(set(req_surfaces))})
        # remove a now-empty concept only when nothing depends on it (never dangle a live dependency)
        if not (v.get("exports") or []) and not _dependants(code_contract, key):
            del code_contract[key]
            dropped_concepts.append(key)
    return {"dropped_operations": dropped_ops, "dropped_concepts": dropped_concepts}


def run(handover: dict, req_text_by_id: dict[str, str], client=None) -> dict:
    """Classify realization surface and strip runtime operations that no requirement's runtime scope
    justifies. Mutates handover['code_contract']; records the non-runtime requirements so they are not
    lost. Returns the review. Fails OPEN (no change) on classification error."""
    if client is None:
        from .client import AgentClient
        client = AgentClient()
    surfaces = classify_requirements(req_text_by_id, client)
    code_contract = handover.get("code_contract") or {}
    review = filter_contract(code_contract, surfaces)
    non_runtime = [{"req_id": rid, "surface": s, "text": req_text_by_id.get(rid, "")}
                   for rid, s in surfaces.items() if s in _NON_RUNTIME]
    handover["non_runtime_concerns"] = non_runtime
    review["non_runtime_requirements"] = [n["req_id"] for n in non_runtime]
    review["_reviewed"] = {"requirements": len(surfaces),
                           "non_runtime": len(non_runtime),
                           "runtime": sum(1 for s in surfaces.values() if s == _RUNTIME)}
    return review
