"""Advisory diagram review — a vision model looks at a rendered aspect diagram.

Complements the deterministic critique: the critique checks the MODEL (near-dup, ownership,
unowned), this checks the PICTURE (does the rendered diagram clearly and correctly represent
the aspect?). It is ADVISORY — the LLM is non-deterministic, so its notes go to `open_issues`
for a human; they never gate the build. The deterministic critique is the gate.

Diagrams are Mermaid; they are rendered to PNG with mermaid-cli (`mmdc`, node — a dev/render
dependency, not shipped) so the vision model has an image to look at.
"""

from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass

import httpx

from .aspect_design import AspectDesign

AGENT_SERVER_URL = os.environ.get("AGENT_SERVER_URL", "http://localhost:7701")
REVIEWER_AGENT = "architect_diagram_reviewer"
_MMDC = shutil.which("mmdc") or os.path.expanduser("~/.nvm/versions/node/v22.20.0/bin/mmdc")


@dataclass
class DiagramReview:
    aspect: str
    ok: bool
    concerns: list[str]


def render_mermaid(mmd: str, out_png: str, timeout: float = 200.0) -> bool:
    """Render Mermaid text to PNG via npx mermaid-cli. Returns True on success."""
    node_bin = os.path.expanduser("~/.nvm/versions/node/v22.20.0/bin")
    env = {**os.environ, "PATH": node_bin + ":" + os.environ.get("PATH", "")}
    with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False) as f:
        f.write(mmd)
        src = f.name
    try:
        r = subprocess.run(["npx", "-y", "@mermaid-js/mermaid-cli", "-i", src, "-o", out_png],
                           capture_output=True, text=True, timeout=timeout, env=env)
        return r.returncode == 0 and os.path.exists(out_png)
    except (OSError, subprocess.TimeoutExpired):
        return False
    finally:
        os.unlink(src)


def review_aspect(design: AspectDesign, mmd: str, *, base_url: str = AGENT_SERVER_URL,
                  timeout: float = 300.0) -> DiagramReview:
    """Render the aspect diagram and ask the vision model whether it represents the aspect.
    On any failure (render or model) returns ok=True with an empty concern list — advisory,
    must never block."""
    png = tempfile.mktemp(suffix=".png")
    try:
        if not render_mermaid(mmd, png):
            return DiagramReview(design.branch, True, [])
        img = base64.b64encode(open(png, "rb").read()).decode()
    except OSError:
        return DiagramReview(design.branch, True, [])
    finally:
        pass
    expected = {
        "aspect": design.branch,
        "components": [c["name"] for c in design.components],
        "interfaces": [i["name"] for i in design.interfaces],
    }
    payload = {
        "model": REVIEWER_AGENT,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text":
             f"This diagram should show the '{design.branch}' aspect with components "
             f"{expected['components']} and interfaces {expected['interfaces']}. "
             "Does it clearly and correctly represent that? Report only real concerns."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}}]}],
        "response_format": {"type": "json_object"}, "temperature": 0.0, "max_tokens": 600,
    }
    try:
        r = httpx.post(f"{base_url}/v1/chat/completions", json=payload, timeout=timeout)
        r.raise_for_status()
        data = json.loads(r.json()["choices"][0]["message"]["content"])
    except Exception:
        return DiagramReview(design.branch, True, [])
    finally:
        if os.path.exists(png):
            os.unlink(png)
    return DiagramReview(design.branch, bool(data.get("matches", True)),
                         list(data.get("concerns", [])))


def open_issues(reviews: list[DiagramReview]) -> list[str]:
    out = []
    for rv in reviews:
        if not rv.ok:
            out.append(f"[diagram] {rv.aspect}: reviewer could not confirm the diagram")
        for c in rv.concerns:
            out.append(f"[diagram] {rv.aspect}: {c}")
    return out
