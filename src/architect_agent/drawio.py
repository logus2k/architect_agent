"""draw.io (diagrams.net) export — same design data as Mermaid, XML output.

Mermaid is the browser default (auto-layout, mermaid.js). This module is the EXPORT
alternative: a deterministic AspectDesign -> draw.io mxGraph XML emitter. draw.io needs
explicit geometry, so a simple grid layout is computed (components row, interfaces row,
consumed-externals row); the user can re-arrange in the draw.io editor afterwards.

One `.drawio` file per aspect. Same content as the Mermaid diagram — owned components,
exposed interfaces, and dashed consumes to external concerns.
"""

from __future__ import annotations

import re
from xml.sax.saxutils import escape

from .aspect_design import AspectDesign

_W, _H = 160, 60
_GAPX, _ROWY = 40, 160


def _cell(cid: str, value: str, x: int, y: int, style: str) -> str:
    return (f'<mxCell id="{cid}" value="{escape(value)}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{_W}" height="{_H}" as="geometry"/></mxCell>')


def _edge(eid: str, src: str, dst: str, dashed: bool = False, label: str = "") -> str:
    style = "edgeStyle=orthogonalEdgeStyle;rounded=0;" + ("dashed=1;" if dashed else "")
    return (f'<mxCell id="{eid}" value="{escape(label)}" style="{style}" edge="1" parent="1" '
            f'source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry"/></mxCell>')


def _id(prefix: str, name: str) -> str:
    return prefix + "_" + re.sub(r"[^0-9a-zA-Z]", "_", name)


def aspect_drawio(design: AspectDesign) -> str:
    cells = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
    edges: list[str] = []

    def row(items, y, style, prefix, label_fn):
        ids = []
        for i, it in enumerate(items):
            cid = _id(prefix, label_fn(it))
            cells.append(_cell(cid, label_fn(it), 40 + i * (_W + _GAPX), y, style))
            ids.append(cid)
        return ids

    comp_ids = row(design.components, 40,
                   "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;", "c",
                   lambda c: c["name"])
    iface_ids = row(design.interfaces, 40 + _ROWY,
                    "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;", "i",
                    lambda i: i["name"])
    ext_ids = row(design.consumes, 40 + 2 * _ROWY,
                  "shape=parallelogram;whiteSpace=wrap;html=1;fillColor=#f5f5f5;dashed=1;", "e",
                  lambda c: c.get("concern", ""))

    provider = comp_ids[0] if comp_ids else None
    for n, iid in enumerate(iface_ids):
        if provider:
            edges.append(_edge(f"pe{n}", provider, iid))
    for n, eid in enumerate(ext_ids):
        if provider:
            edges.append(_edge(f"ce{n}", provider, eid, dashed=True, label="consumes"))

    body = "".join(cells + edges)
    return (f'<mxfile><diagram name="{escape(design.branch)}">'
            f'<mxGraphModel dx="800" dy="600" grid="1" gridSize="10">'
            f'<root>{body}</root></mxGraphModel></diagram></mxfile>')


def emit_all(designs: list[AspectDesign]) -> dict[str, str]:
    return {re.sub(r"[^0-9a-zA-Z]+", "_", d.branch).strip("_") + ".drawio": aspect_drawio(d)
            for d in designs}
