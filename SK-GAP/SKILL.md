---
name: SK-GAP
description: >-
  Compare Current State functional inventory vs TSA, ADR, and migration
  guidelines. Classify New/Modified/Reused/Deprecated.
---

# SK-GAP — Gap Analysis

## Inputs
- CS stories/epics (artifacts/cs or uploaded cs_pack)
- adr_decisions, tsa_analysis, migration_guidelines

## Outputs
`artifacts/ts/gap_register.json`:
```json
{
  "items": [{
    "id": "GAP-###",
    "cs_refs": [],
    "classification": "New|Modified|Reused|Deprecated",
    "rationale": "",
    "tsa_components": [],
    "adr_refs": [],
    "migration_notes": ""
  }]
}
```

## Procedure
1. Inventory CS functional coverage
2. Map each item to TSA components + ADR constraints
3. Classify migration impact
4. Ensure every must CS story is represented or explicitly deprecated

## Must not
Author full target stories (SK-TARGET owns that).
