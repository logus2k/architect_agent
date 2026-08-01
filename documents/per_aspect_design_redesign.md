# Redesign: Per-Aspect Architecture Generation

**Status:** planned — **execution deferred until the Analyst vocabulary+structure redesign
lands** (`analyst_agent/documents/vocabulary_and_structure_redesign.md`). This plan
consumes that plan's output; it cannot start before it.
**Owner discussion:** Analyst ↔ Architect design thread, 2026-08.
**Scope:** the Architect stops designing per-requirement and designs **per aspect/branch**,
producing readable, relevant artifacts for each — instead of one monolithic model and one
unreadable diagram.

---

## 1. Why — verified evidence from the first real run

Restaurant Menu Manager, 60 requirements, published package
`data/architecture/185d83e85fc84e15ab77796c40e22eb4/`:

- **Concept inflation.** 33 `interface def`s for 60 requirements; **six** authentication
  interfaces for one Google-login concern, with literal duplicates.
- **The diagram is broken, not just ugly.** 152 elements laid out in a single horizontal
  row. Real width **19026px**; PlantUML silently truncated it to **4096px** (its default
  `PLANTUML_LIMIT_SIZE`) — the published image showed ~21% of the model and nobody
  detected it. Verified by re-rendering the same `.puml` at a raised limit (19026×576).
- **Root cause (shared with the Analyst plan):** the Architect processes each requirement
  in isolation and emits one monolithic model + one monolithic diagram. There is no notion
  of an aspect, so nothing is grouped, converged, or separately viewable.

Fixing the renderer's truncation is pointless — the monolithic artifact is the wrong thing.
The fix is to generate **per aspect**.

## 2. What changes

The Analyst will hand over (per its plan) a **requirement tree** (single-parent branches),
**tags** (cross-cutting concerns), and a **glossary** (canonical entities). This plan makes
the Architect consume that structure:

### 2.1 Per-branch design replaces per-requirement generation
- The generation stages (`generate.py`) iterate **branches**, not flat requirements. Each
  branch's requirements are designed **together**, so one coherent component/interface is
  produced per aspect instead of scattered per-requirement duplicates.
- This does **not** violate the batch=1 rule — that rule governs *judging* requirements,
  where conflation is bad. *Designing an aspect* wants its requirements seen together.
- **Ownership rule** (prevents re-inflation): the branch that owns a concept designs its
  component **once**; branches merely *tagged* with that concept are **consumers**, not
  co-designers (the tag grants read-context, not write-ownership). Maps onto the
  supplier/consumer the model already emits.

### 2.2 Glossary-anchored naming
- `part def`s and attributes anchor to glossary terms, not model-invented variants. The
  symbol registry's role shrinks — shared entities arrive pre-identified, so it stops trying
  to converge near-synonyms after the fact (the mechanism that failed).

