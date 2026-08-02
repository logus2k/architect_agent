"""Per-aspect design — the Architect designs each branch as a unit.

Replaces per-requirement generation. For each branch of the Analyst's requirement tree,
ONE design call sees ALL the branch's requirements together plus the project glossary and
tags, and produces a coherent aspect: entities anchored to the glossary, and the MINIMAL
set of interfaces (one per boundary, not one per requirement). This is what collapses the
inflation by construction — the model converges within the aspect because it sees the
whole aspect at once, and it names entities from the shared glossary.

See `documents/per_aspect_design_redesign.md`. The design is then run through the built-in
critique (`critique.py`); findings feed a bounded regenerate loop.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

from .client import AgentClient, LLMError

DESIGNER_AGENT = "architect_aspect_designer"
WORKERS = 2   # agent_server --parallel 2


@dataclass
class AspectDesign:
    branch: str
    scope: str = ""
    components: list[dict] = field(default_factory=list)
    functions: list[dict] = field(default_factory=list)
    interfaces: list[dict] = field(default_factory=list)
    consumes: list[dict] = field(default_factory=list)


def _branch_requirements(package: dict, req_ids: list[str]) -> list[str]:
    by_id = {r["req_id"]: r["text"] for r in package.get("requirements", [])}
    return [by_id[r] for r in req_ids if r in by_id]


def design_branch(branch: dict, package: dict, client: AgentClient) -> AspectDesign:
    """Design one aspect. The designer sees the whole branch at once."""
    reqs = _branch_requirements(package, branch.get("req_ids", []))
    payload = json.dumps({
        "branch": branch["name"],
        "scope": branch.get("scope", ""),
        "requirements": reqs,
        "glossary": [{"name": t["name"], "definition": t.get("definition", ""),
                      "kind": t.get("kind", "entity")}
                     for t in package.get("glossary", [])],
        "tags": [t["name"] for t in package.get("tags", [])],
    })
    d = AspectDesign(branch=branch["name"], scope=branch.get("scope", ""))
    try:
        out = client.complete_json(DESIGNER_AGENT, payload)
    except LLMError:
        return d
    d.components = [c for c in out.get("components", []) if c.get("name")]
    d.functions = [f for f in out.get("functions", []) if f.get("name")]
    d.interfaces = [i for i in out.get("interfaces", []) if i.get("name")]
    d.consumes = out.get("consumes", [])
    return d


def design_aspects(package: dict, client: AgentClient | None = None,
                   workers: int = WORKERS) -> list[AspectDesign]:
    """Design every branch. Branches are independent, so this parallelises."""
    client = client or AgentClient()
    branches = package.get("tree", {}).get("branches", [])
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(lambda b: design_branch(b, package, client), branches))


# -- adapters for the critique (interfaces/components by aspect) ---------------

def interfaces_by_aspect(designs: list[AspectDesign]) -> dict[str, list[str]]:
    return {d.branch: [i["name"] for i in d.interfaces] for d in designs}


def components_by_aspect(designs: list[AspectDesign]) -> dict[str, list[str]]:
    return {d.branch: [c["name"] for c in d.components] for d in designs}


def consumes_by_aspect(designs: list[AspectDesign]) -> dict[str, list[str]]:
    return {d.branch: [c.get("concern") for c in d.consumes if c.get("concern")] for d in designs}
