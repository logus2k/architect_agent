# Architect Agent — Implementation Specification

## 1. Overview
This document defines the implementation details required for an LLM‑powered Architect Agent capable of producing SysML v2 models, diagrams, and MBSE artifacts from INCOSE‑validated requirements.

Inference runs entirely on‑prem via the local `agent_server` / `llama-vision` pair — see
§7.1. The agent must function with no internet access.

### 1.1 How to read the prescriptions in this document
Statements here fall into three grades, and they are **not** interchangeable:

- **Verified** — tested against a running system, with the observation recorded.
  Safe to build on.
- **Borrowed** — taken from an adjacent system (usually `~/env/labs/requirements`)
  because it works there. Plausible, but never validated for this pipeline.
- **Design choice** — a judgement call with no measurement behind it.

Prescriptive wording ("must", "requires") appears at all three grades. Where the grade
is not obvious, it is stated inline. A rule resting on one unreplicated run is an open
question wearing the costume of a decision — several early drafts of this document made
exactly that mistake, and the corrections are noted where they occurred.

## 2. System Components

### 2.1 Requirement Interpreter Module
**Purpose:** Convert INCOSE requirements into structured objects.

**Input:** Analyst Agent **package** — `GET http://analyst-agent:7803/projects/{pid}/package`  
**Output:** Internal requirement objects

*Evidence grade: verified — fetched from the live service on 2026-07-18 and consumed
by `generate.load_package()`.*

The Analyst (`assets/analyst_agent`, see its `sdk/how_to.md`) supersedes the earlier
reqqa scorecard contract. One call returns the whole handover:

```jsonc
{
  "manifest":  { "architect_ready": false, "release_status": "draft",
                 "blockers": [...], "counts": { "total": 386, "unclassified": 386 } },
  "requirements": [ { "req_id": "REQ-0005", "text": "...",
                      "classes": ["functional", "interface"],   // multi-label routing
                      "type": "performance",                    // reporting only
                      "constraints": ["latency"],               // closed vocabulary
                      "analysis": { "score": 3.4,
                                    "characteristic_scores": { "C7": 2, "...": 0 } },
                      "lineage":    { "duplicate_of": null, "was_compound": true },
                      "provenance": { "source_document": "...", "page": 9,
                                      "bbox": [...], "section_path": "..." } } ],
  "set_level": {}, "aggregates": {}, "coverage": {}, "problem_statement": {}
}
```

**What the Architect actually consumes.** Required: `req_id` and `text`. Everything else
is used when present and degrades cleanly when absent:

| Field | Used for |
|---|---|
| `classes[]` | Routing to generation stages — **skips our own classifier when present** |
| `analysis.characteristic_scores.C7` | Suppressing invented constraint bounds (below) |
| `lineage.duplicate_of` | Defensive re-filter |
| `provenance.source_file` | ADD source list |
| `manifest.architect_ready` / `blockers` | Readiness gate, surfaced as an open issue |

**Three findings from real packages that contradict the Analyst's own guarantees:**

1. **`classes[]` is NOT always populated.** Its `how_to.md` §3 states the field "is never
   empty (falls back to `["functional"]`)". Two of three live projects — 649 requirements
   — carry `classes: []` throughout, because `classify:run` was never executed on them.
   So classification is treated as *optional upstream input*: when present we use it and
   skip our own classifier; when absent `architect_classifier` fills the gap. Neither
   path is authoritative over the other.
2. **`architect_ready` is `false` on every package today** — the Analyst's release gate is
   not built. Enforcing it would block every run, so `require_ready` defaults to False and
   the blockers are recorded as open issues instead.
3. **Half the requirements bound nothing measurable** — 191 of 386 score C7 < 3.

   **This is an Analyst-side issue, not an Architect responsibility.** Requirement quality
   is fixed upstream by refinement and human sign-off; a package that is genuinely
   `architect_ready` should not contain unverifiable requirements at all. The Architect
   does not, and should not, repair requirements.

   What the Architect does is refuse to paper over the gap: generating a constraint
   expression from text with no number invents a bound the stakeholder never gave, and an
   invented bound is worse than an absent one because it looks authoritative. So such
   requirements are skipped by the constraint stage and recorded as unquantified, with
   the C7 score attached.

   *This guard is defensive, not architectural.* It exists because every package today is
   `draft`. Once the Analyst's release gate lands it should become a no-op — and if it
   ever fires on an `architect_ready` package, that is a defect upstream, not here.

