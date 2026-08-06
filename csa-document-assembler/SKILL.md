---
name: csa-document-assembler
description: DEPRECATED — do not use. Completeness-Validation-Agent now renders lean csa_pack from artifacts. Kept only for historical workflow references.
---

# CSA Document Assembler — DEPRECATED

## Status

**Removed from the CSA control loop** (`csa-parallel-lane-gates` v2).

Use **Completeness-Validation-Agent** final mode instead:

- Reads `artifacts/*.json`
- Writes only lean `csa_pack/` (5 MD + README + arc42 HTML)
- Does **not** write `deliverables/` or `csa_pack/machine/`

## Schema

Historical manifest schema remains at [`schema.json`](schema.json) for old runs only. New runs must not invoke this agent.
