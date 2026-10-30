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
  A resource provided for the ISMS, such as people, time, tools or budget.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsResource extends IsmsRecord {

  private String resourceCategory;
  private String resourceQuantity;
  private LocalDate resourceAllocationDate;
  private String resourceAllocatedTo;
  private String resourceCost;
  private String resourceAvailability;


}