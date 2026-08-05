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
- Update stories and/or write:
  - CS: `artifacts/cs/acceptance_criteria.json`
  - TS: `artifacts/ts/acceptance_criteria.json`

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
