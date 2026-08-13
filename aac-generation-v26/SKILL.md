---
name: aac-generation-v26
description: >-
  Generate Feature-level architecture/design acceptance criteria that constrain downstream technical Stories.
---

# Feature Architecture Acceptance Criteria

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: aac-generation
  name: Feature Architecture Acceptance Criteria
  version: 2.0.0
  purpose: Generate Feature-level architecture/design acceptance criteria that constrain downstream technical Stories.
  responsibility:
    owns:
    - architecture-level acceptance
    - target design constraints
    - migration architecture constraints
    does_not_own:
    - technical implementation details
    - Story SAC
  inputs:
    required:
    - feature
    - architecture_blueprint
    - migration_strategy
  source_usage:
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
  output:
    schema: aac
    required_fields:
    - id
    - feature_id
    - architecture_constraints
    - migration_constraints
    - acceptance_criteria
    - traceability
  rules:
  - AAC remains at Feature level.
  - AAC describes architectural/design conditions that Stories must satisfy.
  - Do not prescribe arbitrary implementation details unsupported by architecture_blueprint.
  - Every AAC must trace to architecture_blueprint or migration_strategy.
  - JSON agents write schema-complete JSON under src/artifacts/canonical/backlog/ only. Markdown Renderer (Claude Sonnet 4.5) writes matching .md twins under src/artifacts/projections/backlog/. Do not dual-write Markdown from JSON agents.
  - JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
  - All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
  - Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.
```
