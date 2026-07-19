"""SysML v2 validation and diagram rendering.

Wraps the SysML v2 Pilot Implementation (the OMG reference implementation) running
headlessly from a single fat jar. Fully offline: no SysON, no GraphViz, no network.

Everything here is deliberately deterministic — this is the authoritative gate that
decides whether generated model text is publishable, so it must not be an LLM.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

#: Default toolchain location; a bind-mounted data/ directory in the container.
DATA_DIR = Path(os.environ.get("ARCHITECT_DATA_DIR", "data"))
TOOLCHAIN = DATA_DIR / "sysml-toolchain"
DEFAULT_JAR = TOOLCHAIN / "jupyter-sysml-kernel-0.60.1-all.jar"
DEFAULT_CLASSES = Path(os.environ.get("ARCHITECT_TOOL_CLASSES", TOOLCHAIN / "classes"))
DEFAULT_LIBRARY = TOOLCHAIN / "sysml.library"

#: The JVM loads 94 library resources on every invocation (~1.7 s), so a slow call
#: is normal and a short timeout will produce spurious failures.
DEFAULT_TIMEOUT_S = 300


class SysMLToolError(RuntimeError):
    """The toolchain could not be run at all — missing jar, JVM, or timeout.

    Distinct from an invalid model, which is a normal result, not an error.
    """


@dataclass
class Issue:
    message: str
    line: int
    column: int

    def __str__(self) -> str:
        return f"{self.message} (line {self.line}, col {self.column})"


@dataclass
class ValidationResult:
    valid: bool
    syntax_errors: list[Issue] = field(default_factory=list)
    semantic_errors: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)
    png: str | None = None
    puml: str | None = None
    render_error: str | None = None

    @property
    def errors(self) -> list[Issue]:
        return self.syntax_errors + self.semantic_errors

    def summary(self) -> str:
        if self.valid:
            return "VALID"
        return "INVALID: " + "; ".join(str(i) for i in self.errors)


def _issues(raw: list[dict]) -> list[Issue]:
    return [Issue(message=i["message"], line=i["line"], column=i["column"]) for i in raw]


def validate(
    model_text: str,
    render_png: str | Path | None = None,
    *,
    jar: Path = DEFAULT_JAR,
    classes: Path = DEFAULT_CLASSES,
    library: Path = DEFAULT_LIBRARY,
    timeout: int = DEFAULT_TIMEOUT_S,
) -> ValidationResult:
    """Validate SysML v2 text, optionally rendering a diagram.

    Rendering only happens when the model is valid — an invalid model cannot be
    resolved into a diagram, so validation necessarily precedes it.

    Artifact ownership: this function cleans up its own temporary `.sysml` input,
    but when `render_png` is given it writes TWO files the caller owns — the PNG at
    `render_png` and its PlantUML source at `render_png + ".puml"`. Both paths are
    returned on the result (`.png`, `.puml`). A caller rendering into a transient
    directory is responsible for removing both; the `.puml` is kept beside the PNG
    deliberately so a diagram can be re-rendered or hand-edited.
    """
    for path, what in ((jar, "kernel jar"), (library, "standard library")):
        if not path.exists():
            raise SysMLToolError(f"{what} not found at {path} — is data/ mounted?")

    tmp = Path(os.environ.get("TMPDIR", "/tmp")) / f"architect_{os.getpid()}.sysml"
    tmp.write_text(model_text)
    try:
        cmd = [
            "java", "-cp", f"{jar}:{classes}", "ArchitectTool",
            # MUST be absolute — a relative path makes loadLibrary() fail on the
            # spaces in its hardcoded subdirectory names.
            str(library.resolve()),
            str(tmp),
        ]
        if render_png:
            cmd.append(str(render_png))
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired as e:
            raise SysMLToolError(f"validation timed out after {timeout}s") from e
    finally:
        tmp.unlink(missing_ok=True)

    # The JVM writes log4j warnings to stdout; our JSON is the last line.
    lines = [ln for ln in proc.stdout.splitlines() if ln.strip().startswith("{")]
    if not lines:
        raise SysMLToolError(
            f"no JSON from toolchain (exit {proc.returncode})\n"
            f"stdout: {proc.stdout[-500:]}\nstderr: {proc.stderr[-500:]}"
        )
    data = json.loads(lines[-1])
    if "exception" in data:
        raise SysMLToolError(f"toolchain exception: {data['exception'][:500]}")

    return ValidationResult(
        valid=data["valid"],
        syntax_errors=_issues(data.get("syntax_errors", [])),
        semantic_errors=_issues(data.get("semantic_errors", [])),
        warnings=_issues(data.get("warnings", [])),
        png=data.get("png"),
        puml=data.get("puml"),
        render_error=data.get("render_error"),
    )


def is_available() -> bool:
    """True if the toolchain can actually run. Cheap enough for a health check."""
    if not (DEFAULT_JAR.exists() and DEFAULT_LIBRARY.exists()):
        return False
    try:
        subprocess.run(["java", "-version"], capture_output=True, timeout=30)
        return True
    except (OSError, subprocess.TimeoutExpired):
        return False
