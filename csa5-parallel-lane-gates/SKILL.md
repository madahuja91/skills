---
name: csa5-parallel-lane-gates
description: HARD CSA swarm control loop — per-lane Completeness, then Completeness renders src/csa_pack. Missing pack = FAIL. No Document Assembler.
---

# CSA Parallel Lane Gates

## Schema

Contract: [`schema.json`](schema.json)

## HARD: Forbidden

1. Completeness only after join when lanes can finish independently.
2. Invoking **CSA-Document-Assembler**.
3. Writing `deliverables/`, alternate Markdown filenames, or `csa_pack/machine/`.
4. Final that only validates JSON / chats a summary / invents `gate-final-*` without packing.
5. Manager success when required pack files are missing on disk.
6. Writing pack outside ACTIVE_ROOT (prefer `src/`).

## ACTIVE_ROOT + pack path

Bootstrap **`ACTIVE_ROOT=src`** (relative). Platform often allows new files **only under `src/`**.

Required client pack (all on disk):

- `src/csa_pack/Executive_Summary.md`
- `src/csa_pack/Business_Architecture.md`
- `src/csa_pack/Application_Architecture.md`
- `src/csa_pack/Data_and_Integration.md`
- `src/csa_pack/Risks_Gaps_and_Traceability.md`
- `src/csa_pack/README.md`
- `src/csa_pack/arc42-c4/{index,context,containers,components}.html`

Artifacts SSOT: `src/artifacts/*.json` (or `artifacts/*.json` only if already created there — prefer `src/artifacts/`).

## Control loop

```text
Bootstrap src/ + shared memory
  -> Discover -> Completeness(csa5-gate-discover)
  -> Fan-out Domain|Tech|Lineage|Integration; Completeness per lane
  -> Join
  -> Completeness(FINAL): RENDER src/csa_pack + csa5-gate-document
```

## Final Completeness = packager + schema judge

If all five specialist artifacts exist, Completeness runs **FINAL** even if Manager brief is vague.

FINAL MUST:

1. Validate each artifact against its agent schema; on gap → FAIL with `target_agent_id`
2. Render all required `src/csa_pack/` files (5 named MD + README + arc42 HTML; no invention)
3. Validate pack against `csa5-gate-document` + pack output-schemas
4. Emit **`gate_id: gate-csa-document`**
5. **FAIL** if any required pack file is missing (no soft pass)
6. On substance gaps → name owner agent so Manager re-runs that specialist (≤2)

No epic-story. No Document Assembler. Only the five lean MD filenames + README.

## Manager FINAL brief (copy this)

```text
mode=FINAL
ACTIVE_ROOT=src
1) Validate src/artifacts/{discovery,domain,architecture,lineage,integration}.json against agent schemas
2) RENDER lean pack under src/csa_pack/ (5 MD + README + arc42-c4 HTML)
3) Validate with csa5-gate-document + pack output-schemas
4) On schema gaps: FAIL with target_agent_id for Manager re-run
5) FAIL if any required pack file missing
Do not return chat-only executive summary. No epic-story. No Assembler.
```

## Per-lane gates

| Lane | gate_id | artifact |
|------|---------|----------|
| Discover | csa5-gate-discover | artifacts/discovery.json |
| Domain | csa5-gate-business-domain | artifacts/domain.json |
| Tech | csa5-gate-tech-architecture | artifacts/architecture.json |
| Lineage | csa5-gate-data-lineage | artifacts/lineage.json |
| Integration | csa5-gate-integration | artifacts/integration.json |
