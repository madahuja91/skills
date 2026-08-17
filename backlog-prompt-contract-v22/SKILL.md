---
name: backlog-prompt-contract-v22
description: >-
  Shared backlog contract plus cwd-aware write paths so agents never create src/src.
---

# Backlog Prompt Contract

Load this skill. Do not copy it into prompts.

## Write paths (do this first)

Logical docs use `src/artifacts/...`. The runner cwd is often already `src`.

1. If cwd is `src` (or cwd already has `artifacts/`): **strip leading `src/`**. Write `artifacts/...` and `_internal/...`. **Never** `mkdir src`. **Never** `src/src`.
2. If cwd is workspace root and `src/` exists: write into that existing `src/artifacts/...`. Do not create another `src`.
3. `write_file("src/artifacts/...")` while cwd is `src` is forbidden — that creates `src/src/artifacts`.

Example: cwd=`.../src` + logical `src/artifacts/packages/x.json` → write `artifacts/packages/x.json`.

## Output tree (after resolve)
- JSON: `artifacts/canonical/backlog/` (Requirement → Epic → Feature → FAC/AAC → Technical-Stories/ST-### → SAC)
- Markdown: `artifacts/projections/backlog/` (Markdown Renderer only; no JSON dump)
- Jira: `artifacts/projections/jira-import.json`
- Packages: `artifacts/packages/`
- Shared memory: `_internal/swarm/shared_memory.json`

## Schema
All `required_fields` present and non-empty.

## Names, not bare IDs
`Order Capture (FEAT-001)` — never `FEAT-001` alone.

## Inline details
Full BR/ADR/migration text. Never "see BR/ADR/migration_strategy".

## epic_names
Empty → LLM titles. Provided → verbatim Epic titles.

## feature_selection
Empty → LLM Feature count. `epic-N-feature-M` → Epic N gets M Features.

## story_layer_selection
Empty → LLM layers. `epic-N-feature-M-story-ui, bff/api` → only those layers.

## Retry
Rerun only the named incomplete agent.
