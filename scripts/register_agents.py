#!/usr/bin/env python3
"""Register the architect_* agent profiles against a running agent_server.

agent_server stores the system prompt TEXT. The .agent.json files carry a path
(matching the house convention for on-disk profiles), so this script resolves the
path to its contents before posting. Registering the path itself leaves the model
with a meaningless system prompt and no error anywhere.
"""
import json
import os
import pathlib
import sys

import httpx

BASE = os.environ.get("AGENT_SERVER_URL", "http://localhost:7701")
ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    agents = sorted((ROOT / "data" / "agents").glob("*.agent.json"))
    if not agents:
        print("no profiles found", file=sys.stderr)
        return 1
    created = updated = failed = 0
    for f in agents:
        prof = json.loads(f.read_text())
        name = prof["name"]
        prompt = ROOT / "data" / "prompts" / f"{name}_system_prompt.txt"
        if not prompt.exists():
            print(f"  MISSING PROMPT {name}", file=sys.stderr)
            failed += 1
            continue
        body = dict(prof, system_prompt=prompt.read_text())
        r = httpx.post(f"{BASE}/admin/api/agents", json=body, timeout=30)
        if r.status_code == 409:
            r = httpx.put(f"{BASE}/admin/api/agents/{name}", json=body, timeout=30)
            updated += r.status_code < 300
            failed += r.status_code >= 300
        elif r.status_code < 300:
            created += 1
        else:
            print(f"  FAIL {name}: {r.status_code} {r.text[:120]}", file=sys.stderr)
            failed += 1
    print(f"created={created} updated={updated} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
