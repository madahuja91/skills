---
skill_revision: 2026-08-12-v22
name: architecture-analysis-v22
description: >-
  Extract target architecture, boundaries, contracts and constraints from architecture_blueprint, and migration sequencing/coexistence/compatibility/cutover/rollback from migration_strategy.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Architecture Analysis

Version `2.0.0`.

## Purpose

Extract target architecture, boundaries, contracts and constraints from architecture_blueprint, and migration sequencing/coexistence/compatibility/cutover/rollback from migration_strategy.

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

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
