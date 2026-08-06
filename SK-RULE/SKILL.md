---
name: SK-RULE
description: >-
  Extract business rules, validations, calculations, eligibility, and
  constraints. Used by Business Rule Extractor.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-RULE — Business Rule Extraction

## Inputs
- capabilities, requirements, legacy_analysis

## Outputs
`ACTIVE_ROOT/artifacts/cs/rules.json`:
```json
{
  "rules": [{
    "id": "BR-###",
    "capability_id": "CAP-###",
    "requirement_ids": ["FR-###"],
    "statement": "",
    "type": "validation|calculation|eligibility|constraint|other",
    "source_refs": []
  }]
}
```

## Procedure
1. Mine validations, calculations, eligibility, constraints from evidence
2. Link to capability and related FRs when known
3. Keep statements atomic and testable

## Must not
Generate stories or AC.
