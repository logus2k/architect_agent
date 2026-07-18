# Architect Agent Technical Architecture

## 1. Purpose
The Architect Agent transforms INCOSE‑compliant requirements (provided by the Analyst Agent) into a complete Model‑Based Systems Engineering (MBSE) architecture package using SysML v2. It produces both textual SysML v2 models and diagram‑layout hints compatible with SysON. Its output is consumed by the Planner Agent to generate executable specifications.

## 2. Inputs
- INCOSE‑validated requirements document (structured JSON or Markdown)
- Domain constraints (optional)
- System context (optional)

## 3. Outputs
- SysML v2 textual model (`.sysml`)
- SysML v2 diagram hints (`.json`)
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
9. Generate diagram‑layout hints for SysON.
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
- **Diagram Hint Generator**
- **Artifact Packager**

### 5.2 Data Flow
1. Analyst Agent → INCOSE requirements → Architect Agent
2. Architect Agent → SysML v2 model + MBSE artifacts → Planner Agent

## 6. SysML v2 Modeling Requirements
### 6.1 Structural Modeling
- Use `package`, `part`, `attribute`, `port`, `interface`, `connection`.
- Define system hierarchy and component boundaries.

### 6.2 Behavioral Modeling
- Use `action`, `activity`, `state`, `transition`, `interaction`.
- Model workflows, lifecycle, and operational behavior.

### 6.3 Constraint Modeling
- Use `constraint`, `parametric`, `equation`.
- Capture performance, resource, safety constraints.

### 6.4 Allocation Modeling
- Use `allocate` relationships.
- Map functions → components → resources.

### 6.5 Requirements Modeling
- Use `requirement`, `deriveReqt`, `satisfy`, `verify`.

## 7. Diagram Hint Specification
Diagram hints are JSON structures consumed by SysON to pre‑arrange diagram layouts.

### 7.1 Example
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
- Represented in SysML v2 + diagram hints.

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

## 9. Integration with SysON
- SysML v2 text saved as `.sysml`
- Diagram hints saved as `.json`
- SysON loads both for visualization and validation

## 10. Integration with Planner Agent
Planner Agent receives:
- SysML v2 model
- Diagram hints
- MBSE artifacts
- Architecture Definition Document

Planner Agent uses these to generate executable specifications.