#### 2.1.1 Requirement Classification
**Superseded in part.** An earlier draft of this section stated the Analyst supplies no
classification and the Architect must do it. That was true of the old reqqa scorecard and
is no longer true: the Analyst emits `classes[]` using the *same six-class vocabulary*
below, and its `classify:run` is the authoritative source when it has been run.

The classifier is retained as a **fallback**, because a package whose `classify:run` was
never executed arrives with `classes: []` — observed on 649 of 734 live requirements.
`classify()` skips any requirement that already carries classes.

**The taxonomy is defined by routing, not by theory.** A class exists only if it sends
the requirement to a different downstream module and a different SysML v2 construct:

| Class | Consumed by | SysML v2 construct |
|---|---|---|
| `functional` | §2.2 Functional Decomposition | `action def` |
| `structural` | §2.3 Logical Architecture | `part def` |
| `interface` | §2.4 Interface Modeling | `port def` / `interface def` |
| `behavioral` | §2.5 Behavior Modeling | `state def` |
| `constraint` | §2.6 Constraint Modeling | `constraint def` |
| `allocation` | §2.7 Allocation Engine | `allocate` |

**Multi‑label, not single‑label.** "The system shall allocate GPUs fairly within 100 ms"
is both `functional` and `constraint`. A requirement routes to every module whose class
it carries. Forcing a single label silently drops the timing budget.

**Implementation:** one agent profile, `architect_classifier`, following the house
pattern — batch = 1, `memory_policy: "none"`, `response_format: json_object`,
`temperature: 0.0`. Per §5.1, classification is per‑item and needs no cross‑item context,
so it parallelises at `WORKERS = 8` with no consistency risk.

**Output** (merged into the internal requirement object):
```json
{
  "req_id": "DOC-0007",
  "classes": ["functional", "constraint"],
  "rationale": "allocation action plus a 100 ms timing bound",
  "confidence": 0.9
}
```

**Failure policy:** a requirement that classifies to `[]` is a hard failure per §4 — it
would otherwise vanish from the architecture with no trace. Low confidence is retained
and surfaced in the ADD's Assumptions and Open Issues section, not silently dropped.

### 2.2 Functional Decomposition Engine
**Purpose:** Break system into hierarchical functions.

**Output Format (Markdown):**
```markdown
- Allocate GPU
  - Validate quota
  - Select GPU
  - Bind session
```

**SysML v2:**
```sysml
action def AllocateGPU;
```
Decomposition emits action *definitions*; the corresponding usages are instantiated
in the logical architecture (§2.3) so that allocations (§2.7) have features to bind to.

### 2.3 Logical Architecture Generator
**Purpose:** Define components and boundaries.

**SysML v2 Example:**
```sysml
package Architecture {
    private import ScalarValues::*;

    part def GPUCluster {
        attribute totalGPUs : Integer;
    }
    part def NotebookSession {
        attribute userId : String;
    }

    part gpuCluster : GPUCluster;
    part notebookSession : NotebookSession;
    action allocateGPU : AllocateGPU;
}
```
`private import ScalarValues::*;` is required — `Integer` and `String` are
standard‑library types and will not resolve without it. **The visibility keyword is
mandatory:** bare `import ScalarValues::*;` is a *syntax* error in the pilot
implementation (tested: 3 syntax errors vs 0 with `private import`). The standard
library itself writes every import this way.

### 2.4 Interface Modeling Engine
**Purpose:** Define ports, flows, contracts.

**SysML v2 Example:**
```sysml
port def GPUPort {
    attribute quota : Integer;
}

interface def GPUAllocationIF {
    end supplier : GPUPort;
    end consumer : GPUPort;
}
```
An interface *definition* declares its `end` ports. A bare `interface X { ... }` is a
usage with no connected ends and is semantically empty.

