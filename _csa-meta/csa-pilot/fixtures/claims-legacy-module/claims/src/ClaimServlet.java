package com.acme.claims;

import java.io.IOException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/** HTTP entry for claim intake (Java EE Servlet 2.5). */
public class ClaimServlet extends HttpServlet {
  private final ClaimService claimService = new ClaimService();

  @Override
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    String claimId = req.getParameter("claimId");
    String status = req.getParameter("status");
    claimService.updateStatus(claimId, status);
    resp.getWriter().write("OK");
  }
}
