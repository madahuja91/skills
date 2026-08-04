package com.acme.claims;

public class Claim {
  private String claimId;
  private String policyId;
  private String status;

  public String getClaimId() { return claimId; }
  public void setClaimId(String claimId) { this.claimId = claimId; }
  public String getPolicyId() { return policyId; }
  public void setPolicyId(String policyId) { this.policyId = policyId; }
  public String getStatus() { return status; }
  public void setStatus(String status) { this.status = status; }
}
