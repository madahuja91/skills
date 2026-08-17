---
name: completeness-validation-v23
description: >-
  Stage-level completeness gate. Never report complete or success when JSON, Markdown, or schema is incomplete.
---

# Completeness Validation

Load this skill. Do not copy it into prompts.

## No false complete

`status` is only `complete` or `incomplete`. Never `success` / `PASS`.

`complete` is allowed only after you list the stage directories and verify every bound-skill `required_field` on disk. If any required field is missing, any Markdown twin is missing, any Feature in Technical Story has no `Technical-Stories/ST-*.json`, or `src/src` exists → `status=incomplete` with `retry_directives`. Empty gap arrays are not a pass if you did not inspect the files.

## Gates
- JSON: every `required_field` present and non-empty
- Markdown: same nested path `.md` twin; human headings for the same fields (no JSON dump)
- Content: BR/ADR/migration inlined
- Paths: if cwd is `src`, artifacts live at `artifacts/...` not `src/artifacts/...`

## Retry
Name the owning subagent + artifact ids + missing fields. Orchestrator reruns them. No max cap. Do not mark complete to finish the stage.
