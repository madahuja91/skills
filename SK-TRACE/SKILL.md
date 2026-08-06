---
name: SK-TRACE
description: >-
  Validate bidirectional traceability across capability, FR, BR, story, AC,
  test, and (TS) legacy/gap/ADR/TSA links.
---

# SK-TRACE — Traceability Validation

## Inputs
- Phase pack under artifacts/cs or artifacts/ts
- `mode`: cs | ts

## Outputs
- CS: `artifacts/traceability/trace_cs.json` (+ optional `artifacts/gates/trace_cs_summary.json`)
- TS: `artifacts/traceability/trace_ts.json`

Include: `score` (0..1), `matrix`, `missing_links`, `orphan_artifacts`.

## Required link types
### CS
capability → requirement → story → AC → test; requirement → rule → story; **story → epic** (`epic_id`)

### TS
All CS links plus story → legacy_story | gap_item → adr | tsa_component; **story → epic**

## Scoring
`score = satisfied_required_links / total_required_links`  
Block recommendation when score < 0.90 (standard policy).

## Must not
Add new functional content to fix gaps — report missing_links only.
