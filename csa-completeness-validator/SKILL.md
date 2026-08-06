---
name: csa-completeness-validator
description: Validates CSA specialist artifacts against JSON Schema and gate rubrics; emits pass/fail gate reports with remediation briefs. Use after every specialist run as Manager subagent.
---

# Completeness Validation Agent Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Role

Subagent invoked by CSA Architecture Manager **after every specialist** (and Assembler). Never invent architecture content; only evaluate.

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

## Deliverable format checks (document gates)

- Narrative CSA sections + epic seeds: **Markdown only**
- arc42/C4: **HTML only** under `csa_pack/arc42-c4/` — never C4 `.md`
- **Richness:** load `csa-rich-content` and **word-count** required files; stub packs fail `gate-csa-document` even if files exist

## Procedure

1. Run **active-root-hygiene** checks first.
2. Load agent skill schema + `quality-rubric.md` for the gate.
3. Validate JSON Schema; score `schema_conformance`.
4. Apply rubric metrics for evidence, completeness, confidence.
5. For specialist gates: apply `csa-rich-content` list-depth expectations (many evidenced rows with descriptions).
6. For `gate-csa-document` / epic readiness: measure word counts + tables + executive scorecard/risks; fail below floors.
7. Build `blocking_gaps` (critical/high that block acceptance) and `warnings`.
8. If fail: write `remediation_brief` using agent `remediation-hints.md` (include measured vs required words).
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
| gate-csa-document | csa_pack/ (MD + arc42-c4 HTML + required Mermaid) | agents/csa-document-assembler |
| gate-epic-story-readiness | epic_story_seeds/*.md | standards/epic-story-mapping |

## Rules

- Do not soft-pass invented stacks or missing evidence on critical claims.
- `max_reruns` is always 2 (Manager-enforced).
- Prefer concrete `files_to_revisit` over vague advice.

## Self quality bar

See `quality-rubric.md`.
