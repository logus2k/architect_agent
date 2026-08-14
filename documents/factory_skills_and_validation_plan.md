# FACTORY — Skills & Validation Remediation Plan

_Authored 2026-08-13. Fixes the class of bug the tester now catches: the delivered app **looks** right
but its interactions are broken (dead "Sign in with Google" / "Send Message" / "Save Configuration"
buttons, fake AI returning `{status:"processing"}`, invented endpoints → 405, creates that never
complete). Root cause: the builder's model **fakes integrations it doesn't know how to build**. The fix
is vetted **skills** (real implementation patterns) + guardrails, with the tester as the safety net._

Each item states **Done when** — a verifiable check, not an assertion. Order: fix root causes (Phase 1–2),
close the loop (Phase 3), pay down debt (Phase 4), then the deeper initiative (Phase 5).

## Context already established (verified)
- opencode v1.18.15 has **native skills** (`SKILL.md`, `name`+`description` frontmatter), loaded on-demand
  by an opencode **agent** via a `skill` tool. Search paths include `~/.claude/skills/` (Claude-compatible).
- One `SKILL.md` in `~/.claude/skills/` is discovered by **both** Claude Code and opencode+local gemma
  (verified: both listed `local-llm`).
- The builder does most generation via **direct model completions** (fast) — the opencode `skill` tool is
  NOT in that path. Hybrid decision: **opencode agent for capability-bearing generation**, direct
  completion for bulk scaffolding.
- `~/.claude/skills/local-llm/SKILL.md` authored; its **text** pattern verified live off `:8500`.

## PROGRESS LOG (2026-08-13)
- **P1.1 google-auth — DONE.** `~/.claude/skills/google-auth/SKILL.md`; discovered by opencode+local model
  and Claude Code; real OAuth2 path + dev sign-in that still issues a session and advances the UI.
- **P1.2 file-upload — DONE.** `~/.claude/skills/file-upload/SKILL.md`; multipart body upload + FastAPI
  `UploadFile`; discovered by both; frontmatter valid.
- **P1.3 local-llm text — DONE (verified live off :8500).** Vision — DONE but **vision is UNAVAILABLE on
  this server**: gemma-4-12b is loaded text-only (no `--mmproj`); the skill now PROBES capability and falls
  back to a real text description (probe verified to return False here). So no fake vision.
