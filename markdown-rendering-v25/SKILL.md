---
name: markdown-rendering-v25
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
  - Write Markdown twins continuously with JSON; do not wait for Governance PASS.
  - Write src/artifacts/projections/backlog/ folder tree mirroring canonical.
  - When writing a backlog JSON artifact, immediately write the matching Markdown twin under src/artifacts/projections/backlog/ with the same nested folders and ID (do not wait for Governance PASS).
  - JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
  - All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
  - Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.

  - Write folder-tree Markdown under src/artifacts/projections/backlog/ mirroring canonical 1:1 (not a single backlog.md only).
  - NEVER remove, drop, merge, or omit any Epic folder under projections/backlog/Epic/.
  - Projection Epic count MUST equal canonical Epic count.
  - On Governance FAIL leave existing Epic markdown untouched.
```
