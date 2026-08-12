# Factory Remediation Plan — Architect & Builder

**Goal.** Close the pending issues in the Architect and Builder so the pipeline delivers a
**coherent, booting, serving, route-complete, requirement-traceable, no-ORM application whose
structure and interfaces are correct by construction**, with every requirement either built or
verifiably deferred.

**Explicit non-goal / ceiling.** Guaranteeing that each endpoint *body* behaves exactly per its
requirement is **not** in scope — that is bounded by the local model (Gemma-4). The plan guarantees
every endpoint **exists, imports, and is reachable**; body quality is as good as the model fills it.

**Discipline (the real risk is process, not design).** Every phase is gated by a **measured
acceptance test**. Nothing is "done" without a green measurement. Deterministic-first: the model is
used only where judgement is genuinely required, and every model output is verified/guarded
deterministically. On any failure: capture the real cause by measurement, never a narrative.

---

## Phase 0 — Fixed acceptance harness (the scoreboard)

**Change.** One reproducible script, `builder_agent/scripts/acceptance.py`, that takes a project id,
builds a throwaway venv from the code's manifest, and reports **green/red** for each:

| Check | Pass condition |
|---|---|
| coherence | `heal.detect(...)` returns 0 issues |
| boots | `import <entrypoint>` succeeds |
| serves | uvicorn starts and `/openapi.json` returns 200 |
| routes | `len(app.routes)` ≥ number of contract services |
| no-ORM | 0 files import `sqlalchemy`/`declarative_base` |
| traceable | every requirement `req_id` is covered by a built element or a verified deferral |

**Acceptance:** the harness runs against the current `code/` and prints a per-criterion scoreboard.
This is the single definition of "done"; all later phases are measured by it.

---

## Phase 1 — Architect completeness gate (fixes the ~2/60 coverage failure)

**Changes.**
1. **Per-element `req_ids`.** `architect_aspect_designer` emits, for each component/function/
   interface, the `req_ids` it realizes (schema + persona change).
2. **`deferred_concerns`** on `AspectDesign`: `{name, target, responsibility, req_ids}` for
   requirements that are genuinely not backend (UI, external human process, client state).
3. **Verified deferral guard (deterministic).** A `frontend_client` deferral is *rejected* if the
   requirement text contains a backend-obligation verb (process/store/validate/persist/return/
   email/discard-server-side); such a requirement is forced back to a backend element. (REQ-0004
   "discard the contact form submission after processing" must fail as a frontend deferral.)
4. **Completeness gate in `refine`.** `covered = ∪ element.req_ids ∪ verified_deferred.req_ids`.
   If a branch's assigned `req_ids ⊄ covered`, emit an **error-level** `unmodeled_requirement`
   finding and regenerate the aspect with the uncovered requirements as explicit constraints
   (bounded rounds). Surviving uncovered requirements make the run `architect_ready: false`.

**Acceptance:** on the Restaurant project, the coverage report shows every `req_id` covered or
verified-deferred; a synthetic mis-deferral of REQ-0004 is refused.

---

## Phase 2 — Architect expressiveness (whole-stack contract)

**Changes.**
1. **Delivery layer in `code_contract`.** Each service interface also yields a `router` element
   (endpoints), so the contract covers entities + services + endpoints — not just the backbone.
2. **`applied_constraints`.** Attach the Analyst's per-requirement `constraints` to the relevant
   contract concept, verbatim, so non-functional requirements reach the Builder.
3. **Deterministic type normalizer.** Convert `List<Category>` → `list[Category]`,
   `Optional[Item]`/`Optional<Item>` → `Item | None`, etc., before the handover is written.

**Acceptance:** `code_contract` covers entities + services + endpoints with Python-native types;
scaffolding it (Phase 3 tooling) yields 0 coherence issues, boots, and routes == services.

---

## Phase 3 — Builder: coherent-by-construction, minimal model, guarded

**Changes.**
1. **Full-structure scaffold** from the contract (models + services + routers + main) — proven this
   session to yield 0 coherence + boots + routes in isolation.
2. **Body fill** by the model on the scaffolds (interface-preserving instruction).
3. **Conformance guards run LAST** (after heal): restore any dropped contract export; re-assert the
   routers + entrypoint; re-scaffold any contract module the model left unparseable.
4. **Heal reduced to a bounded deterministic sweep** (imports/aliases/collisions only) — no
   unbounded model-repair loop. This removes both the oscillation and the per-call opencode cost.
5. **No-ORM enforced** via the Phase-1-stabilized `stack_policy` + conformance rejection.

**Acceptance (Phase-0 harness, fresh clean run):** coherence 0, boots, serves, routes == services,
0 ORM.

---

## Phase 4 — Hygiene

**Changes.** Delete the dead SysML pipeline (`pipeline.py`, `handover.py`@1.0, `generate.py`,
`emit.py`, `sysml.py`, `symbols.py`); update the two spec docs.

**Acceptance:** service still starts; no dead imports; docs match the live path.

---

## Definition of done (measured by Phase 0)

A fresh end-to-end run (Architect → Builder) produces `code/` for which the acceptance harness is
**green on**: coherence, boots, serves, routes==services, no-ORM, and requirement-traceability
(every requirement built or verified-deferred). Endpoint *behaviour* fidelity is explicitly out of
scope (model-bounded) and reported separately, not gated.
