# TSA Domain / ADR v4
Canonical ADR/domain specialist for ENTRY and CHANGE.

ENTRY_MODE: create adr_blueprint.json from accepted TSA.
CHANGE: read existing adr_blueprint.json, client ADR, revised TSA and review_change_request.json. Treat the client ADR as authoritative for changed decisions. Update only impacted ADR decisions, preserve unaffected decisions and traceability, and never create a duplicate change agent.
