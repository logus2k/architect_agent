"""Architect PROPORTIONALITY review — the missing 'is this complexity justified?' gate.

The design/critique/completeness judges all check whether the design is STRUCTURALLY sound and
REALIZES its requirements. None asks the common-sense question a human reviewer asks first: is the
design NO MORE COMPLEX than the requirements demand? A store-some-rows app does not need an ORM and
a database server; forcing that machinery in is over-engineering — and (with a weak local code
generator) it is precisely where the build breaks (column-type footguns, session wiring, circular
relationships) on complexity nobody asked for.

The crucial axis is ORM-vs-stdlib, NOT relational-vs-not. The standard library's embedded database
(Python's `sqlite3`) is ITSELF relational: tables, foreign keys, parent/child links, transactions.
So related entities NEVER justify an ORM by themselves — sqlite3 already covers them. An ORM /
database server is justified only by a SPECIFIC STATED need (reporting/analytics, schema migrations,
multi-engine portability, large-scale concurrency, explicit multi-entity transactions).

Weak local models have a hard prior ("many related entities => ORM + Postgres") and will fabricate a
justification ("transactional integrity") that no requirement states. So we do NOT trust the model's
holistic verdict: the model only EXTRACTS candidate justifications WITH A VERBATIM REQUIREMENT QUOTE,
and this module VERIFIES each quote actually occurs in the requirements (a lexical substring check —
does this literal text appear) and DECIDES in code. A fabricated quote fails the check and is
dropped. This mirrors design_judge, which likewise derives its verdict in code rather than trusting
the model's own flag.

The decided `sanctioned_dependencies` is the top-down allow-list the Builder enforces
(builder.verify.unsanctioned_deps): the design owns the stack; code importing a library nobody
sanctioned is rejected, not accepted.

PROPORTIONALITY_SYSTEM_PROMPT below is the source of truth; registered as
`architect_proportionality_judge` in agent_server (re-register via the admin API).
"""

from __future__ import annotations

PROPORTIONALITY_AGENT = "architect_proportionality_judge"

#: Persistence machinery the model must never smuggle into base_dependencies — whether an ORM is
#: warranted is decided from verified drivers, not from the model listing it as a "base" dep.
_PERSISTENCE_PKGS = {"sqlalchemy", "sqlmodel", "databases", "psycopg2", "psycopg2-binary",
                     "psycopg", "asyncpg", "pymysql", "mysqlclient", "peewee", "tortoise-orm",
                     "pony", "mongoengine", "pymongo", "alembic", "django"}

#: Defining vocabulary each driver's requirement quote MUST contain. The model proposes a driver;
#: code accepts it only if the cited requirement actually uses that driver's language. This stops
#: the recurring misclassification where the model labels ANYTHING "reporting" — a management
#: dashboard, or "generate an AI description" — none of which carry reporting vocabulary. Lexical
#: (does this literal term appear), never semantic.
_DRIVER_KEYWORDS = {
    "reporting": ["report", "analytic", "aggregat", "metric", "statistic", "kpi", "insight",
                  "trend", "breakdown", "group by", "dashboard of"],
    "adhoc_query": ["ad-hoc", "ad hoc", "adhoc", "query", "querying", "filter across",
                    "search across", "join"],
    "migrations": ["migrat", "schema change", "schema evolv", "schema version", "alter the schema",
                   "evolve the schema"],
    "portability": ["database engine", "multiple database", "pluggable database", "postgres",
                    "mysql", "swap database", "different database", "any database"],
}

#: A verified driver -> the persistence stack it sanctions (added on top of base deps in code).
#: Only drivers an ORM GENUINELY addresses that stdlib sqlite3 does not. Deliberately EXCLUDES
#: "scale" (an ORM does not provide scale — that is a DB-server choice) and "transactions" (sqlite3
#: is fully ACID via the stdlib) — those two were pure false-positive vectors on trivial/placeholder
#: text ("support 5 concurrent users", "Define performance targets") and never justify an ORM.
_DRIVER_STACK = {
    "reporting": ["sqlalchemy"], "adhoc_query": ["sqlalchemy"],
    "migrations": ["sqlalchemy", "alembic"], "portability": ["sqlalchemy"],
}

