---
name: SK-AC
description: >-
  Generate Given/When/Then acceptance criteria with Jira-quality clarity:
  concrete actors, inputs, actions, and observable outcomes — never circular FR echoes.
  mode=cs|ts.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# SK-AC — Acceptance Criteria (client / Jira-quality)

## Inputs
- story (or story set)
- related requirements + rules
- `mode`: cs | ts

## Outputs
- CS: `artifacts/cs/acceptance_criteria.json` **and** update AC **table** in each nested story MD
- TS: `artifacts/ts/acceptance_criteria.json` **and** update AC **table** in each nested story MD
- Keep JSON + Markdown in sync
- Also update story JSON `acceptance_criteria` arrays when present

AC Markdown columns: ID | Given | When | Then | Covers FR | Covers BR

## CLIENT DELIVERY STANDARD
AC must be paste-ready into a Jira Acceptance Criteria field:
- A BA/tester can execute without opening FR text
- Each Then names **what is seen/stored/returned** (message, field, status, record state)
- Prefer 3–7 AC per story (happy + key negatives); do not dump 15 vague criteria

## HARD quality bar (mandatory)

### Format
- Atomic Given / When / Then
- **Given** = concrete preconditions (role, data state, config)
- **When** = single user/system action with specific inputs where known
- **Then** = **observable outcome** (UI message, persisted fields, status code, rejected record, MQ message, etc.)

### Forbidden Then clauses (block)
- “the system performs the current-state behavior described by FR-00x”
- “behavior remains within linked acceptance-criteria scope”
- “Apply current-state validation as extracted”
- Restating the FR statement verbatim without an observable result

### Good Then examples
- “login succeeds and session contains GUID, roles, and post-login route”
- “create user is rejected with validation error when email is empty”
- “file > 52,428,800 bytes is rejected and is not sent to data transfer”

### Coverage
- Every must FR → ≥1 AC
- Every critical BR → ≥1 AC (often negative/edge)
- Prefer separate ACs for happy path vs validation failures

## Procedure
1. Read story What/How + FR/BR statements
2. Write concrete AC from observed behavior (use numbers/fields from BRs when present)
3. Link `covers_fr` / `covers_br`
4. Sync JSON pack + each story MD table + story JSON if applicable
5. Self-check: a tester can execute AC without opening FR text

## Must not
Change story scope; invent new FRs; ship circular AC.
