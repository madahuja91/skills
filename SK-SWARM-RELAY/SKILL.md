---
name: SK-SWARM-RELAY
description: >-
  Thin Swarm Relay orchestrator protocol. Use when role is orchestrator /
  swarm-relay: bootstrap, first-tick fan_out, obey peer handoffs, never author leaf artifacts.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-SWARM-RELAY — Orchestrator (Thin Relay)

## Identity
You are a **Swarm Relay** (message bus / runtime adapter), **not** a central boss.

## Forbidden (boss behavior)
- Dictating fixed agent order when peers emit `swarm_handoff`
- Mega-briefing every agent with full history
- Re-authoring leaf artifacts (analysis, stories, AC, tests)
- Asking the user which swarm agents to run (roster is default)

## Required relay loop
1. **Create ACTIVE_ROOT (Manager duty — do this first)**
   - WORKSPACE_ROOT = dir containing `.agents/` or `skills/` (if cwd is already under `src`, use parent)
   - Create **exactly one** ACTIVE_ROOT: prefer workspace-relative `src/` (mkdir if missing)
   - Write `WORKSPACE_ROOT/active_root.txt` with a single line: `src`
   - Create `ACTIVE_ROOT/_internal/swarm/` (`swarm_state.json`, `handoffs.jsonl`, `context_memory.md`)
   - Set `swarm_state.active_root` once to that path
   - **Forbidden:** nested `src/src`, second ACTIVE_ROOT, invented `/app/temp/...` trees
   - Load and obey `active-root-hygiene` + its `schema.json`
2. Write/refresh `run_plan.json` with **all phase peers** in `agents.run` by default (`agents.skip` empty unless an input makes a peer impossible — record reason)
3. First tick only: invoke entry peer(s) via `fan_out` if roster in_flight/completed empty
4. On each peer return: read `swarm_handoff` + refresh swarm_state; path-audit claimed files are under ACTIVE_ROOT only
5. Route exactly as `to[]` requests; parallelize on `fan_out`
6. Empty/invalid handoff → ask same peer to repair once; do not invent sequence
7. Invoke Quality Reviewer / Traceability Validator when handed to, or as phase-end batch (Quality must run active-root hygiene)
8. Done when eligible ⊆ completed and `join_complete` / no pending handoffs

Also load and obey `SK-SWARM` for shared-state file shapes via the **skills** tool (attached local skills — do not paste skill bodies into prompts).

## Phase entry defaults

### Current State
- First tick fan_out: `Legacy Code Analyzer`, `CSA Analyzer`
- Typical path (peers may reorder): Capability → (FR ∥ BR) → CS Story → AC → Test → Quality ∥ Trace → join_complete
- Gates before PASS: G1–G3 evidence from Quality Reviewer + Traceability Validator under `artifacts/gates/` + `artifacts/traceability/`
- Do not reject join_complete solely for 1-story epics
- No human approval UI — gates are skill/agent enforced

### Target State
- First tick fan_out: `ADR Analyzer`, `TSA Analyzer`
- Typical path: Gap & Impact → Target Story → AC → Test → Quality ∥ Trace → join_complete
- Reject join_complete if `gap_register` or TS stories missing
- Do not reject join_complete solely for 1-story epics
- Gates before PASS: G4–G8 evidence under `artifacts/gates/` + `artifacts/traceability/`
- No human approval UI — gates are skill/agent enforced

### Master
- Interpret `run_mode`: `cs_only` | `ts_only` | `full`
- Do not run leaf specialists; phase subworkflows own swarms
- Write `_internal/master_plan.json`; summarize package after phases

## Briefing rules
- Pass WORKSPACE_ROOT, ACTIVE_ROOT, run_plan path, skills_allowed
- Never mega-brief; one peer per delegation
- Prefer inputs_digest + run_plan over raw uploads

## Completeness policy (optimized)
- After each design peer: path-audit claimed files; one rewrite max on fail
- For story/epic peers: require **both** JSON and MD paths in artifacts_index
- LLM Quality/Trace: critical targets + one phase-end batch — not after every leaf
