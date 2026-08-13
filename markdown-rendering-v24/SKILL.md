---
name: markdown-rendering-v24
description: >-
  Render human-readable Markdown from the validated technical backlog JSON.
---

# Markdown Rendering

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: markdown-rendering
  name: Markdown Rendering
  version: 2.0.0
  purpose: Render human-readable Markdown from the validated technical backlog JSON.
  rules:
  - JSON is authoritative.
  - Preserve Epic -> Feature -> Story hierarchy.
  - Display FAC/AAC at Feature level.
  - Display full technical LLD sections at Story level.
  - Display SAC at Story level.
  - Preserve exact Story area names.
  - Do not add content not present in JSON.
  - Run only after Governance PASS. Otherwise status=skipped.
  - Write src/artifacts/projections/backlog.md.

  - Write folder-tree Markdown under src/artifacts/projections/backlog/ mirroring canonical 1:1 (not a single backlog.md only).
  - NEVER remove, drop, merge, or omit any Epic folder under projections/backlog/Epic/.
  - Projection Epic count MUST equal canonical Epic count.
  - On Governance FAIL leave existing Epic markdown untouched.
```
