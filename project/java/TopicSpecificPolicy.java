package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A policy addressing a specific information security topic, supporting the overarching information security policy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TopicSpecificPolicy extends DocumentedInformation {

  private String topicArea;
  private InformationSecurityPolicy parentPolicy;
  private List<SecurityControl> applicableControls;
  private String targetAudience;

}