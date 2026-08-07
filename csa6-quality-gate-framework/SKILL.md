---
name: csa6-quality-gate-framework
description: Shared CSA quality gate contract, scoring dimensions, severity rules, and remediation brief format. Use when Completeness Validator or Manager evaluates specialist artifacts.
---

# Quality Gate Framework

## Schema

Authoritative gate report contract: [`schema.json`](schema.json)

Every Completeness Validator report MUST validate against this schema.

## Result enum

- `pass` — accepted; no critical gaps
- `pass_with_warnings` — accepted; non-critical gaps logged
- `fail` — not accepted; Manager must re-run or escalate

## Scoring dimensions (0–100)

1. `schema_conformance` — JSON Schema validity vs agent schema
2. `evidence_coverage` — % critical claims with non-inferred evidence
3. `completeness` — rubric coverage %
4. `confidence_floor` — min/avg confidence against rubric

## Acceptance rule

Accept only if:

- `result` is `pass` or `pass_with_warnings`
- `blocking_gaps` contains **zero** items with `severity: critical`
- `schema_conformance == 100`

## Severity

| Severity | Meaning | Manager action |
|----------|---------|----------------|
| critical | Blocks epic/story trust | re-run required |
| high | Major gap | re-run if retries remain; else escalate |
| medium | Notable | may pass_with_warnings |
| low | Cosmetic | warning only |

## Output

Write gate report to `artifacts/quality_gate_reports/{gate_id}-{artifact_id}.json` using `schema.json`.
