---
name: backlog-prompt-contract-v21
description: >-
  Shared backlog execution contract. Agents load this skill instead of repeating
  output-tree, schema, naming, selection, and markdown rules in prompts.
---

# Backlog Prompt Contract

Load this skill. Do not copy these rules into systemPrompt or userquery.

## Output tree
- JSON: `src/artifacts/canonical/backlog/` (Requirement → Epic → Feature → FAC/AAC → Technical-Stories/ST-### → SAC)
- Markdown: `src/artifacts/projections/backlog/` (Markdown Renderer only; no JSON dump)
- Jira: `src/artifacts/projections/jira-import.json` after Governance PASS
- Packages: `src/artifacts/packages/`
- Shared memory: `src/_internal/swarm/shared_memory.json`
- Forbidden: `src/canonical/`, flat Feature/FAC/AAC folders, `epic.json`/`feature.json`

## Schema
All skill `required_fields` present and non-empty before status=complete.

## Names, not bare IDs
Write title plus id: `Order Capture (FEAT-001)`. Never `FEAT-001` / `FAC-002` / `AAC-001` / `SAC-003` alone.

## Inline details
Full business-rule, ADR, and migration text. Never "see BR/ADR/migration_strategy".

## epic_names
Unchanged. Empty → LLM titles. Provided → verbatim Epic titles.

## feature_selection
Empty → LLM Feature count per Epic. `epic-N-feature-M` → Epic N gets exactly M Features. Example: `epic-1-feature-1, epic-2-feature-2`.

## story_layer_selection
Empty → LLM/Story Decomposer selects layers (not forced to six). `epic-N-feature-M-story-ui, bff/api` → only those layers for that Feature. Areas: UI, BFF/API, Domain, Persistence, Messaging, Testing.

## Retry
Rerun only the named incomplete agent until complete.

## Active root
Never create a second `src` or `src/src`. Write under the existing workspace `src/artifacts/` tree.
