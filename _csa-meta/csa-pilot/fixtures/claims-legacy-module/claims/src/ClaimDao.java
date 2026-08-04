package com.acme.claims;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.naming.InitialContext;
import javax.sql.DataSource;

/** JDBC DAO against Oracle CLAIM table. */
public class ClaimDao {
  private Connection connection() throws Exception {
    DataSource ds = (DataSource) new InitialContext().lookup("java:comp/env/jdbc/ClaimsDB");
    return ds.getConnection();
  }

  public Claim findById(String claimId) {
    try (Connection c = connection();
         PreparedStatement ps = c.prepareStatement(
             "SELECT CLAIM_ID, POLICY_ID, STATUS FROM CLAIM WHERE CLAIM_ID = ?")) {
      ps.setLong(1, Long.parseLong(claimId));
      ResultSet rs = ps.executeQuery();
      if (!rs.next()) return null;
      Claim claim = new Claim();
      claim.setClaimId(String.valueOf(rs.getLong("CLAIM_ID")));
      claim.setPolicyId(rs.getString("POLICY_ID"));
      claim.setStatus(rs.getString("STATUS"));
      return claim;
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  public void save(Claim claim) {
    try (Connection c = connection();
         PreparedStatement ps = c.prepareStatement(
             "UPDATE CLAIM SET STATUS = ?, POLICY_ID = ? WHERE CLAIM_ID = ?")) {
      ps.setString(1, claim.getStatus());
      ps.setString(2, claim.getPolicyId());
      ps.setLong(3, Long.parseLong(claim.getClaimId()));
      ps.executeUpdate();
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }
}
