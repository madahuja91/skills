---
skill_revision: 2026-08-12-v21
name: epic-generation-v21
description: >-
  Generate high-level business Epics from functional current-state evidence and target transformation intent.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Epic Generation

Version `2.1.0`.

## Purpose

Generate high-level business Epics from functional current-state evidence and target transformation intent.

## Responsibility

```yaml
owns:
- business capability framing
- business outcome framing
- Epic boundary
does_not_own:
- Feature decomposition
- FAC
- AAC
- technical Stories
- LLD
```

## Inputs

```yaml
required:
- requirement
- codebase
- csa_output
- architecture_blueprint
- migration_strategy
optional:
- epic_names
```

## Epic names (`epic_names`)

```yaml
when_empty: LLM derives Epic titles from evidence using business capability/outcome naming.
when_provided: Use user Epic names verbatim as epic title; do not rename, rephrase, abbreviate, or normalize casing; one Epic per name; still assign EPIC-### IDs.
```

## Source usage

```yaml
codebase:
  purpose: Validate actual legacy/current capability where necessary.
csa_output:
  purpose: Primary source for functional current-state understanding.
architecture_blueprint:
  purpose: Understand target capability direction and architectural boundaries without
    introducing implementation detail.
migration_strategy:
  purpose: Understand transformation scope and sequencing constraints.
```

## Analysis

```yaml
mandatory_areas:
- business capability
- business outcome
- functional scope
- actors/personas where supported
- capability boundaries
- current-to-target transformation intent
rules:
- Consolidate related functionality into a meaningful business capability.
- Keep Epic broad enough to contain multiple Features.
- Use business terminology from the source material.
- Describe outcome rather than implementation.
```

## Naming

```yaml
pattern: <Business Capability>
examples:
- Data Management and Submission
- Customer Order Management
- Product Catalog Management
```

## Output

```yaml
schema: epic
required_fields:
- id
- title
- description
- business_capability
- business_outcome
- scope
- traceability
```

## Constraints

```yaml
must:
- remain high level
- represent a business capability and outcome
- be understandable without technical knowledge
must_not:
- mention API endpoints
- mention database tables
- mention classes/services
- mention Kafka/topics
- mention UI components
- describe implementation steps
- split Epic by UI/backend
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
