---
name: current-state-analysis-v23
description: >-
  Extract evidence-backed current-state capabilities, actors, flows, rules, exceptions and codebase behavior. Do not invent target architecture or migration decisions.
---

# Current-State Analysis

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: current-state-analysis
  name: Current-State Analysis
  version: 2.0.0
  purpose: Extract evidence-backed current-state capabilities, actors, flows, rules, exceptions and codebase behavior. Do not invent target architecture or migration decisions.
  responsibility:
    owns:
    - legacy/current behavior evidence
    - CSA capability, actor, flow and exception extraction
    - normalized current-state evidence pack
    does_not_own:
    - target architecture
    - migration sequencing
    - Epic/Feature generation
    - technical Stories
  inputs:
    required:
    - codebase
    - csa_output
    optional:
    - requirement
  analysis:
    mandatory_areas:
    - capabilities
    - actors/personas
    - business/functional flows
    - business rules
    - validations
    - exceptions/error behavior
    - evidence citations
    rules:
    - Separate observed current-state from any target-state language.
    - Every extracted rule or flow must cite CSA and/or codebase evidence.
    - Do not invent target components, APIs, topics, tables or migration cutover.
  output:
    schema: current-state-evidence
    required_fields:
    - id
    - capabilities
    - actors
    - flows
    - rules
    - exceptions
    - evidence
    - traceability
```