PROPORTIONALITY_SYSTEM_PROMPT = """\
You are a software-architecture PROPORTIONALITY reviewer. You are given the FULL set of product REQUIREMENTS and the design's DATA MODEL (persisted entities). The correct architecture is the SIMPLEST one that satisfies the STATED needs — unrequested complexity is a defect, not sophistication.

The proportionate DEFAULT for persistence is the standard library's built-in embedded relational database (Python's `sqlite3`), used directly with simple SQL and NO ORM. sqlite3 is ITSELF relational: it handles tables, foreign keys, parent/child relationships, and transactions. Therefore the mere presence of related entities (an item belongs to a tenant; a menu has categories) is NOT a reason for an ORM — sqlite3 already covers it. Do NOT reason "these entities are related, so it needs a relational database / ORM": that default is already relational.

An ORM (such as SQLAlchemy) is justified ONLY by a SPECIFIC need that a requirement LITERALLY STATES and that an ORM genuinely addresses (things stdlib sqlite3 + simple SQL do NOT already do). For each such need, output the driver AND the VERBATIM requirement text (copied word-for-word from the requirements above) that states it. The ONLY valid drivers are:
- reporting  : a requirement asks the system to GENERATE reports / analytics / aggregations / computed metrics or statistics OVER the data. Merely viewing, listing, or editing records is NOT reporting.
- adhoc_query: a requirement asks for complex or user-defined querying / filtering across many entities.
- migrations : a requirement states the database schema must evolve / migrate over time.
- portability: a requirement states support for multiple or pluggable database engines.

These are NOT drivers (do not output them):
- A management / settings / admin / configuration DASHBOARD (a UI to view or edit records or settings, e.g. "a dashboard to manage the tenant's configuration"): that is ordinary CRUD behind a UI, NOT reporting. Only GENERATING analytics/aggregations/metrics over the data counts as reporting. NEVER a driver.
- Concurrency or scale (e.g. "support at least 5 concurrent users", "expected concurrent load"): sqlite3 handles ordinary concurrency, and an ORM does not provide scale anyway. NEVER a driver.
- Transactions / atomicity (e.g. "save the order and its items together"): sqlite3 is fully transactional via the standard library. NEVER a driver.
- Placeholder / meta requirements (e.g. "Define performance targets", "[specify maximum number] ..."): these state no concrete need. NEVER a driver.
- Ordinary CRUD ("create / update / store / save / display / list X"): NEVER a driver.

Rules: Do NOT invent a driver. Do NOT paraphrase — the `quote` must be copied verbatim from a requirement, or it will be rejected. If no requirement literally states one of the FOUR valid needs, return an EMPTY `orm_drivers` list — that is the expected, correct answer for a CRUD-over-related-entities app, and it means the app uses stdlib sqlite3 with no ORM.

Separately, in `base_dependencies` list the BACKEND Python packages (PyPI names) the non-persistence requirements justify (e.g. a web framework for an HTTP API; an auth library only if login is required). Rules for this list: Python/PyPI packages ONLY — NEVER frontend or JavaScript/CSS libraries (e.g. leaflet, mapbox-gl, react, vue, bootstrap): the frontend is separate and is not pip-installed. Do NOT put any ORM or database driver here — persistence packages are decided from the drivers above. (The build guarantees the chosen web framework separately, so it is fine to include it or not.)

Output ONLY JSON:
{"orm_drivers": [{"driver": "reporting|adhoc_query|migrations|portability", "quote": "<verbatim requirement text>"}],
 "base_dependencies": ["<pypi-name>", ...],
 "over_engineering": [{"element": "<what>", "why": "<complexity the requirements do not justify>", "simpler": "<the proportionate approach>"}],
 "confidence": 0.0-1.0}
No commentary, no markdown fences."""


def _entity_lines(entities: list[dict]) -> str:
    out = []
    for e in entities:
        name = e.get("name") or ""
        resp = e.get("responsibility") or e.get("purpose") or ""
        attrs = ", ".join(a.get("name") for a in (e.get("attributes") or [])
                          if isinstance(a, dict) and a.get("name"))
        out.append(f"- {name}: {resp}" + (f" [holds: {attrs}]" if attrs else ""))
    return "\n".join(out) or "(no entities)"


def data_entities(handover: dict) -> list[dict]:
    """The persisted entities across all aspects — a component is a data entity when it carries
    attributes (fields). Deduped by name. This is the design's data model."""
    seen, ents = set(), []
    for a in (handover.get("by_aspect") or {}).values():
        for c in (a.get("components") or []):
            n = c.get("name")
            if n and n not in seen and c.get("attributes"):
                seen.add(n)
                ents.append(c)
    return ents