### 2.3 One artifact set per aspect
Instead of a single `model.sysml` + one truncated diagram, produce **per branch**:
- a model fragment (the aspect's elements),
- **a diagram that renders fully and is readable** — small enough to never hit the 4096px
  wall (readability by construction, not by tuning the renderer),
- the aspect's slice of the handover.
Plus a top-level package that composes the fragments and a **system-context** view (aspects
and their relationships), not a 152-box strip.

### 2.4 Tag-filtered design context
When designing a component, the Architect pulls the nodes carrying its tag as **context and
consumers** — so the auth component is designed once, knowing every branch that consumes it.

## 3. Success metrics (measurable, verify on Restaurant)

| Metric | Now (verified) | Target |
|---|---|---|
| Auth interfaces | 6 (with dupes) | 1, with N known consumers |
| Total interface defs | 33 | proportional to real boundaries (~<15) |
| Diagram | 1 strip, truncated at 4096/19026px | one per aspect, each renders fully |
| `MenuItem` entity | absent (wrongly merged) | present, from glossary |
| Duplicate defs (interface/state/port) | present (dedup bug) | none |

## 4. Concrete code touch-points (architect_agent)

- `generate.py` — stages iterate branches; accept tree/tags/glossary from the package.
- `load_package` — read the Analyst's tree/tags/glossary (new contract fields).
- `symbols.py` — seed from the glossary; demote string-normalization convergence.
- `emit.py` — emit per-aspect fragments + a composing package; **fix the interface/state/
  port dedup bug** (currently only action/part/constraint are deduped).
- `sysml.py` / `ArchitectTool.java` — render per-aspect diagrams; a diagram that would still
  exceed the limit must **fail loudly or split**, never silently truncate.
- `handover.py` — structure the handover by aspect (branch → components/functions/
  interfaces/constraints), so the Planner gets epics-worth of grouped design.
- `sdk/how_to.md` — bump the contract; the handover becomes aspect-structured.

## 5. Open questions (carried from the SysML-deliverable review)

- **Is SysML v2 a required deliverable, or internal scaffolding?** Verified: nothing
  downstream reads `model.sysml` (the Planner reads only `planner_handover.json`); SysON is
  not running; the diagram has no automated consumer. If SysML-as-deliverable is not a hard
  requirement, per-aspect generation could target the structured handover + per-aspect
  diagrams directly and demote SysML to an optional export — shedding the 127MB JVM from the
  hot path. **Decision required from the owner before Phase 2 of this plan.**
- **Aspect diagram engine:** keep PlantUML/Smetana (per-aspect, so size is bounded) vs a
  lighter renderer once diagrams are small. Defer until sizes are known.

## 6. Dependencies & sequencing

**Hard dependency:** the Analyst must first emit the tree + tags + glossary in its package
(its plan, Phases 1–3). Until then this plan cannot execute — the Architect has no aspects
to design against.

**Phases (once unblocked):**
1. `load_package` reads tree/tags/glossary; `generate.py` iterates branches (design still
   per-requirement inside a branch, but grouped) — measure auth convergence.
2. Ownership rule + tag-filtered context; glossary-anchored naming; dedup fix.
3. Per-aspect artifacts (fragments + readable diagrams + aspect-structured handover);
   resolve the SysML-deliverable question.
4. Contract bump (`sdk/how_to.md`) + Planner alignment.

## 7a. Generality — verified on a second project (2026-08)

The per-aspect design + built-in refine loop was proven on TWO unrelated projects, to
answer "does this work on every project, not just Restaurant?":

| | Restaurant | Job Matching |
|---|---|---|
| requirements | 60 | 386 |
| domain | food / menus | recruitment |
| total interfaces | 14 | 23 |
| near-duplicate interfaces | 0 | 0 |
| ownership violations | 0 | 0 |
| unowned entities | 0 | 0 |
| refine rounds / time | 1 / 32s | 1 / 44s |

The method is domain-independent (reads package fields; generic prompts). **Honest caveat
from eyeballing the jobs interfaces:** a few *soft* overlaps the 0.80 reranker threshold
does not flag — `ProfileManagementInterface` vs `ProfileUpdateInterface`,
`UserManagementInterface` vs `UserControlInterface`. Far milder than the original
6-auth-interface inflation; a reviewer might merge one or two. This is threshold tuning
(0.80 is deliberately conservative — avoid wrongly merging distinct interfaces), not a
domain-specific failure. Left for the critique+human-review loop to surface.

## 7. Status (living)
- **2026-08 — Plan written.** Queued behind the Analyst redesign.
- **2026-08 — Decision (owner): drop SysML v2 + the 127MB kernel jar.** Deliver diagrams
  (from our own model) + the structured handover. Diagram renderer is the standalone
  PlantUML jar (~22MB, Smetana headless — no GraphViz), 6× lighter and diagram-only.
- **2026-08 — Per-aspect diagram DELIVERY proven (validated by viewing the PNGs).**
  Joined the Restaurant tree (6 branches) to the existing handover by `req_id` and rendered
  one diagram per aspect: readable, reasonably sized, no truncation, no SysML. This proves
  the mechanism and the light renderer.
  - **BUT content is NOT fixed — regrouping ≠ redesign (validated by viewing).** The
    diagrams are built from the OLD per-requirement handover, so they still show the
    inflation: User & Access Control has 3 auth interfaces; Menu & Item Catalog has no
    `MenuItem` (only `Category`) and mis-hosts cross-cutting functions
    (RenderResponsiveUserInterface, ResolveTenantIdentity). Clean content requires the
    Architect to DESIGN per aspect (Phases 1-3 below), not just regroup old output.
  - **Renderer generator (throwaway proof):** `/tmp/gen_aspect_diagrams.py`. Lesson for
    the real emitter: keep to ONE PlantUML diagram mode — mixing `class` with `usecase`/
    `rectangle` errors; functions render as `class <<function>>`.
