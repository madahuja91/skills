# Threshold Tuning (Pilot v1)

Defaults after plan + fixture validation intent:

| Gate | Metric | Threshold | Notes |
|------|--------|-----------|-------|
| discover | classification coverage | 90% | On tiny fixtures, compute over listed files only |
| discover | evidence non-inferred on stack | 70% | Critical |
| discover | parallel swarm unlock confidence | ≥60 overall | Manager policy |
| business_domain | critical rules located or flagged | 100% | Critical |
| tech_architecture | layers | ≥3 or monolith justification | WAR fixture uses 3 |
| data_lineage | primary entity path coverage | 80% | CLAIM table is primary |
| integration | I/O classified | 100% of discovered | SOAP client in fixture |
| epic-story-readiness | function→epic | 100% | Critical |
| max_reruns | all agents | 2 | Hard stop then escalate |

## Legacy heuristic emphasis (tuned)

For Java EE WAR fixtures, Completeness Validator should **fail** Discover if:

- `frameworks` contains Spring Boot / Quarkus / Micronaut without matching build evidence
- `web.xml` present but frameworks empty and no unknown+search evidence

## Next tuning after real codebase

- Adjust evidence % if only binaries available
- Allow table-level lineage default for schemas &gt; 200 tables
- Module batching size for Manager scoping
