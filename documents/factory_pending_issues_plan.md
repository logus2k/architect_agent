# FACTORY — Pending Issues Plan (2026-08-14)

Closes the items left open after the auth-infrastructure work. Ordered by: deterministic + no-GPU +
completable first; the app-quality items (need a pipeline re-run) last. Each has a **Done when** check.

## P1 — Backend `get_authenticated_user` scaffold (deterministic, no GPU)
The Architect now records an `environment_capabilities` auth obligation and strips app-auth ops. The
Builder must SCAFFOLD (deterministic code, not model-generated) a `get_authenticated_user()` that returns
the `X-Auth-Request-Email` header when that obligation is present.
**Where:** `builder/contract_scaffold.py` (a scaffolded module `app/security.py` + wire into the app).
**Done when:** a built app exposes an endpoint/util returning the header value; unit-tested by setting the
header and asserting it's read (no model, deterministic).

## P2 — Recreate the live reqqa container from the durable image
The reqqa image bakes the frontend now, but `requirements-reqoach-1` still runs the old image.
**Do:** capture its run spec (`docker inspect`), recreate from `reqqa-orchestration:latest`.
**Done when:** the recreated container serves the Product/Operation lanes from the BAKED image (no docker cp).

## P3 — deploy_agent auto-invokes `nginx_register_app`
After a deploy, the deploy stage should register the app behind oauth2-proxy automatically.
**Do:** deploy_agent computes `suffix` = slug(project_name), `port` = deploy port, reads the handover's
`environment_capabilities` (auth ⇒ gate), and calls the MCP tool (via the MCP service's invoke endpoint).
**Done when:** a `deploy:run` results in a registered, gated route (curl → 302 → Google) with no manual tool call.

## P4 — Public-vs-admin per-path gating in the tool
`nginx_register_app` currently gates the whole `/suffix/`. It must gate only ADMIN paths (from the product
spec's admin surface screens) and leave the public storefront open.
**Do:** add `admin_paths: [..]` (or `public: true` + gated admin prefix); emit a gated location per admin
path + an ungated catch-all.
**Done when:** curl a public page → 200 (app), curl an admin page → 302 (Google).

## P5 — App-state gaps (live app 40/9: dead buttons, incomplete journeys)
Root cause is upstream and now fixed at the Architect (auth out of the contract ⇒ no broken login page).
The honest closure is a pipeline re-run from the fixed Architect, then the tester+fix-loop drives the rest.
**Do:** (after P1–P4) run Architect→Planner→Builder→Deploy→Test once for the fixture; loop remaining UI fails.
**Done when:** tester dimensions are clean OR every residual FAIL is a stated, understood item — measured, not assumed.

## P6 — Two-admin EFFECT (BLOCKED, state honestly)
Confirming `logus2k.tester.agent@gmail.com` passes `/oauth2/auth-admin` needs a real Google login, which
is blocked to headless automation. **Cannot** be auto-verified. The config is applied+valid; the effect is
verifiable only by a human logging in once. Stated as a known limit, not silently "done".

## Order
P1 → P2 → P3 → P4 (all completable/verifiable without a heavy run), then P5 (the demonstration run), P6 noted.

---

## PROGRESS LOG (2026-08-14)

- **P1 — DONE + VERIFIED.** Builder scaffolds `app/security.py` (`get_authenticated_user`/`require_user`
  reading `X-Auth-Request-Email`) + a `/whoami` route, gated on the handover's auth obligation
  (`build.py` `auth_required`; `contract_scaffold.scaffold_security` + `scaffold_api(auth=...)`; kept in
  finalize). Booted a scaffolded app: anon → `{authenticated:false,email:null}`, header →
  `{authenticated:true,email:"alice@…"}`, real routes intact. Builder image rebuilt (live).
- **P2 — DONE + VERIFIED.** reqoach recreated on a freshly-rebuilt `Dockerfile.orchestration` image
  (slim, `reqqa.bff:7802`, frontend baked). Serves overview 97817 B, all lanes, restarts=0, no runtime
  overrides. Fixed a latent hazard: the `reqqa-orchestration:latest` tag had been overwritten by an
  unrelated CUDA build (`reqqa.api:5601`); a naive `compose up` would have crash-looped. Now correct.
- **P3 — DONE + VERIFIED.** `deploy.py` auto-invokes `nginx_register_app` via the MCP invoke endpoint
  (`POST /tools/nginx_register_app/invoke?app=factory`) after a deploy; gating driven by the obligation.
  Real `deploy:run` registered `/restaurant-menu-manager/` (validated+reloaded); route live (HTTP 200).
- **P4 — DONE + VERIFIED.** Tool extended with `public` + `admin_prefix` (sound, PREFIX-based → no
  "page gated, API open" leak; admin `proxy_pass …/admin/` preserves the app's admin routes). Synthetic
  proof through the live proxy: public base → 200 (app body); `/admin/…` → 302 → Google (state carries
  the return path). MCP image rebuilt (live).
- **P5 finding + fix — obligation now derives from PRODUCT SURFACES (not stripped verbs).** The first
  re-run exposed the real defect: with a clean design (no auth verbs emitted, the auth-design skill
  working) `strip_app_auth` removed nothing, so NO obligation fired — yet the app has an `admin` surface
  that must be gated. Fixed deterministically: `capabilities.auth_obligation(removed, product_spec)` now
  reads `product_spec.surfaces/screens` (`audience`, admin surface) as the AUTHORITATIVE signal and emits
  a `gating` recommendation (`{public, admin_prefix}`) from the public/admin split; strip stays as
  belt-and-suspenders. Threaded through `aspect_pipeline.run` (loads `product/product_spec.json`) →
  `aspect_handover.build(product_spec=…)`. Deploy consumes `gating`. Re-ran Architect: obligation now
  fires with `gating={public:true, admin_prefix:"admin"}`, `removed:[]`. Unit-tested on the real spec +
  edge cases (fully-public → none; fully-auth → whole-route gate; strip-fallback).
- **P5 run — IN PROGRESS.** Architect ✓ (40s, obligation fires) → Planner ✓ (86 tasks) → Builder
  (running, now scaffolds the auth seam) → Deploy → Tester (to re-measure the app state).
- **KNOWN REMAINING COUPLING (honest):** nginx admin-gating binds only once the Builder serves its admin
  surface (pages AND their APIs) under the `/admin/` prefix. Until then the `admin_prefix` gate is inert
  (flat admin pages fall under the public base = open). The MECHANISM is proven (P4); the Builder `/admin`
  convention is the follow-through. For this run the app is registered public so it stays testable.
- **P6 — BLOCKED (stated).** Two-admin effect needs a real interactive Google login; config applied +
  `nginx -t` valid; not auto-verifiable.

## P5 RESULT — full run completed + app-state MEASURED (2026-08-14)
Chain ran end-to-end: Architect ✓ → Planner ✓ (86 tasks) → Builder ✓ (74/82 built, runnable) → Deploy ✓
(healthy, auto-registered public base + gated `/admin/`) → Tester ✓. **AUTH INFRA VERIFIED LIVE**: `/whoami`
reads the header, public storefront → 200, `/admin/` → 302. Fixed a real Builder bug on the way: finalize
called `scaffold_api` twice, the 2nd without `auth`, clobbering `/whoami` (both sites now pass `auth`).

**Measured app-state: 29 PASS / 27 FAIL (56 tests).** Dimensions: api 16/23, crud 8/14, journey 2/4,
ui 1/7, ui_journey 2/4, llm_journey 0/4. **Dominant root cause (18/27): model misuses the persistence
seam** — custom (non-CRUD) bodies call `repo.get/create/list(...)` on the FACTORY FUNCTION instead of
`repo("<entity>").get(...)` → `AttributeError: 'function' object has no attribute 'get'` → HTTP 500. The
scaffold's own CRUD bodies are correct; only model-filled custom ops are wrong. finalize doesn't catch it
(module parses + exports intact; it's a RUNTIME error). Remaining: 3 update→None (op lacks an id param),
3 list-empty round-trips, a few 422s, UI dead-button asserts. NOTE: the tester→builder FIX LOOP did NOT
run this pass (`fix_rounds: []`), so none were iterated.

**NEXT (decision):** (a) DETERMINISTIC seam-hardening in the Builder so `repo` cannot be misused (e.g.
give each service a bound `store = repo("<entity>")` and/or a finalize repair that rewrites bare
`repo.<method>(` → `repo("<entity>").<method>(`) — kills the 18 500s at the source, matches the
"invariants = deterministic code" principle; caveat: multi-store modules need per-call entity selection.
(b) run the tester→builder stochastic fix loop (has the error context, fixes one-at-a-time). P5 is
MEASURED but the failures are NOT yet fixed — **NOT done: app is 29/56.**

## FIX — Option A DONE (deterministic seam repair), Option B next (user chose "A then B")
- **A implemented + verified.** New `builder/repo_seam.py`: AST-locates every bare `repo.<crud>(` (a Call
  whose func is an Attribute on `Name('repo')`) and does a POSITION-PRECISE text edit (no regex, comments
  preserved) binding it to a concrete store — the service's single depended-on entity when unambiguous
  (backoffice→tenant, public_display→location: EXACT), else the primary entity as a crash-stop
  (tenant_management→tenant: 5 ambiguous, deferred to B). Wired into build.py after finalize; builder image
  rebuilt. Applied to the live restaurant code (10 sites / 3 modules; none remain). Booted a copy +
  redeployed: the previously-500 endpoints (`get_tenant_dashboard_data`, `get_location_details`) now return
  200; `upload_image`/`submit_contact_form` now 422 (proper request validation, not a crash). The
  AttributeError-500 CLASS is eliminated deterministically.
- **B next:** run the tester→builder fix loop for the residual — the 5 ambiguous multi-store bindings
  (bind the exact store per call) + the non-seam fails (update ops lacking an id param, dead-button UI).
  Re-measuring now (tester re-run) to quantify A's gain before B.
