---
name: SK-CAP
description: >-
  Derive business capabilities from legacy analysis and CSA analysis.
  Used by Business Capability Extractor.
---

# SK-CAP — Capability Synthesis

## Inputs
- `artifacts/cs/legacy_analysis.json`
- `artifacts/cs/csa_analysis.json`
- Optional glossary

## Outputs
`ACTIVE_ROOT/artifacts/cs/capabilities.json`:
```json
{
  "capabilities": [{
    "id": "CAP-###",
    "name": "",
    "description": "",
    "owners": [],
    "source_refs": []
  }]
}
```

## Procedure
1. Cluster behaviors + architecture components into business capabilities
2. Assign stable CAP-### IDs
3. Link source_refs to legacy modules and CSA components
4. Prefer business language over technical module names

## Must not
Write stories, AC, or target-state capabilities beyond evidence.
