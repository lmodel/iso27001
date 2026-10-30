package example;

/* metamodel_version: 1.12.0 */
/* version: 2022/Amd 1:2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsMonitoringItem  {

  private IsmsRole responsibleRole;
  private String monitoringMetric;
  private String monitoringDescription;
  private String monitoringMethod;
  private String monitoringFrequency;
  private String monitoringAnalysisFrequency;
  private String monitoringAnalyst;
  private String monitoringTarget;
  private String monitoringAlertThreshold;
  private String monitoringCurrentValue;
  private String monitoringTrend;


}