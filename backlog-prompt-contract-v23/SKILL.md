---
name: backlog-prompt-contract-v23
description: >-
  Shared backlog contract. Title-based artifact ids (epic-System Data Management, feature-Contract pricing). Completeness must run after Markdown Renderer.
---

# Backlog Prompt Contract

Load this skill. Do not copy it into prompts.

## Write paths
If cwd is `src`, write `artifacts/...` (never `src/artifacts/...`, never `src/src`).

## Title-based ids (not EPIC-001)
- Epic id/folder/file: `epic-<verbatim title>` e.g. `epic-System Data Management`
- Feature: `feature-<verbatim title>` e.g. `feature-Contract pricing`
- FAC/AAC: `fac-<feature title>`, `aac-<feature title>`
- Story/SAC: `story-<title>`, `sac-<title>`
- Requirement: `req-<title>`
Forbidden: `EPIC-001`, `FEAT-001`, `ST-001`. Sanitize `\/:*?"<>|` only; keep spaces.

## Completeness after Markdown
Markdown Renderer writes `.md` twins. Completeness Validator **must run after** that. Incomplete/missing Markdown → `status=incomplete`, tell the manager (`retry_directives`, owning agent = Markdown Renderer). Never skip Completeness. Never `json_only_no_markdown_writes`.

## Schema, names, retry
Required fields non-empty. `id` equals folder name. Retry only the named agent.
