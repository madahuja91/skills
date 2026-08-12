---
name: current-state-analysis
description: >-
  Extract evidence-backed current-state capabilities, actors, flows, rules, exceptions and codebase behavior. Do not invent target architecture or migration decisions.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Current-State Analysis

Version `2.0.0`.

## Purpose

Extract evidence-backed current-state capabilities, actors, flows, rules, exceptions and codebase behavior. Do not invent target architecture or migration decisions.

## Workflow binding

- Codebase Agent
- CSA Agent
- Current-State Orchestrator

## Responsibility

```yaml
owns:
- legacy/current behavior evidence
- CSA capability, actor, flow and exception extraction
- normalized current-state evidence pack
does_not_own:
- target architecture
- migration sequencing
- Epic/Feature generation
- technical Stories
```

## Inputs

```yaml
required:
- codebase
- csa_output
optional:
- requirement
```

## Source usage

```yaml
codebase: Validate actual legacy/current behavior. Cite files, modules, entry points
  and observed rules.
csa_output: Primary source for current capabilities, actors, flows, rules, exceptions
  and evidence.
```

## Analysis

```yaml
mandatory_areas:
- capabilities
- actors/personas
- business/functional flows
- business rules
- validations
- exceptions/error behavior
- inputs and outputs
- current integrations
- evidence citations
rules:
- Separate observed current-state from any target-state language in the sources.
- Every extracted rule or flow must cite CSA and/or codebase evidence.
- Do not invent target components, APIs, topics, tables or migration cutover.
- Normalize overlapping CSA and codebase evidence; do not duplicate conflicting facts
  without noting the conflict.
```

## Output

```yaml
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

## Constraints

```yaml
must:
- remain current-state only
- cite evidence
- preserve functional meaning for downstream Feature generation
must_not:
- invent target architecture
- invent migration decisions
- generate Epics, Features, FAC, AAC or Stories
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
