---
name: fac-generation
description: >-
  Generate Feature-level business and functional acceptance criteria.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Feature Functional Acceptance Criteria

Version `2.0.0`.

## Purpose

Generate Feature-level business and functional acceptance criteria.

## Responsibility

```yaml
owns:
- functional acceptance
- business scenario coverage
- Feature-level Given/When/Then criteria
does_not_own:
- technical Story acceptance
- LLD verification
```

## Inputs

```yaml
required:
- feature
- csa_output
- architecture_blueprint
- migration_strategy
```

## Coverage

- happy path
- mandatory business rules
- validation
- negative scenarios
- boundary conditions
- functional error behavior
- downstream functional outcome
- migration/coexistence behavior where functionally visible

## Format

- Given
- When
- Then

## Output

```yaml
schema: fac
required_fields:
- id
- feature_id
- acceptance_criteria
- traceability
```

## Rules

- Criteria must validate the Feature's functional outcome.
- Criteria must not specify implementation classes or infrastructure.
- Criteria must be understandable by business and QA stakeholders.
- Do not duplicate Story-level technical acceptance.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
