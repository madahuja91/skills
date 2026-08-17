---
name: markdown-rendering-v30
description: >-
  Render human-readable Markdown from the validated technical backlog JSON.
---

## You always write Markdown

You are the Markdown Renderer. Read canonical JSON, write matching `.md` twins under `artifacts/projections/backlog/`.

Forbidden:
- `json_only_no_markdown_writes`
- skipping because `validation.json` is missing or not PASS
- applying the JSON-agent "do not write Markdown" rule to yourself

Jira waits for Governance PASS. Markdown does not.

# Markdown Rendering

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: markdown-rendering
  name: Markdown Rendering
  version: 2.0.0
  purpose: Sole Markdown writer (Claude Sonnet 4.5). Render schema-complete human-readable Markdown from backlog JSON. Do not author JSON.
  rules:
  - JSON is authoritative.
  - Preserve Epic -> Feature -> Story hierarchy.
  - Display FAC/AAC at Feature level.
  - Display full technical LLD sections at Story level.
  - Display SAC at Story level.
  - Preserve exact Story area names.
  - Do not add content not present in JSON.
  - Markdown Renderer owns all Markdown twins and must strictly mirror skill schema fields from JSON; do not wait only for Governance PASS once JSON exists.
  - You ALWAYS write .md twins. The JSON-agent rule "do not write Markdown" does not apply to you.
  - Forbidden status: json_only_no_markdown_writes. That decision is a failure.
  - Do not skip because validation.json is missing or not PASS. Jira waits for PASS; Markdown does not.
  - Write artifacts/projections/backlog/ folder tree mirroring canonical.
  - JSON agents write schema-complete JSON under src/artifacts/canonical/backlog/ only. Markdown Renderer (Claude Sonnet 4.5) writes matching .md twins under src/artifacts/projections/backlog/. Do not dual-write Markdown from JSON agents.
  - JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
  - All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
  - Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.

  - Write folder-tree Markdown under src/artifacts/projections/backlog/ mirroring canonical 1:1 (not a single backlog.md only).
  - NEVER remove, drop, merge, or omit any Epic folder under projections/backlog/Epic/.
  - Projection Epic count MUST equal canonical Epic count.
  - On Governance FAIL leave existing Epic markdown untouched.
```

  # content rule: Never write BR/ADR/migration references; inline full details in every artifact.

## Feature / story selection (replaces 1-Feature-per-Epic and forced 6 layers)
- epic_names is unchanged: verbatim Epic titles when provided; LLM titles when empty.
- feature_selection empty → LLM decides Feature count per Epic.
- feature_selection `epic-1-feature-1, epic-2-feature-2` → Epic 1 gets 1 Feature, Epic 2 gets 2.
- story_layer_selection empty → LLM decides layers per Feature.
- story_layer_selection `epic-1-feature-1-story-ui, bff/api` → only UI and BFF/API Stories for that Feature.

## Human names, not bare IDs
Always write the artifact title/name with the id. Forbidden: referring to FEAT-001 / FAC-002 / AAC-001 / SAC-003 / ST-004 / EPIC-001 by number alone.

## Markdown must not dump JSON
Do not copy the full JSON document into Markdown. JSON lives under `src/artifacts/canonical/backlog/`. Markdown is a human-readable projection only.
