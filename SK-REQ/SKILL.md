---
name: SK-REQ
description: >-
  Extract functional requirements grouped by capability from legacy signals
  and capability set. Used by Functional Requirement Extractor.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-REQ — Requirement Extraction

## Inputs
- `artifacts/cs/capabilities.json`
- `artifacts/cs/legacy_analysis.json`
- Optional glossary

## Outputs
`ACTIVE_ROOT/artifacts/cs/requirements.json`:
```json
{
  "requirements": [{
    "id": "FR-###",
    "capability_id": "CAP-###",
    "statement": "",
    "priority": "must|should|could",
    "source_refs": []
  }]
}
```

## Procedure
1. For each capability, extract observable functional requirements
2. Prefer “system shall…” statements grounded in evidence
3. Mark priority; cite source_refs
4. Do not invent target-state modernization behavior

## Must not
Author stories or business rules (owned by other skills).
