---
name: SK-EPIC
description: >-
  Cluster stories into epics by capability, journey, or bounded context.
  Used after story generation in CS or TS mode.
---

# SK-EPIC — Epic Generation

## Inputs
- stories[]
- capabilities[]
- clustering_policy (default: by capability)

## Outputs
- CS: `artifacts/cs/cs_epics.json`
- TS: `artifacts/ts/ts_epics.json`

```json
{
  "epics": [{
    "id": "CS-EPIC-###|TS-EPIC-###",
    "title": "",
    "business_objective": "",
    "scope_in": [],
    "scope_out": [],
    "story_ids": [],
    "traceability": {"capabilities": []}
  }]
}
```

## Procedure
1. Cluster stories by capability / journey
2. Write epic objective and scope in/out
3. Ensure every story belongs to exactly one primary epic
