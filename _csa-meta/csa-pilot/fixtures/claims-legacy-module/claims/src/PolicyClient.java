package com.acme.claims;

/**
 * Synchronous SOAP-style client to Policy System (legacy Axis stub pattern).
 */
public class PolicyClient {
  private static final String ENDPOINT = "http://policy-internal/services/PolicyService";

  public void validatePolicy(String policyId) {
    // Placeholder for SOAP call to PolicyService
    if (policyId == null || policyId.length() == 0) {
      throw new IllegalArgumentException("policyId required");
    }
    System.out.println("SOAP validatePolicy " + policyId + " via " + ENDPOINT);
  }
}
