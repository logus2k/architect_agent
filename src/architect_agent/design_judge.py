"""Architect DESIGN-PLAUSIBILITY judge — an advisory self-assessment of the design.

The critique loop checks STRUCTURE (ownership, interface dedup, misassignment) and the
completeness check flags entities with no fields. Neither asks the harder question: does the
design actually REALIZE its requirements? This judge does, per aspect — flagging OMISSION (a
required capability nothing covers), DRIFT (a designed element traceable to no requirement),
and OUT-OF-DOMAIN elements (a build/design tool modelled as a product component — the class that
produced junk like "The Architect Agent shall define the Location fields").

ADVISORY, not a gate. Registered in agent_server as `architect_design_judge`;
DESIGN_JUDGE_SYSTEM_PROMPT below is the source of truth (re-register via the admin API).
"""

from __future__ import annotations

from .client import AgentClient

DESIGN_JUDGE_AGENT = "architect_design_judge"

DESIGN_JUDGE_SYSTEM_PROMPT = """\
You are a software-architecture DESIGN judge. You are given ONE feature aspect: its SCOPE, the REQUIREMENTS it must realize, and the DESIGN produced (components with fields, functions with signatures, interfaces with operations), plus what it CONSUMES from other aspects.

Your job is NARROW: flag only two kinds of clearly-wrong design element. Do NOT assess coverage or completeness (whether every requirement is realized) — a requirement is often served by a consumed concern or genuinely belongs to another aspect, so absence here is not necessarily a defect. Judging coverage is NOT your job.

Flag ONLY these — name the category in each issue:
1. OUT-OF-DOMAIN — a design element that is NOT part of the RUNNING product: a build or design tool, an agent that builds software, the developer/architect/designer, or a component/function whose RESPONSIBILITY is a build-time or design-time activity ("validates … during the build", "defines the schema", "at design time"). The running product performs product behaviors, never build/design activities. (This is the key check — it catches nonsense like a "BuildAgent" or "Architect Agent" modelled as a product component.)
2. DRIFT — a design element that is BLATANTLY INVENTED: it corresponds to none of the requirements and none of the aspect's own entities, and is not reasonable implied plumbing (a repository/interface/schema a stated capability obviously needs). Flag only clear, untraceable inventions.

Mark "coherent": false ONLY if you find an out-of-domain or drift element; otherwise "coherent": true. NEVER flag: missing coverage/omission, business rules, cross-cutting concerns (auth, HTTPS, performance, logging), naming choices, thinness, or missing detail. When unsure, coherent=true.

Output ONLY JSON: {"coherent": true|false, "issues": [{"type": "out_of_domain|drift", "detail": "<one sentence>"}], "confidence": 0.0-1.0}
"""


def _fmt_component(c: dict) -> str:
    attrs = ", ".join(f"{a.get('name')}: {a.get('type')}" for a in (c.get("attributes") or [])
                      if isinstance(a, dict) and a.get("name"))
    resp = c.get("responsibility", "")
    return f"- {c.get('name')}: {resp}" + (f" [fields: {attrs}]" if attrs else "")


def _fmt_function(f: dict) -> str:
    ins = ", ".join(f"{p.get('name')}: {p.get('type')}" for p in (f.get("inputs") or [])
                    if isinstance(p, dict) and p.get("name"))
    return f"- {f.get('name')}({ins}) -> {f.get('returns', 'Void')}: {f.get('description', '')}"


def _fmt_interface(i: dict) -> str:
    ops = ", ".join(o.get("name", "") for o in (i.get("operations") or []) if isinstance(o, dict))
    return f"- {i.get('name')} [{i.get('purpose', '')}] ops: {ops or '(none)'}"


def _fmt_consumes(consumes: list) -> str:
    names = []
    for c in consumes or []:
        if isinstance(c, dict):
            names.append(c.get("concern") or c.get("name") or "")
        elif isinstance(c, str):
            names.append(c)
    return ", ".join(n for n in names if n)


def judge_aspect(aspect_name: str, scope: str, req_texts: list[str],
                 components: list[dict], functions: list[dict], interfaces: list[dict],
                 consumes: list | None = None, client: AgentClient | None = None) -> dict:
    """Advisory design verdict for one aspect. Fails OPEN (coherent=true) on bad output."""
    user = (f"ASPECT: {aspect_name}\nSCOPE: {scope}\n\n"
            "REQUIREMENTS this aspect must realize:\n"
            + "\n".join(f"- {t}" for t in req_texts if t) + "\n\n"
            "DESIGN produced:\nComponents:\n"
            + ("\n".join(_fmt_component(c) for c in components) or "(none)") + "\nFunctions:\n"
            + ("\n".join(_fmt_function(f) for f in functions) or "(none)") + "\nInterfaces:\n"
            + ("\n".join(_fmt_interface(i) for i in interfaces) or "(none)")
            + "\nCONSUMES (capabilities/entities provided by OTHER aspects — treat as available): "
            + (_fmt_consumes(consumes) or "(none)"))
    out = client.complete_json(DESIGN_JUDGE_AGENT, user) or {}
    # CODE-LEVEL GUARD: the E4B model cannot be reliably constrained by the prompt alone — it
    # keeps emitting "omission"/coverage findings even when told only to flag out-of-domain/drift
    # (coverage is entangled with the req->aspect mapping problem and false-positives badly). So
    # we KEEP ONLY the two reliable categories and derive `coherent` from them, ignoring the
    # model's own coherent flag and any coverage/omission noise it hallucinates.
    raw = out.get("issues") or []
    valid = [i for i in raw if isinstance(i, dict)
             and str(i.get("type", "")).strip().lower().replace("-", "_") in ("out_of_domain", "drift")]
    return {"coherent": not valid, "issues": valid, "confidence": out.get("confidence")}


def run(handover: dict, req_text_by_id: dict[str, str], client: AgentClient | None = None) -> dict:
    """Judge every aspect's design against its requirements. `req_text_by_id` maps req_id ->
    current requirement text. Returns {results:{aspect:verdict}, incoherent:[aspect,…]}."""
    client = client or AgentClient()
    by_aspect = handover.get("by_aspect") or {}
    results: dict[str, dict] = {}
    for aspect, d in by_aspect.items():
        req_texts = [req_text_by_id.get(rid, rid) for rid in (d.get("req_ids") or [])]
        results[aspect] = judge_aspect(
            aspect, d.get("scope", ""), req_texts,
            d.get("components") or [], d.get("functions") or [], d.get("interfaces") or [],
            consumes=d.get("consumes") or [], client=client)
    return {"results": results,
            "incoherent": sorted(a for a, v in results.items() if not v["coherent"])}