### 2.5 Behavior Modeling Engine
**Purpose:** Generate activities, state machines, interactions.

**SysML v2 Example:**
```sysml
state def SessionLifecycle {
    state Initial;
    state Allocated;
    transition Initial then Allocated;
}
```
There is no `stateMachine` keyword in SysML v2 — state machines are `state def`.
Transitions use `then`, not `->`.

### 2.6 Constraint Modeling Engine
**Purpose:** Define parametric constraints.

**SysML v2 Example:**
```sysml
constraint def GPUFairness {
    in totalGPUs : Integer;
    in users : Integer;
    in fairShare : Real;
    fairShare == totalGPUs / users
}
```
There is no `equation` keyword. A constraint body is a boolean expression, so the
comparison is `==` — a constraint asserts a condition, it does not assign.

### 2.7 Allocation Engine
**Purpose:** Map functions to components.

**SysML v2 Example:**
```sysml
allocate allocateGPU to gpuCluster;
```
Both ends must resolve to *usages* (features) in scope — the lowercase usages declared
in §2.3. Definitions (`AllocateGPU`, `GPUCluster`) are not features and will not resolve.

### 2.8 SysML v2 Text Generator
**Purpose:** Assemble all model fragments into a valid `.sysml` file.

**Output:** `model.sysml`

### 2.9 Diagram Renderer
**Purpose:** Render diagrams from the validated model.

**Output:** `diagrams/*.png` (and `.puml` source alongside)

> **DECISION (2026‑07‑18): diagram hints are dropped.** This module was originally a
> *Diagram Hint Generator* emitting x/y coordinate JSON for SysON. That is no longer
> built. *Evidence:* a 16‑entity model renders from the pilot jar via PlantUML into a
> clean hierarchical layout (1492×349, no crossing edges, definitions below usages)
> with no coordinates supplied. SysON also auto‑layouts. Hints would buy cosmetic
> control at the price of an online stateful applier — a WebSocket client, diagram
> node‑ID resolution, and the `layoutDiagram` mutation. Not worth it.
>
> **Known fidelity gap:** PlantUML output does **not** render multiplicities —
> `part nodes : GPUNode[1..64]` draws as `nodes: GPUNode`. The information is in the
> model and in the ADD, just not on the picture. Revisit only if that becomes a problem.

**Rendering path:** `SysML2PlantUMLSvc.getPlantUMLCode(...)` → inject
`!pragma layout smetana` → `SourceStringReader.outputImage(PNG)`. Pure Java, no
GraphViz, no SysON, no network. Details under §3 Step 6.

---

**The remainder of this section is retained for reference only.** It documents the SysON
layout API that the dropped hint applier would have used. Keep it in case hints are
revived; nothing in the current design depends on it.

**Verified end‑to‑end** against `eclipsesyson/syson` (image built 2026‑07‑10,
digest `sha256:cc0974c3…`) on 2026‑07‑18. The full programmatic path works:

| Step | Mechanism | Result |
|---|---|---|
| Create project | `createProject` (template `sysmlv2-template`) | works |
| Create elements | `createChild` (e.g. `SysMLv2EditService-PartUsage`) | works |
| Create diagram | `createRepresentation` + a `representationDescriptionId` (e.g. "General View") | works |
| Populate diagram | `dropOnDiagram` | works |
| Read node IDs | `diagramEvent` subscription | works |
| Apply positions | `layoutDiagram` | works |
| Persistence | reconnect, then restart the server | positions survived both |

**Constraints discovered — these shape the applier's design:**

1. **Diagrams do not auto‑populate.** A newly created diagram is empty even when its
   target package has children. Elements must be added explicitly with `dropOnDiagram`.
2. **Diagram content is not readable over HTTP.** `viewer.editingContext.representation`
   returns only `RepresentationMetadata`. Nodes and `layoutData` are available *only*
   through the `diagramEvent` **GraphQL subscription over WebSocket** at `/subscriptions`.
