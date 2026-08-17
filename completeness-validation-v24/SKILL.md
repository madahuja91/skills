---
name: completeness-validation-v24
description: >-
  Stage-level completeness gate. Always run after Markdown Renderer. Never report complete when JSON or Markdown is incomplete. Inform the manager to retry Markdown Renderer when .md twins are missing.
---

# Completeness Validation

Load this skill. Do not copy it into prompts.

## Always after Markdown Renderer

On Epic-Feature and Technical Story, you are a sequential node after Markdown Renderer. You always run. You are not an optional subagent.

If any canonical JSON in this stage lacks a same-path `.md` twin, or the Markdown is a stub/JSON dump/empty, then:
- `status=incomplete` (never `complete` or `success`)
- `markdown_gaps` lists the missing/incomplete files
- `owning_agents` includes `Markdown Renderer`
- `retry_directives` tell the **stage orchestrator (manager)** to retry **Markdown Renderer** only

Do not skip this gate. Do not mark complete because JSON exists.

## Title-based folders

Expected ids/folders: `epic-System Data Management`, `feature-Contract pricing`, `story-<title>`. Forbidden as folder names: `EPIC-001`, `FEAT-001`, `ST-001`.

## No false complete

`status` is only `complete` or `incomplete`. Never `success` / `PASS`.

`complete` is allowed only after you list the stage directories and verify every bound-skill `required_field` on disk. If any required field is missing, any Markdown twin is missing, any Feature in Technical Story has no `Technical-Stories/story-*.json`, or `src/src` exists → `status=incomplete` with `retry_directives`. Empty gap arrays are not a pass if you did not inspect the files.

## Gates
- JSON: every `required_field` present and non-empty
- Markdown: same nested path `.md` twin; human headings for the same fields (no JSON dump)
- Content: BR/ADR/migration inlined
- Paths: if cwd is `src`, artifacts live at `artifacts/...` not `src/artifacts/...`

## Retry
Name the owning subagent + artifact ids + missing fields. Orchestrator (manager) reruns them. No max cap. Do not mark complete to finish the stage.
