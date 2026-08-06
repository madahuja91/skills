---
name: SK-AC
description: >-
  Generate Given/When/Then acceptance criteria covering functional
  requirements and business rules. mode=cs|ts.
---

# SK-AC — Acceptance Criteria

## Inputs
- story (or story set)
- related requirements + rules
- `mode`: cs | ts

## Outputs
- Update stories and write:
  - CS: `artifacts/cs/acceptance_criteria.json` **and** update AC **table** in each nested story MD under `epics/<EPIC-ID>/stories/`
  - TS: `artifacts/ts/acceptance_criteria.json` **and** update AC **table** in each nested story MD

Dual surface required: JSON pack + Markdown story files kept in sync.
AC Markdown section must be a table with columns: ID | Given | When | Then | Covers FR | Covers BR.

```json
{
  "acceptance_criteria": [{
    "id": "AC-###",
    "story_id": "",
    "given": "",
    "when": "",
    "then": "",
    "covers_fr": [],
    "covers_br": []
  }]
}
```

## Procedure
1. Ensure every must FR and critical BR has AC coverage
2. Use Given/When/Then; keep atomic
3. Link covers_fr / covers_br

## Must not
Change story scope or invent new FRs.
