# Reaction

!!! note "Schema class name"
    In the CoreMeta4Cat schema this class is named **`CatalyticReaction`** (not `Reaction`) to avoid name conflicts with identically named classes in top-level profiles such as chemdcat-ap. The simplified name **Reaction** is used throughout this documentation for readability. When writing data files or referencing the class programmatically, always use the full schema name `CatalyticReaction`.

The Reaction data class defines metadata required to document catalytic testing procedures, reactor configurations, operating conditions, and analytical methods. It provides structured descriptors necessary to contextualize catalytic performance data.

Core fields include reactor design type, operational parameters, and product identification and quantification methods. The class also specifies metadata required to report and evaluate catalyst performance metrics, enabling structured comparison across experimental studies.

<iframe
    src="../assets/metadata_reaction_hierarchy.html"
    width="100%"
    height= "470vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe><details markdown="1"><summary markdown="1"> **Legend** </summary>

- **Description:**A short description for Comprehension purposes

- **Data Type:** This specifies exactly what kind of information belongs in this field. Most simply, it could be a direct value, such as a number (float) or a piece of text (string). However, the Data Type can also point to another Class in the schema. When this happens, the field is not just a single value; it becomes a structured container. Designating a Class as the Data Type causes the field to contain a complete structured record, defined entirely by its own comprehensive collection of specific fields. Consequently, this allows for the systematic construction of complex data structures via organized, nested information layers within the broader schema architecture.

- **Cardinality:** This controls how many entries a specific data field must have. It defines if a field is required or optional, and whether it can accept a single value versus a list of multiple values.

- **CURIE:** A CURIE (Compact URI) is a short, easy-to-read reference that acts as a useful shortcut for a long, complex web address. Instead of seeing a full URL, you will see a two-part reference like gene:symbol, where the parts are separated by a colon. The first part is the prefix (a short code for the source website), and the second is the local identifier for the specific item. This structure is much easier to read and type, making the schema less cluttered and reducing errors. The full web link (URI) for the CURIE is always available if you click the provided link.

- **Schema Reference:** This link directs you to the complete, technical documentation for this part of the schema. This detailed view is generated automatically by LinkML's documentation tool and provides all underlying rules, data types, and complex relationships for expert users and developers.

- **Slots:** A Slot represents an individual data field or attribute that belongs to a specific Class (entity type) within the schema. If a Class defines an entity like 'Book', the Slots define the individual pieces of information about that book, such as the 'title', 'author', and 'ISBN'. Essentially, Slots are the essential building blocks that define the characteristics and permissible data for every record in the schema.

- **Enumerations:** Often called an Enum, Enumerations are a predefined, fixed list of permissible values that a Slot can accept. It is used to strictly limit the available choices for a data field to ensure consistency and prevent errors. For example, a 'Status' field might be restricted to the Enumeration list of only 'Active', 'Inactive', or 'Pending'. Any data entered that is not on this limited list is considered invalid by the schema.

</details>
## Slots

<details markdown="1" open>
<summary><strong>catalyst quantity</strong> (Recommended, Multivalued)</summary>

**Description:** Mass of catalyst loaded into the reactor.

