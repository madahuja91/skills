# Stories

## US-claim-status-transition — Preserve claim status transition rules
- Epic: EP-claim-intake-core
- Capability: CAP-claim-intake
- Narrative: As an adjuster, I need claim status transitions enforced as in legacy ClaimService
- Trace IDs: BR-claim-status-transition, CMP-claim-service
- Acceptance criteria hooks:
  - Submitted -> UnderReview allowed
  - Invalid transitions rejected with legacy-equivalent message
- CSA refs: `csa_pack/09_traceability_matrix.md`, BR-claim-status-transition
