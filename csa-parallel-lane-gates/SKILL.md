---
name: csa-parallel-lane-gates
description: HARD control loop for CSA swarm — per-lane Completeness with each specialist, cheap join checklist, thin Assembler packaging, final pack Completeness only. Use by Manager, Completeness Validator, and Document Assembler.
---

# CSA Parallel Lane Gates

## Schema

Contract: [`schema.json`](schema.json)

## HARD: Forbidden control patterns

Do **not**:

1. Wait for all parallel specialists to finish, then run Completeness in a batch (“Completeness only after join”).
2. Re-run a heavy Completeness LLM pass that only re-audits gates specialists already passed.
3. Use Assembler to re-analyze the codebase or invent new inventories.
4. Hard-fail final Completeness solely on Jaccard cosmetics or HTML `<table>` markup when substance schemas are met.

## Control loop (required)

```text
Bootstrap shared memory (blocking)
    → Discover
    → Completeness(gate-discover)   # lane gate; rework Discover only
    → Fan-out FOUR specialists IN PARALLEL:
         Domain | Tech | Lineage | Integration
         Each lane: specialist writes artifact + self gate report
                    Manager invokes Completeness for THAT lane as soon as it finishes
                    Fail → rework THAT lane only (peers keep running)
    → Join when all four artifacts are accepted (or escalated)
    → Join checklist ONLY (cheap): 4 accepted paths present in artifacts_index
         Do NOT run a full Completeness LLM “post-join” audit unless a lane lacks a gate report
    → Assembler (thin package — render only)
    → Completeness(gate-csa-document / final)  # pack contract + substance schemas
```

## Per-lane Completeness

| Lane finished | Invoke Completeness with |
|---------------|--------------------------|
| Discover | `gate-discover` + `artifacts/discovery.json` |
| Business Domain | `gate-business-domain` + `artifacts/domain.json` |
| Tech Architecture | `gate-tech-architecture` + `artifacts/architecture.json` |
| Data Lineage | `gate-data-lineage` + `artifacts/lineage.json` |
| Integration | `gate-integration` + `artifacts/integration.json` |

Manager must invoke Completeness **as each lane completes**, not after the slowest peer.

## Thin Assembler

Assembler:

1. Reads accepted `artifacts/*.json` + lane gate reports.
2. Writes `csa_pack/machine/sections/*.json` mapped from specialist fields (see `csa-section-boundaries`).
3. Renders the same 5 Markdown files + `README.md` + `arc42-c4/*.html`.
4. Does **not** re-scan source, invent SP/queue names, or expand scope beyond accepted artifacts.

## Final Completeness (pack only)

Validate:

- Lean 5-doc pack shape + machine section JSON schema conformance (including substance sections).
- SSOT / anti-duplication (`csa-section-boundaries`).
- Evidence preserved for SP/MQ when signals exist.

Prefer remediation of **missing substance fields** over cosmetic HTML/Jaccard-only blockers when schemas pass.

## Same document count

Never create extra client Markdown docs. Fold reference-quality sections into the existing five owners only.
