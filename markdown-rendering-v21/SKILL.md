---
skill_revision: 2026-08-12-v21
name: markdown-rendering-v21
description: >-
  Render human-readable Markdown from the validated technical backlog JSON folder tree.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Markdown Rendering

Version `2.1.0`.

## Purpose

Render human-readable Markdown from the validated technical backlog JSON folder tree.
`projections/backlog/` mirrors `canonical/backlog/` 1:1 (same folders and IDs; `.md` instead of `.json`).

## Output tree

```text
src/artifacts/projections/backlog/
├── README.md
├── Requirement/REQ-###/REQ-###.md
├── Epic/EPIC-###/EPIC-###.md
│   └── Feature/FEAT-###/FEAT-###.md
│       ├── FAC/FAC-###.md
│       ├── AAC/AAC-###.md
│       └── Technical-Stories/ST-###/ST-###.md
│           └── SAC/SAC-###.md
├── Traceability/traceability.md
└── Validation/validation.md
```

## Rules

- JSON under `src/artifacts/canonical/backlog/` is authoritative.
- Mirror every JSON file as an MD file at the same relative path.
- Preserve Epic -> Feature -> Story hierarchy as folders.
- Display FAC/AAC at Feature level.
- Display full technical LLD sections at Story level.
- Display SAC at Story level.
- Preserve exact Story area names.
- Do not add content not present in JSON.
- Run only after Governance PASS. Otherwise status=skipped and leave existing MD untouched.
- NEVER delete Markdown under `projections/backlog/`.
- Write `src/artifacts/projections/backlog/` (folder tree), not a single `backlog.md`.
- After PASS, JSON and MD trees must be informationally identical.
- Mirror Area-folder Story paths: `Technical-Stories/<Area>/...`.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.

## Schema field rendering

For each artifact type, Markdown MUST include every skill-schema required field
(Epic, Feature, FAC, AAC, Technical Story, SAC). Do not summarize away required LLD sections.
Every Feature Markdown tree must include all six Story areas.


`src/artifacts/canonical/backlog/` (JSON) and `src/artifacts/projections/backlog/` (Markdown)
MUST convey the **same information**.

Rules:
- Same folder tree and same IDs (REQ/EPIC/FEAT/FAC/AAC/ST/SAC).
- Every JSON file has a matching `.md` at the same relative path (and vice versa after PASS).
- Every field present in a JSON artifact must appear in its Markdown twin (no silent drops).
- Markdown must not invent content absent from JSON.
- `index.json` ↔ `README.md` must list the same IDs/paths.
- Traceability and Validation have both JSON and MD twins.
