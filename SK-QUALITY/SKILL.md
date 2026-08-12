---
name: SK-QUALITY
description: >-
  Evaluate pack quality: completeness, consistency, duplicates, rule coverage,
  and (TS) ADR compliance + TSA alignment. Emit findings only.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-QUALITY — Quality Validation

## Inputs
- Phase pack
- `mode`: cs | ts
- `policy_profile`: standard | strict | draft

## Outputs
- CS: `artifacts/gates/quality_cs.json` (also mirror to `artifacts/cs/quality_cs.json` if helpful)
- TS: `artifacts/gates/quality_ts.json` (also mirror to `artifacts/ts/quality_ts.json` if helpful)
- Optional compact MD summary as tables: `artifacts/gates/quality_cs.md` / `quality_ts.md`

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
### Active root (always)
- Fail/block if nested `src/src`, multi-root writes, or artifacts outside ACTIVE_ROOT (`active-root-hygiene`)

### CS (G1–G3) — always evaluate
- G1 Requirement Completeness
- G2 Business Rule Coverage
- G3 Story Consistency / duplicates / **dual surface** / **nested epic→stories layout** / **epic_id present**
- **G3 readability (Jira-quality) — warn or block by severity:**
  - `STORY_TITLE_GENERIC` — title matches `Operate …` / `Support the observed…` (**block** for standard/strict)
  - `STORY_DESC_BOILERPLATE` — description lacks As a / What / How structure (**block** for standard/strict)
  - `AC_CIRCULAR` — Then clause references “behavior described by FR-…” or equivalent (**block**)
  - `TEST_BOILERPLATE` — steps/expected are template phrases (“Prepare valid current-state inputs for FR…”, “Observe … current CCDS behavior”) (**block**)
  - `EDGE_GENERIC` — edge handling is only “Apply current-state validation as extracted” (**warn**)
  - `STORY_OVERLOADED` — separable FR clusters packed into one story (**warn**)

### TS (G4–G8) — always evaluate
- G4 ADR Compliance, G5 TSA Alignment, G6 Duplicates, G7 Traceability support, G8 Test/AC coverage
- Dual surface + nested epic layout + epic_id
- Same readability checks as G3 for TS stories/AC/tests

### Story-count guidance (not a hard block)
- Epic with 1 story → **info** only (acceptable when atomic)
- Warn if a single story packs clearly separable FR clusters that should have been split (`STORY_OVERLOADED`)
- Do **not** block solely because an epic has fewer than 2 stories

## Must not
Silently rewrite stories; emit findings + suggested_fix only.
