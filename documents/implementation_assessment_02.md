# Architecture Assessment: Architect Agent (Update 02)

> **Disposition (2026-07-20, verified by running the code):**
> - **§1 confirmations accepted** — both prior fixes are correctly reported as
>   implemented. Re-verified: 8/8 SysML tests pass, `_KIND_PREFIX` matches
>   `(def|usage)`, pipeline makes one `validate(render_png=...)` call.
> - **§2 `.puml` cleanup — addressed as a contract, not a delete.** Verified that
>   `validate(render_png=...)` already **returns both paths** (`result.png`,
>   `result.puml`), so no artifact is ever untracked — the caller always has the
>   handle. The gap was that this ownership was undocumented. Now stated explicitly
>   in the `validate()` docstring, with a test (`test_render_reports_both_artifact_paths`).
>   The `.puml` is deliberately kept beside the PNG (re-render / hand-edit), so
>   deleting it — as the item suggested — would remove useful output. The pipeline
>   itself never renders to a transient path; it always writes into `diagrams/`.
> - **§2 strict `require_ready` — deferred, unchanged.** Still correct to leave
>   False: verified against the live Analyst (`:7803`), every package reports
>   `architect_ready: false` because the upstream release gate is not built.
>   Enforcing now blocks every run. Flips with no code change when the gate lands.


## 1. Overview of Implemented Fixes

Following the previous assessment, I reviewed the codebase to verify the implementation of the suggested performance and accuracy improvements.

### 🟢 Single JVM Invocation for Validation & Rendering (IMPLEMENTED)
- **Status:** Completed in `pipeline.py`.
- **Details:** The pipeline now groups the validation (Step 5) and rendering (Step 6) into a single call: `result = sysml.validate(model, render_png=png_path)`. Since `ArchitectTool.java` natively ensures it only renders if the model validates successfully, this change safely saves ~1.7 seconds of JVM overhead by avoiding a redundant loading of the 94 standard library resources.

### 🟢 Robust SysML Keyword Stripping (IMPLEMENTED)
- **Status:** Completed in `generate.py`.
- **Details:** The `_KIND_PREFIX` regex was successfully updated to `r"^\s*(part|action|port|interface|state|constraint|attribute)(\s+(def|usage))?\s+"`. This effectively mitigates accuracy loss when the model hallucinates `part usage` or `action usage` prefixes, allowing those elements to correctly map to the Symbol Registry.

---

## 2. Outstanding Improvements (Not Yet Implemented)

### 🔴 Artifact Cleanup for Temporary Files
- **Status:** Not implemented.
- **Details:** `sysml.py` still only cleans up the `tmp.sysml` file. `ArchitectTool.java` outputs an intermediate `.puml` file directly alongside the `outPng` path. If these diagrams are generated in transient or `/tmp` directories before being moved, the `.puml` files will be left behind as dangling artifacts. We should add cleanup logic for the PlantUML artifacts.

### 🔴 Strict `require_ready` Enforcement Flag
- **Status:** Not implemented.
- **Details:** The `require_ready` flag in `pipeline.py`'s `run()` function still defaults to `False`. Once the upstream Analyst Agent reliably produces the `architect_ready` flag, this should be flipped to `True` (or actively enforced in the entrypoint) to prevent processing of unreviewed or incomplete requirements, which inherently degrades the generated SysML architecture quality.
