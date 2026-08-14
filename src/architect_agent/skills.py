"""Architect skills — vetted DESIGN guidance injected into aspect design so the Architect designs the
contract correctly for this environment (e.g. auth = oauth2-proxy, NOT app-implemented OAuth).

Same opencode-native / Claude-compatible `SKILL.md` files as the rest of the FACTORY; here we load the
ones whose surface is `architecture` and inject the relevant one (selected by the house reranker over a
short trigger phrase) into the designer payload. Generic: selection is by semantic relevance of a skill's
triggers to the branch requirements, so it generalises to any app and any design skill added later.
"""

from __future__ import annotations

import os

from . import retrieval   # house reranker (sigmoid-scaled 0..1)

SKILLS_DIR = os.environ.get("SKILLS_DIR", "/app/skills")
SELECT_THRESHOLD = float(os.environ.get("SKILL_SELECT_THRESHOLD", "0.005"))


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2]
    fm: dict = {}
    in_meta = False
    for line in fm_raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("metadata:"):
            in_meta = True
            continue
        if in_meta and line.startswith("  ") and ":" in line:
            k, v = line.strip().split(":", 1)
            fm.setdefault("metadata", {})[k.strip()] = v.strip()
            continue
        in_meta = False
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body.strip()


def load_skills(skills_dir: str | None = None) -> list[dict]:
    base = skills_dir or SKILLS_DIR
    out: list[dict] = []
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        p = os.path.join(base, name, "SKILL.md")
        if not os.path.isfile(p):
            continue
        try:
            fm, body = _parse_frontmatter(open(p, encoding="utf-8").read())
        except OSError:
            continue
        if not fm.get("name") or not fm.get("description"):
            continue
        meta = fm.get("metadata", {}) or {}
        surfaces = meta.get("surfaces", "")
        out.append({"name": fm["name"], "description": fm["description"],
                    "surfaces": [s.strip() for s in surfaces.split(",") if s.strip()],
                    "match_text": meta.get("triggers") or fm["description"], "body": body})
    return out


def select_skills(requirement_text: str, surface: str = "architecture",
                  skills: list[dict] | None = None, threshold: float | None = None,
                  top_k: int = 2) -> list[dict]:
    """Reranker-select the design skills relevant to the branch requirements. Reranker down / none -> []."""
    skills = load_skills() if skills is None else skills
    cands = [s for s in skills if s["surfaces"] and surface in s["surfaces"]]
    if not cands or not (requirement_text or "").strip():
        return []
    try:
        scores = retrieval.rerank(requirement_text, [s["match_text"] for s in cands])
    except Exception:  # noqa: BLE001 — reranker down -> no guidance, design proceeds
        return []
    thr = SELECT_THRESHOLD if threshold is None else threshold
    ranked = sorted(zip(scores, cands), key=lambda t: t[0], reverse=True)
    return [s for sc, s in ranked[:top_k] if sc >= thr]


def skills_guidance(selected: list[dict]) -> str:
    """Format selected design skills for the designer payload. Empty string if none."""
    if not selected:
        return ""
    blocks = [f"### DESIGN SKILL: {s['name']}\n{s['description']}\n\n{s['body']}" for s in selected]
    return ("You MUST follow these vetted DESIGN skills where they apply — they encode how THIS "
            "environment works; do not design around them:\n\n" + "\n\n---\n\n".join(blocks))
