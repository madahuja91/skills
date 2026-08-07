---
name: csa5-evidence-citation
description: Rules for citing file paths, line ranges, and artifact kinds on CSA claims. Use when writing specialist artifacts or validating evidence coverage.
---

# Evidence Citation

## Schema

Authoritative evidence object: [schema.json](schema.json)

## When required

Attach `evidence` to:

- Technology/framework/version detections
- Business rules and entities
- Components and integrations
- Field lineage mappings
- Traceability edges used for epic/story seeds

## Format

Use relative paths from `scope.codebase_root`. Prefer precise line ranges when available.

## Coverage target

Gate rubrics expect ≥70% of critical items to have at least one non-`inferred` evidence entry. Pure inference must include `uncertainty_reason`.