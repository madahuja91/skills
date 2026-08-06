---
name: csa-parallel-lane-gates
description: HARD CSA swarm control loop — per-lane Completeness, then Completeness renders lean csa_pack from artifacts. Missing pack = FAIL. No Document Assembler.
---

# CSA Parallel Lane Gates

## Schema

Contract: [`schema.json`](schema.json)

## HARD: Forbidden

1. Completeness only after join (batch) when lanes can finish independently.
2. Invoking **CSA-Document-Assembler**.
3. Writing `deliverables/`, numbered `01_`–`05_` MD, or `csa_pack/machine/`.
4. **Final Completeness that only validates JSON / writes a gate report / chats an executive summary without rendering `csa_pack/`.**
5. Inventing final gate ids (e.g. `gate-final-completeness`). Final gate is **`gate-csa-document`**.
6. Manager declaring success when required pack files are missing on disk.

## Control loop (required)

```text
Bootstrap shared memory (ACTIVE_ROOT preferably src/)
  -> Discover -> Completeness(gate-discover)
  -> Fan-out Domain | Tech | Lineage | Integration (parallel)
       each lane: artifacts/<name>.json ONLY + Completeness(lane gate)
  -> Join when four artifacts accepted
  -> Completeness(FINAL):
       validate artifacts
       RENDER lean csa_pack (required)
       validate pack via gate-csa-document
```

## Who writes what

| Path | Owner |
|------|-------|
| `artifacts/*.json` | Specialists |
| `artifacts/quality_gate_reports/*` | Completeness |
| `_internal/**` | Manager / Completeness / specialists (swarm) |
| `csa_pack/{5 MD, README, arc42-c4/*.html}` | **Completeness FINAL only** |

## Final Completeness = packager first

After join, Completeness MUST create these files on disk under ACTIVE_ROOT before any PASS:

1. `csa_pack/Executive_Summary.md`
2. `csa_pack/Business_Architecture.md`
3. `csa_pack/Application_Architecture.md`
4. `csa_pack/Data_and_Integration.md`
5. `csa_pack/Risks_Gaps_and_Traceability.md`
6. `csa_pack/README.md`
7. `csa_pack/arc42-c4/{index,context,containers,components}.html`

Then emit **`gate_id: gate-csa-document`**.  
If any required pack file is missing → **FAIL** (do not pass_with_warnings).

Map legacy schema content only (`csa-section-boundaries`). No workflow meta in pack.

## Manager FINAL brief (required)

When invoking Completeness after join, Manager brief MUST order:

```text
mode=FINAL
1) Validate accepted artifacts/*.json
2) RENDER lean csa_pack (all required paths)
3) Validate with gate-csa-document
4) Fail if any required pack file missing on disk
```

Do **not** brief Completeness as chat-only executive summary.

## Per-lane Completeness

| Lane | gate_id | artifact |
|------|---------|----------|
| Discover | gate-discover | artifacts/discovery.json |
| Domain | gate-business-domain | artifacts/domain.json |
| Tech | gate-tech-architecture | artifacts/architecture.json |
| Lineage | gate-data-lineage | artifacts/lineage.json |
| Integration | gate-integration | artifacts/integration.json |
