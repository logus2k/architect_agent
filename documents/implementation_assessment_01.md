# Architecture Assessment: Architect Agent

## 1. Architecture Overview

The **Architect Agent** is a pipeline that transforms INCOSE-validated requirements into an MBSE (Model-Based Systems Engineering) architecture package. It produces SysML v2 models, rendered diagrams, and Markdown artifacts. 

**Key Architectural Characteristics:**
* **Stateless House Pattern:** The LLM client (`client.py`) operates statelessly (`memory_policy: "none"`) with a batch size of 1. This prevents the LLM from conflating requirements, maximizing consistency.
* **Symbol Registry (`symbols.py`):** Because stateless LLMs won't naturally agree on names across different generations (e.g., `interfaces.md` vs `allocations.md`), the pipeline uses a central, deterministic Python registry. LLMs propose an *intent* ("GPU cluster"), and the registry mints an authoritative identifier (`GPUCluster`). Future prompts are fed these identifiers and told to use them verbatim.
* **Deterministic Assembly (`emit.py`):** The final generation of the SysML document and Markdown artifacts relies entirely on Python logic and the registry, ensuring that the final files are strictly consistent with the agreed-upon architecture.
* **Headless Validation (`sysml.py` & `ArchitectTool.java`):** SysML validation is a hard gate. The pipeline shells out to a headless Java process wrapping the OMG Pilot Implementation. This guarantees that no invalid model is ever published.

---

## 2. Suggested Performance Improvements

### Single JVM Invocation for Validation & Rendering
In `pipeline.py`, the `sysml.validate()` function is invoked twice:
1. First to validate the generated `model` text (blocking gate).
2. Second to render the PlantUML/PNG diagrams if validation succeeded.

Each JVM invocation loads the OMG SysML standard library (94 resources), taking ~1.7 seconds per run. 
**Improvement:** `ArchitectTool.java` already contains logic to only render the PNG if the model is valid (`if (outPng != null && !result.hasErrors())`). We can pass the `render_png` path to the *first* `sysml.validate()` call in `pipeline.py`. This halves the JVM overhead (saving ~1.7 seconds per generation run) without risking an attempt to render an invalid model.

### Artifact Cleanup for Temporary Files
Currently, `sysml.py` writes the temporary SysML file to `/tmp` and cleans it up. However, `ArchitectTool.java` writes an intermediate `.puml` file right next to the requested `outPng`. While keeping the PlantUML file in the final output directory is useful, if `render_png` happens to be placed in a temporary or transient location, the `.puml` file won't be explicitly tracked or deleted by `sysml.py`'s cleanup trap.

---

## 3. Suggested Accuracy Improvements

### Robust SysML Keyword Stripping in Resolution (`generate.py`)
In `generate.py`, the `_resolve` function strips LLM-hallucinated prefixes from proposed identifiers so they can match the Symbol Registry. Currently, the regex looks like this:
```python
_KIND_PREFIX = re.compile(r"^\s*(part|action|port|interface|state|constraint|attribute)(\s+def)?\s+", re.I)
```
**Improvement:** While this successfully strips "part def", it does not strip "part usage" or "action usage", which LLMs frequently hallucinate when returning usages (features) rather than definitions. Expanding the regex to `(\s+(def|usage))?` will catch these variants and significantly improve the resolution rate, reducing the number of "unresolved" warnings in the final package.

### Strict `require_ready` Enforcement Flag
In `pipeline.py`, `require_ready` defaults to `False`. The codebase mentions this is because upstream analysts don't yet produce the `architect_ready` flag reliably. 
**Improvement:** As upstream dependencies mature, enforcing this flag will improve architecture quality by preventing the pipeline from processing unfinished or unreviewed requirements, which inherently leads to lower-accuracy SysML models.
