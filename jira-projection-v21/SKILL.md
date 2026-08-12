---
skill_revision: 2026-08-12-v21
name: jira-projection-v21
description: >-
  Project the validated technical backlog into Jira-import-oriented JSON.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Jira Projection

Version `2.1.0`.

## Purpose

Project the validated technical backlog into Jira-import-oriented JSON.

## Rules

- Canonical backlog folder tree (`src/artifacts/canonical/backlog/`) remains the source of truth.
- Preserve REQ/EPIC/FEAT/ST IDs as external IDs.
- Preserve parent relationships.
- Preserve FAC/AAC/SAC content in the configured Jira description/acceptance representation.
- Do not flatten technical Story LLD information.
- Do not generate or modify canonical content.
- Run only after Governance PASS. Otherwise status=skipped.
- Read from `src/artifacts/canonical/backlog/` folder tree.
- Write src/artifacts/projections/jira-import.json.
- Until PASS, keep placeholder {"schema_version":"2.0.0","status":"pending","items":[]}.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.

## JSON / Markdown parity (mandatory)

`src/artifacts/canonical/backlog/` (JSON) and `src/artifacts/projections/backlog/` (Markdown)
MUST convey the **same information**.

Rules:
- Same folder tree and same IDs (REQ/EPIC/FEAT/FAC/AAC/ST/SAC).
- Every JSON file has a matching `.md` at the same relative path (and vice versa after PASS).
- Every field present in a JSON artifact must appear in its Markdown twin (no silent drops).
- Markdown must not invent content absent from JSON.
- `index.json` ↔ `README.md` must list the same IDs/paths.
- Traceability and Validation have both JSON and MD twins.
