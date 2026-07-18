"""agent_server client.

Deliberately thin. The house pattern (see ~/env/labs/requirements) is one stateless
call per item: `model` carries the agent preset name, there is no conversation
history, and every preset is registered `memory_policy: "none"`.
"""

from __future__ import annotations

import json
import os
import re

import httpx

AGENT_SERVER_URL = os.environ.get("AGENT_SERVER_URL", "http://localhost:7701")
#: Generous by default: a queued request behind a busy slot legitimately takes
#: minutes, and a short timeout turns contention into a failed run.
DEFAULT_TIMEOUT = float(os.environ.get("ARCHITECT_LLM_TIMEOUT", "900"))

_FENCE = re.compile(r"^```[a-zA-Z]*\n|\n```$")


class LLMError(RuntimeError):
    """Transport failure or unparseable output. Never raised for a *valid* answer
    the caller happens to dislike."""


class AgentClient:
    def __init__(self, base_url: str | None = None, timeout: float = DEFAULT_TIMEOUT):
        self.base_url = (base_url or AGENT_SERVER_URL).rstrip("/")
        self.timeout = timeout

    def complete_json(self, agent: str, user_content: str) -> dict:
        """Call `agent` with one user message, expecting a JSON object back.

        Batch size is deliberately 1: reqqa measured ~96% judge self-consistency at
        batch=1 falling to ~54% at batch 8+, as the model conflates items. Generation
        is at least as sensitive.
        """
        payload = {
            "model": agent,
            "messages": [{"role": "user", "content": user_content}],
            "response_format": {"type": "json_object"},
        }
        try:
            r = httpx.post(f"{self.base_url}/v1/chat/completions",
                           json=payload, timeout=self.timeout)
            r.raise_for_status()
            data = r.json()
        except httpx.HTTPError as e:
            raise LLMError(f"agent_server request failed for '{agent}': {e}") from e
        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            raise LLMError(f"unexpected response shape: {str(data)[:200]}") from e
        return self._parse_json(content, agent)

    @staticmethod
    def _parse_json(content: str, agent: str) -> dict:
        """Tolerate fenced or prose-wrapped JSON. Three attempts, then give up —
        we do not re-prompt, because a retry hides a prompt that needs fixing."""
        for candidate in (content, _FENCE.sub("", content.strip()),
                          content[content.find("{"): content.rfind("}") + 1]):
            try:
                parsed = json.loads(candidate)
                if isinstance(parsed, dict):
                    return parsed
            except (json.JSONDecodeError, ValueError):
                continue
        raise LLMError(f"'{agent}' returned unparseable JSON: {content[:300]}")