3. **The WebSocket uses the legacy `graphql-ws` subprotocol**, not `graphql-transport-ws`.
   Messages are `start`/`data`, not `subscribe`/`next`. Using the modern protocol yields
   a `connection_error` with no further diagnostics.
4. **`layoutDiagram` does *not* require an active subscription.** Tested: called over
   plain HTTP with no WebSocket open, the positions applied and persisted. Only *reading*
   diagram content needs the subscription (constraint 2) — writing layout does not.
   The applier therefore needs the WebSocket once, to resolve node IDs, and can issue
   the mutation over HTTP.
5. **Required non‑null fields** that are easy to miss: `nodeLayoutData[].minComputedSize`
   and `diagramLayoutData.autoLayoutState` (`UNCHANGED` | `ACTIVATE` | `DEACTIVATE`).
   Both are rejected with a validation error if omitted. Tested: all three enum values
   preserved the supplied coordinates — `ACTIVATE` did **not** re‑run auto‑layout over
   them. Pass any value; `UNCHANGED` is the safe default.
6. **ID resolution.** In the subscription payload, `node.targetObjectId` is the semantic
   element ID and `node.id` is the diagram node ID that `layoutDiagram` expects. The
   name → node‑ID mapping therefore requires opening the diagram first; it cannot be
   computed offline.

### 2.10 Artifact Packager
**Purpose:** Bundle all outputs for Planner Agent.

**Output Structure (canonical):**
```
architecture/
  model.sysml
  diagrams/
    logical_architecture.png
    logical_architecture.puml
    behavior.png
    behavior.puml
  artifacts/
    functional_decomposition.md
    logical_architecture.md
    interfaces.md
    behavior.md
    constraints.md
    allocations.md
    verification_plan.md
    ADD.md
```
This is the single authoritative output layout; all other sections refer to it.

## 3. Processing Pipeline

### Step 1 — Load Requirements
Parse Analyst Agent output.

### Step 2 — Build Requirement Objects
Normalize into internal structures, then **classify** each requirement (§2.1.1) to
determine which generation modules consume it. Multi‑label; unclassified is a hard
failure. Parallel at `WORKERS = 8`, batch = 1.

### Step 3 — Generate MBSE Artifacts
Functional → Logical → Interfaces → Behavior → Constraints → Allocation → Verification.

### Step 4 — Generate SysML v2 Model
Combine all fragments.

### Step 5 — Validate (blocking gate)
Validation runs **immediately after model generation, before anything downstream**.
Nothing invalid reaches rendering or packaging.

**Ordering is not arbitrary:** rendering requires a valid model. The renderer parses
and resolves before it can emit PlantUML, so an invalid model cannot be drawn at all.
Validate first, then render.

- **Model:** the generated `.sysml` must parse and resolve. *Evidence: tested, syntax
  and semantic errors both detected.*
- **Regeneration: not implemented, deliberately.** *Evidence: design choice, reasoned.*
  The borrowed `max_iters=3` was never used. With element names owned by the registry
  and emission fully deterministic, re-running the emitter on the same stage output
  produces byte-identical text — a retry cannot fix a validation failure, only hide it.
  A failure here is a defect in the emitter or an unusable model-proposed expression,
  and both are handled at source (see `emit._constraint_body`). The gate fails the run.
- The gate is pass/fail for the whole package. Partial output is not published.
  *Evidence: a design choice, not a measurement.*

### Step 6 — Render Diagrams
Render PNG (plus `.puml` source) from the now‑validated model via the bundled PlantUML.
A render failure is non‑fatal (§4) — the model is already known good.

**Validator — SysML v2 Pilot Implementation, headless.** SysON is *not* required as a
runtime dependency. Tested on 2026‑07‑18 with `jupyter-sysml-kernel-0.60.1.zip`
(126 MB, EPL‑2.0) from the SysML‑v2‑Pilot‑Implementation `2026-05` release: a single
fat jar, Java 21, no Eclipse, no Postgres, no network.

