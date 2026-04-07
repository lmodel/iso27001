package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
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
  private boolean acknowledgmentRequired;
  private List<TopicSpecificPolicy> relatedTopicPolicies;

}