# Architect Agent Technical Architecture

## 1. Purpose
The Architect Agent transforms INCOSE‑compliant requirements (provided by the Analyst Agent) into a complete Model‑Based Systems Engineering (MBSE) architecture package using SysML v2. It produces textual SysML v2 models and rendered diagrams. Its output is consumed by the Planner Agent to generate executable specifications.

## 2. Inputs
The Analyst Agent package, one HTTP call:
`GET http://analyst-agent:7803/projects/{pid}/package`

It carries the requirements, their routing classes, INCOSE quality scores, provenance,
and a readiness manifest. See implementation.md §2.1 for the fields actually consumed
and for three respects in which live packages differ from the Analyst's documented
guarantees.

## 3. Outputs
- SysML v2 textual model (`.sysml`)
- Rendered diagrams (`.png` + `.puml` source)
- MBSE artifacts:
  - Functional decomposition
  - Logical architecture
  - Interface definitions
  - Behavioral models (activities, state machines, interactions)
  - Constraint models (performance, resource, safety)
  - Allocation models (functions → components → resources)
  - Verification plan
  - Architecture Definition Document (ADD)

## 4. Core Responsibilities
1. Interpret INCOSE requirements into SysML v2 requirement objects.
2. Perform functional decomposition.
3. Define logical architecture and structural components.
4. Model interfaces and data flows.
5. Model system behavior using activities, state machines, and interactions.
6. Define constraints and parametric relationships.
7. Allocate functions to components and resources.
8. Generate SysML v2 textual model.
9. Render diagrams from the validated model.
10. Produce MBSE artifacts for Planner Agent consumption.

## 5. Architecture Overview
### 5.1 High-Level Components
- **Requirement Interpreter Module**
- **Functional Decomposition Engine**
- **Logical Architecture Generator**
- **Interface Modeling Engine**
- **Behavior Modeling Engine**
- **Constraint Modeling Engine**
- **Allocation Engine**
- **SysML v2 Text Generator**
- **Diagram Renderer**
- **Artifact Packager**

### 5.2 Data Flow
1. Analyst Agent (`:7803`) → requirements package → Architect Agent
2. Architect Agent → SysML v2 model + diagrams + MBSE artifacts → Planner Agent

Classification is performed upstream by the Analyst using the same six-class
vocabulary the Architect routes on (§8). The Architect classifies only when the
package arrives unclassified.

## 6. SysML v2 Modeling Requirements
### 6.1 Structural Modeling
- Use `package`, `part`, `attribute`, `port`, `interface`, `connection`.
- Define system hierarchy and component boundaries.

### 6.2 Behavioral Modeling
- Use `action`, `activity`, `state`, `transition`, `interaction`.
- Model workflows, lifecycle, and operational behavior.

### 6.3 Constraint Modeling
- Use `constraint def` with a boolean body. There is no `equation` keyword.
- Capture performance, resource, safety constraints.
- **Only where the requirement states a measurable bound.** A requirement scoring
  C7 (Verifiable) below 3 states no number; generating an expression from it invents
  a value the stakeholder never gave. Such requirements are recorded as unquantified.

### 6.4 Allocation Modeling
- Use `allocate` relationships.
- Map functions → components → resources.

### 6.5 Requirements Modeling
- Use `requirement`, `deriveReqt`, `satisfy`, `verify`.

## 7. Diagram Generation

> **Diagram hints were dropped on 2026‑07‑18.** This section originally specified a JSON
> coordinate format to pre‑arrange SysON layouts. It is no longer part of the design.

**Current approach:** diagrams are rendered directly from the validated model by the
SysML v2 Pilot Implementation's bundled PlantUML, using the pure‑Java Smetana layout
engine. No coordinates are supplied and no SysON instance is involved.

*Evidence for the change:* a 16‑entity model rendered to a clean hierarchical layout
(1492×349, no crossing edges) with no positioning input. Supplying coordinates would
have required an online stateful applier — a WebSocket client against SysON's
`diagramEvent` subscription to resolve diagram node IDs, then a `layoutDiagram`
mutation. That machinery bought only cosmetic control and is not built.

**Outputs:** `diagrams/<name>.png` plus the `.puml` source, so a diagram can be
re‑rendered or hand‑adjusted without re‑running the agent.

**Known gap:** PlantUML does not draw multiplicities — `part nodes : GPUNode[1..64]`
appears as `nodes: GPUNode`. The constraint remains in the model and the ADD.

### 7.1 Obsolete — original hint file format (retained for reference)
```json
{
  "diagram": "logical_architecture",
  "nodes": [
    { "id": "GPUCluster", "x": 120, "y": 80 },
    { "id": "NotebookSession", "x": 420, "y": 80 }
  ],
  "edges": [
    { "source": "GPUCluster", "target": "NotebookSession", "type": "flow" }
  ]
}
```

## 8. MBSE Artifact Requirements
### 8.1 Functional Decomposition
- Hierarchical breakdown of system functions.
- Represented in Markdown + SysML v2.

### 8.2 Logical Architecture
- Components, boundaries, responsibilities.
- Represented in SysML v2 + rendered diagrams.

### 8.3 Interfaces
- Ports, flows, contracts.
- Represented in SysML v2.

### 8.4 Behavior Models
- Activities for workflows.
- State machines for lifecycle.
- Interactions for component collaboration.

### 8.5 Constraints
- Performance (latency, throughput)
- Resource (GPU allocation, memory)
- Safety (failure modes)

### 8.6 Allocation Models
- Functions → components
- Components → resources

### 8.7 Verification Plan
- Requirement → verification method mapping.

### 8.8 Architecture Definition Document (ADD)
Human‑readable synthesis of the full architecture package. Unlike the artifacts above,
the ADD is narrative rather than generated model content: it explains and justifies the
architecture for review and sign‑off.

**Required sections:**
1. Introduction — purpose, scope, intended audience.
2. Requirements Summary — source requirements and their origin.
3. Functional Architecture — narrative over the functional decomposition (§8.1).
4. Logical Architecture — components, boundaries, responsibilities (§8.2).
5. Interfaces — external and internal interface summary (§8.3).
6. Behavior — operational scenarios and lifecycle (§8.4).
7. Constraints — performance, resource, and safety constraints (§8.5).
8. Allocation — function → component → resource rationale (§8.6).
9. Verification Approach — summary of the verification plan (§8.7).
10. Traceability — requirement → architecture element coverage.
11. Assumptions and Open Issues — unresolved decisions and known gaps.

**Rules:**
- Derived entirely from the other artifacts; introduces no new model content.
- Every architectural decision states its driving requirement.
- Represented in Markdown.

## 9. Integration with SysON (optional)
- SysML v2 text saved as `.sysml`; SysON can import it for interactive viewing/editing.
- SysON is **not** a runtime dependency: validation and rendering both run from the
  SysML v2 Pilot Implementation jar. See implementation.md §3 Step 6.

## 10. Integration with Planner Agent
Planner Agent receives:
- SysML v2 model
- Rendered diagrams
- MBSE artifacts
- Architecture Definition Document

Planner Agent uses these to generate executable specifications.
