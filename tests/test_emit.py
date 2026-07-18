"""Emitter tests — the output must be valid SysML v2, not merely plausible.

These run the real validator, so they catch emitter bugs the way the Step 5 gate
would: by refusing to accept text the reference implementation rejects.
"""

import pytest

from architect_agent import emit, sysml
from architect_agent.generate import StageOutput
from architect_agent.symbols import Kind, SymbolRegistry

needs_toolchain = pytest.mark.skipif(not sysml.is_available(),
                                     reason="SysML toolchain not present in data/")


def _fixture():
    reg = SymbolRegistry()
    cluster = reg.mint("GPU cluster", Kind.PART_DEF, req_id="R1", description="pool of GPUs")
    cluster_use = reg.mint("GPU cluster", Kind.PART_USAGE, req_id="R1")
    total = reg.mint("total GPUs", Kind.ATTRIBUTE, req_id="R1")
    alloc = reg.mint("allocate GPU", Kind.ACTION_DEF, req_id="R2")
    alloc_use = reg.mint("allocate GPU", Kind.ACTION_USAGE, req_id="R2")
    fair = reg.mint("GPU fairness", Kind.CONSTRAINT_DEF, req_id="R3")
    users = reg.mint("users", Kind.ATTRIBUTE, req_id="R3")

    logical = StageOutput(records=[{"req_id": "R1", "def": cluster.name,
                                    "usage": cluster_use.name,
                                    "attributes": [{"name": total.name, "type": "Integer"}],
                                    "description": "pool of GPUs"}])
    functions = StageOutput(records=[{"req_id": "R2", "name": alloc.name,
                                      "description": "allocate a GPU", "parent": None}])
    cons = StageOutput(records=[{"req_id": "R3", "name": fair.name,
                                 "expression": f"{users.name} >= 1",
                                 "parameters": [{"name": users.name, "type": "Integer"}],
                                 "category": "performance", "description": "fair share"}])
    allocs = StageOutput(records=[{"req_id": "R2", "function": alloc.name,
                                   "component": cluster.name, "rationale": "owner"}])
    return reg, logical, functions, cons, allocs


@needs_toolchain
def test_emitted_model_validates():
    reg, logical, functions, cons, allocs = _fixture()
    model = emit.emit_model("Demo", reg, logical=logical, functions=functions,
                            constraint_defs=cons, allocs=allocs)
    result = sysml.validate(model)
    assert result.valid, f"emitter produced invalid SysML:\n{model}\n{result.summary()}"


@needs_toolchain
def test_malformed_constraint_expression_does_not_break_the_model():
    """A model-proposed expression that is not a comparison must not emit a body
    the grammar rejects — the emitter substitutes a trivially true one."""
    reg, logical, functions, cons, allocs = _fixture()
    cons.records[0]["expression"] = "this is not an expression"
    model = emit.emit_model("Demo", reg, logical=logical, functions=functions,
                            constraint_defs=cons, allocs=allocs)
    assert sysml.validate(model).valid


def test_allocation_uses_usages_not_definitions():
    """`allocate` ends must resolve to features. Definitions are not features."""
    reg, logical, functions, cons, allocs = _fixture()
    model = emit.emit_model("Demo", reg, logical=logical, functions=functions,
                            constraint_defs=cons, allocs=allocs)
    line = next(l for l in model.splitlines() if l.strip().startswith("allocate"))
    assert "allocateGPU to gpuCluster" in line


def test_emission_is_deterministic():
    def build():
        reg, logical, functions, cons, allocs = _fixture()
        return emit.emit_model("Demo", reg, logical=logical, functions=functions,
                               constraint_defs=cons, allocs=allocs)
    assert build() == build()


def test_traceability_lists_every_requirement():
    reg, *_ = _fixture()
    md = emit.traceability_md(reg)
    for rid in ("R1", "R2", "R3"):
        assert rid in md


def test_write_package_creates_canonical_tree(tmp_path):
    root = emit.write_package(tmp_path, model="package P { }",
                              artifacts={"ADD.md": "# ADD\n"},
                              diagrams={"x.png": b"\x89PNG"})
    assert (root / "model.sysml").exists()
    assert (root / "artifacts" / "ADD.md").exists()
    assert (root / "diagrams" / "x.png").exists()
