# CSA Orchestrator Pilot Runbook

## Goal

Validate Manager → specialist → Completeness Validator → re-run loop on **one module** before full-codebase runs.

## Fixture

Use sample module at [`fixtures/claims-legacy-module/`](fixtures/claims-legacy-module/).

## Steps

1. Import `workflow-CSA-Orchestrator-Swarm.json`.
2. Ensure platform can resolve skills from `skills/` (or upload skill packs named as in Manager `skills` array).
3. UI Inputs:
   - LegacyCodebase = complete dump (pilot: zip `skills/pilot/fixtures/claims-legacy-module` if required)
   - ConfirmProceed = `Yes`
4. Run Manager.
5. Observe:
   - `artifacts/execution_plan.json` created
   - Discover gated; if first Discover invents modern stack, Validator must **fail** and Manager re-runs
   - Swarm specialists each gated
   - `csa_pack/` Markdown sections + `arc42-c4/index.html` + Markdown `epic_story_seeds/` produced

## Success criteria (pilot)

| Criterion | Evidence |
|-----------|----------|
| ≥1 corrective re-run OR deliberate fail→pass on Discover | gate reports with attempt≥2 OR documented fail example exercised |
| All accepted artifacts schema-valid | no critical schema gaps |
| CSA pack MD sections 00,04–10 + arc42-c4 HTML index | filesystem |
| Functions/Epics/Stories present with CSA refs | `epic_story_seeds/*.md` |
| No Spring Boot invention on Java EE fixture | discovery.json frameworks |

## Tuned thresholds (v1 pilot)

See [`THRESHOLD_TUNING.md`](THRESHOLD_TUNING.md).

## Failure triage

| Symptom | Action |
|---------|--------|
| Manager skips Validator | Reinforce systemPrompt; check subagent invoke capability |
| Infinite re-runs | Enforce max_reruns=2 in Manager skill |
| Empty epic seeds | Check domain capabilities; Assembler epic-story-mapping |
| Token exhaustion mid-swarm | Narrow Discover `module_map` / Manager sequencing; avoid parallel fan-out |
