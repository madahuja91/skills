---
name: backlog-prompt-contract-v23
description: >-
  Shared backlog contract. Title-based artifact ids (epic-System Data Management, feature-Contract pricing). Markdown Renderer and Completeness Validator are subagents. Completeness checks all files.
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

## Completeness (subagent, all files)
Markdown Renderer and Completeness Validator are **subagents** of the stage orchestrator, same as JSON agents. Completeness is the stage gate for **all** files (JSON + Markdown), not a Markdown-only step. The manager dispatches JSON writers, then Markdown Renderer, then Completeness Validator. json_gaps → owning JSON agent. markdown_gaps → Markdown Renderer. Never skip Completeness. Never `json_only_no_markdown_writes`.

## Schema, names, retry
Required fields non-empty. `id` equals folder name. Retry only the named agent.
