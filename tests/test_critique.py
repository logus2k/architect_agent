"""Critique tests — GPU-free.

The reranker is mocked (near-dup identity is exercised with a deterministic stub), and the
set-logic checks run on a fixture taken from the REAL refined Restaurant design, so these
prove behaviour without touching the GPU.
"""

import pytest

from architect_agent import critique


# --- fixture: the real refined Restaurant design (owner + consumes per aspect) -----------

GLOSSARY = ["Tenant", "TenantAdministrator", "TenantConfiguration", "ContactForm", "Menu",
            "Category", "Item", "FoodImage", "Reservation", "User", "GoogleOAuthLogin",
            "AiDescription", "TenantAsset", "SQLiteInstance",
            # non-component glossary terms that USED to be false-positive "missing" flags:
            "Admin", "ApprovalFlag", "AiOperation", "Allergen"]

COMPONENTS = {
    "Tenant Administration": ["Tenant", "TenantAdministrator", "TenantConfiguration", "ContactForm"],
    "Menu & Item Catalog": ["Menu", "Category", "Item", "FoodImage"],
    "Reservations": ["Reservation"],
    "User & Access Control": ["User", "GoogleOAuthLogin"],
    "AI Content Generation": ["AiDescription"],
    "System Infrastructure": ["TenantAsset", "SQLiteInstance"],
}

CONSUMES = {
    "Tenant Administration": ["authentication", "multi-tenancy", "FoodImage", "Item", "Menu", "Reservation"],
    "Menu & Item Catalog": ["multi-tenancy", "file-upload", "TenantAsset"],
    "Reservations": ["authentication", "security"],
    "User & Access Control": ["authentication", "anonymous"],
    "AI Content Generation": ["LLM", "localization", "FoodImage", "Item"],
    "System Infrastructure": ["multi-tenancy", "localization", "TenantConfiguration"],
}


# --- consumed_but_unowned: the fix for the 22 false positives ----------------------------

def test_no_false_positive_on_roles_attributes_values():
    """The old check flagged Admin/ApprovalFlag/AiOperation/Allergen as 'missing components'.
    They are roles/attributes/values, not owned entities, and are not consumed — so the new
    check must NOT flag them."""
    findings = critique.consumed_but_unowned(COMPONENTS, CONSUMES, GLOSSARY)
    flagged = {s for f in findings for s in f.subjects}
    for noise in ("Admin", "ApprovalFlag", "AiOperation", "Allergen"):
        assert noise not in flagged, f"{noise} should not be flagged"


def test_refined_design_has_no_unowned_entities():
    """Every entity consumed in the refined design is owned by some aspect — so zero gaps."""
    findings = critique.consumed_but_unowned(COMPONENTS, CONSUMES, GLOSSARY)
    assert findings == [], f"unexpected gaps: {[f.reason for f in findings]}"


def test_genuinely_unowned_entity_is_flagged():
    """A real gap — an entity consumed but owned by nobody — must be caught."""
    consumes = dict(CONSUMES)
    consumes["Reservations"] = consumes["Reservations"] + ["PaymentMethod"]
    glossary = GLOSSARY + ["PaymentMethod"]
    findings = critique.consumed_but_unowned(COMPONENTS, consumes, glossary)
    assert [f.subjects[0] for f in findings] == ["PaymentMethod"]
    assert findings[0].severity == "warning"  # external-or-gap; a human confirms


def test_consumed_tag_is_not_treated_as_missing_entity():
    """`authentication` is a concern (tag), consumed everywhere, owned by no COMPONENT — but
    it is not a glossary entity, so it must not be flagged as an unowned entity."""
    findings = critique.consumed_but_unowned(COMPONENTS, CONSUMES, GLOSSARY)
    assert not any("authentication" in f.subjects for f in findings)


# --- ownership_violations: pure logic --------------------------------------------------

def test_ownership_violation_when_entity_defined_twice():
    comps = {"A": ["Tenant", "Menu"], "B": ["Menu"]}
    findings = critique.ownership_violations({k: set(v) for k, v in comps.items()})
    assert [f.subjects[0] for f in findings] == ["Menu"]
    assert findings[0].severity == "error"


def test_no_ownership_violation_when_each_entity_owned_once():
    findings = critique.ownership_violations({k: set(v) for k, v in COMPONENTS.items()})
    assert findings == []


# --- near_duplicate_interfaces: reranker mocked (no GPU) --------------------------------

def test_near_duplicate_flagged_with_mocked_reranker(monkeypatch):
    """Two names the (stubbed) reranker calls the same must be flagged; unrelated must not."""
    def fake_rerank(query, docs):
        # 'FooInterface' ~ 'FooManagementInterface' are "the same"; anything else unrelated.
        base = query.replace("Management", "")
        return [0.95 if d.replace("Management", "") == base else 0.1 for d in docs]

    monkeypatch.setattr(critique, "rerank", fake_rerank)
    findings = critique.near_duplicate_interfaces(
        ["FooInterface", "FooManagementInterface", "BarInterface"], aspect="X")
    pairs = {tuple(sorted(f.subjects)) for f in findings}
    assert ("FooInterface", "FooManagementInterface") in pairs
    assert not any("BarInterface" in p for p in pairs)


def test_near_duplicate_clean_when_all_distinct(monkeypatch):
    monkeypatch.setattr(critique, "rerank", lambda q, docs: [0.1] * len(docs))
    findings = critique.near_duplicate_interfaces(["AInterface", "BInterface", "CInterface"])
    assert findings == []


def test_primitives_are_not_flagged_as_unowned():
    """LLM/Language/Timestamp-style consumed primitives must not be reported as gaps."""
    comps = {"A": ["Widget"]}
    consumes = {"A": ["Timestamp", "UserId", "Language", "PaymentMethod"]}
    glossary = ["Widget", "Timestamp", "UserId", "Language", "PaymentMethod"]
    flagged = {s for f in critique.consumed_but_unowned(comps, consumes, glossary) for s in f.subjects}
    assert "Timestamp" not in flagged and "UserId" not in flagged and "Language" not in flagged
    assert "PaymentMethod" in flagged  # a real domain entity still surfaces
