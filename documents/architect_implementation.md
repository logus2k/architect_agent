# Architect Agent — Implementation & Internal Workflow

**Purpose.** A precise technical description of *how the Architect Agent is implemented and what it
does internally*, for reconstruction/hand-off. Every statement below was read from the live source
in `src/architect_agent/` this session (not from memory); where something is advisory vs. gating,
or a recent addition vs. established, it is called out.

---

## 1. Role, service, chain position

- **Service:** `architect-agent`, HTTP on **`:7804`**. Job-oriented, mirroring the Analyst
  (`api.py`): `POST /projects/{pid}/architect:run` → `{job_id}`, `GET /jobs/{job_id}` to poll,
  `GET /health`. The job body simply calls `aspect_pipeline.run(package, to_repo=True)`.
- **Chain:** stage 2 of **Analyst → Architect → Planner (→ Builder)**. Joins on `req_id`.
- **Input:** the Analyst's validated package (`requirements/package.json`) — requirements, the
  `tree` branches (aspects), and the `glossary`.
- **Output:** an aspect-structured **Planner handover** (`architecture/planner_handover.json`,
  `contract_version 2.0`) plus per-aspect Mermaid diagrams and Markdown artifacts. When `to_repo`
  is set it publishes into the project repo's `architecture/` area and asks reqoach to commit.
- **Reasoning roles** are agent_server **personas** on `:7701` (house pattern: called by name via
  `client.complete_json(<persona>, payload)` with `response_format=json_object`,
  `enable_thinking=false`). The personas are listed in §5.

---

## 2. Design model (the unit of work)

The Architect designs **per aspect (feature branch)**, not per requirement. Each branch comes from
`tree.nodes[].branch` (Analyst). For each branch it produces an `AspectDesign`
(`aspect_design.py`):

```
AspectDesign(branch, scope,
  components: [ {name, responsibility, attributes:[{name,type,inferred}]} ],   # owned entities
  functions:  [ {name, inputs, returns, description} ],
  interfaces: [ {name, purpose, consumers, operations:[{name, inputs:[{name,type}], returns}]} ],
  consumes:   [ {concern} ])                                                   # entities owned elsewhere
```

- **components** = entities this aspect **owns** (creates/stores). Names come **verbatim from the
  glossary**; attribute types are a primitive, a glossary value, or a glossary entity (a foreign-key
  reference).
- **interfaces** = one per boundary (not one per requirement) — this is what collapses many
  requirements into a coherent service surface.
- **consumes** = entities owned by *other* aspects that this one uses (cross-aspect references).

---

## 3. Internal workflow — `aspect_pipeline.run()`

```
load package
  └─ refine.refine(package)                     → designs + open_issues        (§4)
  └─ aspect_handover.build(designs, package, open_issues)  → handover          (§6)
  └─ design_judge.run(handover, req_text)       → handover["design_review"]    (advisory, §5)
  └─ proportionality.run(handover, req_text)    → handover["stack_policy"]     (§7)
  └─ publish:
       aspect_handover.write(handover)          → planner_handover.json
       mermaid.emit_all(designs)                → diagrams/*.mmd (one per aspect)
       _artifacts_md(...)                        → artifacts/*.md
       if to_repo: copy to <repo>/architecture/ + reqoach commit
```

Both `design_review` and `stack_policy` are wrapped in try/except and **never fail the run**
(advisory). `stack_policy` and the `code_contract` inside the handover are **recent additions**
(this session); the rest is the established pipeline.

---

## 4. The refine loop — `refine.refine()` (the Architect's validation loop)

```
designs = design_aspects(package)                       # one architect_aspect_designer call per branch
crit = _run_critique(designs, package)
while rounds < MAX_ROUNDS and not crit.clean:            # ERROR-level findings = not clean
    reconcile_ownership(designs, package)                # regenerate offending aspects with the reasons
    crit = _run_critique(designs, package)
reconcile_interfaces(designs, package)                   # adjudicate near-duplicate interfaces
crit.findings += completeness_findings(designs, glossary)# self-check: did the Architect finish?
open_issues = [error-level findings that survived]
```

