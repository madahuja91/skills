---
name: csa-artifact-contract
description: Shared CSA artifact metadata, ID conventions, confidence scoring, and evidence reference rules. Use when producing or validating any CSA specialist artifact JSON.
---

# CSA Artifact Contract

## Schema

Authoritative envelope: [`schema.json`](schema.json)

All specialist outputs MUST conform to this shared envelope plus their agent-specific payload schema.

## Required metadata (every artifact)

- `artifact_id`: `{agent}-{yyyyMMddHHmmss}` (e.g. `discover-20260804143022`)
- `agent_id`: one of `discover|business_domain|tech_architecture|data_lineage|integration|document_assembler|completeness_validator`
- `agent_version`: semver string
- `timestamp`: ISO-8601
- `scope`: `{ codebase_root, modules[], exclusions[] }`
- `overall_confidence_score`: 0–100 integer
- `schema_version`: `"1.0.0"`

## Evidence rules

Every factual claim that feeds epic/story generation MUST include an `evidence` array entry:

```json
{
  "path": "relative/path/to/file",
  "lines": [10, 25],
  "kind": "code|config|ddl|descriptor|doc|log|inferred",
  "note": "optional short note"
}
```

Prefer `code|config|ddl|descriptor` over `inferred`. If only inferred, set confidence ≤ 40 and explain in `uncertainty_reason`.

## Confidence bands

| Band | Score | Meaning |
|------|-------|---------|
| high | 85–100 | Multi-source or strong descriptor/code evidence |
| medium | 60–84 | Single solid source |
| low | 40–59 | Weak/partial evidence |
| speculative | 0–39 | Inferred; must not block modernization without human review |

## ID conventions

- Domains: `DOM-{slug}`
- Entities: `ENT-{slug}`
- Rules: `BR-{slug}`
- Components: `CMP-{slug}`
- Integrations: `INT-{slug}`
- Lineage: `LIN-{slug}`
- Gaps: `{AGENT_PREFIX}-{nnn}` (e.g. `DISC-014`)

## Unknown over invention

For 20+ year legacy stacks: if version/framework cannot be proven, set value to `"unknown"` with evidence of what was searched. Never invent modern framework names.
