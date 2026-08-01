"""diagram_review tests — GPU-free (failure-safe behavior + formatting).

The vision path itself is non-deterministic and advisory; these tests lock the CONTRACT:
it must never raise or block, and it formats concerns into open_issues correctly.
"""
from architect_agent import diagram_review
from architect_agent.diagram_review import DiagramReview


def test_open_issues_formatting():
    reviews = [
        DiagramReview("Auth", ok=True, concerns=[]),
        DiagramReview("Menu", ok=False, concerns=["MenuItem missing"]),
    ]
    issues = diagram_review.open_issues(reviews)
    assert any("could not confirm" in i and "Menu" in i for i in issues)
    assert any("MenuItem missing" in i for i in issues)
    # a clean review contributes nothing
    assert not any("Auth" in i for i in issues)


def test_review_is_failsafe_when_render_fails(monkeypatch):
    """If rendering fails, review must return ok=True with no concerns — never block."""
    monkeypatch.setattr(diagram_review, "render_mermaid", lambda *a, **k: False)
    from architect_agent.aspect_design import AspectDesign
    rv = diagram_review.review_aspect(AspectDesign(branch="X"), "flowchart TB")
    assert rv.ok is True and rv.concerns == []
