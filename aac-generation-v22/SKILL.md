---
skill_revision: 2026-08-12-v22
name: aac-generation-v22
description: >-
  Generate Feature-level architecture/design acceptance criteria that constrain downstream technical Stories.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Feature Architecture Acceptance Criteria

Version `2.0.0`.

## Purpose

Generate Feature-level architecture/design acceptance criteria that constrain downstream technical Stories.

## Responsibility

```yaml
owns:
- architecture-level acceptance
- target design constraints
- migration architecture constraints
does_not_own:
- technical implementation details
- Story SAC
```

## Inputs

```yaml
required:
- feature
- architecture_blueprint
- migration_strategy
```

## Source Usage

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

## Output

```yaml
schema: aac
required_fields:
- id
- feature_id
- architecture_constraints
- migration_constraints
- acceptance_criteria
- traceability
```

## Rules

```yaml
- AAC remains at Feature level.
- AAC describes architectural/design conditions that Stories must satisfy.
- Do not prescribe arbitrary implementation details unsupported by architecture_blueprint.
- Every AAC must trace to architecture_blueprint or migration_strategy.
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