- **Design → critique → regenerate-with-reasons → re-critique**, bounded by `MAX_ROUNDS`.
- `reconcile_ownership` uses `architect_ownership_adjudicator`; `reconcile_interfaces` uses
  `architect_interface_adjudicator` (merge true duplicates, drop false positives so a pair like
  Authentication/Authorization doesn't dead-end as an open issue).
- Surviving **error-level** findings become `handover.open_issues` — the Architect's own unfinished
  work is surfaced to the Planner/human rather than leaking downstream as a fabricated requirement.

### 4.1 Deterministic critique — `critique.py` (reranker-based, **not** a vision model)

| Finding kind | Check |
|---|---|
| `near_duplicate_interface` | reranker: two interfaces denote the same boundary (sigmoid ≥ threshold) |
| `ownership_violation` | an entity defined in more than one aspect (must be owned by exactly one) |
| `consumed_but_unowned` | an aspect consumes an entity no aspect owns |
| `misassignment` | an element whose requirement is tagged X but sits in branch Y |
| completeness | owned entity with **no attributes**, empty interface, dangling attribute type |

Sameness is judged by the **reranker** (`retrieval.rerank`, sigmoid-scaled), never string matching.
This is the deterministic backbone; the LLM personas do the design and the adjudications.

---

## 5. Personas (agent_server `:7701`)

| Persona | Used by | Job |
|---|---|---|
| `architect_aspect_designer` | `aspect_design.design_branch` | design one aspect (components/functions/interfaces/consumes) |
| `architect_ownership_adjudicator` | `refine.reconcile_ownership` | resolve which aspect owns a contested entity |
| `architect_interface_adjudicator` | `refine.reconcile_interfaces` | merge/keep near-duplicate interfaces |
| `architect_design_judge` | `design_judge.run` | advisory design-plausibility review (out-of-domain / drift) |
| `architect_proportionality_judge` | `proportionality.run` | decide the proportionate persistence + sanctioned deps |
| `architect_judge` | `judge.py` | semantic review / escalate |
| `architect_diagram_reviewer` | `diagram_review` / `vision_review` | advisory review of a rendered diagram (multimodal) |

The `architect_aspect_designer` persona was strengthened this session to state that **its design is
a binding code contract** the Builder implements verbatim.

---

## 6. Output — `planner_handover.json` (`contract_version 2.0`)

`aspect_handover.build` returns:

| Key | Content |
|---|---|
| `contract_version` | `"2.0"` (aspect-structured; SysML dropped) |
| `source_package` | project id/name, run id, aspect count, `architect_ready` echo |
| `by_aspect` | `{branch: {scope, req_ids, components, functions, interfaces, consumes}}` |
| `by_requirement` | `{req_id: {aspect, tags, components(+consumed), functions, interfaces}}` — the Planner joins on `req_id` |
| `components` | global component list with `suggested_module` + attributes |
| `code_contract` | **the Builder contract** (§6.1) — added this session |
| `design_review` | advisory per-aspect verdict (never a gate) |
| `stack_policy` | proportionate persistence + sanctioned dependency allow-list (§7) — added this session |
| `open_issues` | error-level critique findings for a human |

Plus `diagrams/*.mmd` (one Mermaid diagram per aspect) and `artifacts/*.md`.

### 6.1 `code_contract` — the deterministic contract for the Builder

Derived deterministically (`_derive_code_contract`) from the components (entities) and interfaces
(services). One canonical concept per name, so structure is decided once:

```json
{
  "tenant":            {"concept":"Tenant","kind":"entity",
                        "exports":[{"symbol":"Tenant","kind":"class","fields":[{"name":"tenant_id","type":"UUID"}, …]}],
                        "depends_on":[]},
  "tenant_management": {"concept":"TenantManagement","kind":"service",
                        "exports":[{"symbol":"configure_tenant","kind":"function",
                                    "inputs":[{"name":"tenant_id","type":"Tenant"}, …],"returns":"TenantConfiguration"}],
                        "depends_on":["tenant","tenant_configuration","tenant_asset"]}
}
```

- **stack-agnostic** (concepts/kinds/symbols, not file paths — the Builder maps paths per stack).
- `depends_on` is derived from attribute types + operation input/return types that reference other
  concepts (so the Builder generates correct imports).
- Verified this session: 22 concepts (13 entities + 9 services), **0 dangling dependency refs**, and
  scaffolding it deterministically yields a **coherent, booting app (0 coherence issues)**.

---

## 7. `stack_policy` — proportionality review (`proportionality.py`)

Decides the **simplest persistence the requirements justify** and the **third-party dependency
allow-list** the Builder must conform to. To avoid the local model's "many entities ⇒ ORM" prior,
it does **not** trust a holistic verdict: the model extracts candidate ORM-justifying drivers with
verbatim requirement quotes; the code **verifies each quote occurs in the requirements** and that it
carries the driver's vocabulary (reporting / adhoc_query / migrations / portability), else it
defaults to `stdlib sqlite3, no ORM`. Output: `{relational_orm_required, recommended_persistence,
sanctioned_dependencies, over_engineering, verified/rejected_drivers}`.

---

## 8. Current vs. legacy code

The **live path is the `aspect_*` modules** (`aspect_pipeline`, `aspect_design`, `aspect_handover`)
+ `refine`, `critique`, `design_judge`, `proportionality`, `mermaid`, `retrieval`, `client`.

**Legacy / not on the live path** (the earlier SysML-based pipeline, kept but unused by the
service): `pipeline.py`, `handover.py` (contract `1.0`), `generate.py`, `emit.py`, `sysml.py`,
`symbols.py`. `drawio.py` is an alternate diagram export. A reconstruction should follow the
`aspect_*` path and ignore the SysML modules.

---

## 9. Current problems and limitations

Findings from this session. Each is marked **[measured]** (observed from a run/query this session)
or **[structural]** (evident from the code). Stated so a re-implementation fixes them rather than
inheriting them.

### 9.1 Completeness — the design does not cover the requirement set  *(the dominant problem)*

- **No requirements→design/contract completeness gate.** **[structural]** The refine loop validates
  only *internal* consistency (ownership, dedup, dangling types, empty entities). Nothing checks
  that the design realizes the requirements.
- **Measured coverage is very low.** **[measured]** Reranking each of the 60 requirements against
  the `code_contract` elements matched **~2/60** above threshold. The score is understated by terse
  contract stubs, but the direction is real and confirmed by the uncovered list: the contract has
  **no representation** for browsing the menu, switching language (PT/EN), Google auth, submitting/
  accepting/refusing reservations, uploading/displaying images, configuring opening hours, the map/
  OpenStreetMap display, or "discard the contact form". These are requirements with **no
  corresponding entity or operation** — not a scoring artifact.
- **Consequence:** unmodelled requirements are silently dropped from the design and never reach the
  Builder — they surface later as missing features, not as errors.

### 9.2 Expressiveness — the design model is too narrow

- **[structural]** The model has exactly two first-class element kinds: `components` (owned
  **entities**) and `interfaces` (service **operations**). It has **no first-class representation**
  for: UI/frontend behaviour, external integrations (Google OAuth, OpenStreetMap), cross-cutting
  behaviours (i18n / language switching), background/async work, or non-functional requirements.
- **Constraints are extracted but not modelled.** The Analyst emits `constraints` per requirement;
  the Architect design has nowhere to put them, so they do not become anything actionable.
- **`code_contract` covers models + services only** **[measured]** — not routers/endpoints,
  request/response schemas, CRUD, or config. The Builder must scaffold the delivery layer itself;
  without it the non-contract layer drifts (observed as the persistent `missing_module` residual in
  builds).

### 9.3 Validation is advisory, not gating

- **[structural]** `design_review` (`design_judge`), `stack_policy` (`proportionality`), and the
  diagram review are **all advisory** — each is wrapped in try/except and **never fails the run**. A
  design that is incomplete, implausible, or wrongly-scoped still ships.
- The only hard signal is the deterministic critique's **error-level findings** (ownership
  violations, empty entities, dangling types, duplicate interfaces) — narrow and structural, not
  semantic completeness.
