---
skill_revision: 2026-08-12-v22
name: jira-projection-v22
description: >-
  Project the validated technical backlog into Jira-import-oriented JSON.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Jira Projection

Version `2.0.0`.

## Purpose

Project the validated technical backlog into Jira-import-oriented JSON.

## Rules

```yaml
- Canonical backlog remains the source of truth.
- Preserve REQ/EPIC/FEAT/ST IDs as external IDs.
- Preserve parent relationships.
- Preserve FAC/AAC/SAC content in the configured Jira description/acceptance representation.
- Do not flatten technical Story LLD information.
- Do not generate or modify canonical content.
- Run only after Governance PASS. Otherwise status=skipped.
- Write src/artifacts/projections/jira-import.json.
- Until PASS, keep placeholder {"schema_version":"2.0.0","status":"pending","items":[]}.
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
