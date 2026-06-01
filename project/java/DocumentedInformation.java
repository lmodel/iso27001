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
  Abstract class for documented information per Clause 7.5. Captures metadata required for document control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class DocumentedInformation extends NamedEntity {

  private String documentType;
  private String documentReference;
  private String author;
  private String owner;
  private String approvedBy;
  private LocalDate approvedDate;
  private LocalDate effectiveDate;
  private LocalDate reviewDate;
  private String status;
  private String classification;
  private String retentionPeriod;
  private List<String> distributionControls;
  private String storageAndPreservation;
  private String changeControlMethod;
  private Boolean externalOrigin;
  private String externalOriginSource;


}