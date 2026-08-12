---
skill_revision: 2026-08-12-v22
name: backlog-quality-v22
description: >-
  Validate the backlog for architectural correctness and LLD readiness.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Backlog Quality

Version `2.0.0`.

## Purpose

Validate the backlog for architectural correctness and LLD readiness.

## Gates

```yaml
epic:
- business capability/outcome only
- no implementation detail
feature:
- functional boundary
- implementation-neutral
fac:
- Feature-level
- business/functional and testable
aac:
- Feature-level
- architecture/design and traceable to architecture_blueprint or migration_strategy
story:
- completely technical
- LLD-level
- implementation-ready
- correct Story area
- all applicable LLD sections covered
sac:
- Story-level
- technically verifiable
```

## Exact Story Area Enum

```yaml
- UI
- BFF/API
- Domain
- Persistence
- Messaging
- Testing
```

## Blocking Conditions

```yaml
- Story is generic rather than technical.
- Story lacks target components or interfaces where applicable.
- Story lacks data flow where applicable.
- Story lacks migration consideration where applicable.
- Story has unresolved architecture assumptions.
- Story uses an invalid area name.
- SAC only repeats FAC.
- Story conflicts with sibling Story contracts.
- A skipped area still has a Story.
- A selected area has no Story.
```

## Canonical Output

src/artifacts/canonical/validation.json

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