def _norm(s: str) -> str:
    """Normalize for a lexical substring check: lowercase, collapse all whitespace. (Verifying a
    quote literally appears — an exact-match fact, not a semantic judgment.)"""
    return " ".join((s or "").lower().split())


def _decide(raw: dict, req_texts: list[str]) -> dict:
    """Decide the proportionate persistence IN CODE from the model's extracted drivers — keeping
    ONLY drivers whose quote actually occurs in the requirements (fabricated quotes are dropped)."""
    corpus = _norm(" \n ".join(req_texts))
    drivers = raw.get("orm_drivers") if isinstance(raw.get("orm_drivers"), list) else []
    verified, rejected = [], []
    for d in drivers:
        if not isinstance(d, dict):
            continue
        drv = str(d.get("driver", "")).strip().lower()
        q = str(d.get("quote", "")).strip()
        nq = _norm(q)
        grounded = drv in _DRIVER_STACK and len(nq) >= 12 and nq in corpus
        on_topic = any(kw in nq for kw in _DRIVER_KEYWORDS.get(drv, []))
        if grounded and on_topic:
            verified.append({"driver": drv, "quote": q})
        else:
            reason = ("unknown driver" if drv not in _DRIVER_STACK else
                      "quote not found in requirements" if not grounded else
                      f"quote lacks {drv} vocabulary (misclassified)")
            rejected.append({"driver": drv, "quote": q, "reason": reason})

    base = [p for p in (raw.get("base_dependencies") or [])
            if isinstance(p, str) and p.strip().lower() not in _PERSISTENCE_PKGS]
    orm_required = bool(verified)
    persistence_deps = []
    for d in verified:
        persistence_deps += _DRIVER_STACK[d["driver"]]
    sanctioned = sorted(dict.fromkeys([*base, *dict.fromkeys(persistence_deps)]))

    if orm_required:
        why = "; ".join(f"{d['driver']}: \"{d['quote'][:80]}\"" for d in verified)
        persistence = f"ORM (justified by — {why})"
    else:
        persistence = "stdlib sqlite3, no ORM (CRUD over related entities; no reporting/migration/scale requirement)"
    return {"relational_orm_required": orm_required,
            "recommended_persistence": persistence,
            "sanctioned_dependencies": sanctioned,
            "verified_drivers": verified,
            "rejected_drivers": rejected,
            "over_engineering": raw.get("over_engineering") or [],
            "confidence": raw.get("confidence")}


def judge(req_texts: list[str], entities: list[dict], stated_stack: str = "", client=None) -> dict:
    """Proportionality verdict for the whole design. Sends the FULL requirement set (no truncation)
    and the full data model; the model EXTRACTS candidate justifications, this DECIDES in code with
    quote verification. Fails OPEN (default = simple stdlib persistence) on bad model output."""
    if client is None:
        from .client import AgentClient       # lazy: the module's helpers stay import-light
        client = AgentClient()
    reqs = "\n".join(f"- {t}" for t in req_texts if t)
    user = (f"REQUIREMENTS ({len([t for t in req_texts if t])} total — the complete set):\n{reqs}\n\n"
            f"DESIGN DATA MODEL (persisted entities):\n{_entity_lines(entities)}\n\n"
            + (f"STACK STATED SO FAR: {stated_stack}\n\n" if stated_stack else "")
            + "Extract any driver that justifies a heavyweight persistence stack (with a verbatim "
              "requirement quote), list the non-persistence dependencies the requirements justify, "
              "and flag any complexity the requirements do not justify.")
    raw = client.complete_json(PROPORTIONALITY_AGENT, user)
    if not isinstance(raw, dict):
        raw = {}
    return _decide(raw, [t for t in req_texts if t])


def run(handover: dict, req_text_by_id: dict[str, str], stated_stack: str = "", client=None) -> dict:
    """Run the proportionality review over a handover. `req_text_by_id` supplies requirement texts
    (values used; ids irrelevant to proportionality). Returns the decided verdict plus what it
    reviewed."""
    entities = data_entities(handover)
    req_texts = [t for t in (req_text_by_id or {}).values() if isinstance(t, str)]
    verdict = judge(req_texts, entities, stated_stack=stated_stack, client=client)
    verdict["_reviewed"] = {"requirements": len(req_texts), "entities": len(entities)}
    return verdict
