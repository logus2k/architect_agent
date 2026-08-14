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

- **FINAL measurement (fix_rounds=1) — DONE: 40 pass / 9 FAIL (was 41/8).** The auto-fix loop worked
  mechanically (regenerated 3 flagged pages, login.html's dead button fixed) but REVEALED a real skill bug:
  the first google-auth skill hardcoded `/auth/google_auth_url` + `/auth/login_with_google`, which don't
  exist (contract uses `/authentication/...`) -> new 405s. Two fixes applied: (a) skill now says "use the
  page's REAL endpoints, never invent /auth/..."; (b) BIGGER — user insight: real Google auth here is NOT
  app-implemented OAuth (registering a new Google client needs manual Console steps) — it is the shared
  **oauth2-proxy** already fronting the domain. REWROTE the google-auth skill to encode THIS environment:
  gate the app's protected routes in `proxy_server/nginx.conf` behind `auth_request /oauth2/auth`
  (`/oauth2/auth-admin` for owner-only), read the user from the `X-Auth-Request-Email` header, and the
  "Sign in with Google" button navigates to `/oauth2/sign_in?rd=...`. Skill now spans frontend+backend+
  DEPLOY. VALID + discovered by Claude+opencode. KEY LESSON: a skill must encode ENVIRONMENT-SPECIFIC
  mechanism (oauth2-proxy/nginx), and skills that need infra (nginx registration) require a DEPLOY-time
  step not yet wired. NOT done: re-verify a regen using the rewritten skill; wire the nginx-registration
  into the deploy stage; the stray guardrail miss (one /auth/ path survived retries under thinking-on).

- **AUTH / proxy-registration design (2026-08-14, user-confirmed).** The generated app must run BEHIND the
  domain oauth2-proxy — that is the dedicated skill's job: register the app's route in
  `proxy_server/conf/nginx.conf` (a `location /<app>/` block, `proxy_pass` to its deploy port) AND gate the
  protected routes with `auth_request /oauth2/auth` (`/oauth2/auth-admin` for owner-only), forwarding
  `X-Auth-Request-Email`. The `google-auth` skill's Deploy/infra section already carries this block.
  TWO ADMINS enabled + verified live: nginx `/oauth2/auth-admin` `allowed_emails` now =
  `logus2k@gmail.com,logus2k.tester.agent@gmail.com` (comma-list; nginx -t + reload OK; live config shows
  both). Test Gmail creds in `~/env/labs/requirements/.env` (key `logus2k.tester.agent`).
  REALITY CHECKS: (1) automating a real Google login (email+password) headless is blocked by Google's bot
  detection — not scriptable; (2) so authenticated APP testing should SIMULATE oauth2-proxy by setting the
  `X-Auth-Request-Email` header in the tester (user vs admin), not drive Google; (3) oauth2-proxy
  cookie-domain=logus2k.com, provider=google, email-domain=* (any user for /oauth2/auth).
  NOT done: wire the DEPLOY stage (deploy_agent) to apply the nginx register+gate block + reload for each
  app; add header-simulated authenticated passes to the tester; re-verify a regen through the rewritten skill.

- **ROOT FIX: Architect auth-design skill — DONE + VERIFIED (2026-08-14).** The auth churn's ROOT was the
  Architect modelling auth as app-implemented OAuth (`login_with_google(authCode)`, `validate_session`).
  Authored `~/.claude/skills/auth-design/SKILL.md` (surface `architecture`): in THIS env auth is
  infrastructure (oauth2-proxy), so DON'T design app-OAuth endpoints — mark protected surfaces
  `auth: required|admin`, read the user from `X-Auth-Request-Email`, deploy registers the nginx gate.
  Wired the Architect to consume skills: new `architect_agent/skills.py` (loader + `retrieval.rerank`
  selection over `metadata.triggers`, threshold 0.005, surface-filtered), injected into
  `aspect_design.design_branch` payload as `MUST_FOLLOW_design_guidance`; mounted `~/.claude/skills ->
  /app/skills` + `SKILLS_DIR` in the architect compose; image rebuilt. VERIFIED: re-designed the auth
  branch -> `login_with_google/validate_session/authCode/session/token` ALL ABSENT (were the root cause);
  now `getAuthenticatedUser`. Skills are now consumed by BOTH Architect (design) and Builder (impl).
  Residual: a `GoogleOAuthLogin` component name lingers (partial adoption); skill could name the header
  explicitly. Confirms the user's insight: fixing the Architect removes auth as an app feature -> Planner
  has no OAuth tasks, Builder no login endpoints/page, backend just reads the header -> whole pipeline eases.

- **DETERMINISTIC env-capability enforcement (2026-08-14) — the change of approach.** After the user's
  critique ("stochastic prompt-adherence for invariants = a ball of mud"), auth is no longer enforced by a
  skill prompt. MEASURED FIRST: the reranker-router we'd agreed on does NOT generalize — it scores auth
  high ONLY when the concept lexically resembles the Restaurant's "authentication" (0.66); a job-board
  "identity/sign_in" (0.008) or clinic "practitioner login" (0.001) scores as low as non-auth — no
  threshold separates them, so it would couple to the Restaurant. Abandoned it. INSTEAD built
  `architect_agent/capabilities.py` — a DETERMINISTIC invariant: strip any operation whose name is a
  CLOSED, UNIVERSAL auth-implementation verb (login/logout/sign_in/authenticate/oauth/validate_session/
  refresh_token/...), drop a service left empty, record the wiring obligation. MEASURED clean (flags
  login_with_google/validate_session, NOT domain nouns schedule_session/consultation_session/
  get_recent_sessions). VERIFIED GENERALIZATION on 2 domains with the SAME code, no project branches:
  Restaurant (real contract: login_with_google+validate_session stripped, authentication service dropped,
  catalog/reservation/tenant_management kept) AND a synthetic job board (sign_in+logout stripped, domain
  kept, get_recent_sessions kept). Wired into `aspect_handover.build` after `_derive_code_contract`; adds
  `environment_capabilities` (the obligation) to the handover; architect image REBUILT (durable). The
  auth-design skill stays as DOCUMENTATION only — no longer load-bearing (a model leak can't propagate).
  HONEST BOUND: ambiguous "register/signup account" — I strip signup/sign_up but not bare "register"
  (avoids register_device/event false positives), so an account-registration op can survive (tester
  catches it). NOT done: downstream consumers of the obligation — Builder backend scaffold
  (get_authenticated_user reads X-Auth-Request-Email) + deploy nginx gate — not built; full-pipeline demo.

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
