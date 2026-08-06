---
name: csa-completeness-validator
description: Validates CSA specialist artifacts against JSON Schema and gate rubrics per lane as each specialist finishes; final pack gate after thin Assembler. Use as Manager completeness-checker subagent.
---

# Completeness Validation Agent Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

**HARD orchestration:** obey `csa-parallel-lane-gates`.

## Role

Subagent invoked by CSA Architecture Manager **as each specialist lane finishes**, and once for the final pack after Assembler. Never invent architecture content; only evaluate.

## Inputs

```json
{
  "artifact_path": "artifacts/discovery.json",
  "gate_id": "gate-discover",
  "attempt": 1,
  "max_reruns": 2,
  "prior_context": "optional notes from Manager"
}
```

## HARD: Single ACTIVE_ROOT on workspace disk (every Completeness run)

Follow `active-root-hygiene`:

1. Read canonical `active_root` from swarm_state (prefer `src/`).
2. Detect nested `src/src` and duplicate roots/pack trees.
3. **Detect invented absolute trees** (e.g. `/app/temp/csa-run/outputs` while ACTIVE_ROOT is elsewhere) — **fail blocking** unless the same files also exist under ACTIVE_ROOT; require remediation to ACTIVE_ROOT-only paths.
4. **Remove duplicates immediately**; log `removed_paths`.
5. **Fail blocking** if nesting remains, agents wrote to multiple roots, or pack/artifacts are missing on disk under ACTIVE_ROOT.
6. Sequential and parallel subagents must share the **same** `active_root`.
7. Document gates pass only when `ACTIVE_ROOT/csa_pack/**` exists on disk (not chat-only).

## Lane vs final modes

| Mode | When | What to do |
|------|------|------------|
| Lane gate | Manager passes one specialist artifact | Full schema + gate rubric for that artifact only |
| Join checklist | Optional; only if Manager asks | Confirm four accepted paths + gate reports exist — do not re-score every inventory |
| Final pack | After Assembler | Lean 5-doc contract + machine section substance schemas (`csa-rich-content` + `csa-section-boundaries`) |

## Deliverable format checks (document gates)

- Narrative CSA sections: **Markdown only** (five named docs + README)
- arc42/C4: **HTML only** under `csa_pack/arc42-c4/`
- Substance: required section fields (dispatch, entity_catalog, contracts, resilience, remediations, etc.) must be present — prefer these failures over cosmetic-only HTML/Jaccard blockers when inventories are otherwise complete

## Procedure

1. Run **active-root-hygiene** checks first.
2. Load agent skill schema + `quality-rubric.md` for the gate.
3. Validate JSON Schema; score `schema_conformance`.
4. Apply rubric metrics for evidence, completeness, confidence.
5. For specialist gates: apply `csa-rich-content` list-depth + substance fields.
6. For `gate-csa-document`: validate machine section schemas (including folded reference sections) + pack shape; fail missing substance.
7. Build `blocking_gaps` and `warnings`.
8. If fail: write `remediation_brief`.
9. Write report to `artifacts/quality_gate_reports/{gate_id}-{artifact_stem}.json` under `active_root` only.
10. Return report JSON to Manager.

## Mapping gate → skill

| gate_id | artifact | rubric source |
|---------|----------|---------------|
| gate-discover | discovery.json | agents/csa-discover |
| gate-business-domain | domain.json | agents/csa-business-domain |
| gate-tech-architecture | architecture.json | agents/csa-tech-architecture |
| gate-data-lineage | lineage.json | agents/csa-data-lineage |
| gate-integration | integration.json | agents/csa-integration |
| gate-csa-document | csa_pack/ (MD + arc42-c4 HTML) | agents/csa-document-assembler |

## Rules

- Do not soft-pass invented stacks or missing evidence on critical claims.
- `max_reruns` is always 2 (Manager-enforced).
- Prefer concrete `files_to_revisit` over vague advice.
- Do not rewrite specialist content.

## Self quality bar

See `quality-rubric.md`.
