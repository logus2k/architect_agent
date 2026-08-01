"""Mermaid diagram emission — one diagram per aspect, delivered as code.

The Architect ships diagram SOURCE (Mermaid text), rendered client-side by reqoach's
mermaid.js. No server-side renderer, no jar. One diagram per aspect (never one monolith)
so nothing is ever too large to read.

Each aspect diagram shows: the components it OWNS (with attributes), the interfaces it
exposes, which component provides which interface, and — as dashed external nodes — the
concerns/entities it CONSUMES from other aspects. A separate system overview shows the
aspects and their consume relationships.
"""

from __future__ import annotations

import re

from .aspect_design import AspectDesign


def _id(name: str) -> str:
    """A Mermaid-safe node id."""
    return "n_" + re.sub(r"[^0-9a-zA-Z]", "_", name)


def _esc(text: str) -> str:
    """Escape for a Mermaid label (quotes + line breaks)."""
    return text.replace('"', "'").replace("\n", " ")


def aspect_diagram(design: AspectDesign) -> str:
    """One aspect as a Mermaid flowchart."""
    L = ["flowchart TB", f'  %% {design.branch}']
    owned_ids = {}

    if design.components:
        L.append(f'  subgraph OWN["{_esc(design.branch)}"]')
        L.append("    direction TB")
        for c in design.components:
            cid = _id(c["name"])
            owned_ids[c["name"]] = cid
            attrs = c.get("attributes") or []
            label = c["name"]
            if attrs:
                label += "<br/>" + "<br/>".join(
                    f"{a.get('name')}: {a.get('type')}" for a in attrs[:6])
            L.append(f'    {cid}["{_esc(label)}"]')
        L.append("  end")

    # interfaces the aspect exposes (stadium shape)
    for i in design.interfaces:
        iid = _id(i["name"])
        L.append(f'  {iid}(["{_esc(i["name"])}"])')
        # a component provides it (best-effort: first owned component, if any)
        if owned_ids:
            provider = next(iter(owned_ids.values()))
            L.append(f"  {provider} --> {iid}")

    # consumed concerns/entities from other aspects (dashed external)
    for c in design.consumes:
        concern = c.get("concern")
        if not concern:
            continue
        eid = _id("ext_" + concern)
        L.append(f'  {eid}[/"{_esc(concern)}"/]')
        # link from the aspect (its first component) to the consumed thing
        if owned_ids:
            L.append(f"  {next(iter(owned_ids.values()))} -.consumes.-> {eid}")

    L.append("  classDef ext fill:#eee,stroke:#999,stroke-dasharray:3 3;")
    ext_ids = [_id("ext_" + (c.get("concern") or "")) for c in design.consumes if c.get("concern")]
    if ext_ids:
        L.append(f"  class {','.join(ext_ids)} ext;")
    return "\n".join(L)


def system_overview(designs: list[AspectDesign]) -> str:
    """Aspects and their consume relationships — the top-level map, not a 150-box strip."""
    L = ["flowchart LR"]
    owner_of: dict[str, str] = {}
    for d in designs:
        for c in d.components:
            owner_of[c["name"]] = d.branch
    for d in designs:
        L.append(f'  {_id(d.branch)}["{_esc(d.branch)}"]')
    seen = set()
    for d in designs:
        for c in d.consumes:
            concern = c.get("concern")
            owner = owner_of.get(concern)
            if owner and owner != d.branch and (d.branch, owner) not in seen:
                seen.add((d.branch, owner))
                L.append(f"  {_id(d.branch)} -.-> {_id(owner)}")
    return "\n".join(L)


def emit_all(designs: list[AspectDesign]) -> dict[str, str]:
    """Return {filename: mermaid_source} for every aspect plus the system overview."""
    out = {"_system_overview.mmd": system_overview(designs)}
    for d in designs:
        out[re.sub(r"[^0-9a-zA-Z]+", "_", d.branch).strip("_") + ".mmd"] = aspect_diagram(d)
    return out
