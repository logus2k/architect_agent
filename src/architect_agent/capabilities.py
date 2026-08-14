"""Deterministic enforcement of ENVIRONMENT-PROVIDED capabilities.

Some cross-cutting concerns are provided by the FACTORY *environment*, not by each app. AUTHENTICATION is
one: a shared oauth2-proxy performs the Google sign-in and injects the user's email as the
`X-Auth-Request-Email` request header, so an app must implement NO authentication itself. We enforce that
**deterministically**, so the invariant holds regardless of what the (stochastic) design model emitted —
never by hoping a prompt is obeyed.

Detection uses a CLOSED, domain-agnostic vocabulary of auth *implementation verbs* (login, logout,
sign_in, authenticate, oauth, authCode, validate_session, refresh_token, …). These mean "authentication"
in every domain, unlike ambiguous domain nouns ("session" in `consultation_session` / `schedule_session`),
which is why it generalises instead of coupling to any one project's naming. MEASURED: it flags
`login_with_google` / `validate_session` while leaving `schedule_session` / `consultation_session` /
`get_recent_sessions` untouched.

The model may still *classify* which surfaces need a signed-in user (a reliable binary judgment) — that is
expressed as an `auth` attribute elsewhere; this module only guarantees the app builds no auth code.
"""

from __future__ import annotations

#: Closed, universal auth-IMPLEMENTATION tokens. Substring match on an operation symbol. Specific enough
#: (`validate_session`, not bare `session`) to avoid domain-noun false positives.
_AUTH_OP_TOKENS = (
    "login", "logout", "signin", "sign_in", "signup", "sign_up", "authenticate", "authentication",
    "oauth", "authcode", "auth_code", "exchange_code", "validate_session", "create_session",
    "refresh_token", "verify_token", "session_token", "issue_token", "revoke_token", "google_auth",
)


def is_auth_operation(symbol: str) -> bool:
    """True if an operation name is an auth-implementation verb (universal, domain-agnostic)."""
    n = (symbol or "").lower()
    return any(tok in n for tok in _AUTH_OP_TOKENS)


def strip_app_auth(contract: dict) -> tuple[dict, list[dict]]:
    """Remove every app-implemented auth operation from the code contract (auth is provided by the
    environment's oauth2-proxy). A service concept left with no operations is dropped entirely. Mutates
    and returns `contract`, plus the list of removed items. Deterministic and generic."""
    removed: list[dict] = []
    for key in list(contract):
        v = contract[key]
        exports = v.get("exports") or []
        kept = []
        for e in exports:
            if e.get("kind") == "function" and is_auth_operation(e.get("symbol", "")):
                removed.append({"concept": key, "op": e.get("symbol")})
            else:
                kept.append(e)
        v["exports"] = kept
        if v.get("kind") == "service" and not kept:
            del contract[key]
            removed.append({"concept": key, "op": "<empty auth service dropped>"})
    return contract, removed


def _needs_auth_surface(product_spec: dict) -> tuple[bool, bool, bool]:
    """Read the PRODUCT spec's surfaces/screens and decide the app's auth shape. Returns
    (needs_auth, has_public, has_admin):
      * needs_auth — any surface/screen requires a signed-in user (audience != 'public');
      * has_public — at least one surface/screen is open to anyone (audience == 'public');
      * has_admin  — a distinct admin surface exists (id/surface == 'admin').
    This is the AUTHORITATIVE signal — it reflects a product decision ("who may see this"), not whether
    the design model happened to emit an auth verb. Deterministic; a missing/blank spec ⇒ all False."""
    ps = product_spec or {}
    surfaces = ps.get("surfaces") or []
    screens = ps.get("screens") or []
    def _aud(x):
        return str((x or {}).get("audience", "")).strip().lower()
    def _sid(x):
        return str((x or {}).get("id", (x or {}).get("surface", ""))).strip().lower()
    auds = [_aud(s) for s in surfaces] + [_aud(s) for s in screens]
    needs_auth = any(a and a != "public" for a in auds)
    has_public = any(a == "public" for a in auds)
    has_admin = any(_sid(s) == "admin" for s in surfaces) or \
                any(str((s or {}).get("surface", "")).strip().lower() == "admin" for s in screens)
    return needs_auth, has_public, has_admin


def auth_obligation(removed: list[dict], product_spec: dict | None = None) -> dict | None:
    """The environment must provide authentication when EITHER the product spec declares a surface that
    needs a signed-in user (the authoritative signal) OR the design emitted app-auth ops we stripped
    (belt-and-suspenders). Records the wiring obligation for the deploy stage (gate behind oauth2-proxy)
    and the backend (read X-Auth-Request-Email), plus a deterministic GATING recommendation derived from
    the public/admin surface split so deploy knows whether to keep a public storefront open. Generic."""
    needs_auth, has_public, has_admin = _needs_auth_surface(product_spec or {})
    if not needs_auth and not removed:
        return None
    # Gating recommendation: an app with BOTH a public surface and an admin surface keeps the base open
    # and gates the admin area (public storefront must not require login); an app that is authenticated
    # throughout gates the whole route. Purely from the product surface split — no guessing.
    if has_public and has_admin:
        gating = {"public": True, "admin_prefix": "admin"}
    elif has_public and needs_auth:
        # public pages plus some authenticated actions but no distinct admin surface: keep the app open
        # at the edge; the app itself gates the protected actions in-code via get_authenticated_user.
        gating = {"public": True, "admin_prefix": None}
    else:
        gating = {"public": False, "admin_prefix": None}   # whole route gated (nothing public)
    return {
        "capability": "authentication",
        "provided_by": "environment (oauth2-proxy)",
        "reason": ("product surfaces require a signed-in user" if needs_auth
                   else "design emitted app-auth operations (stripped)"),
        "surface_signal": {"needs_auth": needs_auth, "has_public": has_public, "has_admin": has_admin},
        "gating": gating,
        "removed": removed,
        "wiring": {
            "deploy": "register the app behind oauth2-proxy in nginx via nginx_register_app "
                      "(public base + admin_prefix gate, or whole-route gate per `gating`)",
            "backend": "read the authenticated user from the X-Auth-Request-Email request header "
                       "(no login/session code)",
        },
    }
