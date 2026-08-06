---
name: csa-rich-content
description: Enforces lean 5-doc CSA pack rendered from artifacts SSOT. No machine/sections duplicate; no deliverables folder.
---

# CSA Output Quality

## Schema

[`schema.json`](schema.json)

## Client pack (only)

1. `Executive_Summary.md`
2. `Business_Architecture.md`
3. `Application_Architecture.md`
4. `Data_and_Integration.md`
5. `Risks_Gaps_and_Traceability.md`
6. `README.md` + `arc42-c4/*.html`

Rendered by **Completeness** from `artifacts/*.json`.  
**No** `csa_pack/machine/`. **No** `deliverables/`. **No** Assembler.

## Core policy

1. Specialist schema completeness first (`artifacts/*.json` required fields + evidence).
2. Completeness maps artifacts → five Markdown owners (`csa-section-boundaries`).
3. Fail if forbidden duplicate trees exist.
4. Prefer substance gaps over cosmetic HTML/Jaccard-only fails.

## Specialist floors

| Artifact | Minimum |
|----------|---------|
| domain.json | ≥3 domains, ≥8 capabilities, workflows + dispatch when evidenced |
| architecture.json | ≥5 layers, deploy/security/cross-cutting/build |
| lineage.json | ≥3 sources, ≥10 lineage rows, entity_catalog |
| integration.json | ≥6 integrations, contracts + exceptions + resilience |

## Blocking checks

required_files_present, artifact_schema_conformance, specialist_list_depth, forbidden_duplicate_trees, section_anti_redundancy, pack_shape_valid, shared_memory_present

Do **not** require `csa_pack/machine/sections/*.json`.