**Data Type:** Mass

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`coremeta4cat:catalyst_quantity`](https://w3id.org/nfdi4cat/coremeta4cat/catalyst_quantity)

**Schema Reference:** [catalyst_quantity](./elements/slots/catalyst_quantity.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Mass">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [Mass](./elements/classes/Mass.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Mass target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of Mass:**

<details markdown="1" id="schema-class-MolarMass">
<summary><strong>MolarMass</strong></summary>

**Description:** A Mass (physical quality) that quantifies the mass of a homogeneous ChemicalSubstance containing 6.02 x 10^23 atoms or molecules.

**CURIE:** [`AFR:0002409`](http://purl.allotrope.org/ontologies/result#AFR_0002409)

**Schema Reference:** [MolarMass](./elements/classes/MolarMass.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolarMass target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_quantity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>catalyst type</strong> (Recommended, Multivalued)</summary>

**Description:** The catalytic regime of the reaction (e.g. heterogeneous, homogeneous,
biocatalysis, electrocatalysis, photocatalysis). For the physical
form/presentation of the catalyst itself, use catalyst_form instead.

Deliberately kept `recommended` rather than `required` (see nfdi4cat/
CoreMeta4Cat#117): classification here can be genuinely disputed or
not yet covered by CatalysisResearchFieldEnum for a novel catalyst,
and forcing a value would push researchers into a premature or
contested classification rather than leaving the field unset until
consensus/vocabulary catches up. Open for discussion in a follow-up
issue if a different tradeoff is wanted. See also nfdi4cat/
CoreMeta4Cat#116 on whether this two-slot design (catalyst_type +
catalyst_form) or PR #118's CatalystType class hierarchy should be
the long-term mechanism -- kept as two enums here because the
VOC4CAT terms show CatalystType conflates the regime axis
(Heterogeneous/Homogeneous/Bio/Electro/Photo) with the physical-form
axis (ThinFilm/Bulk/Powdered/DepositedSample/Supported -- identical
VOC4CAT ids to catalyst_form's permissible values), which are
independent and often both apply to the same catalyst at once.

**Data Type:** CatalysisResearchFieldEnum

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`VOC4CAT:0007014`](https://w3id.org/nfdi4cat/voc4cat_0007014)

**Schema Reference:** [catalyst_type](./elements/slots/catalyst_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>catalyst form</strong> (Recommended, Multivalued)</summary>

**Description:** The physical form or presentation of the catalyst as loaded into the
reactor (e.g. thin film, bulk, powder, supported). A separate axis
from catalyst_type (the catalytic regime).

**Data Type:** CatalystFormEnum

**Cardinality:**  Recommended, Multivalued

**Schema Reference:** [catalyst_form](./elements/slots/catalyst_form.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_form target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>reaction name</strong> (Recommended)</summary>

**Description:** A name for the catalytic reaction which assigns the reactants and
(desired) products (e.g. "ammonia synthesis", "Fischer-Tropsch synthesis").

**Data Type:** string

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0007009`](https://w3id.org/nfdi4cat/voc4cat_0007009)

**Schema Reference:** [reaction_name](./elements/slots/reaction_name.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reaction_name target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>reactor temperature range</strong> (Optional, Multivalued)</summary>

**Description:** Temperature range in the reactor during the reaction, provided as a
QuantitativeRange with min_value and max_value (unit_code: "Cel").
For a single set-point, set min_value equal to max_value.

**Data Type:** QuantitativeRange

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007032`](https://w3id.org/nfdi4cat/voc4cat_0007032)

**Schema Reference:** [reactor_temperature_range](./elements/slots/reactor_temperature_range.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-QuantitativeRange">
<summary><strong>QuantitativeRange</strong></summary>

**Description:** A quantitative property expressed as a range between a lower and upper bound,
sharing a common unit. Used where an experiment operates over a range of
conditions (e.g. a temperature sweep, a feed concentration window).

Aligned to qudt:Quantity (as in the DCAT-AP-PLUS QuantitativeAttribute pattern)
but with min_value / max_value instead of a single value to represent an
interval rather than a point value. Provide the shared unit as a QUDT DefinedTerm.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [QuantitativeRange](./elements/classes/QuantitativeRange.md)

**Slots**

<details markdown="1">
<summary><strong>title</strong> (Optional)</summary>

**Description:** No description available

**Data Type:** string

**Cardinality:**  Optional

**Schema Reference:** [title](./elements/slots/title.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20title target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>description</strong> (Optional)</summary>

**Description:** No description available

**Data Type:** string

**Cardinality:**  Optional

**Schema Reference:** [description](./elements/slots/description.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20description target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20QuantitativeRange target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_temperature_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** Atmosphere

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007809`](https://w3id.org/nfdi4cat/voc4cat_0007809)

**Schema Reference:** [has_atmosphere](./elements/slots/has_atmosphere.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Atmosphere">
<summary><strong>Atmosphere</strong></summary>

**Description:** A qualitative descriptor of the gaseous environment or atmospheric
conditions during a process (e.g. "air", "N2", "5% H2/Ar").

**CURIE:** [`coremeta4cat:Atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/Atmosphere)

**Schema Reference:** [Atmosphere](./elements/classes/Atmosphere.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Atmosphere target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of Atmosphere:**

<details markdown="1" id="schema-class-CalcinationGaseousEnvironment">
<summary><strong>CalcinationGaseousEnvironment</strong></summary>

**Description:** The specific gaseous environment maintained during a calcination step
(e.g. "air", "N2", "10% O2/N2").

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [CalcinationGaseousEnvironment](./elements/classes/CalcinationGaseousEnvironment.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CalcinationGaseousEnvironment target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>experiment pressure</strong> (Optional, Multivalued)</summary>

**Description:** Total pressure in the reactor during the experiment.

**Data Type:** Pressure

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000118`](https://w3id.org/nfdi4cat/voc4cat_0000118)

**Schema Reference:** [experiment_pressure](./elements/slots/experiment_pressure.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Pressure">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [Pressure](./elements/classes/Pressure.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Pressure target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>feed composition range</strong> (Optional, Multivalued)</summary>

**Description:** Feed composition range studied, provided as a QuantitativeRange.
Express concentration bounds in an appropriate unit (e.g. "mol/L", "%" for
vol% or mol%). For fixed-composition experiments use reactant.has_concentration.

**Data Type:** QuantitativeRange

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:feed_composition_range`](https://w3id.org/nfdi4cat/coremeta4cat/feed_composition_range)

**Schema Reference:** [feed_composition_range](./elements/slots/feed_composition_range.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>QuantitativeRange</strong></summary>

**Description:** A quantitative property expressed as a range between a lower and upper bound,
sharing a common unit. Used where an experiment operates over a range of
conditions (e.g. a temperature sweep, a feed concentration window).

Aligned to qudt:Quantity (as in the DCAT-AP-PLUS QuantitativeAttribute pattern)
but with min_value / max_value instead of a single value to represent an
interval rather than a point value. Provide the shared unit as a QUDT DefinedTerm.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-QuantitativeRange) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20feed_composition_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has experiment duration</strong> (Optional)</summary>

**Description:** Total duration of the experiment or measurement run.

**Data Type:** Duration

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_experiment_duration](./elements/slots/has_experiment_duration.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Duration">
<summary><strong>Duration</strong></summary>

**Description:** A quantitative measure of elapsed time (duration of a process step).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [Duration](./elements/classes/Duration.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Duration target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_experiment_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>product identification method</strong> (Mandatory, Multivalued)</summary>

**Description:** The analytical method used to identify and/or quantify reaction products.
Should reference a CharacterizationTechnique instance (e.g. GCMS, HPLC_MS).
The abstract stub ProductIdentificationMethod is retained for backward compatibility.

**Data Type:** ProductIdentificationMethod

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:product_identification_method`](https://w3id.org/nfdi4cat/coremeta4cat/product_identification_method)

**Schema Reference:** [product_identification_method](./elements/slots/product_identification_method.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-ProductIdentificationMethod">
<summary><strong>ProductIdentificationMethod</strong></summary>

**Description:** Abstract Plan representing the method used to identify and quantify reaction
products. In practice, users should reference a concrete CharacterizationTechnique
subclass from coremeta4cat_characterization_ap (e.g. GCMS, HPLC_MS, NMRSpectroscopy).

This abstract class is retained for backward compatibility with the original
CoreMeta4Cat monolith. It is a subclass of CatalysisPlan (which is itself a Plan,
prov:Plan / OBI:0000272) so that it can participate in the realized_plan slot,
and so it (and every other CoreMeta4Cat protocol/technique class) can carry a
persistent id.

**CURIE:** [`OBI:0000272`](http://purl.obolibrary.org/obo/OBI_0000272)

**Schema Reference:** [ProductIdentificationMethod](./elements/classes/ProductIdentificationMethod.md)

**Slots**

<details markdown="1">
<summary><strong>id</strong> (Optional)</summary>

**Description:** No description available

**Data Type:** string

**Cardinality:**  Optional

**Schema Reference:** [id](./elements/slots/id.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20id target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ProductIdentificationMethod target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20product_identification_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>used starting material</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the StartingMaterial(s) of a ChemicalReaction.

**Data Type:** StartingMaterial

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RO:0004009`](http://purl.obolibrary.org/obo/RO_0004009)

**Schema Reference:** [used_starting_material](./elements/slots/used_starting_material.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-StartingMaterial">
<summary><strong>StartingMaterial</strong></summary>

**Description:** A ChemicalSubstance with that has a starting material role in a synthesis.

**CURIE:** [`PROCO:0000029`](http://purl.obolibrary.org/obo/PROCO_0000029)

**Schema Reference:** [StartingMaterial](./elements/classes/StartingMaterial.md)

**Slots**

<details markdown="1">
<summary><strong>has molar equivalent</strong> (Optional)</summary>

**Description:** A slot to provide the MolarEquivalent of a ChemicalSubstance, such as the DissolvingSubstance, Starting Material or Reactant, within the context of a chemical reaction.

**Data Type:** MolarEquivalent

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_molar_equivalent](./elements/slots/has_molar_equivalent.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-MolarEquivalent">
<summary><strong>MolarEquivalent</strong></summary>

**Description:** A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a reference substance in a chemical reaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [MolarEquivalent](./elements/classes/MolarEquivalent.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolarEquivalent target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_molar_equivalent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-Temperature">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [Temperature](./elements/classes/Temperature.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Temperature target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-Volume">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [Volume](./elements/classes/Volume.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Volume target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-Density">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

**Schema Reference:** [Density](./elements/classes/Density.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Density target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has concentration</strong> (Optional)</summary>

**Description:** The slot to provide the Concentration of a ChemicalSubstance.

**Data Type:** Concentration

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_concentration](./elements/slots/has_concentration.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-Concentration">
<summary><strong>Concentration</strong></summary>

**Description:** A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume of the mixture.

**CURIE:** [`CHMO:0002820`](http://purl.obolibrary.org/obo/CHMO_0002820)

**Schema Reference:** [Concentration](./elements/classes/Concentration.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Concentration target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has ph value</strong> (Optional)</summary>

**Description:** The slot to provide the PHValue of a ChemicalSubstance.

**Data Type:** PHValue

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_ph_value](./elements/slots/has_ph_value.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-PHValue">
<summary><strong>PHValue</strong></summary>

**Description:** No description available

**CURIE:** [`SIO:001089`](http://semanticscience.org/resource/SIO_001089)

**Schema Reference:** [PHValue](./elements/classes/PHValue.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PHValue target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_ph_value target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>composed of</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to provide the chemical entities of which a ChemicalSubstance is composed of.

**Data Type:** ChemicalEntity

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [composed_of](./elements/slots/composed_of.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-ChemicalEntity">
<summary><strong>ChemicalEntity</strong></summary>

**Description:** Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

**CURIE:** [`CHEBI:23367`](http://purl.obolibrary.org/obo/CHEBI_23367)

**Schema Reference:** [ChemicalEntity](./elements/classes/ChemicalEntity.md)

**Slots**

<details markdown="1">
<summary><strong>inchi</strong> (Recommended)</summary>

**Description:** The slot to provide the InChi descriptor of a ChemicalEntity.

**Data Type:** InChi

**Cardinality:**  Recommended

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [inchi](./elements/slots/inchi.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-InChi">
<summary><strong>InChi</strong></summary>

**Description:** A structure descriptor which conforms to the InChI format specification.

**CURIE:** [`CHEMINF:000113`](http://semanticscience.org/resource/CHEMINF_000113)

**Schema Reference:** [InChi](./elements/classes/InChi.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20InChi target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inchi target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>inchikey</strong> (Recommended)</summary>

**Description:** The slot to provide the InChiKey of a ChemicalEntity.

**Data Type:** InChIKey

**Cardinality:**  Recommended

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [inchikey](./elements/slots/inchikey.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-InChIKey">
<summary><strong>InChIKey</strong></summary>

**Description:** No description available

**CURIE:** [`CHEMINF:000059`](http://semanticscience.org/resource/CHEMINF_000059)

**Schema Reference:** [InChIKey](./elements/classes/InChIKey.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20InChIKey target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inchikey target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>smiles</strong> (Recommended)</summary>

**Description:** The slot to provide the canonical SMILES descriptor of a ChemicalEntity.

**Data Type:** SMILES

**Cardinality:**  Recommended

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [smiles](./elements/slots/smiles.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-SMILES">
<summary><strong>SMILES</strong></summary>

**Description:** A structure descriptor that denotes a molecular structure as a graph and conforms to the SMILES format specification.

**CURIE:** [`CHEMINF:000018`](http://semanticscience.org/resource/CHEMINF_000018)

**Schema Reference:** [SMILES](./elements/classes/SMILES.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SMILES target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smiles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>molecular formula</strong> (Recommended)</summary>

**Description:** The slot to provide the IUPAC formula of a ChemicalEntity.

**Data Type:** MolecularFormula

**Cardinality:**  Recommended

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [molecular_formula](./elements/slots/molecular_formula.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-MolecularFormula">
<summary><strong>MolecularFormula</strong></summary>

**Description:** A structure descriptor which identifies each constituent element by its chemical symbol and indicates the number of atoms of each element found in each discrete molecule of that compound.

**CURIE:** [`CHEMINF:000042`](http://semanticscience.org/resource/CHEMINF_000042)

**Schema Reference:** [MolecularFormula](./elements/classes/MolecularFormula.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolecularFormula target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20molecular_formula target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>iupac name</strong> (Recommended)</summary>

**Description:** The slot to provide the IUPAC name of a ChemicalEntity.

**Data Type:** IUPACName

**Cardinality:**  Recommended

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [iupac_name](./elements/slots/iupac_name.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-IUPACName">
<summary><strong>IUPACName</strong></summary>

**Description:** A systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out by the International Union of Pure and Applied Chemistry (IUPAC).

**CURIE:** [`CHEMINF:000107`](http://semanticscience.org/resource/CHEMINF_000107)

**Schema Reference:** [IUPACName](./elements/classes/IUPACName.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20IUPACName target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20iupac_name target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has molar mass</strong> (Recommended)</summary>

**Description:** The slot to provide the MolarMass of a ChemicalEntity.

**Data Type:** MolarMass

**Cardinality:**  Recommended

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_molar_mass](./elements/slots/has_molar_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>MolarMass</strong></summary>

**Description:** A Mass (physical quality) that quantifies the mass of a homogeneous ChemicalSubstance containing 6.02 x 10^23 atoms or molecules.

**CURIE:** [`AFR:0002409`](http://purl.allotrope.org/ontologies/result#AFR_0002409)

*Full field list already shown [earlier on this page](#schema-class-MolarMass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_molar_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ChemicalEntity target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20composed_of target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has amount</strong> (Optional)</summary>

**Description:** The slot to provide the AmountConcentration of a ChemicalSubstance.

**Data Type:** AmountOfSubstance

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_amount](./elements/slots/has_amount.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-AmountOfSubstance">
<summary><strong>AmountOfSubstance</strong></summary>

**Description:** The total amount of substance used in a ChemicalReaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [AmountOfSubstance](./elements/classes/AmountOfSubstance.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AmountOfSubstance target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_amount target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20StartingMaterial target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_starting_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>used reactant</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the Reagent(s) of a ChemicalReaction.

**Data Type:** Reagent

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RO:0004009`](http://purl.obolibrary.org/obo/RO_0004009)

**Schema Reference:** [used_reactant](./elements/slots/used_reactant.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Reagent">
<summary><strong>Reagent</strong></summary>

**Description:** A ChemicalSubstance that is consumed or transformed in a ChemicalReaction.

**CURIE:** [`SIO:010411`](http://semanticscience.org/resource/SIO_010411)

**Schema Reference:** [Reagent](./elements/classes/Reagent.md)

**Slots**

<details markdown="1">
<summary><strong>has molar equivalent</strong> (Optional)</summary>

**Description:** A slot to provide the MolarEquivalent of a ChemicalSubstance, such as the DissolvingSubstance, Starting Material or Reactant, within the context of a chemical reaction.

**Data Type:** MolarEquivalent

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_molar_equivalent](./elements/slots/has_molar_equivalent.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>MolarEquivalent</strong></summary>

**Description:** A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a reference substance in a chemical reaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-MolarEquivalent) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_molar_equivalent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has concentration</strong> (Optional)</summary>

**Description:** The slot to provide the Concentration of a ChemicalSubstance.

**Data Type:** Concentration

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_concentration](./elements/slots/has_concentration.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Concentration</strong></summary>

**Description:** A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume of the mixture.

**CURIE:** [`CHMO:0002820`](http://purl.obolibrary.org/obo/CHMO_0002820)

*Full field list already shown [earlier on this page](#schema-class-Concentration) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has ph value</strong> (Optional)</summary>

**Description:** The slot to provide the PHValue of a ChemicalSubstance.

**Data Type:** PHValue

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_ph_value](./elements/slots/has_ph_value.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>PHValue</strong></summary>

**Description:** No description available

**CURIE:** [`SIO:001089`](http://semanticscience.org/resource/SIO_001089)

*Full field list already shown [earlier on this page](#schema-class-PHValue) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_ph_value target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>composed of</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to provide the chemical entities of which a ChemicalSubstance is composed of.

**Data Type:** ChemicalEntity

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [composed_of](./elements/slots/composed_of.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ChemicalEntity</strong></summary>

**Description:** Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

**CURIE:** [`CHEBI:23367`](http://purl.obolibrary.org/obo/CHEBI_23367)

*Full field list already shown [earlier on this page](#schema-class-ChemicalEntity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20composed_of target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has amount</strong> (Optional)</summary>

**Description:** The slot to provide the AmountConcentration of a ChemicalSubstance.

**Data Type:** AmountOfSubstance

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_amount](./elements/slots/has_amount.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>AmountOfSubstance</strong></summary>

**Description:** The total amount of substance used in a ChemicalReaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-AmountOfSubstance) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_amount target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Reagent target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_reactant target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>generated product</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the Product(s) of a ChemicalReaction.

**Data Type:** ChemicalProduct

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RO:0004008`](http://purl.obolibrary.org/obo/RO_0004008)

**Schema Reference:** [generated_product](./elements/slots/generated_product.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-ChemicalProduct">
<summary><strong>ChemicalProduct</strong></summary>

**Description:** A chemical substance that is produced by a ChemicalReaction.

**CURIE:** [`NCIT:C48810`](http://purl.obolibrary.org/obo/NCIT_C48810)

**Schema Reference:** [ChemicalProduct](./elements/classes/ChemicalProduct.md)

**Slots**

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has concentration</strong> (Optional)</summary>

**Description:** The slot to provide the Concentration of a ChemicalSubstance.

**Data Type:** Concentration

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_concentration](./elements/slots/has_concentration.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Concentration</strong></summary>

**Description:** A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume of the mixture.

**CURIE:** [`CHMO:0002820`](http://purl.obolibrary.org/obo/CHMO_0002820)

*Full field list already shown [earlier on this page](#schema-class-Concentration) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has ph value</strong> (Optional)</summary>

**Description:** The slot to provide the PHValue of a ChemicalSubstance.

**Data Type:** PHValue

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_ph_value](./elements/slots/has_ph_value.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>PHValue</strong></summary>

**Description:** No description available

**CURIE:** [`SIO:001089`](http://semanticscience.org/resource/SIO_001089)

*Full field list already shown [earlier on this page](#schema-class-PHValue) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_ph_value target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>composed of</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to provide the chemical entities of which a ChemicalSubstance is composed of.

**Data Type:** ChemicalEntity

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [composed_of](./elements/slots/composed_of.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ChemicalEntity</strong></summary>

**Description:** Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

**CURIE:** [`CHEBI:23367`](http://purl.obolibrary.org/obo/CHEBI_23367)

*Full field list already shown [earlier on this page](#schema-class-ChemicalEntity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20composed_of target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has amount</strong> (Optional)</summary>

**Description:** The slot to provide the AmountConcentration of a ChemicalSubstance.

**Data Type:** AmountOfSubstance

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_amount](./elements/slots/has_amount.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>AmountOfSubstance</strong></summary>

**Description:** The total amount of substance used in a ChemicalReaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-AmountOfSubstance) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_amount target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ChemicalProduct target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20generated_product target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>used catalyst</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the Catalyst of a ChemicalReaction.

**Data Type:** Catalyst

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RXNO:0000425`](http://purl.obolibrary.org/obo/RXNO_0000425)

**Schema Reference:** [used_catalyst](./elements/slots/used_catalyst.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Catalyst">
<summary><strong>Catalyst</strong></summary>

**Description:** A ChemicalSubstance or MaterialEntity that initiates or accelerates a ChemicalReaction without itself being affected.

**CURIE:** [`SIO:010344`](http://semanticscience.org/resource/SIO_010344)

**Schema Reference:** [Catalyst](./elements/classes/Catalyst.md)

**Slots**

<details markdown="1">
<summary><strong>has molar equivalent</strong> (Optional)</summary>

**Description:** A slot to provide the MolarEquivalent of a ChemicalSubstance, such as the DissolvingSubstance, Starting Material or Reactant, within the context of a chemical reaction.

**Data Type:** MolarEquivalent

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_molar_equivalent](./elements/slots/has_molar_equivalent.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>MolarEquivalent</strong></summary>

**Description:** A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a reference substance in a chemical reaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-MolarEquivalent) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_molar_equivalent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has concentration</strong> (Optional)</summary>

**Description:** The slot to provide the Concentration of a ChemicalSubstance.

**Data Type:** Concentration

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_concentration](./elements/slots/has_concentration.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Concentration</strong></summary>

**Description:** A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume of the mixture.

**CURIE:** [`CHMO:0002820`](http://purl.obolibrary.org/obo/CHMO_0002820)

*Full field list already shown [earlier on this page](#schema-class-Concentration) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has ph value</strong> (Optional)</summary>

**Description:** The slot to provide the PHValue of a ChemicalSubstance.

**Data Type:** PHValue

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_ph_value](./elements/slots/has_ph_value.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>PHValue</strong></summary>

**Description:** No description available

**CURIE:** [`SIO:001089`](http://semanticscience.org/resource/SIO_001089)

*Full field list already shown [earlier on this page](#schema-class-PHValue) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_ph_value target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>composed of</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to provide the chemical entities of which a ChemicalSubstance is composed of.

**Data Type:** ChemicalEntity

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [composed_of](./elements/slots/composed_of.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ChemicalEntity</strong></summary>

**Description:** Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

**CURIE:** [`CHEBI:23367`](http://purl.obolibrary.org/obo/CHEBI_23367)

*Full field list already shown [earlier on this page](#schema-class-ChemicalEntity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20composed_of target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has amount</strong> (Optional)</summary>

**Description:** The slot to provide the AmountConcentration of a ChemicalSubstance.

**Data Type:** AmountOfSubstance

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_amount](./elements/slots/has_amount.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>AmountOfSubstance</strong></summary>

**Description:** The total amount of substance used in a ChemicalReaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-AmountOfSubstance) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_amount target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Catalyst target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_catalyst target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>used solvent</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the chemical substance that had a solvent role (CHEBI:35223) in a ChemicalReaction.

**Data Type:** DissolvingSubstance

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`prov:wasAssociatedWith`](http://www.w3.org/ns/prov#wasAssociatedWith)

**Schema Reference:** [used_solvent](./elements/slots/used_solvent.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-DissolvingSubstance">
<summary><strong>DissolvingSubstance</strong></summary>

**Description:** A liquid ChemicalSubstance that dissolves or that is capable of dissolving a ChemicalSubstance.

**CURIE:** [`SIO:010417`](http://semanticscience.org/resource/SIO_010417)

**Schema Reference:** [DissolvingSubstance](./elements/classes/DissolvingSubstance.md)

**Slots**

<details markdown="1">
<summary><strong>has percentage of total</strong> (Optional)</summary>

**Description:** A slot to specify the percentage of a specific ChemicalSubstance in relation to the total amount of that same substance used across a multi-step reaction.

**Data Type:** PercentageOfTotal

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_percentage_of_total](./elements/slots/has_percentage_of_total.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-PercentageOfTotal">
<summary><strong>PercentageOfTotal</strong></summary>

**Description:** A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a reference substance in a chemical reaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [PercentageOfTotal](./elements/classes/PercentageOfTotal.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PercentageOfTotal target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_percentage_of_total target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has concentration</strong> (Optional)</summary>

**Description:** The slot to provide the Concentration of a ChemicalSubstance.

**Data Type:** Concentration

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_concentration](./elements/slots/has_concentration.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Concentration</strong></summary>

**Description:** A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume of the mixture.

**CURIE:** [`CHMO:0002820`](http://purl.obolibrary.org/obo/CHMO_0002820)

*Full field list already shown [earlier on this page](#schema-class-Concentration) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has ph value</strong> (Optional)</summary>

**Description:** The slot to provide the PHValue of a ChemicalSubstance.

**Data Type:** PHValue

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_ph_value](./elements/slots/has_ph_value.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>PHValue</strong></summary>

**Description:** No description available

**CURIE:** [`SIO:001089`](http://semanticscience.org/resource/SIO_001089)

*Full field list already shown [earlier on this page](#schema-class-PHValue) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_ph_value target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>composed of</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to provide the chemical entities of which a ChemicalSubstance is composed of.

**Data Type:** ChemicalEntity

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [composed_of](./elements/slots/composed_of.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ChemicalEntity</strong></summary>

**Description:** Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

**CURIE:** [`CHEBI:23367`](http://purl.obolibrary.org/obo/CHEBI_23367)

*Full field list already shown [earlier on this page](#schema-class-ChemicalEntity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20composed_of target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has amount</strong> (Optional)</summary>

**Description:** The slot to provide the AmountConcentration of a ChemicalSubstance.

**Data Type:** AmountOfSubstance

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_amount](./elements/slots/has_amount.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>AmountOfSubstance</strong></summary>

**Description:** The total amount of substance used in a ChemicalReaction.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-AmountOfSubstance) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_amount target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DissolvingSubstance target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_solvent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has duration</strong> (Optional)</summary>

**Description:** A slot to provide the duration of a ChemicalReaction.

**Data Type:** duration

**Cardinality:**  Optional

**CURIE:** [`schema:duration`](http://schema.org/duration)

**Schema Reference:** [has_duration](./elements/slots/has_duration.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>used reactor</strong> (Mandatory, Multivalued)</summary>

**Description:** The slot to specify the reactor used in a ChemicalReaction.

**Data Type:** Reactor

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`prov:wasAssociatedWith`](http://www.w3.org/ns/prov#wasAssociatedWith)

**Schema Reference:** [used_reactor](./elements/slots/used_reactor.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Reactor">
<summary><strong>Reactor</strong></summary>

**Description:** A reactor is a container for controlling a biological or chemical reaction or process.

**CURIE:** [`AFE:0000153`](http://purl.allotrope.org/ontologies/equipment#AFE_0000153)

**Schema Reference:** [Reactor](./elements/classes/Reactor.md)

**Slots**

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Reactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of Reactor:**

<details markdown="1" id="schema-class-ChemicalReactor">
<summary><strong>ChemicalReactor</strong></summary>

**Abstract Class**

**Description:** Abstract Reactor (chemdcat-ap) subclass representing a catalytic reactor
vessel.

Reactor is more specific than the general Device (AgenticEntity): it restricts
the used_reactor relation (is_a: carried_out_by) on Reaction to dedicated
reactor equipment. This semantic distinction separates analytical
instruments (Device) from reaction vessels (Reactor). ChemicalReactor
further specializes chemdcat-ap's generic Reactor for catalysis use cases.

Concrete subclasses (FixedBedReactor, CSTR, PlugFlowReactor, …) specify
reactor geometry and operating mode.
Linked from Reaction via used_reactor (restricted to range: ChemicalReactor).

**CURIE:** [`VOC4CAT:0007018`](https://w3id.org/nfdi4cat/voc4cat_0007018)

**Schema Reference:** [ChemicalReactor](./elements/classes/ChemicalReactor.md)

**Slots**

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ChemicalReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-ElectrochemicalReactor">
<summary><strong>ElectrochemicalReactor</strong></summary>

**Description:** Electrochemical reactor used in electrocatalytic experiments, including
H-cells, flow cells, and membrane electrode assemblies.

**CURIE:** [`VOC4CAT:0000193`](https://w3id.org/nfdi4cat/voc4cat_0000193)

**Schema Reference:** [ElectrochemicalReactor](./elements/classes/ElectrochemicalReactor.md)

**Slots**

<details markdown="1">
<summary><strong>has cathode</strong> (Recommended)</summary>

**Description:** The electrode where reduction occurs in an electrochemical cell. It is
the negative electrode in an electrolytic cell, while it is the
positive electrode in a galvanic cell.

**Data Type:** string

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0007254`](https://w3id.org/nfdi4cat/voc4cat_0007254)

**Schema Reference:** [has_cathode](./elements/slots/has_cathode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_cathode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has anode</strong> (Recommended)</summary>

**Description:** The electrode where oxidation occurs in an electrochemical cell. It is
the positive electrode in an electrolytic cell, while it is the
negative electrode in a galvanic cell.

**Data Type:** string

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0007255`](https://w3id.org/nfdi4cat/voc4cat_0007255)

**Schema Reference:** [has_anode](./elements/slots/has_anode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_anode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>cell operating mode</strong> (Recommended)</summary>

**Description:** The functional mode of an electrochemical cell based on the direction
of energy conversion.

**Data Type:** CellOperatingModeEnum

**Cardinality:**  Recommended

**CURIE:** [`coremeta4cat:cell_operating_mode`](https://w3id.org/nfdi4cat/coremeta4cat/cell_operating_mode)

**Schema Reference:** [cell_operating_mode](./elements/slots/cell_operating_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20cell_operating_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has active area</strong> (Optional)</summary>

**Description:** In contrast to substrate area, the actual area of a sample or
electrode which is active.

**Data Type:** Area

**Cardinality:**  Optional

**CURIE:** [`VOC4CAT:0007258`](https://w3id.org/nfdi4cat/voc4cat_0007258)

**Schema Reference:** [has_active_area](./elements/slots/has_active_area.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-Area">
<summary><strong>Area</strong></summary>

**Description:** A quantitative measure of surface area (e.g. active electrode area).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [Area](./elements/classes/Area.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Area target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_active_area target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>faradaic current</strong> (Recommended)</summary>

**Description:** The current that is flowing through an electrochemical cell and is
causing (or is caused by) chemical reactions.

**Data Type:** ElectricCurrent

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0007259`](https://w3id.org/nfdi4cat/voc4cat_0007259)

**Schema Reference:** [faradaic_current](./elements/slots/faradaic_current.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-ElectricCurrent">
<summary><strong>ElectricCurrent</strong></summary>

**Description:** A quantitative measure of electric current (e.g. faradaic current in an electrochemical cell).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [ElectricCurrent](./elements/classes/ElectricCurrent.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectricCurrent target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20faradaic_current target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectrochemicalReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-CSTR">
<summary><strong>CSTR</strong></summary>

**Description:** Continuous stirred tank reactor (CSTR) — a well-mixed, continuous-flow
reactor operating at steady state.

**CURIE:** [`VOC4CAT:0007019`](https://w3id.org/nfdi4cat/voc4cat_0007019)

**Schema Reference:** [CSTR](./elements/classes/CSTR.md)

**Slots**

<details markdown="1">
<summary><strong>stirring rate</strong> (Recommended)</summary>

**Description:** The rate at which the stirrer rotates, typically expressed in
revolutions per unit time (e.g. revolutions per minute).

**Data Type:** AngularVelocity

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0008114`](https://w3id.org/nfdi4cat/voc4cat_0008114)

**Schema Reference:** [stirring_rate](./elements/slots/stirring_rate.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-AngularVelocity">
<summary><strong>AngularVelocity</strong></summary>

**Description:** Rate of rotational motion, typically expressed in revolutions per minute.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [AngularVelocity](./elements/classes/AngularVelocity.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AngularVelocity target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>residence time</strong> (Recommended)</summary>

**Description:** The average time a unit of fluid spends inside the reactor before
exiting.

**Data Type:** Duration

**Cardinality:**  Recommended

**Schema Reference:** [residence_time](./elements/slots/residence_time.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Duration</strong></summary>

**Description:** A quantitative measure of elapsed time (duration of a process step).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Duration) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20residence_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactor working volume</strong> (Recommended)</summary>

**Description:** Volume of the reaction chamber, calculated by its dimensions. Volume
of pipes and valves connected to the reactor is not included.

**Data Type:** Volume

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0000153`](https://w3id.org/nfdi4cat/voc4cat_0000153)

**Schema Reference:** [reactor_working_volume](./elements/slots/reactor_working_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_working_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactor diameter</strong> (Optional)</summary>

**Description:** The internal diameter of the reactor vessel.

**Data Type:** LengthQuantity

**Cardinality:**  Optional

**Schema Reference:** [reactor_diameter](./elements/slots/reactor_diameter.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-LengthQuantity">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [LengthQuantity](./elements/classes/LengthQuantity.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20LengthQuantity target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_diameter target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirrer diameter</strong> (Optional)</summary>

**Description:** The effective diameter of the stirrer. Typically expressed as the
distance across the rotating blade or mixing head from one tip to
the opposite tip.

**Data Type:** LengthQuantity

**Cardinality:**  Optional

**CURIE:** [`VOC4CAT:0008115`](https://w3id.org/nfdi4cat/voc4cat_0008115)

**Schema Reference:** [stirrer_diameter](./elements/slots/stirrer_diameter.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirrer_diameter target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactor stirrer type</strong> (Optional)</summary>

**Description:** The category of mechanical or magnetic agitation device used in the
reactor, such as a magnetic stirrer or an overhead mechanical (steel
shaft) stirrer. Distinct from the synthesis-context stirrer_type slot
(coremeta4cat_synthesis_ap), since reactor and synthesis-vessel stirring
may use different equipment.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`VOC4CAT:0008113`](https://w3id.org/nfdi4cat/voc4cat_0008113)

**Schema Reference:** [reactor_stirrer_type](./elements/slots/reactor_stirrer_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_stirrer_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CSTR target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-PlugFlowReactor">
<summary><strong>PlugFlowReactor</strong></summary>

**Description:** Plug flow reactor (PFR) — a tubular reactor in which reactant composition
varies along the axis with no axial mixing.

**CURIE:** [`VOC4CAT:0007102`](https://w3id.org/nfdi4cat/voc4cat_0007102)

**Schema Reference:** [PlugFlowReactor](./elements/classes/PlugFlowReactor.md)

**Slots**

<details markdown="1">
<summary><strong>tube length</strong> (Recommended)</summary>

**Description:** The length of the tubular reaction chamber.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended

**Schema Reference:** [tube_length](./elements/slots/tube_length.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20tube_length target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>tube internal diameter</strong> (Recommended)</summary>

**Description:** The internal diameter of the tubular reaction chamber.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended

**Schema Reference:** [tube_internal_diameter](./elements/slots/tube_internal_diameter.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20tube_internal_diameter target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flow direction</strong> (Recommended)</summary>

**Description:** The direction of reactant flow through the tube (e.g. upflow,
downflow, horizontal).

**Data Type:** string

**Cardinality:**  Recommended

**Schema Reference:** [flow_direction](./elements/slots/flow_direction.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_direction target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of tubes</strong> (Recommended)</summary>

**Description:** The number of parallel tubes in the reactor.

**Data Type:** integer

**Cardinality:**  Recommended

**Schema Reference:** [number_of_tubes](./elements/slots/number_of_tubes.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_tubes target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>tube material</strong> (Recommended)</summary>

**Description:** Material used for the construction of the reactor tube(s).

**Data Type:** string

**Cardinality:**  Recommended

**Schema Reference:** [tube_material](./elements/slots/tube_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20tube_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst particle size</strong> (Recommended)</summary>

**Description:** A measure of the characteristic linear dimension of a particle in a
sample, typically reported as diameter or sieve fraction range.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0008212`](https://w3id.org/nfdi4cat/voc4cat_0008212)

**Schema Reference:** [catalyst_particle_size](./elements/slots/catalyst_particle_size.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_particle_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlugFlowReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-Autoclave">
<summary><strong>Autoclave</strong></summary>

**Description:** Autoclave reactor — a sealed pressure vessel for batch reactions at
elevated temperature and/or pressure.

**CURIE:** [`NCIT:C93052`](http://purl.obolibrary.org/obo/NCIT_C93052)

**Schema Reference:** [Autoclave](./elements/classes/Autoclave.md)

**Slots**

<details markdown="1">
<summary><strong>agitation type</strong> (Recommended)</summary>

**Description:** The category of agitation used inside the autoclave (e.g. magnetic
stirring, mechanical overhead stirring, rocking, none).

**Data Type:** string

**Cardinality:**  Recommended

**Schema Reference:** [agitation_type](./elements/slots/agitation_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20agitation_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reaction chamber material</strong> (Recommended)</summary>

**Description:** Material used for the construction of the inner reaction chamber
(the surface in direct contact with the reaction mixture). Distinct
from vessel_material, the material of the outer pressure vessel/shell.

**Data Type:** string

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0000156`](https://w3id.org/nfdi4cat/voc4cat_0000156)

**Schema Reference:** [reaction_chamber_material](./elements/slots/reaction_chamber_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reaction_chamber_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel internal volume</strong> (Recommended)</summary>

**Description:** The internal (working) volume of the autoclave vessel.

**Data Type:** Volume

**Cardinality:**  Recommended

**Schema Reference:** [vessel_internal_volume](./elements/slots/vessel_internal_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_internal_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel material</strong> (Recommended)</summary>

**Description:** Material used for the construction of the outer autoclave vessel/
pressure shell. Distinct from reaction_chamber_material, the material
of the inner reaction chamber lining.

**Data Type:** string

**Cardinality:**  Recommended

**Schema Reference:** [vessel_material](./elements/slots/vessel_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>batch duration</strong> (Recommended)</summary>

**Description:** The total duration of the batch reaction inside the autoclave, from
start to end of the reaction step.

**Data Type:** Duration

**Cardinality:**  Recommended

**Schema Reference:** [batch_duration](./elements/slots/batch_duration.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Duration</strong></summary>

**Description:** A quantitative measure of elapsed time (duration of a process step).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Duration) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20batch_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Autoclave target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-SlurryReactor">
<summary><strong>SlurryReactor</strong></summary>

**Description:** Slurry reactor — a three-phase reactor in which catalyst particles are
suspended in a liquid phase through which gas is bubbled.

**CURIE:** [`coremeta4cat:SlurryReactor`](https://w3id.org/nfdi4cat/coremeta4cat/SlurryReactor)

**Schema Reference:** [SlurryReactor](./elements/classes/SlurryReactor.md)

**Slots**

<details markdown="1">
<summary><strong>catalyst particle size</strong> (Recommended)</summary>

**Description:** A measure of the characteristic linear dimension of a particle in a
sample, typically reported as diameter or sieve fraction range.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0008212`](https://w3id.org/nfdi4cat/voc4cat_0008212)

**Schema Reference:** [catalyst_particle_size](./elements/slots/catalyst_particle_size.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_particle_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gas liquid ratio</strong> (Recommended)</summary>

**Description:** The volumetric ratio of gas to liquid phase in the slurry reactor.

**Data Type:** float

**Cardinality:**  Recommended

**Schema Reference:** [gas_liquid_ratio](./elements/slots/gas_liquid_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gas_liquid_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>agitation sparging rate</strong> (Recommended)</summary>

**Description:** The volumetric flow rate at which gas is sparged/bubbled through the
liquid phase, or the rate of mechanical agitation used to maintain
the slurry suspension.

**Data Type:** VolumeFlowRate

**Cardinality:**  Recommended

**Schema Reference:** [agitation_sparging_rate](./elements/slots/agitation_sparging_rate.md)

**Data Type Class Details:**

<details markdown="1" id="schema-class-VolumeFlowRate">
<summary><strong>VolumeFlowRate</strong></summary>

**Description:** Volume of fluid passing a given point per unit time.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

**Schema Reference:** [VolumeFlowRate](./elements/classes/VolumeFlowRate.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20VolumeFlowRate target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20agitation_sparging_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impeller type</strong> (Recommended)</summary>

**Description:** The category of impeller used to agitate and suspend the slurry
(e.g. Rushton turbine, pitched blade, anchor).

**Data Type:** string

**Cardinality:**  Recommended

**Schema Reference:** [impeller_type](./elements/slots/impeller_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impeller_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>agitation speed</strong> (Recommended)</summary>

**Description:** The rotational speed of the agitator/impeller, typically expressed
in revolutions per unit time.

**Data Type:** AngularVelocity

**Cardinality:**  Recommended

**Schema Reference:** [agitation_speed](./elements/slots/agitation_speed.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>AngularVelocity</strong></summary>

**Description:** Rate of rotational motion, typically expressed in revolutions per minute.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-AngularVelocity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20agitation_speed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SlurryReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-Microreactor">
<summary><strong>Microreactor</strong></summary>

**Description:** Microreactor — a miniaturised flow reactor with characteristic dimensions
in the sub-millimetre range, enabling precise thermal control and rapid
screening.

**CURIE:** [`VOC4CAT:0000234`](https://w3id.org/nfdi4cat/voc4cat_0000234)

**Schema Reference:** [Microreactor](./elements/classes/Microreactor.md)

**Slots**

<details markdown="1">
<summary><strong>channel material</strong> (Recommended)</summary>

**Description:** Material used for the construction of the microreactor channels.

**Data Type:** string

**Cardinality:**  Recommended

**Schema Reference:** [channel_material](./elements/slots/channel_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20channel_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>channel dimensions</strong> (Recommended, Multivalued)</summary>

**Description:** The characteristic dimensions (e.g. width, depth) of the microreactor
channels.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended, Multivalued

**Schema Reference:** [channel_dimensions](./elements/slots/channel_dimensions.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20channel_dimensions target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of channels</strong> (Recommended)</summary>

**Description:** The number of parallel channels in the microreactor.

**Data Type:** integer

**Cardinality:**  Recommended

**Schema Reference:** [number_of_channels](./elements/slots/number_of_channels.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_channels target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Microreactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-FixedBedReactor">
<summary><strong>FixedBedReactor</strong></summary>

**Description:** Fixed bed reactor — a tubular reactor packed with a stationary catalyst bed.
The most common reactor type in heterogeneous catalysis testing.

**CURIE:** [`coremeta4cat:FixedBedReactor`](https://w3id.org/nfdi4cat/coremeta4cat/FixedBedReactor)

**Schema Reference:** [FixedBedReactor](./elements/classes/FixedBedReactor.md)

**Slots**

<details markdown="1">
<summary><strong>catalyst particle size</strong> (Recommended)</summary>

**Description:** A measure of the characteristic linear dimension of a particle in a
sample, typically reported as diameter or sieve fraction range.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0008212`](https://w3id.org/nfdi4cat/voc4cat_0008212)

**Schema Reference:** [catalyst_particle_size](./elements/slots/catalyst_particle_size.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_particle_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst bed diameter</strong> (Recommended)</summary>

**Description:** The internal diameter of the packed catalyst bed section.

**Data Type:** LengthQuantity

**Cardinality:**  Recommended

**Schema Reference:** [catalyst_bed_diameter](./elements/slots/catalyst_bed_diameter.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_bed_diameter target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst bed volume</strong> (Recommended)</summary>

**Description:** The bulk volume taken up by the catalyst and potential diluent in a
fixed bed reactor.

**Data Type:** Volume

**Cardinality:**  Recommended

**CURIE:** [`VOC4CAT:0007021`](https://w3id.org/nfdi4cat/voc4cat_0007021)

**Schema Reference:** [catalyst_bed_volume](./elements/slots/catalyst_bed_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_bed_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst dilution material</strong> (Optional)</summary>

**Description:** An inert solid mixed with catalyst particles in a fixed bed to modify
bed properties (e.g. improve heat/mass transfer, dilute activity).

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`VOC4CAT:0008218`](https://w3id.org/nfdi4cat/voc4cat_0008218)

**Schema Reference:** [catalyst_dilution_material](./elements/slots/catalyst_dilution_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_dilution_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst bed height</strong> (Optional)</summary>

**Description:** The axial length of the packed catalyst section in a reactor,
measured along the direction of flow.

**Data Type:** LengthQuantity

**Cardinality:**  Optional

**CURIE:** [`VOC4CAT:0008217`](https://w3id.org/nfdi4cat/voc4cat_0008217)

**Schema Reference:** [catalyst_bed_height](./elements/slots/catalyst_bed_height.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>LengthQuantity</strong></summary>

**Description:** A quantitative measure of length or spatial dimension (nm, mm, cm).

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-LengthQuantity) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_bed_height target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FixedBedReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1" id="schema-class-FluidizedBedReactor">
<summary><strong>FluidizedBedReactor</strong></summary>

**Description:** Fluidized bed reactor — a reactor in which the catalyst particles are
suspended in an upward-flowing gas or liquid stream.

**CURIE:** [`coremeta4cat:FluidizedBedReactor`](https://w3id.org/nfdi4cat/coremeta4cat/FluidizedBedReactor)

**Schema Reference:** [FluidizedBedReactor](./elements/classes/FluidizedBedReactor.md)

**Slots**

<details markdown="1">
<summary><strong>gas distributor type</strong> (Optional, Multivalued)</summary>

**Description:** Type or design of the gas distributor plate in a fluidized bed reactor.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gas_distributor_type`](https://w3id.org/nfdi4cat/coremeta4cat/gas_distributor_type)

**Schema Reference:** [gas_distributor_type](./elements/slots/gas_distributor_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gas_distributor_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bed expansion height</strong> (Optional, Multivalued)</summary>

**Description:** Height of bed expansion above the settled bed height under operating conditions.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:bed_expansion_height`](https://w3id.org/nfdi4cat/coremeta4cat/bed_expansion_height)

**Schema Reference:** [bed_expansion_height](./elements/slots/bed_expansion_height.md)

**Unit:** cm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bed_expansion_height target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bubble size distribution</strong> (Optional)</summary>

**Description:** Description or characterization of bubble size distribution in the fluidized bed.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`coremeta4cat:bubble_size_distribution`](https://w3id.org/nfdi4cat/coremeta4cat/bubble_size_distribution)

**Schema Reference:** [bubble_size_distribution](./elements/slots/bubble_size_distribution.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bubble_size_distribution target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>alternative label</strong> (Optional)</summary>

**Description:** The slot to specify an alternative label, name or title for a MaterialEntity.

**Data Type:** string

**Cardinality:**  Optional

**CURIE:** [`skos:altLabel`](http://www.w3.org/2004/02/skos/core#altLabel)

**Schema Reference:** [alternative_label](./elements/slots/alternative_label.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20alternative_label target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has physical state</strong> (Optional)</summary>

**Description:** The slot to specify the physical state of a MaterialEntity.

**Data Type:** PhysicalStateEnum

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_physical_state](./elements/slots/has_physical_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_physical_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has mass</strong> (Optional)</summary>

**Description:** The slot to provide the Mass of a MaterialEntity.

**Data Type:** Mass

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_mass](./elements/slots/has_mass.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Mass</strong></summary>

**Description:** The strength of a body's gravitational attraction to other bodies.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Mass) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has volume</strong> (Optional)</summary>

**Description:** The slot to provide the Volume of a MaterialEntity.

**Data Type:** Volume

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_volume](./elements/slots/has_volume.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Volume</strong></summary>

**Description:** A measure of regions in three-dimensional space.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Volume) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has density</strong> (Optional)</summary>

**Description:** The slot to provide the Density of a MaterialEntity.

**Data Type:** Density

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_density](./elements/slots/has_density.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Density</strong></summary>

**Description:** A measure of the mass per unit volume of a substance.

**CURIE:** [`SIO:001406`](http://semanticscience.org/resource/SIO_001406)

*Full field list already shown [earlier on this page](#schema-class-Density) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_density target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FluidizedBedReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_reactor target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has yield</strong> (Optional)</summary>

**Description:** A slot to provide the percentage of how much of the ChemicalProduct was produced by a ChemicalReaction.

**Data Type:** Yield

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_yield](./elements/slots/has_yield.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-Yield">
<summary><strong>Yield</strong></summary>

**Description:** A dimensionless physical quantity describing the fraction of a product B that is formed from a reactant A taking into account the stoichiometry. If A fully reacts to B without side-reactions, the yield of product B is 1 (or 100 %).

**CURIE:** [`CHMO:0002855`](http://purl.obolibrary.org/obo/CHMO_0002855)

**Schema Reference:** [Yield](./elements/classes/Yield.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Yield target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_yield target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>has reaction step</strong> (Optional, Multivalued)</summary>

**Description:** A slot to specify a step (part) of a ChemicalReaction that is itself a ChemicalReaction.

**Data Type:** ChemicalReaction

**Cardinality:**  Optional, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [has_reaction_step](./elements/slots/has_reaction_step.md)

**Data Type Class Details:**

<details markdown="1" open id="schema-class-ChemicalReaction">
<summary><strong>ChemicalReaction</strong></summary>

**Description:** A process that leads to the transformation of one set of chemical substances to another and that is the subject matter of a DataGeneratingActivity.

**CURIE:** [`SIO:010345`](http://semanticscience.org/resource/SIO_010345)

**Schema Reference:** [ChemicalReaction](./elements/classes/ChemicalReaction.md)

**Slots**

<details markdown="1">
<summary><strong>used starting material</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the StartingMaterial(s) of a ChemicalReaction.

**Data Type:** StartingMaterial

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RO:0004009`](http://purl.obolibrary.org/obo/RO_0004009)

**Schema Reference:** [used_starting_material](./elements/slots/used_starting_material.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>StartingMaterial</strong></summary>

**Description:** A ChemicalSubstance with that has a starting material role in a synthesis.

**CURIE:** [`PROCO:0000029`](http://purl.obolibrary.org/obo/PROCO_0000029)

*Full field list already shown [earlier on this page](#schema-class-StartingMaterial) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_starting_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>used reactant</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the Reagent(s) of a ChemicalReaction.

**Data Type:** Reagent

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RO:0004009`](http://purl.obolibrary.org/obo/RO_0004009)

**Schema Reference:** [used_reactant](./elements/slots/used_reactant.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Reagent</strong></summary>

**Description:** A ChemicalSubstance that is consumed or transformed in a ChemicalReaction.

**CURIE:** [`SIO:010411`](http://semanticscience.org/resource/SIO_010411)

*Full field list already shown [earlier on this page](#schema-class-Reagent) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_reactant target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>generated product</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the Product(s) of a ChemicalReaction.

**Data Type:** ChemicalProduct

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RO:0004008`](http://purl.obolibrary.org/obo/RO_0004008)

**Schema Reference:** [generated_product](./elements/slots/generated_product.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ChemicalProduct</strong></summary>

**Description:** A chemical substance that is produced by a ChemicalReaction.

**CURIE:** [`NCIT:C48810`](http://purl.obolibrary.org/obo/NCIT_C48810)

*Full field list already shown [earlier on this page](#schema-class-ChemicalProduct) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20generated_product target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>used catalyst</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the Catalyst of a ChemicalReaction.

**Data Type:** Catalyst

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`RXNO:0000425`](http://purl.obolibrary.org/obo/RXNO_0000425)

**Schema Reference:** [used_catalyst](./elements/slots/used_catalyst.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Catalyst</strong></summary>

**Description:** A ChemicalSubstance or MaterialEntity that initiates or accelerates a ChemicalReaction without itself being affected.

**CURIE:** [`SIO:010344`](http://semanticscience.org/resource/SIO_010344)

*Full field list already shown [earlier on this page](#schema-class-Catalyst) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_catalyst target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>used solvent</strong> (Recommended, Multivalued)</summary>

**Description:** The slot to specify the chemical substance that had a solvent role (CHEBI:35223) in a ChemicalReaction.

**Data Type:** DissolvingSubstance

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`prov:wasAssociatedWith`](http://www.w3.org/ns/prov#wasAssociatedWith)

**Schema Reference:** [used_solvent](./elements/slots/used_solvent.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>DissolvingSubstance</strong></summary>

**Description:** A liquid ChemicalSubstance that dissolves or that is capable of dissolving a ChemicalSubstance.

**CURIE:** [`SIO:010417`](http://semanticscience.org/resource/SIO_010417)

*Full field list already shown [earlier on this page](#schema-class-DissolvingSubstance) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_solvent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has duration</strong> (Optional)</summary>

**Description:** A slot to provide the duration of a ChemicalReaction.

**Data Type:** duration

**Cardinality:**  Optional

**CURIE:** [`schema:duration`](http://schema.org/duration)

**Schema Reference:** [has_duration](./elements/slots/has_duration.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>used reactor</strong> (Optional)</summary>

**Description:** The slot to specify the reactor used in a ChemicalReaction.

**Data Type:** Reactor

**Cardinality:**  Optional

**CURIE:** [`prov:wasAssociatedWith`](http://www.w3.org/ns/prov#wasAssociatedWith)

**Schema Reference:** [used_reactor](./elements/slots/used_reactor.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Reactor</strong></summary>

**Description:** A reactor is a container for controlling a biological or chemical reaction or process.

**CURIE:** [`AFE:0000153`](http://purl.allotrope.org/ontologies/equipment#AFE_0000153)

*Full field list already shown [earlier on this page](#schema-class-Reactor) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20used_reactor target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has temperature</strong> (Optional)</summary>

**Description:** The slot to provide the Temperature of a MaterialEntity or an Activity, whereas the temperature of the Activity is ontologically rooted in the temperature of the material entities that participate in the Activity.

**Data Type:** Temperature

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_temperature](./elements/slots/has_temperature.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Temperature</strong></summary>

**Description:** A physical quantity that quantitatively expresses the attribute of hotness or coldness.

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Temperature) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has pressure</strong> (Optional)</summary>

**Description:** The slot to provide data about the pressure of a MaterialEntity or an Activity, whereas the Pressure of an Activity is ontologically a quality borne by the material entities participating in the Activity.

**Data Type:** Pressure

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_pressure](./elements/slots/has_pressure.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Pressure</strong></summary>

**Description:** No description available

**CURIE:** [`qudt:Quantity`](http://qudt.org/schema/qudt/Quantity)

*Full field list already shown [earlier on this page](#schema-class-Pressure) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has yield</strong> (Optional)</summary>

**Description:** A slot to provide the percentage of how much of the ChemicalProduct was produced by a ChemicalReaction.

**Data Type:** Yield

**Cardinality:**  Optional

**CURIE:** [`SIO:000008`](http://semanticscience.org/resource/SIO_000008)

**Schema Reference:** [has_yield](./elements/slots/has_yield.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>Yield</strong></summary>

**Description:** A dimensionless physical quantity describing the fraction of a product B that is formed from a reactant A taking into account the stoichiometry. If A fully reacts to B without side-reactions, the yield of product B is 1 (or 100 %).

**CURIE:** [`CHMO:0002855`](http://purl.obolibrary.org/obo/CHMO_0002855)

*Full field list already shown [earlier on this page](#schema-class-Yield) -- this class is reached from multiple fields.*

</details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_yield target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>has reaction step</strong> (Optional, Multivalued)</summary>

**Description:** A slot to specify a step (part) of a ChemicalReaction that is itself a ChemicalReaction.

**Data Type:** ChemicalReaction

**Cardinality:**  Optional, Multivalued

**CURIE:** [`BFO:0000051`](http://purl.obolibrary.org/obo/BFO_0000051)

**Schema Reference:** [has_reaction_step](./elements/slots/has_reaction_step.md)

**Data Type Class Details:**

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_reaction_step target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>related resource</strong> (Optional, Multivalued)</summary>

**Description:** No description available

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**Schema Reference:** [related_resource](./elements/slots/related_resource.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20related_resource target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ChemicalReaction target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20has_reaction_step target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>related resource</strong> (Optional)</summary>

**Description:** No description available

**Data Type:** string

**Cardinality:**  Optional

**Schema Reference:** [related_resource](./elements/slots/related_resource.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20related_resource target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

