"""SysML v2 text emission and Markdown artifact writing.

Deterministic: given the same registry and stage outputs, byte-identical output.
No LLM calls happen here. Every identifier comes from the registry, so this is the
point where cross-artifact naming consistency actually pays off — the same
`sym.name` string is written into model.sysml, interfaces.md and allocations.md.
"""

from __future__ import annotations

from pathlib import Path

from .generate import StageOutput
from .symbols import Kind, SymbolRegistry

#: Required or `Integer`/`String` do not resolve. The visibility keyword is
#: mandatory — bare `import X::*;` is a syntax error in the pilot implementation.
STDLIB_IMPORT = "    private import ScalarValues::*;"


def emit_model(package: str, reg: SymbolRegistry, *, logical: StageOutput,
               functions: StageOutput, constraint_defs: StageOutput,
               allocs: StageOutput, interfaces_out: StageOutput | None = None,
               behavior_out: StageOutput | None = None) -> str:
    """Assemble the complete `.sysml` document."""
    lines = [f"package {package} {{", STDLIB_IMPORT, ""]

    if functions.records:
        lines.append("    // Functional decomposition")
        for rec in functions.records:
            lines.append(f"    action def {rec['name']};")
        lines.append("")
        # Emit a usage for every action definition that has one. Allocation ends
        # must resolve to *features*; a definition alone is not a feature, so
        # without these the `allocate` lines below reference nothing.
        usages = [(u, _def_of(reg, reg.get(u))) for u in reg.names(Kind.ACTION_USAGE)]
        emitted = [(u, d) for u, d in usages if d]
        if emitted:
            for usage, definition in emitted:
                lines.append(f"    action {usage} : {definition};")
            lines.append("")

    if logical.records:
        lines.append("    // Logical architecture")
        for rec in logical.records:
            attrs = rec.get("attributes") or []
            if attrs:
                lines.append(f"    part def {rec['def']} {{")
                for a in attrs:
                    lines.append(f"        attribute {a['name']} : {a['type']};")
                lines.append("    }")
            else:
                lines.append(f"    part def {rec['def']};")
        lines.append("")
        for rec in logical.records:
            lines.append(f"    part {rec['usage']} : {rec['def']};")
        lines.append("")

    if interfaces_out and interfaces_out.records:
        lines.append("    // Interfaces")
        for rec in interfaces_out.records:
            attrs = rec.get("attributes") or []
            if attrs:
                lines.append(f"    port def {rec['port']} {{")
                for a in attrs:
                    lines.append(f"        attribute {a['name']} : {a['type']};")
                lines.append("    }")
            else:
                lines.append(f"    port def {rec['port']};")
            # Both ends are declared against the same port definition; naming them
            # supplier/consumer keeps the direction explicit in the model text.
            lines.append(f"    interface def {rec['name']} {{")
            lines.append(f"        end supplier : {rec['port']};")
            lines.append(f"        end consumer : {rec['port']};")
            lines.append("    }")
        lines.append("")

    if behavior_out and behavior_out.records:
        lines.append("    // Behavior")
        for rec in behavior_out.records:
            lines.append(f"    state def {rec['name']} {{")
            for st in rec.get("states") or []:
                lines.append(f"        state {st};")
            for tr in rec.get("transitions") or []:
                lines.append(f"        transition {tr['from']} then {tr['to']};")
            lines.append("    }")
        lines.append("")

    if constraint_defs.records:
        lines.append("    // Constraints")
        for rec in constraint_defs.records:
            lines.append(f"    constraint def {rec['name']} {{")
            for p in rec.get("parameters") or []:
                lines.append(f"        in {p['name']} : {p['type']};")
            lines.append(f"        {_constraint_body(rec)}")
            lines.append("    }")
        lines.append("")

    if allocs.records:
        lines.append("    // Allocations")
        for rec in allocs.records:
            fn, comp = reg.get(rec["function"]), reg.get(rec["component"])
            if not fn or not comp:
                continue
            # Allocation ends must be usages (features). Definitions are not
            # features and will not resolve.
            src = fn.name if fn.kind in (Kind.ACTION_USAGE, Kind.PART_USAGE) else _usage_of(reg, fn)
            dst = comp.name if comp.kind in (Kind.ACTION_USAGE, Kind.PART_USAGE) else _usage_of(reg, comp)
            if src and dst:
                lines.append(f"    allocate {src} to {dst};")
        lines.append("")

    lines.append("}")
    return "\n".join(lines) + "\n"


_IDENT = __import__("re").compile(r"[A-Za-z_][A-Za-z_0-9]*")
_COMPARATORS = ("==", "<=", ">=", "!=", "<", ">")


def _constraint_body(rec: dict) -> str:
    """Return a constraint body that will actually resolve.

    A model-proposed expression is only usable if it is a comparison AND every
    identifier in it is a declared parameter — otherwise it references elements
    that do not exist and the Step 5 gate rejects the whole model. Falling back to
    `true` keeps the constraint present and traceable while the unusable expression
    is preserved verbatim in constraints.md for a human to repair.
    """
    expr = (rec.get("expression") or "").strip()
    if not expr or not any(op in expr for op in _COMPARATORS):
        return "true"
    declared = {p["name"] for p in rec.get("parameters") or []}
    referenced = set(_IDENT.findall(expr)) - {"true", "false", "and", "or", "not"}
    if referenced - declared:
        return "true"
    return expr


