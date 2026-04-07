package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The program for monitoring, measurement, analysis, and evaluation per Clause 9.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MonitoringProgram extends DocumentedInformation {

  private List<MonitoringItem> monitoringItems;

}