package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A single item to be monitored and measured per 9.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MonitoringItem  {

  private String metricName;
  private String metricDescription;
  private String measurementMethod;
  private String measurementFrequency;
  private String responsibleParty;
  private String analysisFrequency;
  private String analyst;
  private String targetThreshold;
  private String alertThreshold;
  private String currentValue;
  private String trend;

}