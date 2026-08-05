"""Planner handover from the per-aspect design.

Supersedes the old per-requirement `handover.py`. Structured by ASPECT (the Architect now
designs per aspect), but STILL keyed by `req_id` under `by_requirement` so the Planner's
existing reader (`planner_agent/src/planner/architecture.py`) joins unchanged. Adds
`by_aspect` (the natural unit for Planner epics) and the critique's open issues.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from .aspect_design import AspectDesign

CONTRACT_VERSION = "2.0"   # aspect-structured; SysML dropped


def _module(name: str) -> str:
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name)
    return re.sub(r"_+", "_", s).lower().strip("_")


def build(designs: list[AspectDesign], *, package: dict,
          tree_nodes: list[dict] | None = None,
          open_issues: list[str] | None = None) -> dict:
    """Assemble the aspect-structured handover.

    `tree_nodes`: the Analyst tree's [{req_id, branch, tags}] — used to key elements back to
    requirements. Falls back to the package's own tree.
    """
    nodes = tree_nodes or package.get("tree", {}).get("nodes", [])
    reqs_by_branch: dict[str, list[str]] = {}
    branch_by_req: dict[str, str] = {}
    tags_by_req: dict[str, list[str]] = {}
    for n in nodes:
        branch_by_req[n["req_id"]] = n.get("branch")
        tags_by_req[n["req_id"]] = n.get("tags", [])
        reqs_by_branch.setdefault(n.get("branch"), []).append(n["req_id"])

    by_aspect = {}
    components_global = []
    for d in designs:
        by_aspect[d.branch] = {
            "scope": d.scope,
            "req_ids": reqs_by_branch.get(d.branch, []),
            "components": d.components,
            "functions": d.functions,
            "interfaces": d.interfaces,
            "consumes": d.consumes,
        }
        for c in d.components:
            components_global.append({"name": c["name"], "owner_aspect": d.branch,
                                      "suggested_module": _module(c["name"]),
                                      "attributes": c.get("attributes", [])})

    # req_id -> its aspect's elements, so the Planner joins on req_id as before.
    by_requirement = {}
    design_by_branch = {d.branch: d for d in designs}
    for req_id, branch in branch_by_req.items():
        d = design_by_branch.get(branch)
        if not d:
            continue
        # Per the handover contract (sdk/how_to.md §3), by_requirement elements are OBJECTS,
        # not bare names — the Planner's reader joins on `.name` / `.suggested_module` /
        # `.responsibility` / `.supplier` / `.consumer`. Emitting strings crashes it.
        by_requirement[req_id] = {
            "aspect": branch,
            "tags": tags_by_req.get(req_id, []),
            "components": [{"name": c["name"],
                            "suggested_module": _module(c["name"]),
                            "responsibility": c.get("responsibility", ""),
                            "attributes": c.get("attributes", [])} for c in d.components],
            "functions": [{"name": f["name"]} for f in d.functions],
            "interfaces": [{"name": i["name"],
                            "supplier": branch,
                            "consumer": ", ".join(i.get("consumers", []) or [])}
                           for i in d.interfaces],
        }

    manifest = package.get("manifest", {})
    return {
        "contract_version": CONTRACT_VERSION,
        "source_package": {
            "project_id": manifest.get("project_id"),
            "project_name": manifest.get("project_name"),
            "architect_ready": manifest.get("architect_ready", False),
            "requirements_received": len(package.get("requirements", [])),
            "aspects": len(designs),
        },
        "by_aspect": by_aspect,
        "by_requirement": by_requirement,
        "components": components_global,
        "open_issues": open_issues or [],
    }


def write(doc: dict, root: str | Path) -> Path:
    path = Path(root) / "planner_handover.json"
    path.write_text(json.dumps(doc, indent=2) + "\n")
    return path
