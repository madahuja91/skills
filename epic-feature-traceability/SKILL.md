---
name: epic-feature-traceability
description: >-
  Maintain traceability from source requirements/current-state evidence to Epic and Feature artifacts.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Epic Feature Traceability

Version `2.0.0`.

## Purpose

Maintain traceability from source requirements/current-state evidence to Epic and Feature artifacts.

## ID prefixes

- REQ
- EPIC
- FEAT
- FAC
- AAC

## Source lineage

- requirement
- codebase
- csa_output
- architecture_blueprint
- migration_strategy

## Rules

- Every Epic must trace to one or more requirements/source capabilities.
- Every Feature must trace to its Epic.
- Every Feature must trace to current-state evidence.
- Target-state intent must trace to architecture_blueprint where applicable.
- Migration intent must trace to migration_strategy where applicable.
- FAC and AAC must trace to their Feature.
- IDs must be stable and unique.
- No orphan artifacts.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
