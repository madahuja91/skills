---
name: SK-TEST
description: >-
  Generate positive, negative, and integration test scenarios with executable
  steps and expected results tied to AC — not template boilerplate. mode=cs|ts.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# SK-TEST — Test Scenario Generation (client / QA-ready)

## Inputs
- stories + acceptance_criteria
- integrations from analysis when available
- `mode`: cs | ts

## Outputs
- CS: `artifacts/cs/test_scenarios.json` **and** update Testing Scenarios tables in nested story MD
- TS: `artifacts/ts/test_scenarios.json` **and** update nested story MD
- Sync story JSON `testing_scenarios` when present
- After writing tests, set related story DoD rows for testing to **done** (not pending)

Use separate tables: Positive / Negative / Integration  
Columns: ID | Preconditions/Systems | Steps | Expected | Covers AC

## CLIENT DELIVERY STANDARD
Scenarios must look like a QA engineer wrote them for a client UAT pack:
- Example data in steps (ids, roles, dates, sizes)
- Expected results filled (never empty)
- Positive / Negative correctly classified (do not put happy-path under Negative)
- Integration rows only when a real cross-system hop exists — not empty “—” placeholders pretending coverage

## HARD quality bar (mandatory)

### Steps
- Numbered, executable actions with **example data** when known (user, file name, size, field values)
- Name the entry point (screen/API/job) when known from story/evidence

### Expected
- Concrete observable results aligned to the AC Then clause
- Include error text/status when testing negative paths if known from BRs

### Forbidden (block)
- “Prepare valid current-state inputs for FR-00x”
- “Observe UI, service, database… through current CCDS behavior”
- “Observed current-state behavior remains within the linked acceptance-criteria scope”
- “Apply current-state validation, eligibility… as extracted”

### Coverage
1. Each AC → ≥1 scenario
2. Each story → ≥1 positive and ≥1 negative (when validations exist)
3. Integrations present → ≥1 integration scenario
4. TS mode: add migration-path scenarios when impact is Modified/New

## Procedure
1. Read AC Then outcomes; write scenarios that prove them
2. Prefer one scenario per distinct outcome (don’t merge happy + fail)
3. Update MD + JSON; mark DoD testing complete
4. Self-check: a QA engineer can run the scenario from the table alone

## Must not
Redefine requirements; ship boilerplate scenarios.
