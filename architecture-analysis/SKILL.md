---
name: architecture-analysis
description: >-
  Extract target architecture, boundaries, contracts and constraints from architecture_blueprint, and migration sequencing, coexistence, compatibility, cutover and rollback from migration_strategy.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Architecture Analysis

Version `2.0.0`.

## Purpose

Extract target architecture, boundaries, contracts and constraints from architecture_blueprint, and migration sequencing, coexistence, compatibility, cutover and rollback from migration_strategy.

## Workflow binding

- Blueprint Agent
- Migration Agent
- Architecture Orchestrator

## Responsibility

```yaml
owns:
- target architecture extraction
- component/API/domain/persistence/messaging boundaries
- migration constraint extraction
does_not_own:
- current-state invention
- Epic/Feature business scope
- technical Story LLD
```

## Inputs

```yaml
required:
- architecture_blueprint
- migration_strategy
optional:
- current_state_evidence
```

## Source usage

```yaml
architecture_blueprint:
  authoritative: true
  areas:
  - target architecture
  - component boundaries
  - API contracts
  - domain boundaries
  - persistence ownership
  - messaging decisions
  - integration patterns
  - security architecture
  - non-functional architectural constraints
migration_strategy:
  authoritative: true
  areas:
  - coexistence
  - sequencing
  - compatibility
  - migration boundaries
  - cutover
  - rollback considerations
```

## Analysis

```yaml
rules:
- Use architecture_blueprint as the single architecture/design input. Do not create
  a separate ADR source.
- Do not invent contracts or boundaries unsupported by architecture_blueprint.
- Do not invent cutover/rollback unsupported by migration_strategy.
- Keep extraction at architecture/design level; do not write technical Stories.
```

## Output

```yaml
schema: architecture-context
required_fields:
- id
- boundaries
- contracts
- constraints
- sequencing
- coexistence
- compatibility
- cutover
- rollback
- traceability
```

## Constraints

```yaml
must:
- trace every constraint to architecture_blueprint or migration_strategy
- preserve target vs current-state separation
must_not:
- invent architecture decisions
- generate backlog items
- collapse Feature business scope into technical components
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
