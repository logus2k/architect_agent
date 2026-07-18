"""Tests for the symbol registry.

The registry's whole purpose is cross-artifact naming consistency, so the tests
that matter are the convergence ones: two callers describing the same concept
must land on one symbol.
"""

import pytest

from architect_agent.symbols import Kind, SymbolRegistry, RESERVED


def test_definition_is_pascal_usage_is_camel():
    r = SymbolRegistry()
    assert r.mint("GPU cluster", Kind.PART_DEF).name == "GPUCluster"
    assert r.mint("GPU cluster", Kind.PART_USAGE).name == "gpuCluster"


def test_acronym_survives_casing():
    """'GPU' must not become 'Gpu' — the usual naive title-casing bug."""
    r = SymbolRegistry()
    assert r.mint("GPU node", Kind.PART_DEF).name == "GPUNode"
    assert r.mint("GPU node", Kind.PART_USAGE).name == "gpuNode"


@pytest.mark.parametrize("a,b", [
    ("GPU cluster", "gpu cluster"),
    ("GPU Cluster", "GPU  clusters"),
    ("notebook session", "Notebook Sessions"),
])
def test_same_concept_converges_to_one_symbol(a, b):
    """The core guarantee: independent callers phrasing a concept differently
    get the same symbol, not two near-duplicates."""
    r = SymbolRegistry()
    first = r.mint(a, Kind.PART_DEF)
    second = r.mint(b, Kind.PART_DEF)
    assert first.name == second.name
    assert len(r) == 1


def test_distinct_concepts_do_not_merge():
    r = SymbolRegistry()
    r.mint("GPU cluster", Kind.PART_DEF)
    r.mint("GPU node", Kind.PART_DEF)
    assert len(r) == 2


def test_reserved_word_is_avoided():
    """`attribute state : String` is a real syntax error in the pilot
    implementation; the registry must never mint a reserved identifier."""
    r = SymbolRegistry()
    sym = r.mint("state", Kind.ATTRIBUTE)
    assert sym.name.lower() not in RESERVED
    assert sym.name == "stateElement"


def test_collision_between_different_kinds_gets_suffixed():
    """Two different kinds can both want 'Session'; names are globally unique so
    the SysML namespace stays unambiguous."""
    r = SymbolRegistry()
    a = r.mint("session", Kind.PART_DEF)
    b = r.mint("session", Kind.STATE_DEF)
    assert a.name != b.name
    assert {a.name, b.name} == {"Session", "Session2"}


def test_req_ids_accumulate_for_traceability():
    r = SymbolRegistry()
    r.mint("GPU cluster", Kind.PART_DEF, req_id="DOC-0001")
    sym = r.mint("gpu clusters", Kind.PART_DEF, req_id="DOC-0007")
    assert sym.req_ids == ["DOC-0001", "DOC-0007"]


def test_minting_is_deterministic_across_instances():
    """Same inputs, same order → same names, so reruns diff cleanly."""
    def build():
        r = SymbolRegistry()
        for intent in ("GPU cluster", "notebook session", "scheduler", "state"):
            r.mint(intent, Kind.PART_DEF)
        return r.names()
    assert build() == build()


def test_prompt_block_lists_authoritative_names():
    r = SymbolRegistry()
    r.mint("GPU cluster", Kind.PART_DEF, description="pool of GPU nodes")
    r.mint("allocate GPU", Kind.ACTION_DEF)
    block = r.as_prompt_block()
    assert "part def GPUCluster — pool of GPU nodes" in block
    assert "action def AllocateGPU" in block


def test_prompt_block_truncation_is_visible():
    """Silent truncation would read as 'you know about everything'; it must not be."""
    r = SymbolRegistry()
    for i in range(10):
        r.mint(f"component {i}", Kind.PART_DEF)
    block = r.as_prompt_block(limit=3)
    assert "and 7 more (truncated)" in block


def test_validate_text_reports_dropped_names():
    r = SymbolRegistry()
    r.mint("GPU cluster", Kind.PART_DEF)
    r.mint("notebook session", Kind.PART_DEF)
    missing = r.validate_text("part def GPUCluster { }")
    assert missing == ["NotebookSession"]


def test_roundtrip_persistence(tmp_path):
    r = SymbolRegistry()
    r.mint("GPU cluster", Kind.PART_DEF, req_id="DOC-0001", description="pool")
    r.mint("GPU cluster", Kind.PART_USAGE)
    path = tmp_path / "symbols.json"
    r.save(path)

    loaded = SymbolRegistry.load(path)
    assert loaded.names() == r.names()
    assert loaded.get("GPUCluster").req_ids == ["DOC-0001"]
    # After reload the registry must still converge, not mint a duplicate.
    again = loaded.mint("gpu clusters", Kind.PART_DEF)
    assert again.name == "GPUCluster"
    assert len(loaded) == 2


@pytest.mark.parametrize("a,b", [
    ("enforce per user GPU quota", "EnforcePerUserGPUQuota"),
    ("GPU cluster", "GPUCluster"),
    ("notebook session", "notebookSession"),
    ("allocate GPU", "AllocateGPU"),
])
def test_pascal_and_phrase_forms_converge(a, b):
    """Regression: agents are inconsistent about casing. One stage returned
    'enforce per user GPU quota' and another 'EnforcePerUserGPUQuota' for the same
    concept, minting EnforcePerUserGPUQuota and EnforcePerUserGPUQuota2 in a real
    run. Both forms must reach one symbol."""
    r = SymbolRegistry()
    assert r.mint(a, Kind.ACTION_DEF).name == r.mint(b, Kind.ACTION_DEF).name
    assert len(r) == 1


def test_resolver_strips_sysml_keyword_prefix():
    """Regression: on real data the model returned every interface endpoint as
    'part dataManagementService' rather than 'dataManagementService', so none
    resolved and all interfaces lost both ends."""
    from architect_agent.generate import _resolve
    r = SymbolRegistry()
    r.mint("data management service", Kind.PART_USAGE)
    assert _resolve(r, "part dataManagementService", Kind.PART_USAGE) == "dataManagementService"
    assert _resolve(r, "dataManagementService", Kind.PART_USAGE) == "dataManagementService"
    assert _resolve(r, "data management service", Kind.PART_USAGE) == "dataManagementService"
    assert _resolve(r, "part def NoSuchThing", Kind.PART_USAGE) is None
