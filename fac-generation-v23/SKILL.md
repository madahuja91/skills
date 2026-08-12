---
name: fac-generation-v23
description: >-
  Generate Feature-level business and functional acceptance criteria.
---

# Feature Functional Acceptance Criteria

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: fac-generation
  name: Feature Functional Acceptance Criteria
  version: 2.0.0
  purpose: Generate Feature-level business and functional acceptance criteria.
  responsibility:
    owns:
    - functional acceptance
    - business scenario coverage
    - Feature-level Given/When/Then criteria
    does_not_own:
    - technical Story acceptance
    - LLD verification
  inputs:
    required:
    - feature
    - csa_output
    - architecture_blueprint
    - migration_strategy
  coverage:
  - happy path
  - mandatory business rules
  - validation
  - negative scenarios
  - boundary conditions
  - functional error behavior
  - downstream functional outcome
  - migration/coexistence behavior where functionally visible
  output:
    schema: fac
    required_fields:
    - id
    - feature_id
    - acceptance_criteria
    - traceability
  rules:
  - Criteria must validate the Feature's functional outcome.
  - Criteria must not specify implementation classes or infrastructure.
  - Criteria must be understandable by business and QA stakeholders.
  - Do not duplicate Story-level technical acceptance.
  format:
  - Given
  - When
  - Then
```
