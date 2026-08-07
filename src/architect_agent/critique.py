"""Built-in design critique — the deterministic backbone of the Architect's refine loop.
NOTE: the loop lives inside the Architect (like the Analyst's own refine loop).

The problems a per-aspect design can have (found by inspecting the Restaurant diagrams)
are model problems the diagram merely reveals, and every one is objectively checkable —
so the critique is deterministic + reranker-based, NOT a vision model eyeballing a PNG.
Each finding carries precise reasoning the Architect can act on when it regenerates.

Checks:
  near_duplicate_interfaces  reranker — two interfaces that denote the same boundary
  ownership_violations       an entity defined in more than one aspect (should be owned
                             once, consumed elsewhere via a tag)
  consumed_but_unowned       set difference — an entity some aspect consumes that no aspect
                             owns (a real gap); replaces the old glossary-coverage check,
                             which over-flagged every role/attribute/value in the glossary
  misassignment              an element whose requirement is tagged X but sits in a branch
                             that does not own X

Vision review (advisory, elsewhere) supplements this for genuinely visual issues; it is
not the gate. The loop: design -> critique -> if findings, regenerate with the reasons,
bounded; still failing -> escalate to a human.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass, field

from .retrieval import rerank

#: Sigmoid score above which two element names denote the same thing. The reranker put a
#: real near-dup (TenantConfigurationInterface vs …ManagementInterface) at ~0.95 and
#: unrelated pairs below 0.5, so 0.8 is safely inside the gap.
DUP_THRESHOLD = 0.80


@dataclass
class Finding:
    kind: str                       # near_duplicate_interface | ownership_violation |
                                    # unowned_entity | cross_cutting_placement
    severity: str                   # "error" (must fix) | "warning" (should)
    subjects: list[str]             # the elements involved
    reason: str                     # precise, actionable
    aspect: str | None = None
    score: float | None = None


@dataclass
class Critique:
    findings: list[Finding] = field(default_factory=list)

    @property
    def clean(self) -> bool:
        return not any(f.severity == "error" for f in self.findings)

    def by_kind(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for f in self.findings:
            out[f.kind] = out.get(f.kind, 0) + 1
        return out


def near_duplicate_interfaces(interfaces: list[str], *, threshold: float = DUP_THRESHOLD,
                              aspect: str | None = None) -> list[Finding]:
    """Flag interface pairs the reranker judges to be the same boundary. One rerank call
    per interface against the rest; symmetric pairs de-duped."""
    findings: list[Finding] = []
    names = sorted(set(interfaces))
    seen: set[tuple[str, str]] = set()
    for i, name in enumerate(names):
        others = names[:i] + names[i + 1:]
        if not others:
            continue
        scores = rerank(name, others)
        for other, s in zip(others, scores):
            key = tuple(sorted((name, other)))
            if s >= threshold and key not in seen:
                seen.add(key)
                findings.append(Finding(
                    kind="near_duplicate_interface", severity="error",
                    subjects=list(key), aspect=aspect, score=round(s, 2),
                    reason=(f"'{key[0]}' and '{key[1]}' score {s:.2f} similar — they name "
                            "the same boundary; design one interface, not two.")))
    return findings


#: Glossary terms that are primitives/types/values, not ownable entities. Consuming these
#: is never a gap. Deliberately small and suffix-based — a false miss just adds one warning.
_PRIMITIVE_SUFFIXES = ("Id", "Timestamp", "Date", "Time", "Flag", "Status", "Count",
                       "Name", "Type", "Number", "Amount", "Code", "Url", "Text")
_PRIMITIVES = {"Timestamp", "Date", "Time", "Language", "String", "Integer", "Boolean", "Real"}


def _is_primitive(name: str) -> bool:
    return name in _PRIMITIVES or name.endswith(_PRIMITIVE_SUFFIXES)


def consumed_but_unowned(components_by_aspect: dict[str, list[str]],
                         consumes_by_aspect: dict[str, list[str]],
                         glossary_terms: list[str]) -> list[Finding]:
    """An ENTITY that some aspect consumes but no aspect owns.

    Replaces the naive "glossary term with no component" check (which over-flagged every
    role/attribute in the glossary). Deterministic set logic — names come from one glossary
    so they match exactly. Concerns (tags) are ignored; only glossary ENTITIES count, and
    primitives/types are skipped.

    Severity is WARNING, not error: we cannot deterministically tell an EXTERNAL dependency
    (LLM, a third-party service) from a genuine coverage gap (a domain entity nobody owns).
    Both read as "consumed but unowned — external dependency or uncovered entity; confirm."
    A human/Planner rules; it does not block the build.
    """
    glossary = set(glossary_terms)
    owned = {c for cs in components_by_aspect.values() for c in cs}
    findings: list[Finding] = []
    seen: set[str] = set()
    for aspect, consumes in consumes_by_aspect.items():
        for name in consumes:
            if name in glossary and name not in owned and not _is_primitive(name) and name not in seen:
                seen.add(name)
                findings.append(Finding(
                    kind="unowned_entity", severity="warning", subjects=[name], aspect=aspect,
                    reason=(f"'{name}' is consumed (by '{aspect}') but owned by no aspect — "
                            "an external dependency or an uncovered entity; confirm.")))
    return findings


def ownership_violations(defined_by_aspect: dict[str, set[str]]) -> list[Finding]:
    """An entity DEFINED in more than one aspect. It should be owned by one aspect and
    consumed elsewhere via its tag, not re-defined per aspect (that is how `tenant` ended
    up in five diagrams)."""
    findings: list[Finding] = []
    aspects_of: dict[str, list[str]] = {}
    for aspect, names in defined_by_aspect.items():
        for n in names:
            aspects_of.setdefault(n, []).append(aspect)
    for name, aspects in sorted(aspects_of.items()):
        if len(aspects) > 1:
            findings.append(Finding(
                kind="ownership_violation", severity="error", subjects=[name],
                reason=(f"'{name}' is defined in {len(aspects)} aspects "
                        f"({', '.join(sorted(aspects))}); one aspect must own it and the "
                        "others consume it via its tag.")))
    return findings


def misassignment(nodes: list[dict], branch_owner_tag: dict[str, str] | None = None) -> list[Finding]:
    """A node tagged with a concern owned by another branch, placed away from its owner.

    `nodes`: [{req_id, branch, tags}]. `branch_owner_tag`: which branch owns each tag
    (e.g. authentication -> 'User & Access Control'). A node whose tag is owned elsewhere is
    fine (that is the cross-cutting case) UNLESS it carries no other reason to be where it
    is — this check is advisory (warning), since single-parent placement is intentional.
    """
    findings: list[Finding] = []
    owner = branch_owner_tag or {}
    for n in nodes:
        for tag in n.get("tags", []):
            home = owner.get(tag)
            if home and n.get("branch") and home != n["branch"]:
                # Expected for genuine cross-cutting; only note it so the loop can check
                # the element was modelled as a CONSUMER, not a re-definition.
                findings.append(Finding(
                    kind="cross_cutting_placement", severity="warning",
                    subjects=[n["req_id"]], aspect=n.get("branch"),
                    reason=(f"{n['req_id']} carries tag '{tag}' owned by '{home}' but sits "
                            f"in '{n['branch']}' — ensure it consumes '{tag}', not redefines it.")))
    return findings


_COMPLETENESS_PRIMS = {"String", "Integer", "Real", "Boolean", "DateTime", "UUID",
                       "Decimal", "Void"}


def _base_type(t: str) -> str:
    """Strip List<…>/Optional<…> wrappers to the inner type name."""
    t = (t or "").strip()
    for w in ("List<", "Optional<"):
        if t.startswith(w) and t.endswith(">"):
            return _base_type(t[len(w):-1])
    return t


def completeness_findings(designs, glossary_terms) -> list[Finding]:
    """Did the Architect finish its job? A self-assessment over the FULL per-aspect design:
      - an owned entity (component) with NO attributes — its data model was never specified
        (this is the "the Architect shall define X's fields" leak that becomes junk downstream);
      - an interface that exposes NO operations;
      - an attribute whose type is not a primitive, a glossary term, or a defined component.
    Only the first is an ERROR (surfaces as a handover open issue); the rest are warnings. This
    is what stops the Architect from shipping an incomplete handover that the Planner then
    questions and the resolver turns into a fabricated requirement."""
    glossary = {t for t in (glossary_terms or [])}
    comp_names = {c.get("name") for d in designs for c in (getattr(d, "components", None) or [])
                  if isinstance(c, dict) and c.get("name")}
    defined = glossary | comp_names | _COMPLETENESS_PRIMS
    findings: list[Finding] = []
    for d in designs:
        branch = getattr(d, "branch", None)
        for c in (getattr(d, "components", None) or []):
            if not isinstance(c, dict) or not c.get("name"):
                continue
            name = c["name"]
            attrs = [a for a in (c.get("attributes") or []) if isinstance(a, dict) and a.get("name")]
            if not attrs:
                findings.append(Finding(
                    kind="incomplete_entity", severity="error", subjects=[name], aspect=branch,
                    reason=(f"Component '{name}' (aspect '{branch}') has NO attributes defined — "
                            "the Architect owns this entity but never specified its data model.")))
                continue
            for a in attrs:
                bt = _base_type(a.get("type") or "")
                if bt and bt not in defined:
                    findings.append(Finding(
                        kind="undefined_type", severity="warning", subjects=[name, bt], aspect=branch,
                        reason=(f"Attribute '{name}.{a['name']}' has type '{bt}', which is not a "
                                "primitive, a glossary term, or a defined component.")))
        for i in (getattr(d, "interfaces", None) or []):
            if isinstance(i, dict) and i.get("name") and not (i.get("operations") or []):
                findings.append(Finding(
                    kind="empty_interface", severity="warning", subjects=[i["name"]], aspect=branch,
                    reason=(f"Interface '{i['name']}' (aspect '{branch}') exposes no operations — "
                            "the Architect did not specify how it is called.")))
    return findings


def critique_design(*, interfaces_by_aspect: dict[str, list[str]],
                    components_by_aspect: dict[str, list[str]],
                    glossary_terms: list[str],
                    consumes_by_aspect: dict[str, list[str]] | None = None,
                    nodes: list[dict] | None = None,
                    branch_owner_tag: dict[str, str] | None = None) -> Critique:
    """Run the full deterministic critique over a per-aspect design."""
    findings: list[Finding] = []
    for aspect, ifaces in interfaces_by_aspect.items():
        findings += near_duplicate_interfaces(ifaces, aspect=aspect)
    findings += ownership_violations({a: set(cs) for a, cs in components_by_aspect.items()})
    if consumes_by_aspect is not None:
        findings += consumed_but_unowned(components_by_aspect, consumes_by_aspect, glossary_terms)
    if nodes:
        findings += misassignment(nodes, branch_owner_tag)
    return Critique(findings=findings)
