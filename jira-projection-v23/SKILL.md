---
name: jira-projection-v23
description: >-
  Project the validated technical backlog into Jira-import-oriented JSON.
---

# Jira Projection

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: jira-projection
  name: Jira Projection
  version: 2.0.0
  purpose: Project the validated technical backlog into Jira-import-oriented JSON.
  rules:
  - Canonical backlog remains the source of truth.
  - Preserve REQ/EPIC/FEAT/ST IDs as external IDs.
  - Preserve parent relationships.
  - Preserve FAC/AAC/SAC content in the configured Jira description/acceptance representation.
  - Do not flatten technical Story LLD information.
  - Do not generate or modify canonical content.
  - Run only after Governance PASS. Otherwise status=skipped.
  - Write src/artifacts/projections/jira-import.json.
  - Until PASS, keep placeholder {"schema_version":"2.0.0","status":"pending","items":[]}.
```
