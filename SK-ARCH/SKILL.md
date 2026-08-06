---
name: SK-ARCH
description: >-
  Interpret CSA or TSA architecture documents into components, boundaries,
  interfaces, data domains, and NFR anchors. mode=csa|tsa.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-ARCH — Architecture Analysis

## Inputs
- Architecture document(s)
- `mode`: `csa` | `tsa`

## Outputs
- CSA → `ACTIVE_ROOT/artifacts/cs/csa_analysis.json`
- TSA → `ACTIVE_ROOT/artifacts/ts/tsa_analysis.json`

```json
{
  "mode": "csa|tsa",
  "components": [{"id": "", "name": "", "type": "", "responsibilities": []}],
  "boundaries": [{"id": "", "from": "", "to": "", "mechanism": ""}],
  "interfaces": [{"id": "", "provider": "", "consumer": "", "contract_ref": ""}],
  "data_domains": [{"id": "", "name": "", "entities": []}],
  "nfr_anchors": [{"id": "", "category": "", "statement": ""}]
}
```

## Procedure
1. Extract components and ownership boundaries
2. Capture interfaces/contracts and data domains
3. Record NFR anchors relevant to functional stories
4. Cite source sections; mark missingInformation when thin

## Must not
Extract detailed FRs/rules from code (CSA mode) or invent gap scores (TSA mode).