- **`open_issues` are surfaced, not resolved.** **[structural]** The refine loop bounds at
  `MAX_ROUNDS`; remaining error-level findings are written to `open_issues` and the handover ships
  anyway. There is no gate that blocks a design with unresolved errors.

### 9.4 Model-dependence and run-to-run instability

- **The design itself is model-generated** (`architect_aspect_designer`). Its *semantic* correctness
  and completeness against the requirements are **unverified** — a self-consistent contract of the
  *wrong shape* passes every internal check.
- **`stack_policy` is model-driven and unstable.** **[measured]** Across two live runs this session
  the persistence decision **flipped**: a "dashboard to *manage* configuration" and "generate an AI
  description" were mis-scored by the judge as *reporting*, which re-sanctioned an ORM
  (SQLAlchemy). It only became usable after adding code-side guards (verbatim-quote verification +
  driver-vocabulary keyword checks), and its output can still vary between runs. The proportionality
  gate is a mitigation over a weak judge, not a reliable decision.

### 9.5 Contract representation nits

- **Non-Python generic syntax.** **[measured]** Operation/attribute types are emitted C#/Java-style
  (`List<Category>`, `Optional<Item>`) rather than Python-native (`list[Category]`, `Category | None`).
  A Python Builder must normalize them.
- **Glossary `kind` mismatch.** **[measured]** The `architect_aspect_designer` persona assumes
  glossary terms carry a `kind` (actor/entity/value), but the Analyst's glossary has **no `kind`
  field**. The Architect infers entity-ness from context instead of a supplied tag.

### 9.6 Code hygiene

- **[structural]** The earlier **SysML pipeline is dead code but still present** (`pipeline.py`,
  `handover.py` @ contract `1.0`, `generate.py`, `emit.py`, `sysml.py`, `symbols.py`). It is not on
  the live path (`api.py` uses `aspect_pipeline`) but is a confusion/maintenance hazard, and two
  handover contracts (`1.0` legacy, `2.0` live) coexist in the tree.

### 9.7 Summary

The Architect reliably produces an **internally consistent, structurally correct design of the
data/service backbone**, and the `code_contract` derived from it is deterministic and
collision-free. Its limitations are **completeness** (it models a fraction of the requirements),
**expressiveness** (only entities + service operations), **the absence of gating** (all semantic
review is advisory), and **model-driven instability** in the one place it makes a judgement call
(persistence). The highest-value fix is §9.1: a requirements→design completeness gate inside the
refine loop.
