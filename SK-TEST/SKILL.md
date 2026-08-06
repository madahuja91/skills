---
name: SK-TEST
description: >-
  Generate positive, negative, and integration test scenarios tied to
  acceptance criteria. mode=cs|ts (TS may include migration paths).
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-TEST — Test Scenario Generation

## Inputs
- stories + acceptance_criteria
- integrations from analysis when available
- `mode`: cs | ts

## Outputs
- CS: `artifacts/cs/test_scenarios.json` **and** update Testing Scenarios **tables** in each nested story MD
- TS: `artifacts/ts/test_scenarios.json` **and** update Testing Scenarios **tables** in each nested story MD

Dual surface required. Use separate tables for Positive / Negative / Integration (columns: ID | Preconditions/Systems | Steps | Expected | Covers AC).

```json
{
  "scenarios": [{
    "id": "TSEN-###",
    "story_id": "",
    "type": "positive|negative|integration|migration",
    "preconditions": [],
    "steps": [],
    "expected": [],
    "covers_ac": []
  }]
}
```

## Procedure
1. Each AC → ≥1 scenario
2. Each story → ≥1 positive and ≥1 negative when policy requires
3. Stories with integrations → ≥1 integration scenario
4. TS mode: add migration-path scenarios when impact is Modified/New

## Must not
Redefine requirements or rewrite stories.
