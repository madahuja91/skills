---
name: SK-QUALITY
description: >-
  Evaluate pack quality: completeness, consistency, developable story size,
  Jira readability, rule coverage, and (TS) ADR/TSA alignment. Emit findings only.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-QUALITY — Quality Validation (client-readiness)

## Inputs
- Phase pack
- `mode`: cs | ts
- `policy_profile`: standard | strict | draft

## Outputs
- CS: `artifacts/gates/quality_cs.json` (also mirror to `artifacts/cs/quality_cs.json` if helpful)
- TS: `artifacts/gates/quality_ts.json` (also mirror to `artifacts/ts/quality_ts.json` if helpful)
- Optional compact MD summary: `artifacts/gates/quality_cs.md` / `quality_ts.md`

## CLIENT READINESS
Treat the pack as a **client deliverable**, not an internal pipeline dump.
`PASS` means a client BA/PO could review the backlog without embarrassment.
Pipeline completeness alone is **not** enough for PASS under standard/strict.

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
- **G3 readability (Jira-quality) — block for standard/strict unless noted:**
  - `STORY_TITLE_GENERIC` — title matches `Operate …` / `Support the observed…` (**block**)
  - `STORY_DESC_BOILERPLATE` — description lacks As a / What / How structure (**block**)
  - `AC_CIRCULAR` — Then clause references “behavior described by FR-…” (**block**)
  - `TEST_BOILERPLATE` — template phrases (“Prepare valid current-state inputs for FR…”, “Observe … current CCDS behavior”) (**block**)
  - `EDGE_GENERIC` — edge handling is only “Apply current-state validation as extracted” (**warn**)
- **G3 developability (HARD for standard/strict):**
  - Count FRs from `functional_requirement_ids` (or legacy `requirement_ids`)
  - `STORY_OVERLOADED` — story has **≥4 FRs** OR mixes clearly separable journeys (**block**, not warn)
  - `EPIC_MEGA_1TO1` — epic count ≈ story count **and** average FRs/story ≥3 (**block**)
  - `CAPABILITY_STORY_DUMP` — one story owns an entire capability’s FR set when that set has ≥3 FRs (**block**)

### TS (G4–G8) — always evaluate
- G4 ADR Compliance, G5 TSA Alignment, G6 Duplicates, G7 Traceability support, G8 Test/AC coverage
- Dual surface + nested epic layout + epic_id
- Same readability + developability checks as G3 for TS stories/AC/tests

### Story-count policy
- Epic with 1 story → **info** only when that story has ≤2 FRs and is truly atomic
- Otherwise prefer multi-story epics; **block** mega 1:1 dumps via codes above
- Do **not** PASS overall if any `block` finding exists under standard/strict

## Status rules
- `PASS` only when no `block` findings
- `PASS_WITH_WARNINGS` when only warn/info
- `FAIL` when any block finding exists

## Must not
Silently rewrite stories; emit findings + suggested_fix only. Do not mark developability issues as mere warnings under standard/strict.
