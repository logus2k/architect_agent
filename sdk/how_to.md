# Architect Agent — capabilities and interfaces

**Audience:** the Planner Agent (and any other consumer of a validated architecture).
**Service:** none — the Architect is a **batch job**, not a server. Output is published to
disk (§2).
**Status of this document:** written 2026-07-18 against a working implementation and
verified by running it on live Analyst packages. Where something is designed-but-not-built
it says so explicitly — do not infer capability from silence.

---

## 1. What the Architect does

It turns a **validated requirement package** from the Analyst (`analyst-agent:7803`) into a
**validated SysML v2 architecture**, and republishes it in a form that needs no SysML
knowledge to consume.

It is the second stage of the chain **Analyst → Architect → Planner**.

Its defining property is that **nothing it publishes is unvalidated**. Generated model text
is parsed and name-resolved against the SysML v2 standard library by the OMG reference
implementation before anything is written; a model that fails is not published at all,
partially or otherwise. Diagrams are rendered only from a model that already passed.

### What it does NOT do
- It does **not** decide tasks, sizing, feasibility, languages, file layout or build order.
  Those are the Planner's, and the Architect deliberately says nothing about them.
- It does **not** repair requirements. Quality is fixed upstream by the Analyst's refinement
  loop. Where a requirement states no measurable bound, the Architect refuses to invent one.
- It does **not** decide that an architecture is correct. A model can be valid SysML and
  still say the wrong thing; a judge flags those for a human (§5).
- It does **not** watch for changes. Re-running is explicit.

---

## 2. The one file you need

```
data/architecture/<project_id>/planner_handover.json
```

`<project_id>` is the Analyst project id — the same key you already use. Mount the
Architect's `data/` read-only, or copy the file.

```python
path = f"data/architecture/{project_id}/planner_handover.json"
```

Everything else in the package is optional context:

```
data/architecture/<project_id>/
  planner_handover.json     ← the contract, §3
  model.sysml               SysML v2 source (you should not need to parse this)
  symbols.json              element registry, with requirement trace ids
  artifacts/                ADD.md, traceability.md, and a table per artifact
  diagrams/                 rendered PNG + PlantUML source
```

There is no HTTP endpoint. If one would be materially easier on your side, ask — it is a
small addition, but nothing needs it today.

---

## 3. The handover record

```jsonc
{
  "contract_version": "1.0",

  "source_package": {
    "project_id": "4a5f2e16…", "run_id": "5755e967…",
    "architect_ready": false,          // mirrored from the Analyst manifest, §6
    "release_status": "draft",
    "requirements_received": 386, "requirements_modelled": 372
  },

  "classification": { "from_analyst": 0, "from_architect_fallback": 386,
                      "unclassified": 0 },          // §4

  // Keyed by req_id — this is the join.
  "by_requirement": {
    "REQ-0013": {
      "classes": ["functional", "interface"],
      "classified_by": "architect",                  // "analyst" | "architect", §4
      "components":  [ { "name": "MatchingService", "usage": "matchingService",
                         "responsibility": "computes job/candidate match scores",
                         "attributes": [ { "name": "matchScore", "type": "Real" } ] } ],
      "functions":   [ { "name": "MatchJobSeekersToPostings" } ],
      "interfaces":  [ { "name": "MatchingResultInterface",
                         "supplier": "matchingService",
                         "consumer": "webApplicationInterface" } ],
      "constraints": [ { "name": "MatchLatency", "expression": "latencyMs <= 200",
                         "category": "performance" } ],
      "allocations": [ { "function": "MatchJobSeekersToPostings",
                         "component": "MatchingService" } ],
      "state_machines": [ { "name": "SessionLifecycle", "states": ["Idle", "Active"],
                            "transitions": [ { "from": "Idle", "to": "Active" } ] } ]
    }
  },

  // Every component once, so one element has one name everywhere you meet it.
  "components": [ { "name": "MatchingService", "usage": "matchingService",
                    "suggested_module": "matching_service",
                    "responsibility": "…", "req_ids": ["REQ-0013", "REQ-0017"] } ],

  // Edges derived from declared interfaces. Usable as task dependencies.
  "depends_on": [ { "from": "webApplicationInterface", "to": "matchingService",
                    "via": "MatchingResultInterface" } ],

  // Everything the Architect could not settle. Do not build on these silently.
  "open_issues": [
    { "kind": "unquantified_constraint", "req_id": "REQ-0030",
      "detail": "states no measurable bound (C7=2) — upstream refinement needed" },
    { "kind": "semantic_defect", "req_id": "REQ-0006", "element": "UserAccountLifecycle",
      "detail": "judge flagged: transition Disabled→Enabled may not be the intended path",
      "suggested_fix": "review the transitions" }
  ]
}
```

### Guarantees
- **`req_id` is the key**, used verbatim — the same key the Analyst emits and the ADD
  traceability table uses.
- **Every name in this file appears identically in `model.sysml`.** Element names are minted
  by a registry, not by a language model, so they are stable across regeneration and
  consistent across every artifact.
