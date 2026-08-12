---
name: traceability
description: >-
  Maintain stable IDs and complete lineage from source requirement through technical implementation.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# End-to-End Traceability

Version `2.0.0`.

## Purpose

Maintain stable IDs and complete lineage from source requirement through technical implementation.

## ID prefixes

- REQ
- EPIC
- FEAT
- FAC
- AAC
- ST
- SAC

## Hierarchy

- Requirement -> Epic
- Epic -> Feature
- Feature -> FAC
- Feature -> AAC
- Feature -> Story
- Story -> SAC

## Source lineage

- codebase
- csa_output
- architecture_blueprint
- migration_strategy

## Story lineage

```yaml
every_story_must_reference:
- feature_id
- fac_ids
- aac_ids
- architecture_blueprint references
- migration_strategy references
- current_state evidence
- sibling dependencies where applicable
```

## Rules

- IDs remain stable across reruns when artifact identity is unchanged.
- IDs must never be reused for a different artifact.
- No orphan Stories.
- No duplicate IDs.
- Every SAC resolves to a Story.

## Canonical output

`src/artifacts/canonical/traceability.json`

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