A ~20‑line Java class drives it:
```java
SysMLInteractive si = SysMLInteractive.getInstance();
SysMLInteractiveResult r = si.process(source);
r.getSyntaxErrors();    // grammar violations
r.getSemanticErrors();  // unresolved names, type errors
r.hasErrors();          // → pipeline exit code
```
`SysMLInteractiveResult` separates syntax from semantic errors, which maps directly onto
the two failure modes in §4. Confirmed working: `stateMachine` / `->` produce syntax
errors; a missing `private import ScalarValues::*;` produces the semantic error
`Couldn't resolve reference to Type 'Integer'`.

**Standard library loading — solved. `loadLibrary()` requires an ABSOLUTE path.**
This is the single most important operational detail:

```java
si.loadLibrary("/abs/path/to/sysml.library");   // works — 94 resources, ~1.7 s
si.loadLibrary("relative/path/to/sysml.library"); // FAILS
```

With a **relative** path, EMF URI‑encodes the spaces in the hardcoded subdirectory names
(`KERNEL_LIBRARIES_DIRECTORY = "Kernel Libraries"`) and then fails to decode them:
`FileNotFoundException: .../Kernel%20Libraries/...`. With an absolute path the same
library loads cleanly. Do **not** rename the library directories to avoid the spaces —
the names are hardcoded constants, and renaming makes `loadLibrary` silently read
**zero** files while still reporting success. Silent zero‑load is the dangerous failure
mode: validation then passes everything.

Verified with the library loaded:

| Input | Syntax | Semantic | Exit |
|---|---|---|---|
| valid model with `private import ScalarValues::*;` | 0 | 0 | 0 (VALID) |
| same model, import omitted | 0 | 2 — `Couldn't resolve reference to Type 'Integer'` | 1 (INVALID) |

Semantic validation is therefore fully functional offline, and Step 6 can be a real
gate rather than a syntax‑only check.

#### Diagram rendering — also offline, also without SysON
The same jar bundles PlantUML (4509 classes) and a SysML→PlantUML translator. Verified:
a valid model renders to PNG with **no GraphViz and no SysON**.

Two traps, both hit and solved:
- `viz()` and `getSVG()` shell out to GraphViz `dot` and fail if it is absent. Setting
  `GRAPHVIZ_DOT=smetana` does **not** help — this PlantUML build treats it as a literal
  executable path.
- The working path is `SysML2PlantUMLSvc.getPlantUMLCode(...)`, which returns PlantUML
  *source* without invoking any layout engine, then rasterising via
  `SourceStringReader` with `!pragma layout smetana` injected. Smetana is pure Java.

Confirmed output: 491 chars of PlantUML → an 18 KB, 404×317 PNG correctly showing the
package, part usages, part definitions, attributes and composition.

This makes SysON optional for the whole pipeline: validation and rendering both run
from one jar. SysON remains useful as an interactive modelling UI, not as a dependency.

#### Vision review — ADVISORY, not a gate
Diagram PNGs can be reviewed by the local vision model (`gemma-4` with the
`gemma4_e4b/mmproj-F16.gguf` adapter, `active_model_vision: true`), via the standard
`/v1/chat/completions` call with an `image_url` data URI.

**Corrected finding.** An earlier draft of this document recorded a false negative —
the reviewer rejecting a correct diagram — and concluded the model was unreliable. That
was wrong twice over. The failing call used an ad-hoc prompt containing "Be strict:
answer false if the diagram does not show what is asked", which biased it toward
rejection; and a later run reached the model with its *system prompt unset* (the agent
had been registered with a file path where the prompt text belonged), so it improvised
a schema of its own.

With `architect_diagram_reviewer` correctly registered, the same diagram and question
returns:

```json
{"matches": true,
 "reason": "The diagram shows a GPUCluster part containing NotebookSession parts...",
 "elements_seen": [{"name": "gpuCluster", "type": "GPUCluster"}, ...]}
```

The element list is accurate, and an earlier control question (asking about a database
and REST gateway that are not present) correctly returned `false`. So the model both
reads diagrams and discriminates.