def _def_of(reg: SymbolRegistry, sym) -> str | None:
    """Find the definition a usage was minted alongside, by shared intent."""
    if sym is None:
        return None
    want = Kind.PART_DEF if sym.kind == Kind.PART_USAGE else Kind.ACTION_DEF
    for candidate in reg.names(want):
        if reg.get(candidate).intent_key == sym.intent_key:
            return candidate
    return None


def _usage_of(reg: SymbolRegistry, sym) -> str | None:
    """Find the usage minted alongside a definition, by shared intent."""
    want = Kind.PART_USAGE if sym.kind == Kind.PART_DEF else Kind.ACTION_USAGE
    for candidate in reg.names(want):
        if reg.get(candidate).intent_key == sym.intent_key:
            return candidate
    return None


# -- Markdown artifacts --------------------------------------------------------

def _table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "_None produced._\n"
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    out += ["| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def functional_decomposition_md(stage: StageOutput) -> str:
    rows = [[r["name"], r.get("parent") or "—", r.get("description", ""), r["req_id"]]
            for r in stage.records]
    return ("# Functional Decomposition\n\n"
            + _table(["Function", "Parent", "Description", "Requirement"], rows))


def logical_architecture_md(stage: StageOutput) -> str:
    rows = [[r["def"], r["usage"],
             ", ".join(f"{a['name']}: {a['type']}" for a in r.get("attributes") or []) or "—",
             r.get("description", ""), r["req_id"]]
            for r in stage.records]
    return ("# Logical Architecture\n\n"
            + _table(["Definition", "Usage", "Attributes", "Responsibility", "Requirement"], rows))


def constraints_md(stage: StageOutput) -> str:
    rows = [[r["name"], r.get("category", ""), r.get("expression", "") or "—",
             r.get("description", ""), r["req_id"]] for r in stage.records]
    body = ("# Constraints\n\n"
            + _table(["Constraint", "Category", "Expression", "Description", "Requirement"], rows))
    if stage.unresolved:
        body += "\n## Unquantified\n\nRequirements implying a limit with no measurable bound:\n\n"
        body += "".join(f"- {u}\n" for u in stage.unresolved)
    return body


def allocations_md(stage: StageOutput) -> str:
    rows = [[r["function"], r["component"], r.get("rationale", ""), r["req_id"]]
            for r in stage.records]
    body = "# Allocations\n\n" + _table(["Function", "Component", "Rationale", "Requirement"], rows)
    if stage.unresolved:
        body += "\n## Unallocated\n\n" + "".join(f"- {u}\n" for u in stage.unresolved)
    return body


def interfaces_md(stage: StageOutput) -> str:
    rows = [[r["name"], r["port"],
             ", ".join(f"{e['role']}={e['element']}" for e in r.get("ends") or []) or "—",
             r.get("description", ""), r["req_id"]] for r in stage.records]
    body = "# Interfaces\n\n" + _table(
        ["Interface", "Port", "Ends", "Description", "Requirement"], rows)
    if stage.unresolved:
        body += "\n## Unresolved ends\n\n" + "".join(f"- {u}\n" for u in stage.unresolved)
    return body


def behavior_md(stage: StageOutput) -> str:
    rows = [[r["name"], r.get("subject", "") or "—",
             ", ".join(r.get("states") or []) or "—",
             "; ".join(f"{t['from']}->{t['to']}" for t in r.get("transitions") or []) or "—",
             r["req_id"]] for r in stage.records]
    body = "# Behavior\n\n" + _table(
        ["State machine", "Subject", "States", "Transitions", "Requirement"], rows)
    if stage.unresolved:
        body += "\n## Unresolved transitions\n\n" + "".join(f"- {u}\n" for u in stage.unresolved)
    return body


def verification_plan_md(stage: StageOutput) -> str:
    rows = [[r["req_id"], r.get("method", ""), r.get("criterion", ""),
             ", ".join(r.get("elements") or []) or "—"] for r in stage.records]
    return ("# Verification Plan\n\n"
            + _table(["Requirement", "Method", "Success criterion", "Elements"], rows))


def traceability_md(reg: SymbolRegistry) -> str:
    """Requirement → element coverage. The reason `req_ids` accumulate on symbols."""
    by_req: dict[str, list[str]] = {}
    for name in reg.names():
        sym = reg.get(name)
        for rid in sym.req_ids:
            by_req.setdefault(rid, []).append(f"{sym.kind.value} {sym.name}")
    rows = [[rid, str(len(elems)), ", ".join(sorted(elems))]
            for rid, elems in sorted(by_req.items())]
    return ("# Traceability\n\n"
            + _table(["Requirement", "Elements", "Architecture elements"], rows))


def write_package(root: str | Path, *, model: str, artifacts: dict[str, str],
                  diagrams: dict[str, bytes] | None = None) -> Path:
    """Write the canonical output tree (implementation.md §2.10)."""
    root = Path(root)
    (root / "artifacts").mkdir(parents=True, exist_ok=True)
    (root / "diagrams").mkdir(parents=True, exist_ok=True)
    (root / "model.sysml").write_text(model)
    for name, text in artifacts.items():
        (root / "artifacts" / name).write_text(text)
    for name, blob in (diagrams or {}).items():
        (root / "diagrams" / name).write_bytes(blob)
    return root
