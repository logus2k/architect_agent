# Architect Agent

Transforms INCOSE-validated requirements from the Analyst Agent (`:7803`) into an MBSE
architecture package: SysML v2 model, rendered diagrams, and MBSE artifacts for the
Planner Agent.

```bash
curl -s http://localhost:7803/projects/<PID>/package -o package.json
PYTHONPATH=src ./.venv/bin/python -m architect_agent.pipeline package.json -o architecture
```

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

All pipeline stages built and exercised against a real 386-requirement Analyst package
(run on a 12-requirement subset; see below). 33 tests pass, including integration tests
that drive the real SysML v2 jar.

Pipeline: load → classify (only if the package is unclassified) → generate
(functional, logical, interface, behaviour, constraint, allocation, verification) →
emit → **validate (blocking)** → render → judge → package.

Two review layers, neither of which gates the build on an LLM's opinion:
- **Semantic judge** — catches valid SysML that means the wrong thing (e.g. a constraint
  asserting the failure condition). `wrong` *and* `uncertain` escalate to a human.
- **Vision review** — advisory only, recorded in the ADD's Open Issues.

Known limits: no full-scale run (386 requirements at `--parallel 1` takes hours);
interface ends are recorded but not connected to specific parts in the model text;
no `satisfy`/`verify` relationships yet. See `documents/implementation.md` §8 for the
module-by-module status and §1.1 for how the spec's prescriptions are graded
(*verified* / *borrowed* / *design choice* — not interchangeable).
