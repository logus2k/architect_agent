The current architecture of your `architect-agent` has a solid foundation. You have effectively isolated the deterministic constraints (via the `reconcile_ownership` and `reconcile_interfaces` loops) from the probabilistic output of the LLM personas. Bounding the design loop to a specific branch via the `tree.nodes[].branch` is exactly the right strategy to keep the Gemma 4 E4B IT context window focused.

However, the current pipeline suffers from structural blind spots that cripple its ability to pass a complete, actionable design to `opencode`. Below is a technical advisory report detailing these gaps and how to restructure the implementation to guarantee strict INCOSE requirement traceability and predictable builder outcomes.

### 1. Remediating the Completeness Failure (The 2/60 Gap)

**The Problem:** The most critical failure in the current implementation is that unmodeled requirements are silently dropped from the design. Your `refine.refine()` loop validates *internal consistency*—ensuring no ownership violations, no empty entities, and no dangling types—but it completely lacks a *requirements-to-design* completeness gate. As you observed, only ~2 out of 60 requirements successfully matched the elements in the `code_contract`.

**The Fix:**
You must introduce a hard coverage gate within the `_run_critique()` cycle.

* Before returning `crit.clean`, the critique engine must iterate through every `req_id` assigned to the current aspect branch.


* If a `req_id` cannot be traced to at least one component, function, or interface in the `AspectDesign`, the engine must generate an error-level finding (e.g., `unmodeled_requirement`).


* This forces the `architect_aspect_designer` persona to ingest the unmodeled requirements as an explicit prompt constraint in the next iteration, ensuring that every INCOSE requirement survives the transition from Analyst to Planner.



### 2. Expanding the Design Model's Expressiveness

**The Problem:** The current `AspectDesign` model only recognizes two first-class element kinds: components (entities) and interfaces (service operations). It completely lacks representations for UI, external integrations, routing, and non-functional constraints. Because the Builder (`opencode`) is not provided with endpoints, CRUD definitions, or frontend schemas, it attempts to hallucinate the delivery layer itself, resulting in the persistent `missing_module` residual.

**The Fix:**
Expand the `code_contract` schema to encompass the full stack architecture.

* **Introduce New Kinds:** Add `frontend_component`, `router_endpoint`, and `background_worker` to the allowed `kind` mappings within the contract.


* **Model Constraints:** The Analyst agent emits specific `constraints` for each requirement. You must create a binding array in the `code_contract` (e.g., `applied_constraints: []`) so non-functional requirements (like latency thresholds or specific i18n language toggles) are passed verbatim to `opencode`.



### 3. Fixing the `opencode` Typing and Glossary Mismatch

**The Problem:** The pipeline currently emits C#/Java-style generic syntax (e.g., `List<Category>`) instead of Python-native types. Furthermore, the `architect_aspect_designer` persona hallucinated a `kind` attribute for the glossary terms because the Analyst's `glossary` array does not include one.

**The Fix:**

* **Strict Type Normalization:** Before compiling the final `planner_handover.json`, pass the output through a deterministic normalizer function that converts angled-bracket generics into Python-native types (e.g., `list[Category]` or `Category | None`). `opencode` relies heavily on Language Server Protocol (LSP) diagnostics; feeding it incorrect typing syntax will immediately break its compiler feedback loop.


* **Pre-Process the Glossary:** Since the glossary terms lack a `kind` field (actor/entity/value), inject an isolated LLM pre-processing step at the very beginning of `aspect_pipeline.run()`. This step should strictly categorize every glossary term into a specific `kind` *before* the aspect designer ever sees it, eliminating run-to-run classification drift.



### 4. Hardening the Gates & Stabilizing Proportionality

**The Problem:** Wrapping semantic checks like `design_review` and `stack_policy` in `try/except` blocks makes them purely advisory. If an incomplete or overly engineered design slips through the `MAX_ROUNDS` limit, it still ships downstream. Additionally, relying on Gemma 4 for the `proportionality.run` verdict caused the persistence decision (ORM vs. no ORM) to flip-flop across runs based on mis-scored vocabulary.

**The Fix:**

* **Make Error-Level Findings Fatal:** If error-level findings survive the refinement loop and land in `open_issues`, the run must be flagged as `architect_ready: false`. A design with unresolved structural flaws should never be passed to `opencode`.


* **Lock Down Persistence Logic:** Continue enforcing the recently added code-side guards for the `stack_policy`. Treat the model's extraction of "drivers" purely as a search mechanism. The deterministic Python layer must make the final decision by verifying verbatim quotes against a strict dictionary of driver vocabulary.



### Pipeline Orchestration Note

As you continue to build this out, ensure the legacy SysML code (`pipeline.py`, `sysml.py`, etc.) is fully excised from the repository. It adds unnecessary maintenance overhead.

To maximize the parallel execution capacity of your RTX 4090 during the refine loop, keep the orchestrator lean. Exposing these job-oriented API tasks via `aiohttp` and streaming the critique iterations through `python-socketio` will ensure the architecture remains strictly non-blocking. You can also utilize Data Version Control (DVC) or MLflow to track the permutations of the `planner_handover.json` across different `MAX_ROUNDS` configurations to objectively measure which prompt constraints yield the highest INCOSE coverage trace.
