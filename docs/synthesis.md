# Synthesis

The Synthesis data class captures metadata required to document catalyst preparation procedures in a structured and reproducible manner. It defines the minimum information necessary to describe synthesis routes and their relevant parameters.

Metadata are organized hierarchically based on the selected synthesis method. Method-specific child fields are activated depending on the preparation approach (e.g., co-precipitation requiring fields such as precipitating agent, synthesis pH, aging time, and aging temperature). In addition, method-independent fields—such as precursor identity, precursor quantity, and storage conditions—are included to ensure consistent documentation across synthesis strategies.


**CURIE:** [`OBI:0000070`](OBI:0000070)

<iframe
    src="/CoreMeta4Cat/assets/metadata_synthesis_hierarchy.html"
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
<summary><strong>nominal composition</strong> (Mandatory, Multivalued)</summary>

**Description:** Nominal elemental or chemical composition of the catalyst (e.g. 5wt% Pt/Al2O3).

**Data Type:** string

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:nominal_composition`](https://w3id.org/nfdi4cat/coremeta4cat/nominal_composition)

**Schema Reference:** [nominal_composition](./elements/slots/nominal_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nominal_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>catalyst measured properties</strong> (Mandatory, Multivalued)</summary>

**Description:** Key measured properties of the resulting catalyst
(e.g. BET surface area, sieve fraction, molar ratio).

**Data Type:** string

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:catalyst_measured_properties`](https://w3id.org/nfdi4cat/coremeta4cat/catalyst_measured_properties)

**Schema Reference:** [catalyst_measured_properties](./elements/slots/catalyst_measured_properties.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_measured_properties target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>storage conditions</strong> (Recommended, Multivalued)</summary>

**Description:** Conditions under which the catalyst is stored (e.g. inert atmosphere, 4°C).

**Data Type:** string

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`coremeta4cat:storage_conditions`](https://w3id.org/nfdi4cat/coremeta4cat/storage_conditions)

**Schema Reference:** [storage_conditions](./elements/slots/storage_conditions.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20storage_conditions target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>support</strong> (Optional, Multivalued)</summary>

**Description:** Support material on which the active phase is deposited (e.g. Al2O3, SiO2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:support`](https://w3id.org/nfdi4cat/coremeta4cat/support)

**Schema Reference:** [support](./elements/slots/support.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20support target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used in a process or sample preparation.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent](./elements/slots/solvent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>sample pretreatment</strong> (Optional, Multivalued)</summary>

**Description:** Pre-treatment applied to the sample before a process or measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000122`](https://w3id.org/nfdi4cat/voc4cat_0000122)

**Schema Reference:** [sample_pretreatment](./elements/slots/sample_pretreatment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_pretreatment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>had input entity</strong> (Mandatory, Multivalued)</summary>

**Description:** The Precursor(s) consumed during this Synthesis.

**Data Type:** Precursor

**Cardinality:**  Mandatory, Multivalued

**Schema Reference:** [had_input_entity](./elements/slots/had_input_entity.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>Precursor</strong></summary>

**Description:** A MaterialSample that serves as input material in a catalyst Synthesis.
Precursors are consumed or transformed during the preparation process.

**CURIE:** [`CHEBI:52717`](http://purl.obolibrary.org/obo/CHEBI_52717)

**Schema Reference:** [Precursor](./elements/classes/Precursor.md)

**Slots**

<details markdown="1">
<summary><strong>precursor quantity</strong> (Mandatory, Multivalued)</summary>

**Description:** Quantity of precursor used in synthesis.

**Data Type:** float

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:precursor_quantity`](https://w3id.org/nfdi4cat/coremeta4cat/precursor_quantity)

**Schema Reference:** [precursor_quantity](./elements/slots/precursor_quantity.md)

**Unit:** g

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precursor_quantity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Precursor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20had_input_entity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>had output entity</strong> (Recommended, Multivalued)</summary>

**Description:** The CatalystSample produced by this Synthesis.

**Data Type:** CatalystSample

**Cardinality:**  Recommended, Multivalued

**Schema Reference:** [had_output_entity](./elements/slots/had_output_entity.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>CatalystSample</strong></summary>

**Description:** A MaterialSample that is the product of a catalyst Synthesis.
The specific type of catalyst (e.g. heterogeneous, supported metal)
is expressed via rdf_type using a voc4cat term.

**CURIE:** [`OBI:0000747`](http://purl.obolibrary.org/obo/OBI_0000747)

**Schema Reference:** [CatalystSample](./elements/classes/CatalystSample.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CatalystSample target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20had_output_entity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>realized plan</strong> (Mandatory)</summary>

**Description:** The PreparationMethod (protocol) realized in this Synthesis.

**Data Type:** PreparationMethod

**Cardinality:**  Mandatory

**Schema Reference:** [realized_plan](./elements/slots/realized_plan.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>PreparationMethod</strong></summary>

**Abstract Class**

**Description:** An abstract Plan describing the protocol used to prepare a catalyst.
Concrete subclasses (Impregnation, CoPrecipitation, …) specify the
method-specific parameters. Linked from Synthesis via realized_plan.

The specific preparation method type should additionally be expressed
via rdf_type on the Synthesis activity using a voc4cat term
(e.g. VOC4CAT:0007016 for preparation method).

**CURIE:** [`OBI:0000272`](http://purl.obolibrary.org/obo/OBI_0000272)

**Schema Reference:** [PreparationMethod](./elements/classes/PreparationMethod.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PreparationMethod target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of PreparationMethod:**

<details markdown="1">
<summary><strong>Impregnation</strong></summary>

**Description:** Catalyst preparation by impregnation: a solution of the active phase
precursor is brought into contact with the support material.

**CURIE:** [`coremeta4cat:Impregnation`](https://w3id.org/nfdi4cat/coremeta4cat/Impregnation)

**Schema Reference:** [Impregnation](./elements/classes/Impregnation.md)

**Slots**

<details markdown="1">
<summary><strong>impregnation type</strong> (Optional, Multivalued)</summary>

**Description:** Type of impregnation used (wet, dry, incipient wetness).

**Data Type:** ImpregnationTypeEnum

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:impregnation_type`](https://w3id.org/nfdi4cat/coremeta4cat/impregnation_type)

**Schema Reference:** [impregnation_type](./elements/slots/impregnation_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impregnation duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the impregnation step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:impregnation_duration`](https://w3id.org/nfdi4cat/coremeta4cat/impregnation_duration)

**Schema Reference:** [impregnation_duration](./elements/slots/impregnation_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impregnation temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during the impregnation step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:impregnation_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/impregnation_temperature)

**Schema Reference:** [impregnation_temperature](./elements/slots/impregnation_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_device`](https://w3id.org/nfdi4cat/coremeta4cat/drying_device)

**Schema Reference:** [drying_device](./elements/slots/drying_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/slots/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_time`](https://w3id.org/nfdi4cat/coremeta4cat/drying_time)

**Schema Reference:** [drying_time](./elements/slots/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/slots/drying_atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/slots/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/slots/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/slots/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/slots/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/slots/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/slots/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Impregnation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CoPrecipitation</strong></summary>

**Description:** Catalyst preparation by co-precipitation: precursor salts are
simultaneously precipitated from solution by a precipitating agent.

**CURIE:** [`coremeta4cat:CoPrecipitation`](https://w3id.org/nfdi4cat/coremeta4cat/CoPrecipitation)

**Schema Reference:** [CoPrecipitation](./elements/classes/CoPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>precipitating agent</strong> (Optional, Multivalued)</summary>

**Description:** Chemical agent used to induce precipitation (e.g. NaOH, NH3).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:precipitating_agent`](https://w3id.org/nfdi4cat/coremeta4cat/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/slots/precipitating_agent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_agent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of the precipitating agent.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:precipitating_concentration`](https://w3id.org/nfdi4cat/coremeta4cat/precipitating_concentration)

**Schema Reference:** [precipitating_concentration](./elements/slots/precipitating_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis ph</strong> (Optional, Multivalued)</summary>

**Description:** pH value maintained or targeted during synthesis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/slots/synthesis_ph.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_ph target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing rate</strong> (Optional, Multivalued)</summary>

**Description:** Stirring rate during mixing of synthesis components.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_rate`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/slots/mixing_rate.md)

**Unit:** rpm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the mixing step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_time`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_time)

**Schema Reference:** [mixing_time](./elements/slots/mixing_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/slots/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>order of addition</strong> (Optional, Multivalued)</summary>

**Description:** Order in which reagents or components are combined.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:order_of_addition`](https://w3id.org/nfdi4cat/coremeta4cat/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/slots/order_of_addition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20order_of_addition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration</strong> (Optional, Multivalued)</summary>

**Description:** Filtration method used to separate the precipitate (e.g. vacuum filtration).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filtration`](https://w3id.org/nfdi4cat/coremeta4cat/filtration)

**Schema Reference:** [filtration](./elements/slots/filtration.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification</strong> (Optional, Multivalued)</summary>

**Description:** Purification method applied after synthesis (e.g. washing, dialysis).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:purification`](https://w3id.org/nfdi4cat/coremeta4cat/purification)

**Schema Reference:** [purification](./elements/slots/purification.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during aging of the precipitate or gel.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:aging_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/slots/aging_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the aging step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:aging_time`](https://w3id.org/nfdi4cat/coremeta4cat/aging_time)

**Schema Reference:** [aging_time](./elements/slots/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_device`](https://w3id.org/nfdi4cat/coremeta4cat/drying_device)

**Schema Reference:** [drying_device](./elements/slots/drying_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/slots/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_time`](https://w3id.org/nfdi4cat/coremeta4cat/drying_time)

**Schema Reference:** [drying_time](./elements/slots/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/slots/drying_atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/slots/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/slots/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/slots/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/slots/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/slots/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/slots/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CoPrecipitation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SolGel</strong></summary>

**Description:** Catalyst preparation by the sol-gel process: hydrolysis and condensation
of precursor molecules to form a colloidal network (gel).

**CURIE:** [`coremeta4cat:SolGel`](https://w3id.org/nfdi4cat/coremeta4cat/SolGel)

**Schema Reference:** [SolGel](./elements/classes/SolGel.md)

**Slots**

<details markdown="1">
<summary><strong>hydrolysis ratio</strong> (Optional, Multivalued)</summary>

**Description:** Molar ratio of water to alkoxide precursor used in hydrolysis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:hydrolysis_ratio`](https://w3id.org/nfdi4cat/coremeta4cat/hydrolysis_ratio)

**Schema Reference:** [hydrolysis_ratio](./elements/slots/hydrolysis_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20hydrolysis_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the aging step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:aging_time`](https://w3id.org/nfdi4cat/coremeta4cat/aging_time)

**Schema Reference:** [aging_time](./elements/slots/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying</strong> (Optional, Multivalued)</summary>

**Description:** Drying method used for the gel (e.g. supercritical drying, freeze drying).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying`](https://w3id.org/nfdi4cat/coremeta4cat/drying)

**Schema Reference:** [drying](./elements/slots/drying.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surfactant template</strong> (Optional, Multivalued)</summary>

**Description:** Surfactant or structure-directing agent used as a template.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:surfactant_template`](https://w3id.org/nfdi4cat/coremeta4cat/surfactant_template)

**Schema Reference:** [surfactant_template](./elements/slots/surfactant_template.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surfactant_template target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_device`](https://w3id.org/nfdi4cat/coremeta4cat/drying_device)

**Schema Reference:** [drying_device](./elements/slots/drying_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/slots/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_time`](https://w3id.org/nfdi4cat/coremeta4cat/drying_time)

**Schema Reference:** [drying_time](./elements/slots/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/slots/drying_atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SolGel target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Solvothermal</strong></summary>

**Description:** Catalyst preparation under elevated temperature and pressure in a
sealed vessel using a non-aqueous solvent.

**CURIE:** [`coremeta4cat:Solvothermal`](https://w3id.org/nfdi4cat/coremeta4cat/Solvothermal)

**Schema Reference:** [Solvothermal](./elements/classes/Solvothermal.md)

**Slots**

<details markdown="1">
<summary><strong>filling volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume of solution relative to autoclave volume (filling degree).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filling_volume`](https://w3id.org/nfdi4cat/coremeta4cat/filling_volume)

**Schema Reference:** [filling_volume](./elements/slots/filling_volume.md)

**Unit:** mL

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filling_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirrer type</strong> (Optional, Multivalued)</summary>

**Description:** Type of stirrer used (e.g. magnetic, mechanical, none).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:stirrer_type`](https://w3id.org/nfdi4cat/coremeta4cat/stirrer_type)

**Schema Reference:** [stirrer_type](./elements/slots/stirrer_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirrer_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>cooling rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate at which the reactor is cooled after synthesis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:cooling_rate`](https://w3id.org/nfdi4cat/coremeta4cat/cooling_rate)

**Schema Reference:** [cooling_rate](./elements/slots/cooling_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20cooling_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/slots/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/slots/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/slots/equipment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_type`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_type)

**Schema Reference:** [vessel_type](./elements/slots/vessel_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Solvothermal target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PlasmaAssisted</strong></summary>

**Description:** Catalyst preparation using plasma treatment to modify surface
properties or deposit active components.

**CURIE:** [`coremeta4cat:PlasmaAssisted`](https://w3id.org/nfdi4cat/coremeta4cat/PlasmaAssisted)

**Schema Reference:** [PlasmaAssisted](./elements/classes/PlasmaAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>plasma type</strong> (Optional, Multivalued)</summary>

**Description:** Type of plasma used (e.g. DBD, microwave, RF plasma).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:plasma_type`](https://w3id.org/nfdi4cat/coremeta4cat/plasma_type)

**Schema Reference:** [plasma_type](./elements/slots/plasma_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20plasma_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>power input</strong> (Optional, Multivalued)</summary>

**Description:** Power input to the plasma reactor or other energy source.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:power_input`](https://w3id.org/nfdi4cat/coremeta4cat/power_input)

**Schema Reference:** [power_input](./elements/slots/power_input.md)

**Unit:** W

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20power_input target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>exposure time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of plasma or other energy exposure.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:exposure_time`](https://w3id.org/nfdi4cat/coremeta4cat/exposure_time)

**Schema Reference:** [exposure_time](./elements/slots/exposure_time.md)

**Unit:** min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20exposure_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure applied during synthesis (e.g. in autoclave or plasma reactor).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/slots/synthesis_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/slots/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/slots/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/slots/equipment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_type`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_type)

**Schema Reference:** [vessel_type](./elements/slots/vessel_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlasmaAssisted target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CombustionSynthesis</strong></summary>

**Description:** Catalyst preparation by combustion of a fuel/oxidizer mixture,
producing metal oxide catalysts in a single rapid step.

**CURIE:** [`coremeta4cat:CombustionSynthesis`](https://w3id.org/nfdi4cat/coremeta4cat/CombustionSynthesis)

**Schema Reference:** [CombustionSynthesis](./elements/classes/CombustionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>fuel</strong> (Optional, Multivalued)</summary>

**Description:** Organic fuel used in combustion synthesis (e.g. urea, glycine).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:fuel`](https://w3id.org/nfdi4cat/coremeta4cat/fuel)

**Schema Reference:** [fuel](./elements/slots/fuel.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>oxidizer</strong> (Optional, Multivalued)</summary>

**Description:** Oxidizer used in combustion synthesis (e.g. metal nitrates).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:oxidizer`](https://w3id.org/nfdi4cat/coremeta4cat/oxidizer)

**Schema Reference:** [oxidizer](./elements/slots/oxidizer.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20oxidizer target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fuel to oxidizer ratio</strong> (Optional, Multivalued)</summary>

**Description:** Molar ratio of fuel to oxidizer.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:fuel_to_oxidizer_ratio`](https://w3id.org/nfdi4cat/coremeta4cat/fuel_to_oxidizer_ratio)

**Schema Reference:** [fuel_to_oxidizer_ratio](./elements/slots/fuel_to_oxidizer_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel_to_oxidizer_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>set temperature</strong> (Optional, Multivalued)</summary>

**Description:** Target temperature set for the combustion reaction.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:set_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/set_temperature)

**Schema Reference:** [set_temperature](./elements/slots/set_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20set_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>post treatment</strong> (Optional, Multivalued)</summary>

**Description:** Post-synthesis treatment applied to the combustion product.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:post_treatment`](https://w3id.org/nfdi4cat/coremeta4cat/post_treatment)

**Schema Reference:** [post_treatment](./elements/slots/post_treatment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20post_treatment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/slots/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/slots/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/slots/equipment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_type`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_type)

**Schema Reference:** [vessel_type](./elements/slots/vessel_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CombustionSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>AtomicLayerDeposition</strong></summary>

**Description:** Catalyst preparation by atomic layer deposition (ALD): sequential
self-limiting surface reactions deposit a conformal thin film
of active phase onto a substrate.

**CURIE:** [`coremeta4cat:AtomicLayerDeposition`](https://w3id.org/nfdi4cat/coremeta4cat/AtomicLayerDeposition)

**Schema Reference:** [AtomicLayerDeposition](./elements/classes/AtomicLayerDeposition.md)

**Slots**

<details markdown="1">
<summary><strong>substrate</strong> (Optional, Multivalued)</summary>

**Description:** Substrate material on which the ALD film is deposited.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000024`](https://w3id.org/nfdi4cat/voc4cat_0000024)

**Schema Reference:** [substrate](./elements/slots/substrate.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20substrate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pulse time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the precursor pulse in each ALD cycle.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:pulse_time`](https://w3id.org/nfdi4cat/coremeta4cat/pulse_time)

**Schema Reference:** [pulse_time](./elements/slots/pulse_time.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pulse_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purging duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the purge step between ALD pulses.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000112`](https://w3id.org/nfdi4cat/voc4cat_0000112)

**Schema Reference:** [purging_duration](./elements/slots/purging_duration.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purging_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>deposition temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during the deposition step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:deposition_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/slots/deposition_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>carrier gas</strong> (Optional, Multivalued)</summary>

**Description:** Carrier gas used in a process (e.g. in GC analysis or ALD deposition).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:carrier_gas`](https://w3id.org/nfdi4cat/coremeta4cat/carrier_gas)

**Schema Reference:** [carrier_gas](./elements/slots/carrier_gas.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AtomicLayerDeposition target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>DepositionPrecipitation</strong></summary>

**Description:** Catalyst preparation by deposition-precipitation: the active phase
is precipitated directly onto the support surface.

**CURIE:** [`coremeta4cat:DepositionPrecipitation`](https://w3id.org/nfdi4cat/coremeta4cat/DepositionPrecipitation)

**Schema Reference:** [DepositionPrecipitation](./elements/classes/DepositionPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>deposition temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during the deposition step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:deposition_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/slots/deposition_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>deposition time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the deposition step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:deposition_time`](https://w3id.org/nfdi4cat/coremeta4cat/deposition_time)

**Schema Reference:** [deposition_time](./elements/slots/deposition_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating agent</strong> (Optional, Multivalued)</summary>

**Description:** Chemical agent used to induce precipitation (e.g. NaOH, NH3).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:precipitating_agent`](https://w3id.org/nfdi4cat/coremeta4cat/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/slots/precipitating_agent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_agent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of the precipitating agent.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:precipitating_concentration`](https://w3id.org/nfdi4cat/coremeta4cat/precipitating_concentration)

**Schema Reference:** [precipitating_concentration](./elements/slots/precipitating_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis ph</strong> (Optional, Multivalued)</summary>

**Description:** pH value maintained or targeted during synthesis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/slots/synthesis_ph.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_ph target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing rate</strong> (Optional, Multivalued)</summary>

**Description:** Stirring rate during mixing of synthesis components.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_rate`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/slots/mixing_rate.md)

**Unit:** rpm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the mixing step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_time`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_time)

**Schema Reference:** [mixing_time](./elements/slots/mixing_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/slots/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>order of addition</strong> (Optional, Multivalued)</summary>

**Description:** Order in which reagents or components are combined.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:order_of_addition`](https://w3id.org/nfdi4cat/coremeta4cat/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/slots/order_of_addition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20order_of_addition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration</strong> (Optional, Multivalued)</summary>

**Description:** Filtration method used to separate the precipitate (e.g. vacuum filtration).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filtration`](https://w3id.org/nfdi4cat/coremeta4cat/filtration)

**Schema Reference:** [filtration](./elements/slots/filtration.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification</strong> (Optional, Multivalued)</summary>

**Description:** Purification method applied after synthesis (e.g. washing, dialysis).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:purification`](https://w3id.org/nfdi4cat/coremeta4cat/purification)

**Schema Reference:** [purification](./elements/slots/purification.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during aging of the precipitate or gel.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:aging_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/slots/aging_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the aging step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:aging_time`](https://w3id.org/nfdi4cat/coremeta4cat/aging_time)

**Schema Reference:** [aging_time](./elements/slots/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_device`](https://w3id.org/nfdi4cat/coremeta4cat/drying_device)

**Schema Reference:** [drying_device](./elements/slots/drying_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/slots/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_time`](https://w3id.org/nfdi4cat/coremeta4cat/drying_time)

**Schema Reference:** [drying_time](./elements/slots/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/slots/drying_atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/slots/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/slots/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/slots/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/slots/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/slots/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/slots/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DepositionPrecipitation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MicrowaveAssisted</strong></summary>

**Description:** Catalyst preparation using microwave irradiation to rapidly and
uniformly heat the reaction mixture.

**CURIE:** [`coremeta4cat:MicrowaveAssisted`](https://w3id.org/nfdi4cat/coremeta4cat/MicrowaveAssisted)

**Schema Reference:** [MicrowaveAssisted](./elements/classes/MicrowaveAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>power</strong> (Optional, Multivalued)</summary>

**Description:** Microwave power applied.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:power`](https://w3id.org/nfdi4cat/coremeta4cat/power)

**Schema Reference:** [power](./elements/slots/power.md)

**Unit:** W

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20power target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>microwave frequency</strong> (Optional, Multivalued)</summary>

**Description:** Frequency of microwave irradiation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:microwave_frequency`](https://w3id.org/nfdi4cat/coremeta4cat/microwave_frequency)

**Schema Reference:** [microwave_frequency](./elements/slots/microwave_frequency.md)

**Unit:** GHz

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20microwave_frequency target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/slots/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/slots/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/slots/equipment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_type`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_type)

**Schema Reference:** [vessel_type](./elements/slots/vessel_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MicrowaveAssisted target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SonochemicalSynthesis</strong></summary>

**Description:** Catalyst preparation using ultrasonic irradiation to drive chemical
reactions via acoustic cavitation.

**CURIE:** [`coremeta4cat:SonochemicalSynthesis`](https://w3id.org/nfdi4cat/coremeta4cat/SonochemicalSynthesis)

**Schema Reference:** [SonochemicalSynthesis](./elements/classes/SonochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>sonication power</strong> (Optional, Multivalued)</summary>

**Description:** Acoustic power applied during sonication.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sonication_power`](https://w3id.org/nfdi4cat/coremeta4cat/sonication_power)

**Schema Reference:** [sonication_power](./elements/slots/sonication_power.md)

**Unit:** W

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sonication_power target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sonication duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of ultrasonic irradiation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sonication_duration`](https://w3id.org/nfdi4cat/coremeta4cat/sonication_duration)

**Schema Reference:** [sonication_duration](./elements/slots/sonication_duration.md)

**Unit:** min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sonication_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during a process or measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/slots/temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_device`](https://w3id.org/nfdi4cat/coremeta4cat/drying_device)

**Schema Reference:** [drying_device](./elements/slots/drying_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/slots/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_time`](https://w3id.org/nfdi4cat/coremeta4cat/drying_time)

**Schema Reference:** [drying_time](./elements/slots/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/slots/drying_atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/slots/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/slots/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/slots/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/slots/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/slots/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/slots/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SonochemicalSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>FlameSprayPyrolysis</strong></summary>

**Description:** Catalyst preparation by flame spray pyrolysis (FSP): a liquid precursor
solution is atomised and combusted in a flame to produce nanoparticles.

**CURIE:** [`VOC4CAT:0007031`](https://w3id.org/nfdi4cat/voc4cat_0007031)

**Schema Reference:** [FlameSprayPyrolysis](./elements/classes/FlameSprayPyrolysis.md)

**Slots**

<details markdown="1">
<summary><strong>flame type</strong> (Optional, Multivalued)</summary>

**Description:** Type of flame used in FSP (e.g. methane/oxygen, H2/O2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:flame_type`](https://w3id.org/nfdi4cat/coremeta4cat/flame_type)

**Schema Reference:** [flame_type](./elements/slots/flame_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flame_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Flow rate of a fluid or gas.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:flow_rate`](https://w3id.org/nfdi4cat/coremeta4cat/flow_rate)

**Schema Reference:** [flow_rate](./elements/slots/flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>inlet system</strong> (Optional, Multivalued)</summary>

**Description:** Configuration of the precursor inlet system.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:inlet_system`](https://w3id.org/nfdi4cat/coremeta4cat/inlet_system)

**Schema Reference:** [inlet_system](./elements/slots/inlet_system.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inlet_system target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flame ring</strong> (Optional, Multivalued)</summary>

**Description:** Configuration of the supporting flame ring.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:flame_ring`](https://w3id.org/nfdi4cat/coremeta4cat/flame_ring)

**Schema Reference:** [flame_ring](./elements/slots/flame_ring.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flame_ring target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>dispersant</strong> (Optional, Multivalued)</summary>

**Description:** Dispersant used (e.g. in DLS measurement or flame spray pyrolysis).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:dispersant`](https://w3id.org/nfdi4cat/coremeta4cat/dispersant)

**Schema Reference:** [dispersant](./elements/slots/dispersant.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20dispersant target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>capillary pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure applied at the capillary nozzle during FSP.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:capillary_pressure`](https://w3id.org/nfdi4cat/coremeta4cat/capillary_pressure)

**Schema Reference:** [capillary_pressure](./elements/slots/capillary_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20capillary_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fuel dispersant ratio</strong> (Optional, Multivalued)</summary>

**Description:** Volume ratio of fuel to dispersant used in FSP.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:fuel_dispersant_ratio`](https://w3id.org/nfdi4cat/coremeta4cat/fuel_dispersant_ratio)

**Schema Reference:** [fuel_dispersant_ratio](./elements/slots/fuel_dispersant_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel_dispersant_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for filtration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filtration_device`](https://w3id.org/nfdi4cat/coremeta4cat/filtration_device)

**Schema Reference:** [filtration_device](./elements/slots/filtration_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filter type</strong> (Optional, Multivalued)</summary>

**Description:** Type of filter membrane or medium used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filter_type`](https://w3id.org/nfdi4cat/coremeta4cat/filter_type)

**Schema Reference:** [filter_type](./elements/slots/filter_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FlameSprayPyrolysis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MechanochemicalSynthesis</strong></summary>

**Description:** Catalyst preparation by mechanical milling or grinding, optionally
combined with thermal treatment.

**CURIE:** [`coremeta4cat:MechanochemicalSynthesis`](https://w3id.org/nfdi4cat/coremeta4cat/MechanochemicalSynthesis)

**Schema Reference:** [MechanochemicalSynthesis](./elements/classes/MechanochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>vessel volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume of the milling vessel.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_volume`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_volume)

**Schema Reference:** [vessel_volume](./elements/slots/vessel_volume.md)

**Unit:** mL

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>size and material</strong> (Optional, Multivalued)</summary>

**Description:** Size and material of the milling vessel and components.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:size_and_material`](https://w3id.org/nfdi4cat/coremeta4cat/size_and_material)

**Schema Reference:** [size_and_material](./elements/slots/size_and_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20size_and_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>milling speed</strong> (Optional, Multivalued)</summary>

**Description:** Rotational speed during milling.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:milling_speed`](https://w3id.org/nfdi4cat/coremeta4cat/milling_speed)

**Schema Reference:** [milling_speed](./elements/slots/milling_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20milling_speed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>milling duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the milling process.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:milling_duration`](https://w3id.org/nfdi4cat/coremeta4cat/milling_duration)

**Schema Reference:** [milling_duration](./elements/slots/milling_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20milling_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball material</strong> (Optional, Multivalued)</summary>

**Description:** Material of the milling balls (e.g. zirconia, stainless steel).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ball_material`](https://w3id.org/nfdi4cat/coremeta4cat/ball_material)

**Schema Reference:** [ball_material](./elements/slots/ball_material.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball size</strong> (Optional, Multivalued)</summary>

**Description:** Diameter of the milling balls.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ball_size`](https://w3id.org/nfdi4cat/coremeta4cat/ball_size)

**Schema Reference:** [ball_size](./elements/slots/ball_size.md)

**Unit:** mm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball to powder ratio</strong> (Optional, Multivalued)</summary>

**Description:** Mass ratio of milling balls to powder charge.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ball_to_powder_ratio`](https://w3id.org/nfdi4cat/coremeta4cat/ball_to_powder_ratio)

**Schema Reference:** [ball_to_powder_ratio](./elements/slots/ball_to_powder_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_to_powder_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/slots/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/slots/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/slots/equipment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_type`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_type)

**Schema Reference:** [vessel_type](./elements/slots/vessel_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MechanochemicalSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Sublimation</strong></summary>

**Description:** Catalyst preparation by sublimation: a solid precursor is vaporised
and deposited onto a substrate without passing through a liquid phase.

**CURIE:** [`coremeta4cat:Sublimation`](https://w3id.org/nfdi4cat/coremeta4cat/Sublimation)

**Schema Reference:** [Sublimation](./elements/classes/Sublimation.md)

**Slots**

<details markdown="1">
<summary><strong>synthesis pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure applied during synthesis (e.g. in autoclave or plasma reactor).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/slots/synthesis_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/slots/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/slots/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/slots/equipment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vessel_type`](https://w3id.org/nfdi4cat/coremeta4cat/vessel_type)

**Schema Reference:** [vessel_type](./elements/slots/vessel_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Sublimation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MolecularSynthesis</strong></summary>

**Description:** Catalyst preparation by molecular (organometallic or coordination)
chemistry routes, including crystallisation and purification steps.

**CURIE:** [`coremeta4cat:MolecularSynthesis`](https://w3id.org/nfdi4cat/coremeta4cat/MolecularSynthesis)

**Schema Reference:** [MolecularSynthesis](./elements/classes/MolecularSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>reaction vessel</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction vessel used (e.g. Schlenk flask, round-bottom flask).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:reaction_vessel`](https://w3id.org/nfdi4cat/coremeta4cat/reaction_vessel)

**Schema Reference:** [reaction_vessel](./elements/slots/reaction_vessel.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reaction_vessel target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for mixing (e.g. magnetic stirrer, vortex mixer).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_device`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_device)

**Schema Reference:** [mixing_device](./elements/slots/mixing_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of stirring or agitation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:stirring_duration`](https://w3id.org/nfdi4cat/coremeta4cat/stirring_duration)

**Schema Reference:** [stirring_duration](./elements/slots/stirring_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring speed</strong> (Optional, Multivalued)</summary>

**Description:** Rotational speed of stirring or agitation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:stirring_speed`](https://w3id.org/nfdi4cat/coremeta4cat/stirring_speed)

**Schema Reference:** [stirring_speed](./elements/slots/stirring_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_speed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:mixing_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/slots/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for filtration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filtration_device`](https://w3id.org/nfdi4cat/coremeta4cat/filtration_device)

**Schema Reference:** [filtration_device](./elements/slots/filtration_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filter type</strong> (Optional, Multivalued)</summary>

**Description:** Type of filter membrane or medium used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filter_type`](https://w3id.org/nfdi4cat/coremeta4cat/filter_type)

**Schema Reference:** [filter_type](./elements/slots/filter_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystallisation solvents</strong> (Optional, Multivalued)</summary>

**Description:** Solvent(s) used for crystallisation.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:crystallisation_solvents`](https://w3id.org/nfdi4cat/coremeta4cat/crystallisation_solvents)

**Schema Reference:** [crystallisation_solvents](./elements/slots/crystallisation_solvents.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystallisation_solvents target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitation agent</strong> (Optional, Multivalued)</summary>

**Description:** Agent used to induce precipitation in molecular synthesis.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:precipitation_agent`](https://w3id.org/nfdi4cat/coremeta4cat/precipitation_agent)

**Schema Reference:** [precipitation_agent](./elements/slots/precipitation_agent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitation_agent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystallisation duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the crystallisation step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:crystallisation_duration`](https://w3id.org/nfdi4cat/coremeta4cat/crystallisation_duration)

**Schema Reference:** [crystallisation_duration](./elements/slots/crystallisation_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystallisation_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used for washing or recrystallisation during purification.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:purification_solvent`](https://w3id.org/nfdi4cat/coremeta4cat/purification_solvent)

**Schema Reference:** [purification_solvent](./elements/slots/purification_solvent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification_solvent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature ramp</strong> (Optional, Multivalued)</summary>

**Description:** Temperature ramp rate applied during drying or activation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:temperature_ramp`](https://w3id.org/nfdi4cat/coremeta4cat/temperature_ramp)

**Schema Reference:** [temperature_ramp](./elements/slots/temperature_ramp.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature_ramp target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/atmosphere)

**Schema Reference:** [atmosphere](./elements/slots/atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_device`](https://w3id.org/nfdi4cat/coremeta4cat/drying_device)

**Schema Reference:** [drying_device](./elements/slots/drying_device.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/slots/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_time`](https://w3id.org/nfdi4cat/coremeta4cat/drying_time)

**Schema Reference:** [drying_time](./elements/slots/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:drying_atmosphere`](https://w3id.org/nfdi4cat/coremeta4cat/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/slots/drying_atmosphere.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolecularSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ExsolutionSynthesis</strong></summary>

**Description:** Catalyst preparation by exsolution: metal nanoparticles are grown on
a perovskite oxide surface by reduction/oxidation cycling.

**CURIE:** [`coremeta4cat:ExsolutionSynthesis`](https://w3id.org/nfdi4cat/coremeta4cat/ExsolutionSynthesis)

**Schema Reference:** [ExsolutionSynthesis](./elements/classes/ExsolutionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/slots/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/slots/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/slots/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_cycles`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/slots/number_of_cycles.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/slots/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/slots/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/slots/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ExsolutionSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20realized_plan target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

