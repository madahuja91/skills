---
name: SK-PACKAGE
description: >-
  Assemble phase package manifests and a human backlog index without inventing
  story content. Makes deliverables visible in the run download.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-PACKAGE — Packaging + client backlog index

## Purpose
Produce the **first file a client opens**: a clean Functional Epic & Story index.
Users often see empty orchestrator UI output + skill noise in the tarball — this skill fixes discoverability.

## Outputs (all required when phase artifacts exist)
- `artifacts/package/cs_manifest.json` and/or `ts_manifest.json`
- `artifacts/package/final_manifest.json` (master only)
- **Client entry points (mandatory):**
  - CS: `artifacts/cs/00_BACKLOG_INDEX.md`
  - TS: `artifacts/ts/00_BACKLOG_INDEX.md`
  - Mirror: `artifacts/package/BACKLOG_INDEX.md`
  - Optional short exec blurb: `artifacts/cs/00_CLIENT_SUMMARY.md` (½ page: scope, epic count, how to read)

## `00_BACKLOG_INDEX.md` must include
1. One-paragraph **client purpose** (“Functional Current-State Epic/Story backlog for …”)
2. Counts: epics, stories, AC, tests, quality status, trace status
3. Table of epics → child stories (ID | Title | Why / outcome | FR count | path)
4. Relative paths to each `epics/<ID>/epic.md` and story MD
5. Where JSON SoR lives (`cs_epics.json`, `cs_stories.json`, gates, trace)
6. Banner: **Start here for client review / Jira mapping**
7. If Quality has block findings, list them at the top — do not hide failures

## Procedure
1. Collect existing artifact paths only (JSON + MD) — do not invent stories
2. Build manifest with template_version, skill versions, gate results, approvals
3. Fail packaging if stories exist as JSON without matching MD (or vice versa)
4. Fail packaging if `EPIC_MEGA_1TO1` / `STORY_OVERLOADED` block findings exist in quality gate (surface paths; do not rewrite)
5. Write `00_BACKLOG_INDEX.md` so a human opening the tarball finds the backlog in <30 seconds
6. Update swarm artifacts_index with package paths

## Must not
Invent missing stories to make the package look complete.
Rewrite story substance.
