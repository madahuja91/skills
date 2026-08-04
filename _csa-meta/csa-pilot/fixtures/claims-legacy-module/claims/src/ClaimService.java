package com.acme.claims;

/**
 * Claim domain service — status workflow rules.
 */
public class ClaimService {
  private final ClaimDao dao = new ClaimDao();
  private final PolicyClient policyClient = new PolicyClient();

  public void updateStatus(String claimId, String newStatus) {
    Claim claim = dao.findById(claimId);
    if (claim == null) {
      throw new IllegalArgumentException("Claim not found");
    }
    String current = claim.getStatus();
    // BR-claim-status-transition
    if ("Submitted".equals(current) && "UnderReview".equals(newStatus)) {
      claim.setStatus(newStatus);
    } else if ("UnderReview".equals(current)
        && ("Approved".equals(newStatus) || "Rejected".equals(newStatus))) {
      if ("Approved".equals(newStatus)) {
        policyClient.validatePolicy(claim.getPolicyId());
      }
      claim.setStatus(newStatus);
    } else {
      throw new IllegalStateException("Invalid transition " + current + " -> " + newStatus);
    }
    dao.save(claim);
  }
}
