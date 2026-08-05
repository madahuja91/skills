---
name: SK-STORY
description: >-
  Generate Current State functional stories from capabilities, FRs, and rules
  using the enterprise CS template.
---

# SK-STORY — Current State Story Generation

## Inputs
- capabilities, requirements, rules
- Template version (default 1.0.0)

## Outputs
- `artifacts/cs/cs_stories.json` (array of stories per story.schema) — **required**
- `artifacts/cs/stories/*.md` — **required** one MD file per story (use enterprise CS template)

## Dual surface (mandatory)
Every story MUST be written as:
1. JSON entry in `cs_stories.json` (system of record)
2. Matching Markdown file for human / Jira review

Do not finish with JSON-only or MD-only.

## Required story fields
ID, Title, Business Objective, Description, Functional Requirements, Business Rules,
Assumptions/Dependencies, Acceptance Criteria (may be filled later by SK-AC),
Data & Integration, Edge Cases, Testing Scenarios (may be filled by SK-TEST),
Traceability, Definition of Done.

## Procedure
1. Map each must-priority FR set into cohesive stories
2. Assign `CS-STORY-###` IDs; keep one capability primary per story when possible
3. Embed FR/BR refs; leave AC/tests stubs only if SK-AC/SK-TEST will run next
4. No target-state redesign

## Must not
Add ADR/TSA/migration fields (those are Target State only).
