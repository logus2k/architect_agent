"""Integration tests for the SysML v2 toolchain.

These drive the real jar — no mocks. They are slow (~2 s JVM + library load per
call) but they are the only thing that proves the gate actually gates.
"""

import pytest

from architect_agent import sysml

pytestmark = pytest.mark.skipif(not sysml.is_available(),
                                reason="SysML toolchain not present in data/")

VALID = """
package Demo {
    private import ScalarValues::*;
    part def GPUCluster { attribute totalGPUs : Integer; }
    part cluster : GPUCluster;
}
"""


def test_valid_model_passes():
    r = sysml.validate(VALID)
    assert r.valid
    assert r.errors == []


def test_bare_import_is_a_syntax_error():
    """`import X::*;` without a visibility keyword does not parse — the mistake
    an earlier draft of the spec made."""
    r = sysml.validate(VALID.replace("private import", "import"))
    assert not r.valid
    assert r.syntax_errors


def test_missing_import_is_a_semantic_error():
    """Distinguishing this from a syntax error is the whole reason we load the
    standard library: `Integer` is unresolvable without it."""
    r = sysml.validate(VALID.replace("    private import ScalarValues::*;\n", ""))
    assert not r.valid
    assert not r.syntax_errors
    assert any("Integer" in e.message for e in r.semantic_errors)


def test_reserved_word_rejected():
    """Guards the RESERVED list in symbols.py: if the grammar ever stops treating
    `state` as reserved, this test tells us the list is over-broad."""
    r = sysml.validate("package Demo { part def P { attribute state : Integer; } }")
    assert not r.valid


def test_render_produces_png(tmp_path):
    out = tmp_path / "demo.png"
    r = sysml.validate(VALID, render_png=out)
    assert r.valid
    assert out.exists() and out.stat().st_size > 1000
    assert out.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
    assert (tmp_path / "demo.png.puml").exists()


def test_invalid_model_is_not_rendered(tmp_path):
    """Rendering an unvalidated model is meaningless; the tool must refuse."""
    out = tmp_path / "nope.png"
    r = sysml.validate("package Demo { stateMachine X { } }", render_png=out)
    assert not r.valid
    assert not out.exists()


def test_missing_toolchain_raises_not_returns_invalid(tmp_path):
    """A broken install must never masquerade as 'your model is invalid'."""
    with pytest.raises(sysml.SysMLToolError):
        sysml.validate(VALID, jar=tmp_path / "absent.jar")
