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
  An item in the inventory of information and other associated assets: what it is, who owns and looks after it, where it is, how it is classified and how much it matters.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsAsset  {

  private List<IsmsControl> relevantControls;
  private String assetCategory;
  private String assetOwner;
  private String assetCustodian;
  private String assetClassification;
  private String assetLocation;
  private String assetCriticality;
  private URI ismsId;
  private String title;
  private String description;


}