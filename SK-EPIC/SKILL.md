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
- CS: `artifacts/cs/cs_epics.json` (index) **required**
- TS: `artifacts/ts/ts_epics.json` (index) **required**
- Nested Markdown (industry / Jira hierarchy) **required**:
  - `artifacts/cs/epics/<EPIC-ID>/epic.md`
  - `artifacts/cs/epics/<EPIC-ID>/stories/<STORY-ID>.md`
  - Same pattern under `artifacts/ts/epics/...`

## Clustering rules (industry standard)
- An Epic groups related Stories that share one business outcome
- **Do not force** multiple stories: if evidence supports only one cohesive story for that epic, keep **one**
- Create **multiple** stories when the capability/journey naturally splits (e.g. inquire vs maintain vs authorize vs integrate, or distinct actors/flows)
- Prefer clustering by capability / user journey / bounded context
- Every story must set `epic_id` and appear in parent epic `story_ids`
- Anti-pattern: inventing fake splits just to inflate story count **or** dumping unrelated work into one mega-story

```json
{
  "epics": [{
    "id": "CS-EPIC-###|TS-EPIC-###",
    "title": "",
    "business_objective": "",
    "scope_in": [],
    "scope_out": [],
    "story_ids": ["STORY-A"],
    "traceability": {"capabilities": []}
  }]
}
```

## Procedure
1. Decide story boundaries from evidence (FRs/behaviors/actors) — split only when boundaries are real
2. Cluster by capability / journey; one epic may have 1..N stories
3. Write epic objective and scope in/out as **tables**
4. Ensure every story belongs to exactly one primary epic (`epic_id` + `story_ids`)
5. Write nested `epic.md` with Child Stories table pointing to `stories/<STORY-ID>.md`
6. Prefer enterprise template `templates/epic.md`
7. Self-check: each epic has ≥1 story; multi-story only where justified in rationale/scope
