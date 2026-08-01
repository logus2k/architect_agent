# Completion Plan — verify the unverified, finish the unfinished

**Status:** executing. Living checklist; each item states how it will be VERIFIED (not just
"done"). Spans architect_agent (primary), analyst_agent, and reqoach — see also
`per_aspect_design_redesign.md`, `../../analyst_agent/documents/vocabulary_and_structure_redesign.md`,
`../../labs/requirements/documents/project_git_repo_requirement.md`.

## Where we are
- Analyst vocabulary+tree+package: LIVE, verified. Per-aspect design+refine+critique:
  verified on two projects (Restaurant 60, Jobs 386) — 0 near-dup, 0 ownership, 0 unowned.
- But the new flow runs as **standalone modules I invoke by hand** — it is NOT the
  Architect's pipeline, produces no package, emits no diagrams, and the contract is unbumped.

## Phase A — Architect new pipeline (keystone; everything hangs off a real package)
- [ ] A1. `load_package` reads `glossary`/`tags`/`tree` from the Analyst package.
      *Verify:* unit test loads a fixture package, asserts fields present.
- [ ] A2. Mermaid diagram emitter — one `.mmd` per aspect from the design.
      *Verify:* render a sample to SVG/PNG (dev-only) and VIEW it; ship the `.mmd` text.
- [ ] A3. Aspect-structured handover (`planner_handover.json`) from the per-aspect design
      (by_requirement + by_aspect + components/interfaces/consumes + open issues).
      *Verify:* unit test asserts shape; Planner reader (`architecture.py`) still parses it.
- [ ] A4. New pipeline entry: package → design_aspects → refine → emit handover + mermaid +
      artifacts, replacing the SysML generation path. Drop the SysML jar dependency.
      *Verify:* end-to-end run on Restaurant; read metrics; VIEW one mermaid diagram.
- [ ] A5. Contract bump `sdk/how_to.md`: aspect-structured handover + mermaid, no SysML.
      *Verify:* doc matches the emitted artifact keys.

## Phase B — Test coverage for the new modules (GPU-free)
- [ ] B1. Unit tests for `aspect_design.py` (mock AgentClient) — parsing, adapters.
- [ ] B2. Unit tests for `refine.py` (mock client) — reconcile strips non-owners, loop bound,
      escalation. *Verify:* pytest green.
- [ ] B3. Exercise + test the `misassignment` critique check (currently never run).
- [ ] B4. Threshold note: soft interface overlaps (ProfileManagement/Update). Decide — leave
      to human review (recommended) or lower the near-dup threshold and re-measure both
      projects. *Verify:* whichever, re-run and read the counts.

## Phase C — reqoach + infra (authorized)
- [ ] C1. Wire local repo creation into project creation (reqoach intercepts create).
      *Verify:* create a project → repo exists at `~/env/project-repos/<pid>` with layout.
- [ ] C2. nginx per-agent edge routes (`/analyst/`, `/architect/`, …) + retire the bff proxy.
      *Verify:* `curl logus2k.com/analyst/health` (or equivalent) routes to the Analyst.
- [ ] C3. Agents write outputs into the project repo (Analyst `requirements/`, Architect
      `architecture/`). *Verify:* run each, read the committed files under the repo.
- [ ] C4. GitHub remote pending-action surfaced in the UI (token via use-once paste).
      *Verify:* pending action visible; local push to a test remote works with a throwaway token.

## Phase D — Analyst loose ends
- [ ] D1. `structure:run` verified through the AUTHENTICATED endpoint (only in-container so far).
- [ ] D2. Glossary under-merge (images/descriptions) — the LLM-canonicalizer is conservative;
      decide if the residual split is acceptable (it is, for now) or tighten. *Verify:* re-run,
      read term count.

## Execution order
A (keystone) → B (lock it with tests) → C (infra) → D (loose ends). Within A: A1→A3→A2→A4→A5.
GPU-heavy steps (A4 end-to-end, C3 Architect run) gated on GPU availability.

## Status log
- 2026-08 — plan written.
- 2026-08 — Phase A: A1-A4 built + verified. New per-aspect pipeline
  (`aspect_pipeline.py`) runs end-to-end, no SysML/jar; emits aspect-structured
  `planner_handover.json` (contract 2.0, req_id-keyed) + per-aspect Mermaid diagrams +
  artifacts. 12 unit tests (mermaid/handover/critique) + end-to-end Restaurant run + a real
  diagram VIEWED. A5 (contract bump) remaining.
  - HONEST caveats: (1) run-to-run non-determinism — one run 0 issues/1 round, another 3/2;
    (2) `consumed_but_unowned` over-eager on EXTERNAL deps/primitives (flagged LLM, Language,
    Timestamp as gaps) — needs to distinguish external from internal (follow-up B-ish);
    (3) minor design quirks (an attribute modelled as a component; an aspect consuming a
    concern it also owns).
- 2026-08 — **DEPLOYED** the per-aspect pipeline (todo #3, Architect side). VERIFIED:
  - A4/deploy: `aspect_pipeline.py` now has a CLI (`python -m architect_agent.aspect_pipeline
    <PID|package.json>`), fetches the Analyst package over HTTP or reads a local file
    (`load_package`), publishes to `$ARCHITECT_DATA_DIR/architecture/<pid>` (real bind-mount,
    NOT /tmp). Dockerfile slimmed to `python:3.12-slim` — **JDK build stage + 127MB jar +
    SysML toolchain removed**. `docker compose build` succeeds; container runs the new CLI
    (verified `--help` + `load_package` local-file). 65 tests still green.
  - A5: `sdk/how_to.md` §2 (files: no model.sysml/symbols.json; diagrams are `.mmd`) and §7
    (regenerate = the new CLI) updated to 2.0; top note reconciled.
  - D1 (partial): `/projects/{pid}/structure:run` confirmed **registered in the running
    analyst-agent container** and auth-gated (blanket 401 without an oauth2 session). Happy
    path needs a browser login — cannot exercise headless; wiring is live.
  - STILL OPEN (user-gated infra unit C): reqoach lifecycle backend does not exist yet (reqqa
    src = bff.py + repo.py only); retiring bff + per-agent edge routes + frontend rewire
    touches the LIVE logus2k.com product — needs the user's go. Seam decided: Architect
    publishes to `architecture/`; **reqoach** (git author identity) commits agent outputs.
