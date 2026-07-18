"""Advisory diagram review by the local vision model.

This is NOT a build gate. The authoritative check is `sysml.validate()`, which is
deterministic. A vision model asked "is this diagram right?" was measured returning
a false negative on a correct diagram, so gating on it would fail builds
unpredictably. Its output belongs in the ADD's Open Issues section, nowhere else.

Kept because it catches a class of problem validation cannot: a model that is
syntactically and semantically valid but depicts something other than intended.
"""

from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from pathlib import Path

import httpx

AGENT_SERVER_URL = os.environ.get("AGENT_SERVER_URL", "http://localhost:7701")
REVIEWER_AGENT = "architect_diagram_reviewer"
#: 818 tokens was the observed cost with thinking enabled on a 32K slot, so this
#: is generous rather than tight. Too small a budget truncates before any JSON.
MAX_TOKENS = 2048


@dataclass
class Review:
    matches: bool
    reason: str
    elements_seen: list[str]
    concerns: list[str]

    def as_open_issue(self, subject: str) -> str | None:
        """Render as an ADD Open Issues line, or None if nothing to report."""
        if self.matches and not self.concerns:
            return None
        parts = []
        if not self.matches:
            parts.append(f"Diagram review did not confirm '{subject}': {self.reason}")
        parts.extend(self.concerns)
        return "; ".join(parts)


def review_diagram(
    png_path: str | Path,
    subject: str,
    *,
    base_url: str = AGENT_SERVER_URL,
    agent: str = REVIEWER_AGENT,
    timeout: float = 300.0,
) -> Review:
    """Ask the vision model whether `png_path` depicts `subject`.

    `subject` should describe intent in plain language ("a GPU cluster containing
    notebook sessions"), matching how the reviewer prompt is framed.
    """
    img = base64.b64encode(Path(png_path).read_bytes()).decode()
    payload = {
        "model": agent,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text",
                 "text": f"Does this diagram depict the following? {subject}"},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/png;base64,{img}"}},
            ],
        }],
        "response_format": {"type": "json_object"},
        "temperature": 0.0,
        "max_tokens": MAX_TOKENS,
    }
    r = httpx.post(f"{base_url}/v1/chat/completions", json=payload, timeout=timeout)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    data = json.loads(_strip_fences(content))
    return Review(
        matches=bool(data.get("matches", False)),
        reason=str(data.get("reason", "")),
        elements_seen=list(data.get("elements_seen", [])),
        concerns=list(data.get("concerns", [])),
    )


def _strip_fences(text: str) -> str:
    """Models sometimes wrap JSON in markdown fences despite json_object mode."""
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else t
        t = t.rsplit("```", 1)[0]
    start, end = t.find("{"), t.rfind("}")
    return t[start:end + 1] if start >= 0 and end > start else t
