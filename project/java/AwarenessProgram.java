package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The awareness program ensuring personnel understand their information security responsibilities per Clause 7.3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AwarenessProgram extends DocumentedInformation {

  private List<String> awarenessTopics;
  private List<String> deliveryMethods;
  private String targetAudience;
  private String frequency;
  private String completionTracking;
  private String effectivenessMeasures;

}