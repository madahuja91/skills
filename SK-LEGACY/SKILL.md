---
name: SK-LEGACY
description: >-
  Analyze legacy codebase for modules, entry points, integrations, data stores,
  observed behaviors, and risk hotspots. Used by Legacy Code Analyzer.
---

# SK-LEGACY — Legacy Analysis

## Inputs
- Legacy codebase handle/path (upload or workspace)
- Optional scope domains

## Outputs
Write `ACTIVE_ROOT/artifacts/cs/legacy_analysis.json`:
```json
{
  "modules": [{"id": "", "name": "", "path": "", "responsibilities": []}],
  "entry_points": [{"id": "", "type": "", "location": ""}],
  "integrations": [{"id": "", "system": "", "direction": "", "protocol": ""}],
  "data_stores": [{"id": "", "type": "", "entities": []}],
  "observed_behaviors": [{"id": "", "description": "", "module_ids": []}],
  "risk_hotspots": [{"id": "", "reason": "", "severity": "low|med|high"}]
}
```

## Procedure
1. Inventory modules/packages and entry points (APIs, jobs, UI, messaging)
2. Map integrations and data stores with evidence paths
3. Capture observed behaviors tied to modules (not invented business epics)
4. Flag risk hotspots (complexity, dual-write, undocumented batch)
5. Update swarm artifacts_index; hand off per SK-SWARM

## Must not
Invent epics/stories or target-state redesign.
