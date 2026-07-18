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

```

---

# 📄 **implementation.md**  
*(Raw Markdown — copy/paste directly)*

```markdown
# Architect Agent — Implementation Specification

## 1. Overview
This document defines the implementation details required for an LLM‑powered Architect Agent capable of producing SysML v2 models, diagram hints, and MBSE artifacts from INCOSE‑validated requirements.

## 2. System Components

### 2.1 Requirement Interpreter Module
**Purpose:** Convert INCOSE requirements into structured objects.

**Input:** Analyst Agent output  
**Output:** Internal requirement objects

**Data Structure:**
```json
{
  "id": "REQ-001",
  "text": "The system shall allocate GPUs fairly.",
  "type": "functional",
  "constraints": ["fairness", "resource"]
}
```

### 2.2 Functional Decomposition Engine
**Purpose:** Break system into hierarchical functions.

**Output Format (Markdown):**
```markdown
- Allocate GPU
  - Validate quota
  - Select GPU
  - Bind session
```

**SysML v2:**
```sysml
action AllocateGPU { }
```

### 2.3 Logical Architecture Generator
**Purpose:** Define components and boundaries.

**SysML v2 Example:**
```sysml
package Architecture {
    part GPUCluster { attribute totalGPUs: Integer; }
    part NotebookSession { attribute userId: String; }
}
```

### 2.4 Interface Modeling Engine
**Purpose:** Define ports, flows, contracts.

**SysML v2 Example:**
```sysml
interface GPUAllocationIF { attribute quota: Integer; }
```

### 2.5 Behavior Modeling Engine
**Purpose:** Generate activities, state machines, interactions.

**SysML v2 Example:**
```sysml
stateMachine SessionLifecycle {
    state Initial;
    state Allocated;
    transition Initial -> Allocated;
}
```

### 2.6 Constraint Modeling Engine
**Purpose:** Define parametric constraints.

**SysML v2 Example:**
```sysml
constraint GPUFairness { equation fairShare = totalGPUs / users; }
```

### 2.7 Allocation Engine
**Purpose:** Map functions to components.

**SysML v2 Example:**
```sysml
allocate AllocateGPU to GPUCluster;
```

### 2.8 SysML v2 Text Generator
**Purpose:** Assemble all model fragments into a valid `.sysml` file.

**Output:** `model.sysml`

### 2.9 Diagram Hint Generator
**Purpose:** Produce JSON layout hints for SysON.

**Output:** `logical_architecture.json`

### 2.10 Artifact Packager
**Purpose:** Bundle all outputs for Planner Agent.

**Output Structure:**
```
/architecture/
  model.sysml
  logical_architecture.json
  functional_decomposition.md
  logical_architecture.md
  interfaces.md
  behavior.md
  constraints.md
  allocations.md
  verification_plan.md
  ADD.md
```

## 3. Processing Pipeline

### Step 1 — Load Requirements
Parse Analyst Agent output.

### Step 2 — Build Requirement Objects
Normalize into internal structures.

### Step 3 — Generate MBSE Artifacts
Functional → Logical → Interfaces → Behavior → Constraints → Allocation → Verification.

### Step 4 — Generate SysML v2 Model
Combine all fragments.

### Step 5 — Generate Diagram Hints
Produce JSON for SysON.

### Step 6 — Package Artifacts
Prepare directory for Planner Agent.

## 4. Error Handling
- Missing requirement → skip and log
- Invalid SysML v2 syntax → regenerate fragment
- Missing diagram hint → fallback to auto‑layout

## 5. Performance Requirements
- Must process 200+ requirements
- Must generate complete SysML v2 model under 5 seconds
- Must produce deterministic output given identical input

## 6. Security Requirements
- No external network calls
- All processing on‑prem
- All artifacts stored locally

## 7. Integration Requirements
### 7.1 SysON
- `.sysml` and `.json` files placed in SysON workspace directory

### 7.2 Planner Agent
- Receives full architecture package

## 8. Example Output Structure
```
architecture/
  model.sysml
  diagrams/
    logical_architecture.json
    behavior.json
  artifacts/
    functional_decomposition.md
    logical_architecture.md
    interfaces.md
    behavior.md
    constraints.md
    allocations.md
    verification_plan.md
    ADD.md
```

## 9. Completion Criteria
The Architect Agent is considered complete when:
- All MBSE artifacts are generated
- SysML v2 model validates in SysON
- Diagram hints render correctly
- Planner Agent can generate executable specifications from the output
