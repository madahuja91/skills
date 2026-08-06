---
name: SK-ADR
description: >-
  Interpret Architecture Decision Records into decision objects with
  functional impact. Used by ADR Analyzer.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-ADR — ADR Interpretation

## Inputs
- ADR documents / pack

## Outputs
`artifacts/ts/adr_decisions.json`:
```json
{
  "decisions": [{
    "id": "ADR-###",
    "title": "",
    "status": "accepted|proposed|superseded|deprecated",
    "forces": [],
    "decision": "",
    "consequences": [],
    "functional_impact": ""
  }]
}
```

## Procedure
1. Parse each ADR; normalize IDs
2. Extract forces, decision, consequences
3. Write functional_impact relevant to story generation
4. Flag superseded ADRs so stories do not treat them as active

## Must not
Generate stories or gap classifications.
