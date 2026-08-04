# Expected Pilot Outcomes (Claims Fixture)

Use as a checklist when reviewing Manager output on `fixtures/claims-legacy-module`.

## discovery.json

- frameworks include Java EE Servlet / Servlet 2.5 with evidence `WEB-INF/web.xml`
- MUST NOT list Spring Boot
- databases Oracle (or unknown with DDL evidence)
- module_map includes claims

## domain.json

- `DOM-claims`, `ENT-claim`, `BR-claim-status-transition`
- rule implementation_location → `ClaimService.java` / `updateStatus`

## architecture.json

- layers presentation + business + data
- components ClaimServlet, ClaimService, ClaimDao
- analysis_scope: `static`
- c4_views.containers: single WAR

## lineage.json

- source CLAIMS / CLAIM table
- lineage claimId → CLAIM_ID

## integration.json

- PolicyClient outbound SOAP/legacy sync

## csa_pack

- Markdown sections `00`, `04`–`10` present
- HTML site `arc42-c4/index.html` (+ context/containers/components)
- No C4 `.md` files
- epic_story_seeds as `functions.md` / `epics.md` / `stories.md` with CSA refs

## Quality gates

- At least one gate report per specialist under `artifacts/quality_gate_reports/`
- If an early Discover invents Spring Boot, expect fail + re-run before swarm
