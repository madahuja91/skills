---
name: markdown-rendering-v28
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
  - Write src/artifacts/projections/backlog/ folder tree mirroring canonical.
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
