---
name: completeness-validation-v24
description: >-
  Stage-level completeness gate. Subagent of the stage orchestrator. Check ALL files (JSON and Markdown). Retry the owning subagent for each gap.
---

# Completeness Validation

Load this skill. Do not copy it into prompts.

## You are a subagent of the manager

You hang under the stage orchestrator (`parent` → `subagent`), same as Epic Agent, Feature Agent, and Markdown Renderer. You are not a sequential default agent and you are not nested under Markdown Renderer.

The manager must dispatch you after the JSON specialists and Markdown Renderer. You still check **every** file this stage owns.

## Stage gate for ALL files

Inspect JSON and Markdown. Gaps name the real owner:

- Missing/empty JSON `required_field` → owning JSON agent (Epic Agent, Feature Agent, FAC Agent, Story agent, …)
- Missing FAC/AAC or `story-<title>` JSON → owning JSON agent
- Missing or stub `.md` twin → **Markdown Renderer**
- `src/src` → `status=incomplete`

`status=incomplete`. `retry_directives` tell the **manager** which subagent to rerun. Never treat Completeness as Markdown-only.

## Title-based folders

Expected ids/folders: `epic-System Data Management`, `feature-Contract pricing`, `story-<title>`. Forbidden as folder names: `EPIC-001`, `FEAT-001`, `ST-001`.

## No false complete

`status` is only `complete` or `incomplete`. Never `success` / `PASS`.

`complete` is allowed only after you list the stage directories and verify every bound-skill `required_field` on disk. Empty gap arrays are not a pass if you did not inspect the files.

## Gates
- JSON: every `required_field` present and non-empty
- Markdown: same nested path `.md` twin; human headings for the same fields (no JSON dump)
- Content: BR/ADR/migration inlined
- Paths: if cwd is `src`, artifacts live at `artifacts/...` not `src/artifacts/...`

## Retry
Name the owning subagent + artifact ids + missing fields. Orchestrator (manager) reruns them. No max cap. Do not mark complete to finish the stage.