- **P1.4 wire builder — DONE (delivery works) + honest gap.** Delivery = INJECTION into the direct-
  completion path. Built `builder/skills.py` (loads SKILL.md, selects by the house reranker over a
  `metadata.triggers` phrase; floor 0.005 cleanly separates match from no-match; requires a declared
  `surfaces` so harness skills like `ci-ready` don't leak); injected into `frontend._prompt_product`;
  mounted `~/.claude/skills -> /app/skills` in the builder compose + `SKILLS_DIR`/`EMBEDDINGS_URL`; builder
  image rebuilt. VERIFIED in-container: skills load, right skill selected per requirement, none for CRUD.
  END-TO-END VERIFIED PARTIAL: after a skills-injected regen + redeploy, `reservation_form.html`'s "Sign in
  with Google" button is **no longer dead** (adopted the real session_token/localStorage/advance pattern) —
  but `login.html` **still dead**: the model wrote a placeholder `alert("Redirecting…")` instead of the
  skill's dev-signin call. So skills MATERIALLY reduce fakes but adoption is not 100% (model variance).
  CLOSER = P3.6 auto-fix loop (tester flags the residual dead button -> regenerate with the skill + the
  specific failure). Also worth: strengthen the prompt to forbid placeholder `alert()` stubs.

- **P2.5 invented-endpoint guardrail — DONE (detector verified).** `frontend._fetch_paths` (lexical scan,
  no regex) + `_invented_endpoints`: any same-origin `fetch()` path that is not a real contract endpoint,
  not a page/asset (`.html/.css/...`), and not infra (`/uploads,/health,...`) is flagged as invented.
  Wired into the generation retry loop — an invented call triggers a corrective regeneration with the real
  endpoint allowlist. VERIFIED: flags `/menu_management/get_counts` + `/reservation_management/get_recent`
  (the real 405 offenders) while ignoring real endpoints, navs, uploads, external URLs.

- **P3.6 frontend auto-fix loop — CODE DONE (compiled+deployed); verification PENDING GPU.**
  `frontend.regenerate_page(slug, report)` rebuilds one page with skills + guardrail + the tester report as
  a correction; `build.fix_page`; API `POST /projects/{pid}/builder:fix-page` (route live). Tester
  `_fix_frontend_round` loops each `ui` FAIL page to builder:fix-page; the run loop now fixes BOTH backend
  500s (builder:fix) AND broken pages (builder:fix-page) per round, re-testing from the updated repo (no
  redeploy needed — the tester boots from code/). NOT yet run end-to-end (regeneration needs the model/GPU,
  currently on hold) and images not yet rebuilt durable.
- **P4.7 reqqa durability — Dockerfile FIXED + image rebuilt + BAKE VERIFIED.** The reqqa Dockerfile never
  COPY'd `frontend/` (why the Overview/tester UI was always `docker cp`'d, reverting on recreate). Added
  `COPY frontend/ frontend/`; rebuilt `reqqa-orchestration:latest`. VERIFIED the image now contains the full
  frontend (product.html present; overview.html has the Product lane) — durable. REMAINING: recreate the
  live `requirements-reqoach-1` from the new image to adopt it (deferred — no compose found; the running
  container still serves the docker-cp'd copy, which matches on-disk, so it works until recreated).

## Phase 1 — Skills → real integrations (root cause)
1. **Author `google-auth` skill** (sign-in that actually sets a session and advances the UI; real OAuth
   redirect/callback pattern + a clearly-labelled dev fallback that still authenticates).
   **Done when:** opencode + Claude list it; its code pattern runs and returns a session.
2. **Author `file-upload` skill** (multipart to a real endpoint; never a base64 blob in the query string).
   **Done when:** listed by both; a sample multipart POST to a scaffold endpoint succeeds.
3. **Verify `local-llm` vision** against `:8500` with a real image data-URI.
   **Done when:** the vision call returns an on-topic caption (currently UNVERIFIED).
4. **Wire the builder to use skills:** mount `~/.claude/skills` into the builder container; set
   `opencode.json` `permission.skill:{"*":"allow"}`; route capability features (AI description, Google
   sign-in, image upload) through an **opencode agent** (keep direct completion for bulk).
   **Done when:** a fresh build's AI-description endpoint calls the LLM for real, and the auth/upload
   buttons produce an effect (tester dead-button/journey gates pass for them).

## Phase 2 — Guardrail: no invented endpoints
5. **Constrain generation to the contract.** After frontend gen, scan each page's `fetch()` paths against
   the live OpenAPI; any unknown path → regenerate that page. (Optionally expose the contract as an MCP
   tool for opencode paths so it can only call real endpoints.)
   **Done when:** the tester ui gate shows zero invented-endpoint 405s.

## Phase 3 — Close the validation loop (frontend auto-fix)
6. **`builder:fix-page`.** The tester loops each flagged page (dead button / dead link / invented endpoint
   / non-completing journey) back with the failure report; the builder regenerates that page; re-test; N
   rounds — the frontend analog of the existing backend 500-loop.
   **Done when:** a flagged page is auto-regenerated and its gate flips PASS.

## Phase 4 — Pay down debt (before any "big run")
7. **Durability:** rebuild the reqqa image (or mount its source) so the Overview lanes (Product, Operation)
   and the tester UI changes survive a container recreate — they are currently `docker cp`'d.
   **Done when:** recreate `requirements-reqoach-1` and the lanes + dead-button gate are still present.
8. **Root-cause `make_reservation`** (app bug vs flow-too-complex). **Done when:** stated with evidence.
9. **Measure the full gate runtime** with the dead-button per-button reloads; optimise if too slow.
   **Done when:** a full `tester:run` completes in a measured, acceptable time.
10. **Frontend `thinking-off` default** decision (currently env-only). **Done when:** set intentionally
    with a one-page speed/quality check.

## Phase 5 — Deeper (separate initiative)
11. **Architect/backend consume the product spec** so "authenticated" surfaces get **real auth** (ties to
    `google-auth`) and services/entities are shaped by personas/journeys — not only the frontend.

## Recommended order
1 → 2 → 3, then 7 (durability) before any big run, then 8–10 cleanup, then 11 as its own initiative.
Phases 1–3 turn the app from "looks right, broken interactions" into "actually works."
