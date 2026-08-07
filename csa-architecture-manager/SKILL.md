---
name: csa-architecture-manager
description: CSA Manager — bootstrap src/, per-lane Completeness, schema-gap re-runs of owner specialists, FINAL lean 5-doc pack. No epic-story. No Document Assembler.
---

# CSA Architecture Manager

## Schema

[`schema.json`](schema.json)

## Identity

Orchestrator. Admit work; do not author specialist leaf JSON. **No Document Assembler.** **No epic-story readiness.**

## HARD — load skills (do not restate)

- `csa-swarm-shared-memory`
- `csa-parallel-lane-gates`
- `active-root-hygiene`
- `csa-section-boundaries` / `csa-rich-content`

## HARD — skills freshness (before any specialist work)

Platform may copy skills **from user cache** (`Skills cache summary: N cache hits, 0 fresh installs`). That is **stale-risk**. Manager has no platform API to force “fresh installs,” but **must** refresh disk copies and verify lean pack contracts before Discover.

### Trigger (any of these)

- Log/message contains `0 fresh installs` or `from user cache` for pack-driving skills
- `.agents/skills/csa-pack-schemas/SKILL.md` is missing
- Any loaded pack skill still does **not** name the five lean MD files (`Executive_Summary.md`, `Business_Architecture.md`, `Application_Architecture.md`, `Data_and_Integration.md`, `Risks_Gaps_and_Traceability.md`)

### Required action (command_line, before Discover)

1. Fetch pinned skills from GitHub into `.agents/skills/` (overwrite):

```bash
PIN=ed3b91e12c284c15aaa4a59b80a017c411934714
TMP=$(mktemp -d)
git clone --depth 1 https://github.com/madahuja91/skills.git "$TMP/skills" || exit 1
cd "$TMP/skills" && git fetch --depth 1 origin "$PIN" && git checkout "$PIN"
mkdir -p .agents/skills
for s in csa-pack-schemas csa-completeness-validator csa-architecture-manager \
  csa-parallel-lane-gates csa-section-boundaries csa-rich-content \
  gate-csa-document mermaid-diagrams arc42-c4-views; do
  rm -rf ".agents/skills/$s"
  cp -a "$TMP/skills/$s" ".agents/skills/$s"
done
test -f .agents/skills/csa-pack-schemas/SKILL.md
grep -q Executive_Summary.md .agents/skills/csa-pack-schemas/SKILL.md
```

(Adjust paths if workspace root differs; PowerShell: equivalent `Remove-Item`/`Copy-Item`/`git`.)

2. After refresh, load pack rules via **skill tool / read_file** from `.agents/skills/csa-pack-schemas/` (and related skills above) — prefer those files over any earlier cached summary in context.
3. Tell every sub-agent brief: **use refreshed `.agents/skills/...` contracts; lean five MD filenames only.**
4. If clone/copy/verify fails → **STOP**. Write `src/_internal/swarm/SKILLS_STALE.md` with the failure and ask the human to clear the platform user skills cache. Do **not** start Discover/FINAL on unverified skills.

**Limitation:** this cannot change the platform’s “0 fresh installs” counter; it only replaces on-disk skill files the agents can re-read. If the harness never re-reads disk, human cache clear is still required.

## Control loop

```text
Bootstrap src/ + shared memory
  -> Discover -> Completeness(lane)
     on fail: re-run Discover (≤2) with remediation_brief
  -> Fan-out Domain | Tech | Lineage | Integration
     Completeness(lane) per finished lane
     on fail: re-run THAT owner specialist (≤2) to fill schema gaps
  -> Join (all lanes accepted or escalated)
  -> Completeness(FINAL): render src/csa_pack + gate-csa-document
     on fail naming target_agent_id: re-run that specialist, then FINAL again
     on pack-only fail: re-run Completeness FINAL (≤2)
```

## Schema-gap remediation (HARD)

When Completeness returns `fail` / `rerun_recommended`:

1. Read `target_agent_id` + `remediation_brief.schema_fields_missing` + `blocking_gaps`.
2. Re-invoke **only that owner specialist** with the remediation brief (do not switch specialties).
3. Re-invoke Completeness for that lane (or FINAL after join).
4. Cap at `max_reruns = 2` per owner.
5. Never mark done on chat-only summaries.

Owner map: discover | business_domain | tech_architecture | data_lineage | integration.

## Required client pack (done criteria)

On disk under `src/csa_pack/`:

1. `Executive_Summary.md`
2. `Business_Architecture.md`
3. `Application_Architecture.md`
4. `Data_and_Integration.md`
5. `Risks_Gaps_and_Traceability.md`
6. `README.md`
7. `arc42-c4/{index,context,containers,components}.html`

Plus `src/artifacts/{discovery,domain,architecture,lineage,integration}.json`.

Forbidden: alternate Markdown pack names, `epic_story_seeds/`, `deliverables/`, `csa_pack/machine/`.

## Manager FINAL brief (copy exactly)

```text
mode=FINAL
ACTIVE_ROOT=src
1) Validate src/artifacts/{discovery,domain,architecture,lineage,integration}.json against agent schemas
2) RENDER lean pack: 5 MD + README + arc42-c4 HTML under src/csa_pack/
3) Validate with gate-csa-document + pack output-schemas
4) On schema gaps: FAIL with target_agent_id so Manager re-runs that specialist
5) FAIL if any required pack file missing
Do not return chat-only executive summary. No epic-story. No Assembler.
```

## HARD — done

Not done until specialist JSON + full lean `src/csa_pack/` exist on disk and Completeness FINAL passed (or escalated after max re-runs).
