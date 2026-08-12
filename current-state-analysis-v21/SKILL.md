---
skill_revision: 2026-08-12-v21
name: current-state-analysis-v21
description: >-
  Extract evidence-backed current-state capabilities, actors, flows, rules, exceptions and codebase behavior. Do not invent target architecture or migration decisions.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Current-State Analysis

Version `2.1.0`.

## Purpose

Extract evidence-backed current-state capabilities, actors, flows, rules, exceptions and codebase behavior. Do not invent target architecture or migration decisions.

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

## Analysis

```yaml
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

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
