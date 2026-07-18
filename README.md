# Architect Agent

Transforms INCOSE-validated requirements (from the Analyst Agent / reqqa) into an MBSE
architecture package: SysML v2 model, rendered diagrams, and MBSE artifacts for the
Planner Agent.

Runs fully offline. Inference is local (`agent_server` + `llama-vision`); SysML v2
validation and diagram rendering run from the OMG Pilot Implementation jar. No SysON,
no GraphViz, no network at runtime.

## Layout

```
src/architect_agent/
  symbols.py         symbol registry — authoritative element names
  sysml.py           validation + diagram rendering (wraps the jar)
  vision_review.py   advisory diagram review (never gates)
java/ArchitectTool.java   headless validate+render, emits JSON
data/                bind-mounted; toolchain + agent profiles/prompts
documents/           technical_architecture.md, implementation.md
```

## Setup

```bash
./scripts/fetch_toolchain.sh      # one-time, needs network (~127 MB)
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
PYTHONPATH=src ./.venv/bin/python -m pytest tests/ -q
```

`data/sysml-toolchain/` is git-ignored — the kernel jar is ~127 MB and the SysML
standard library is 8 MB. Provision, don't commit.

## Agent profiles

Ten `architect_*` profiles live in `data/agents/`, prompts in `data/prompts/`.
Register them against a running agent_server:

```bash
./.venv/bin/python scripts/register_agents.py
```

Note: agent_server stores the system prompt **text**, not a file path. Posting a path
registers the path string as the prompt, and the model silently improvises — the
symptom is well-formed JSON in a schema you never asked for.

## Status

Working and tested end-to-end: classification → symbol minting → SysML generation →
validation → rendering → advisory review, with zero symbol drift.

Not built yet: the per-stage generation engines (§2.2–2.8), artifact packaging, and
the ADD writer. See `documents/implementation.md` §1.1 for how to read the
prescriptions in the spec — statements are graded *verified*, *borrowed*, or
*design choice*, and they are not interchangeable.