**It stays advisory anyway.** *Evidence grade: design choice.* Not because the model was
measured unreliable — that measurement was an artifact — but because a non-deterministic
judge should not fail a build when a deterministic one (§3 Step 5) already covers
correctness. Vision catches a different class of problem: a model that is valid but
depicts the wrong thing. That belongs in the ADD's Open Issues, not in the exit code.

**Still unmeasured:** the false-positive/negative rate over a real evaluation set. Two
correct answers on two questions is not a characterisation.

### Step 7 — Package Artifacts
Prepare directory for Planner Agent.

## 4. Error Handling
- Missing requirement → **hard failure**, never skipped. A dropped requirement is an
  untraceable coverage hole in an INCOSE context; the run stops and reports it.
- Invalid SysML v2 syntax → regenerate the fragment, max 3 attempts, then fail the run
  (Step 6).
- Diagram fails to render → non‑fatal. The model is still valid and is published;
  the failure is recorded in the ADD's Open Issues. *Design choice, not measured.*

Failures are surfaced, not logged and swallowed. The requirements lab's fail‑soft
pattern (a failed judge silently lowers coverage without lowering the score) is
explicitly **not** adopted here.

## 5. Performance Requirements
- Must process 200+ requirements

### 5.1 Scale strategy
Adapted from `~/env/labs/requirements` (reqqa), which runs the same agent_server +
llama-vision pair at comparable scale. What transfers:

- **Batch = 1 for per‑item generation.** reqqa measured ~96% judge self‑consistency at
  batch=1, dropping to ~54% at batch 8+ because the model conflates items
  (`specs/baseline/technical_architecture.md:246`). Generation is at least as sensitive.
- **Stateless calls.** Every reqqa preset is `memory_policy: "none"` with a single user
  message and no history. Adopt the same; do not rely on conversational carry‑over.
- **Budgeted chunking on characters, not tokens.** reqqa uses `MAX_ITEMS_PER_CHUNK = 25`
  / `MAX_CHARS_PER_CHUNK = 4000` (`src/reqqa/segment/chunker.py:16-18`). No tokenizer
  exists in that codebase; context limits are documented, not enforced.
- **Map‑reduce with a Python reduce.** Aggregation is plain Python where it can be;
  the LLM reduce is reserved for genuinely judgemental synthesis.
- **Parallelism — do NOT copy `WORKERS = 8`** (`src/reqqa/jobs.py:48`). *Evidence:
  refuted by measurement.* llama-vision serves gemma-4 with `--parallel 1`, so eight
  concurrent requests queue behind a single slot and time out rather than running
  faster; the pipeline failed twice this way before the cause was found. The default
  is now 2 (`ARCHITECT_WORKERS`), and the ceiling that matters is llama-vision's
  `--parallel`, not ours. Note it was observed at `2` earlier the same day and `1`
  later — read it live, do not assume.

**What does NOT transfer — and this is the important part.** reqqa solves cross‑item
consistency by moving the cross‑item work *out* of the LLM: duplicate detection is O(n)
reranker calls against `embeddings_server` with `OVERLAP_THRESHOLD = 0.8`, and only the
survivors reach an LLM (`src/reqqa/score/setlevel.py:41,82`). It has **no symbol table,
no glossary, no shared registry** — confirmed absent by inspection.

That works because reqqa's cross‑item problem is *detection* (are these two the same?),
which a reranker can answer. The Architect Agent's cross‑item problem is *generation
consistency*: a component named in `interfaces.md` must be the exact same identifier in
`allocations.md` and in `model.sysml`. No reranker produces that.

**Consequence:** the Architect Agent needs a mechanism reqqa does not have — a
deterministic **symbol registry** maintained in Python across calls, seeded by the
logical architecture stage and passed into every later prompt as authoritative names.
Element naming must not be left to independent LLM calls. This is the main scale risk
and the piece with no prior art in the stack.

**Also inherited as a warning:** reqqa's `coverage.py:117` interpolates the entire
requirement set into a prompt with no size bound — the concrete overflow path at scale.
Any Architect prompt that embeds the full requirement set needs an explicit bound.

