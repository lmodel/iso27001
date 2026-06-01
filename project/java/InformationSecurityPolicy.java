package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The information security policy established by top management per Clause 5.2. Provides framework for setting objectives and demonstrates commitment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationSecurityPolicy extends DocumentedInformation {

  private String policyStatement;
  private String policyObjectivesFramework;
  private List<String> commitmentStatements;
  private String applicabilityStatement;
  private LocalDate communicationDate;
  private Boolean acknowledgmentRequired;
  private LocalDate lastPolicyReviewDate;
  private LocalDate nextPolicyReviewDate;
  private List<TopicSpecificPolicy> relatedTopicPolicies;
  private List<String> integratedManagementSystems;


}