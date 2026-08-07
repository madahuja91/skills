---
name: csa-rich-content
description: Enforces lean 5-doc CSA pack from artifacts SSOT — legacy schema content only. No workflow meta, machine/sections, or deliverables.
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
2. Completeness builds **pack substance** that validates against each `output-schemas/*.schema.json`, then renders five Markdown owners (`csa-section-boundaries`).
3. **Thin Markdown = FAIL.** A short overview that omits required schema sections does not pass even if the five filenames exist.
4. Fail if forbidden duplicate trees exist.
5. Prefer substance gaps over cosmetic HTML/Jaccard-only fails.
6. **Client pack = legacy only:** no workflow/swarm/gate/process meta in any `csa_pack/**` file.

## Specialist floors

| Artifact | Minimum |
|----------|---------|
| domain.json | ≥3 domains, ≥8 capabilities, workflows + dispatch when evidenced |
| architecture.json | ≥5 layers, deploy/security/cross-cutting/build + populated `c4_views` |
| lineage.json | ≥3 sources, ≥10 lineage rows, entity_catalog |
| integration.json | ≥6 integrations, contracts + exceptions + resilience |

## Pack document floors (blocking)

Each client MD must cover **all** `required` fields of its output-schema (tables/sections, not a stub summary). Approximate depth floors for Completeness judgment:

| Doc | Must show (non-exhaustive) |
|-----|----------------------------|
| Executive_Summary | overview + metrics≥5 + readiness≥4 + findings≥5 + risks≥5 + effort + strategy + success metrics |
| Business_Architecture | contexts≥3 + CAP-*≥8 + dictionary≥8 + flows≥3 + dispatch≥5 + flags + providers + gaps |
| Application_Architecture | 5 layers + CMP-*≥8 + build/runtime + deploy + security + cross-cutting + runtime evidence + DEBT-*≥5 + ops gaps |
| Data_and_Integration | stores≥3 + entities≥5 + LIN-*≥10 + SP rules≥5 + INT-*≥6 + contracts + exceptions + resilience |
| Risks_Gaps_and_Traceability | GAP-*≥5 + RISK-*≥5 + ASM-*≥3 + ACT-*≥3 + REG-*≥3 + trace links≥10 |

## Blocking checks

required_files_present, artifact_schema_conformance, **pack_output_schema_conformance**, specialist_list_depth, forbidden_duplicate_trees, section_anti_redundancy, pack_shape_valid, shared_memory_present, no_workflow_meta_in_csa_pack

Do **not** require writing `csa_pack/machine/sections/*.json` as a client deliverable. Temporary pack-substance JSON under `_internal/completeness_validation/` for schema checks is allowed.
