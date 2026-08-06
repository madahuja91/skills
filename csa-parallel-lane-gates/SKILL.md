---
name: csa-parallel-lane-gates
description: HARD CSA swarm control loop — per-lane Completeness, then Completeness renders lean csa_pack from artifacts. No Document Assembler. No duplicate deliverables/machine folders.
---

# CSA Parallel Lane Gates

## Schema

Contract: [`schema.json`](schema.json)

## HARD: Forbidden

1. Completeness only after join (batch) when lanes can finish independently.
2. Invoking **CSA-Document-Assembler** (removed from the control loop).
3. Writing client packs under `deliverables/`, numbered `01_`–`05_` MD, or `csa_pack/machine/sections/` copies of artifacts.
4. Duplicating the same narrative into `analysis/` + `deliverables/` + `csa_pack/`.
5. Hard-fail final gate on cosmetics when artifact substance schemas pass.

## Control loop (required)

```text
Bootstrap shared memory
  → Discover → Completeness(gate-discover)
  → Fan-out Domain | Tech | Lineage | Integration (parallel)
       each lane: write artifacts/<name>.json ONLY
                  Completeness(lane gate) as soon as that lane finishes
  → Join when four artifacts accepted
  → Completeness(FINAL):
       validate accepted artifacts against specialist schemas
       RENDER lean csa_pack from artifacts (no Assembler)
       validate pack shape
```

## Who writes what

| Path | Owner | Allowed |
|------|-------|---------|
| `artifacts/*.json` | Specialists | YES — SSOT |
| `artifacts/quality_gate_reports/*` | Completeness | YES |
| `_internal/**` | Manager / Completeness / specialists (swarm only) | YES |
| `csa_pack/{5 MD, README, arc42-c4/*.html}` | **Completeness (final only)** | YES |
| `csa_pack/machine/**` | — | **NO** |
| `deliverables/**` | — | **NO** |
| `analysis/*.md` | Optional specialist scratch only | Not client deliverables |

## Final Completeness = packager + validator

After join, Completeness MUST:

1. Read accepted `artifacts/{discovery,domain,architecture,lineage,integration}.json`.
2. Render ONLY:
   - `csa_pack/Executive_Summary.md`
   - `csa_pack/Business_Architecture.md`
   - `csa_pack/Application_Architecture.md`
   - `csa_pack/Data_and_Integration.md`
   - `csa_pack/Risks_Gaps_and_Traceability.md`
   - `csa_pack/README.md`
   - `csa_pack/arc42-c4/{index,context,containers,components}.html`
3. Map content from artifact fields (see `csa-section-boundaries`). Do not invent.
4. Leave gate reports under `artifacts/quality_gate_reports/` — never inside `csa_pack/`.
5. Delete or refuse `deliverables/` and `csa_pack/machine/` if created.

## Per-lane Completeness

| Lane | gate_id | artifact |
|------|---------|----------|
| Discover | gate-discover | artifacts/discovery.json |
| Domain | gate-business-domain | artifacts/domain.json |
| Tech | gate-tech-architecture | artifacts/architecture.json |
| Lineage | gate-data-lineage | artifacts/lineage.json |
| Integration | gate-integration | artifacts/integration.json |

## Same document count

Still exactly five named client Markdown docs + README + HTML hub. No extras.