- **`constraints[].expression`** parsed and resolved against the SysML v2 standard library.
  Safe to quote in acceptance criteria. `null` means the model proposed nothing usable.
- **A requirement may be absent from `by_requirement`** — it produced no elements. That is
  not an error.

### Two intended uses

1. **Naming.** Derive artifact names from components the Architect already named
   (`MatchingService` → `matching_service.py`) instead of inventing them per task.
2. **Acceptance criteria.** Cite `latencyMs <= 200` rather than "should be fast".

If you would invent a component the Architect already defined for that requirement, its
name wins — otherwise the two designs diverge again and this file is decorative.

---

## 4. Classification — routing labels and where they came from

The Architect routes on six classes, the same vocabulary the Analyst uses:

| class | SysML v2 |
|---|---|
| `functional` | `action def` |
| `structural` | `part def` |
| `interface` | `port def` / `interface def` |
| `behavioral` | `state def` |
| `constraint` | `constraint def` |
| `allocation` | `allocate` |

Multi-label: a requirement routes to every class it carries.

**`classes[]` is populated even when the Analyst supplied none.** The Analyst documents the
field as never empty, but a package whose `classify:run` was not executed carries
`classes: []` throughout — 386 of 386 on the current jobs project, found independently by
both the Architect and the Planner. The Architect classifies anything arriving unclassified,
so routing has a signal either way.

`classified_by` says which source produced them, because they are not equivalent evidence:

| Value | Meaning |
|---|---|
| `analyst` | From `classify:run`. Authoritative — the Architect does not re-classify. |
| `architect` | Fallback. Usable, but a second opinion, not the requirements author's. |

When the Analyst starts running `classify:run`, this flips to `analyst` with no change on
your side. Treat the fallback as a bridge.

---

## 5. Review layers — what has and has not been checked

| Layer | Deterministic? | Gates the build? |
|---|---|---|
| SysML v2 validation (OMG reference implementation) | yes | **yes** — nothing invalid is published |
| Semantic judge | no (local model) | no — escalates to a human |
| Vision review of the rendered diagram | no | no — advisory only |

**Validation proves the model parses and resolves. It does not prove the model is right.**
A constraint asserting `requested > quota` for a rule that should *reject* over-quota
requests is perfectly valid SysML and precisely backwards — an observed case. The judge
exists for that class of defect and reports `ok` / `wrong` / `uncertain`; **both `wrong` and
`uncertain` reach `open_issues`**, because treating abstention as approval makes review
decorative.

An `open_issues` entry of kind `semantic_defect` means a human has not yet ruled. Building
on it is a choice, not a default.

---

## 6. Readiness — read this before consuming

`source_package.architect_ready` is mirrored from the Analyst manifest; the Architect never
sets it. **Branch on it, not on data being present.**

> **Today it is `false` on every package**, because the Analyst's release gate is not built
> and no project has completed refinement. A `draft` package is valid input for development;
> it is not approved. The Architect models it anyway and records the blockers as open issues.

Related, and visible in the ADD's traceability table:

- **Refined requirements differ from their source document.** When the Analyst's refinement
  loop rewrites a requirement, the architecture derives from the rewritten text. Anyone
  quoting the source PDF will find different wording.
- **`needs_human` requirements are modelled, and flagged.** Consuming unapproved text
  without saying so is how an architecture ends up traceable to something nobody signed off.

---

## 7. Regenerating

```bash
curl -s http://analyst-agent:7803/projects/<PID>/package -o package.json
python -m architect_agent.pipeline package.json -p <PackageName> [--limit N]
#   -> data/architecture/<project_id>/
```

Deterministic given the same package: element names come from the registry, and emission is
plain code, so reruns diff cleanly. The *content* the model proposes is not bit-reproducible,
but the naming is.

A full run is slow — one local model slot, one LLM call per requirement per applicable stage.
`--limit` exists for development.

---

## 8. Known gaps

| Gap | Impact on you |
|---|---|
| No HTTP service | fetch is a file read, not a request (§2) |
| No full-scale validated run yet | largest verified run is a subset; a 386-requirement run is in progress |
| `depends_on` is often empty | only populated where an interface resolved both ends; empty ≠ no dependencies |
| Interface ends not connected to specific parts in the model text | `interfaces[].supplier/consumer` here is richer than `model.sysml` |
| No `satisfy` / `verify` relationships in the model | traceability lives in `artifacts/traceability.md`, not in SysML |
| Vision review uncharacterised | advisory only; do not weight it |

---

## 9. Integration status

The join in §3 depends on both sides using the same requirement ids. As of 2026-07-18 the
Planner's committed `plan.json` traces to `NFR-03` / `NFR-97` and reads
`labs/requirements/store/projects/…/scorecard.json`, a store that is now empty after the
reqqa refactor. The Analyst emits `REQ-0005` / `REQ-0013`.

**Until the Planner reads the Analyst package and adopts `req_id`, this file can be produced
but nothing can be attached to it.** That work is on the Planner side; nothing in the
Architect needs to change for it.