## 6. Security Requirements
- No external network calls
- All processing on‑prem
- All artifacts stored locally

## 7. Integration Requirements

### 7.1 Inference — agent_server + llama-vision
The Architect Agent is wired like every other agent in the stack. Nothing leaves the host.

- **Inference backend:** `llama-vision` (`127.0.0.1:8500`), a local llama.cpp server.
  Verified loaded models: `gemma-4` (chat), `bge-m3` (embeddings), `ma2-360m-dpo-b01`.
- **Agent profiles:** `agent_server` (`127.0.0.1:7701`) owns prompts and configuration.
  Profiles live in `agent_server/data/agents/<name>.agent.json`, system prompts in
  `agent_server/data/prompts/`.

**Profile schema** — these four keys are present in all 93 registered profiles; only
`robot` adds a fifth (`tts_field`), so the four are the required set:
```json
{
  "name": "architect_decompose",
  "system_prompt": "/agent_server/app/data/prompts/architect_decompose_system_prompt.txt",
  "params_override": {
    "max_tokens": 2048,
    "temperature": 0.0,
    "top_p": 0.9,
    "chat_template_kwargs": { "enable_thinking": false }
  },
  "memory_policy": "none"
}
```

**Invocation** — OpenAI‑compatible; the `model` field carries the *agent name*, not a
model name. Verified live against `planner_decompose`:
```
POST http://127.0.0.1:7701/v1/chat/completions
{ "model": "<agent_name>",
  "messages": [{"role": "user", "content": "..."}],
  "response_format": {"type": "json_object"} }
```
Base URL comes from `AGENT_SERVER_URL` (default `http://localhost:7701`).

**Placement:** the stack already has an `incose_*` agent family upstream (Analyst) and a
`planner*` family downstream. No `architect*` agents are registered yet — they are the
work to be created.

**How many profiles:** as many as prompt diversity requires — no more, no fewer. A stage
gets its own profile when it needs a genuinely different system prompt or different
`params_override`; stages that would share a prompt share a profile. The count follows
from the prompts, it is not fixed up front.

### 7.2 SysON
- Self‑hosted container; no external service. See §2.9 for the verified API path.

### 7.3 Planner Agent
- Receives full architecture package

## 8. Implementation Status

*As built on 2026-07-18. This section exists because earlier revisions of this document
described modules that did not exist, and later ones described as missing modules that
did. Verified against the code and a passing test suite (33 tests).*

| §   | Module | Status |
|-----|--------|--------|
| 2.1 | Requirement Interpreter | built — `generate.load_package` |
| 2.1.1 | Classification (fallback) | built — `generate.classify` |
| 2.2 | Functional Decomposition | built — `generate.decompose` |
| 2.3 | Logical Architecture | built — `generate.logical` |
| 2.4 | Interface Modeling | built — `generate.interfaces` |
| 2.5 | Behavior Modeling | built — `generate.behavior` |
| 2.6 | Constraint Modeling | built — `generate.constraints` (skips C7 < 3) |
| 2.7 | Allocation | built — `generate.allocations`, LLM + deterministic fallback |
| 2.8 | SysML v2 Text Generator | built — `emit.emit_model` |
| 2.9 | Diagram Renderer | built — `sysml.validate(render_png=...)` |
| 2.10 | Artifact Packager | built — `emit.write_package` |
| — | Semantic judge | built — `judge.review`, escalates to human |
| — | Vision review | built — `vision_review`, advisory only |

**Not built:** interface `end` connection to specific parts (ends are recorded in
`interfaces.md` but both ends are declared against one port def); nested part
containment; `satisfy`/`verify` requirement relationships in the model text.

**Largest untested area:** everything is proven on ≤12 requirements. The biggest real
package is 386, and no full-scale run has been made — at `--parallel 1` that is hours.

## 9. Completion Criteria
The Architect Agent is considered complete when:
- All MBSE artifacts are generated
- SysML v2 model validates in SysON
- Diagrams render correctly from the validated model
- Planner Agent can generate executable specifications from the output
