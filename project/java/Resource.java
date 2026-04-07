package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A resource provided for the ISMS per Clause 7.1, including personnel, infrastructure, technology, and budget.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Resource extends NamedEntity {

  private String resourceType;
  private String quantity;
  private LocalDate allocationDate;
  private String allocatedTo;
  private String cost;
  private String availabilityStatus;

}