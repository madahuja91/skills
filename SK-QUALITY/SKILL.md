---
name: SK-QUALITY
description: >-
  Evaluate pack quality: completeness, consistency, duplicates, rule coverage,
  and (TS) ADR compliance + TSA alignment. Emit findings only.
---

# SK-QUALITY — Quality Validation

## Inputs
- Phase pack
- `mode`: cs | ts
- `policy_profile`: standard | strict | draft

## Outputs
- CS: `artifacts/gates/quality_cs.json`
- TS: `artifacts/gates/quality_ts.json`

```json
{
  "scores": {},
  "findings": [{
    "code": "",
    "severity": "info|warn|block",
    "message": "",
    "artifact_refs": [],
    "suggested_fix": ""
  }]
}
```

## Rubrics
### CS (G1–G3)
Requirement completeness, business rule coverage, story consistency/duplicates

### TS (G4–G6, G8 support)
ADR compliance, TSA alignment, duplicate detection, test/AC coverage signals

## Must not
Silently rewrite stories; emit findings + suggested_fix only.
