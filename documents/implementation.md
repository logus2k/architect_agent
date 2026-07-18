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
