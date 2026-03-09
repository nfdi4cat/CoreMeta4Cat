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

**CURIE:** [`catcore:nominal_composition`](https://w3id.org/nfdi4cat/catcore/nominal_composition)

**Schema Reference:** [nominal_composition](./elements/nominal_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nominal_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>catalyst measured properties</strong> (Mandatory, Multivalued)</summary>

**Description:** Key measured properties of the resulting catalyst
(e.g. BET surface area, sieve fraction, molar ratio).

**Data Type:** string

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`catcore:catalyst_measured_properties`](https://w3id.org/nfdi4cat/catcore/catalyst_measured_properties)

**Schema Reference:** [catalyst_measured_properties](./elements/catalyst_measured_properties.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_measured_properties target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>storage conditions</strong> (Recommended, Multivalued)</summary>

**Description:** Conditions under which the catalyst is stored (e.g. inert atmosphere, 4°C).

**Data Type:** string

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`catcore:storage_conditions`](https://w3id.org/nfdi4cat/catcore/storage_conditions)

**Schema Reference:** [storage_conditions](./elements/storage_conditions.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20storage_conditions target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>support</strong> (Optional, Multivalued)</summary>

**Description:** Support material on which the active phase is deposited (e.g. Al2O3, SiO2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:support`](https://w3id.org/nfdi4cat/catcore/support)

**Schema Reference:** [support](./elements/support.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20support target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used in a process or sample preparation.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent](./elements/solvent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>sample pretreatment</strong> (Optional, Multivalued)</summary>

**Description:** Pre-treatment applied to the sample before a process or measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000122`](https://w3id.org/nfdi4cat/voc4cat_0000122)

**Schema Reference:** [sample_pretreatment](./elements/sample_pretreatment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_pretreatment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>had input entity</strong> (Mandatory, Multivalued)</summary>

**Description:** The Precursor(s) consumed during this Synthesis.

**Data Type:** Precursor

**Cardinality:**  Mandatory, Multivalued

**Schema Reference:** [had_input_entity](./elements/had_input_entity.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>Precursor</strong></summary>

**Description:** A MaterialSample that serves as input material in a catalyst Synthesis.
Precursors are consumed or transformed during the preparation process.

**CURIE:** [`CHEBI:52717`](http://purl.obolibrary.org/obo/CHEBI_52717)

**Schema Reference:** [Precursor](./elements/Precursor.md)

**Slots**

<details markdown="1">
<summary><strong>precursor quantity</strong> (Mandatory, Multivalued)</summary>

**Description:** Quantity of precursor used in synthesis.

**Data Type:** float

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`catcore:precursor_quantity`](https://w3id.org/nfdi4cat/catcore/precursor_quantity)

**Schema Reference:** [precursor_quantity](./elements/precursor_quantity.md)

**Unit:** g

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precursor_quantity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Precursor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20had_input_entity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>had output entity</strong> (Recommended, Multivalued)</summary>

**Description:** The CatalystSample produced by this Synthesis.

**Data Type:** CatalystSample

**Cardinality:**  Recommended, Multivalued

**Schema Reference:** [had_output_entity](./elements/had_output_entity.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>CatalystSample</strong></summary>

**Description:** A MaterialSample that is the product of a catalyst Synthesis.
The specific type of catalyst (e.g. heterogeneous, supported metal)
is expressed via rdf_type using a voc4cat term.

**CURIE:** [`OBI:0000747`](http://purl.obolibrary.org/obo/OBI_0000747)

**Schema Reference:** [CatalystSample](./elements/CatalystSample.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CatalystSample target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20had_output_entity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>realized plan</strong> (Mandatory)</summary>

**Description:** The PreparationMethod (protocol) realized in this Synthesis.

**Data Type:** PreparationMethod

**Cardinality:**  Mandatory

**Schema Reference:** [realized_plan](./elements/realized_plan.md)

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

**Schema Reference:** [PreparationMethod](./elements/PreparationMethod.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PreparationMethod target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of PreparationMethod:**

<details markdown="1">
<summary><strong>Impregnation</strong></summary>

**Description:** Catalyst preparation by impregnation: a solution of the active phase
precursor is brought into contact with the support material.

**CURIE:** [`catcore:Impregnation`](https://w3id.org/nfdi4cat/catcore/Impregnation)

**Schema Reference:** [Impregnation](./elements/Impregnation.md)

**Slots**

<details markdown="1">
<summary><strong>impregnation type</strong> (Optional, Multivalued)</summary>

**Description:** Type of impregnation used (wet, dry, incipient wetness).

**Data Type:** ImpregnationTypeEnum

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:impregnation_type`](https://w3id.org/nfdi4cat/catcore/impregnation_type)

**Schema Reference:** [impregnation_type](./elements/impregnation_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impregnation duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the impregnation step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:impregnation_duration`](https://w3id.org/nfdi4cat/catcore/impregnation_duration)

**Schema Reference:** [impregnation_duration](./elements/impregnation_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impregnation temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during the impregnation step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:impregnation_temperature`](https://w3id.org/nfdi4cat/catcore/impregnation_temperature)

**Schema Reference:** [impregnation_temperature](./elements/impregnation_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Impregnation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CoPrecipitation</strong></summary>

**Description:** Catalyst preparation by co-precipitation: precursor salts are
simultaneously precipitated from solution by a precipitating agent.

**CURIE:** [`catcore:CoPrecipitation`](https://w3id.org/nfdi4cat/catcore/CoPrecipitation)

**Schema Reference:** [CoPrecipitation](./elements/CoPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>precipitating agent</strong> (Optional, Multivalued)</summary>

**Description:** Chemical agent used to induce precipitation (e.g. NaOH, NH3).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_agent`](https://w3id.org/nfdi4cat/catcore/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/precipitating_agent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_agent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of the precipitating agent.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_concentration`](https://w3id.org/nfdi4cat/catcore/precipitating_concentration)

**Schema Reference:** [precipitating_concentration](./elements/precipitating_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis ph</strong> (Optional, Multivalued)</summary>

**Description:** pH value maintained or targeted during synthesis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/synthesis_ph.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_ph target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing rate</strong> (Optional, Multivalued)</summary>

**Description:** Stirring rate during mixing of synthesis components.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_rate`](https://w3id.org/nfdi4cat/catcore/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/mixing_rate.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the mixing step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_time`](https://w3id.org/nfdi4cat/catcore/mixing_time)

**Schema Reference:** [mixing_time](./elements/mixing_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>order of addition</strong> (Optional, Multivalued)</summary>

**Description:** Order in which reagents or components are combined.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:order_of_addition`](https://w3id.org/nfdi4cat/catcore/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/order_of_addition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20order_of_addition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration</strong> (Optional, Multivalued)</summary>

**Description:** Filtration method used to separate the precipitate (e.g. vacuum filtration).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration`](https://w3id.org/nfdi4cat/catcore/filtration)

**Schema Reference:** [filtration](./elements/filtration.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification</strong> (Optional, Multivalued)</summary>

**Description:** Purification method applied after synthesis (e.g. washing, dialysis).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:purification`](https://w3id.org/nfdi4cat/catcore/purification)

**Schema Reference:** [purification](./elements/purification.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during aging of the precipitate or gel.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_temperature`](https://w3id.org/nfdi4cat/catcore/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/aging_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the aging step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CoPrecipitation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SolGel</strong></summary>

**Description:** Catalyst preparation by the sol-gel process: hydrolysis and condensation
of precursor molecules to form a colloidal network (gel).

**CURIE:** [`catcore:SolGel`](https://w3id.org/nfdi4cat/catcore/SolGel)

**Schema Reference:** [SolGel](./elements/SolGel.md)

**Slots**

<details markdown="1">
<summary><strong>hydrolysis ratio</strong> (Optional, Multivalued)</summary>

**Description:** Molar ratio of water to alkoxide precursor used in hydrolysis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:hydrolysis_ratio`](https://w3id.org/nfdi4cat/catcore/hydrolysis_ratio)

**Schema Reference:** [hydrolysis_ratio](./elements/hydrolysis_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20hydrolysis_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the aging step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying</strong> (Optional, Multivalued)</summary>

**Description:** Drying method used for the gel (e.g. supercritical drying, freeze drying).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying`](https://w3id.org/nfdi4cat/catcore/drying)

**Schema Reference:** [drying](./elements/drying.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surfactant template</strong> (Optional, Multivalued)</summary>

**Description:** Surfactant or structure-directing agent used as a template.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:surfactant_template`](https://w3id.org/nfdi4cat/catcore/surfactant_template)

**Schema Reference:** [surfactant_template](./elements/surfactant_template.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surfactant_template target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SolGel target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Solvothermal</strong></summary>

**Description:** Catalyst preparation under elevated temperature and pressure in a
sealed vessel using a non-aqueous solvent.

**CURIE:** [`catcore:Solvothermal`](https://w3id.org/nfdi4cat/catcore/Solvothermal)

**Schema Reference:** [Solvothermal](./elements/Solvothermal.md)

**Slots**

<details markdown="1">
<summary><strong>filling volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume of solution relative to autoclave volume (filling degree).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filling_volume`](https://w3id.org/nfdi4cat/catcore/filling_volume)

**Schema Reference:** [filling_volume](./elements/filling_volume.md)

**Unit:** mL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filling_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirrer type</strong> (Optional, Multivalued)</summary>

**Description:** Type of stirrer used (e.g. magnetic, mechanical, none).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirrer_type`](https://w3id.org/nfdi4cat/catcore/stirrer_type)

**Schema Reference:** [stirrer_type](./elements/stirrer_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirrer_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>cooling rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate at which the reactor is cooled after synthesis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:cooling_rate`](https://w3id.org/nfdi4cat/catcore/cooling_rate)

**Schema Reference:** [cooling_rate](./elements/cooling_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20cooling_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Solvothermal target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PlasmaAssisted</strong></summary>

**Description:** Catalyst preparation using plasma treatment to modify surface
properties or deposit active components.

**CURIE:** [`catcore:PlasmaAssisted`](https://w3id.org/nfdi4cat/catcore/PlasmaAssisted)

**Schema Reference:** [PlasmaAssisted](./elements/PlasmaAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>plasma type</strong> (Optional, Multivalued)</summary>

**Description:** Type of plasma used (e.g. DBD, microwave, RF plasma).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:plasma_type`](https://w3id.org/nfdi4cat/catcore/plasma_type)

**Schema Reference:** [plasma_type](./elements/plasma_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20plasma_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>power input</strong> (Optional, Multivalued)</summary>

**Description:** Power input to the plasma reactor or other energy source.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:power_input`](https://w3id.org/nfdi4cat/catcore/power_input)

**Schema Reference:** [power_input](./elements/power_input.md)

**Unit:** W

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20power_input target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>exposure time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of plasma or other energy exposure.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:exposure_time`](https://w3id.org/nfdi4cat/catcore/exposure_time)

**Schema Reference:** [exposure_time](./elements/exposure_time.md)

**Unit:** min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20exposure_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure applied during synthesis (e.g. in autoclave or plasma reactor).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/synthesis_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlasmaAssisted target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CombustionSynthesis</strong></summary>

**Description:** Catalyst preparation by combustion of a fuel/oxidizer mixture,
producing metal oxide catalysts in a single rapid step.

**CURIE:** [`catcore:CombustionSynthesis`](https://w3id.org/nfdi4cat/catcore/CombustionSynthesis)

**Schema Reference:** [CombustionSynthesis](./elements/CombustionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>fuel</strong> (Optional, Multivalued)</summary>

**Description:** Organic fuel used in combustion synthesis (e.g. urea, glycine).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fuel`](https://w3id.org/nfdi4cat/catcore/fuel)

**Schema Reference:** [fuel](./elements/fuel.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>oxidizer</strong> (Optional, Multivalued)</summary>

**Description:** Oxidizer used in combustion synthesis (e.g. metal nitrates).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:oxidizer`](https://w3id.org/nfdi4cat/catcore/oxidizer)

**Schema Reference:** [oxidizer](./elements/oxidizer.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20oxidizer target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fuel to oxidizer ratio</strong> (Optional, Multivalued)</summary>

**Description:** Molar ratio of fuel to oxidizer.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fuel_to_oxidizer_ratio`](https://w3id.org/nfdi4cat/catcore/fuel_to_oxidizer_ratio)

**Schema Reference:** [fuel_to_oxidizer_ratio](./elements/fuel_to_oxidizer_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel_to_oxidizer_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>set temperature</strong> (Optional, Multivalued)</summary>

**Description:** Target temperature set for the combustion reaction.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:set_temperature`](https://w3id.org/nfdi4cat/catcore/set_temperature)

**Schema Reference:** [set_temperature](./elements/set_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20set_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>post treatment</strong> (Optional, Multivalued)</summary>

**Description:** Post-synthesis treatment applied to the combustion product.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:post_treatment`](https://w3id.org/nfdi4cat/catcore/post_treatment)

**Schema Reference:** [post_treatment](./elements/post_treatment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20post_treatment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CombustionSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>AtomicLayerDeposition</strong></summary>

**Description:** Catalyst preparation by atomic layer deposition (ALD): sequential
self-limiting surface reactions deposit a conformal thin film
of active phase onto a substrate.

**CURIE:** [`catcore:AtomicLayerDeposition`](https://w3id.org/nfdi4cat/catcore/AtomicLayerDeposition)

**Schema Reference:** [AtomicLayerDeposition](./elements/AtomicLayerDeposition.md)

**Slots**

<details markdown="1">
<summary><strong>substrate</strong> (Optional, Multivalued)</summary>

**Description:** Substrate material on which the ALD film is deposited.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000024`](https://w3id.org/nfdi4cat/voc4cat_0000024)

**Schema Reference:** [substrate](./elements/substrate.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20substrate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pulse time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the precursor pulse in each ALD cycle.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:pulse_time`](https://w3id.org/nfdi4cat/catcore/pulse_time)

**Schema Reference:** [pulse_time](./elements/pulse_time.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pulse_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purging duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the purge step between ALD pulses.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000112`](https://w3id.org/nfdi4cat/voc4cat_0000112)

**Schema Reference:** [purging_duration](./elements/purging_duration.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purging_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>deposition temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during the deposition step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:deposition_temperature`](https://w3id.org/nfdi4cat/catcore/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/deposition_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>carrier gas</strong> (Optional, Multivalued)</summary>

**Description:** Carrier gas used in a process (e.g. in GC analysis or ALD deposition).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:carrier_gas`](https://w3id.org/nfdi4cat/catcore/carrier_gas)

**Schema Reference:** [carrier_gas](./elements/carrier_gas.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AtomicLayerDeposition target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>DepositionPrecipitation</strong></summary>

**Description:** Catalyst preparation by deposition-precipitation: the active phase
is precipitated directly onto the support surface.

**CURIE:** [`catcore:DepositionPrecipitation`](https://w3id.org/nfdi4cat/catcore/DepositionPrecipitation)

**Schema Reference:** [DepositionPrecipitation](./elements/DepositionPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>deposition temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during the deposition step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:deposition_temperature`](https://w3id.org/nfdi4cat/catcore/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/deposition_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>deposition time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the deposition step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:deposition_time`](https://w3id.org/nfdi4cat/catcore/deposition_time)

**Schema Reference:** [deposition_time](./elements/deposition_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating agent</strong> (Optional, Multivalued)</summary>

**Description:** Chemical agent used to induce precipitation (e.g. NaOH, NH3).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_agent`](https://w3id.org/nfdi4cat/catcore/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/precipitating_agent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_agent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of the precipitating agent.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_concentration`](https://w3id.org/nfdi4cat/catcore/precipitating_concentration)

**Schema Reference:** [precipitating_concentration](./elements/precipitating_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis ph</strong> (Optional, Multivalued)</summary>

**Description:** pH value maintained or targeted during synthesis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/synthesis_ph.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_ph target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing rate</strong> (Optional, Multivalued)</summary>

**Description:** Stirring rate during mixing of synthesis components.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_rate`](https://w3id.org/nfdi4cat/catcore/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/mixing_rate.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the mixing step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_time`](https://w3id.org/nfdi4cat/catcore/mixing_time)

**Schema Reference:** [mixing_time](./elements/mixing_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>order of addition</strong> (Optional, Multivalued)</summary>

**Description:** Order in which reagents or components are combined.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:order_of_addition`](https://w3id.org/nfdi4cat/catcore/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/order_of_addition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20order_of_addition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration</strong> (Optional, Multivalued)</summary>

**Description:** Filtration method used to separate the precipitate (e.g. vacuum filtration).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration`](https://w3id.org/nfdi4cat/catcore/filtration)

**Schema Reference:** [filtration](./elements/filtration.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification</strong> (Optional, Multivalued)</summary>

**Description:** Purification method applied after synthesis (e.g. washing, dialysis).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:purification`](https://w3id.org/nfdi4cat/catcore/purification)

**Schema Reference:** [purification](./elements/purification.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during aging of the precipitate or gel.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_temperature`](https://w3id.org/nfdi4cat/catcore/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/aging_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the aging step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DepositionPrecipitation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MicrowaveAssisted</strong></summary>

**Description:** Catalyst preparation using microwave irradiation to rapidly and
uniformly heat the reaction mixture.

**CURIE:** [`catcore:MicrowaveAssisted`](https://w3id.org/nfdi4cat/catcore/MicrowaveAssisted)

**Schema Reference:** [MicrowaveAssisted](./elements/MicrowaveAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>power</strong> (Optional, Multivalued)</summary>

**Description:** Microwave power applied.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:power`](https://w3id.org/nfdi4cat/catcore/power)

**Schema Reference:** [power](./elements/power.md)

**Unit:** W

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20power target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>microwave frequency</strong> (Optional, Multivalued)</summary>

**Description:** Frequency of microwave irradiation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:microwave_frequency`](https://w3id.org/nfdi4cat/catcore/microwave_frequency)

**Schema Reference:** [microwave_frequency](./elements/microwave_frequency.md)

**Unit:** GHz

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20microwave_frequency target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MicrowaveAssisted target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SonochemicalSynthesis</strong></summary>

**Description:** Catalyst preparation using ultrasonic irradiation to drive chemical
reactions via acoustic cavitation.

**CURIE:** [`catcore:SonochemicalSynthesis`](https://w3id.org/nfdi4cat/catcore/SonochemicalSynthesis)

**Schema Reference:** [SonochemicalSynthesis](./elements/SonochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>sonication power</strong> (Optional, Multivalued)</summary>

**Description:** Acoustic power applied during sonication.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sonication_power`](https://w3id.org/nfdi4cat/catcore/sonication_power)

**Schema Reference:** [sonication_power](./elements/sonication_power.md)

**Unit:** W

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sonication_power target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sonication duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of ultrasonic irradiation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sonication_duration`](https://w3id.org/nfdi4cat/catcore/sonication_duration)

**Schema Reference:** [sonication_duration](./elements/sonication_duration.md)

**Unit:** min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sonication_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during a process or measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SonochemicalSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>FlameSprayPyrolysis</strong></summary>

**Description:** Catalyst preparation by flame spray pyrolysis (FSP): a liquid precursor
solution is atomised and combusted in a flame to produce nanoparticles.

**CURIE:** [`VOC4CAT:0007031`](https://w3id.org/nfdi4cat/voc4cat_0007031)

**Schema Reference:** [FlameSprayPyrolysis](./elements/FlameSprayPyrolysis.md)

**Slots**

<details markdown="1">
<summary><strong>flame type</strong> (Optional, Multivalued)</summary>

**Description:** Type of flame used in FSP (e.g. methane/oxygen, H2/O2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flame_type`](https://w3id.org/nfdi4cat/catcore/flame_type)

**Schema Reference:** [flame_type](./elements/flame_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flame_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Flow rate of a fluid or gas.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flow_rate`](https://w3id.org/nfdi4cat/catcore/flow_rate)

**Schema Reference:** [flow_rate](./elements/flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>inlet system</strong> (Optional, Multivalued)</summary>

**Description:** Configuration of the precursor inlet system.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:inlet_system`](https://w3id.org/nfdi4cat/catcore/inlet_system)

**Schema Reference:** [inlet_system](./elements/inlet_system.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inlet_system target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flame ring</strong> (Optional, Multivalued)</summary>

**Description:** Configuration of the supporting flame ring.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flame_ring`](https://w3id.org/nfdi4cat/catcore/flame_ring)

**Schema Reference:** [flame_ring](./elements/flame_ring.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flame_ring target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>dispersant</strong> (Optional, Multivalued)</summary>

**Description:** Dispersant used (e.g. in DLS measurement or flame spray pyrolysis).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:dispersant`](https://w3id.org/nfdi4cat/catcore/dispersant)

**Schema Reference:** [dispersant](./elements/dispersant.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20dispersant target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>capillary pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure applied at the capillary nozzle during FSP.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:capillary_pressure`](https://w3id.org/nfdi4cat/catcore/capillary_pressure)

**Schema Reference:** [capillary_pressure](./elements/capillary_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20capillary_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fuel dispersant ratio</strong> (Optional, Multivalued)</summary>

**Description:** Volume ratio of fuel to dispersant used in FSP.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fuel_dispersant_ratio`](https://w3id.org/nfdi4cat/catcore/fuel_dispersant_ratio)

**Schema Reference:** [fuel_dispersant_ratio](./elements/fuel_dispersant_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel_dispersant_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for filtration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration_device`](https://w3id.org/nfdi4cat/catcore/filtration_device)

**Schema Reference:** [filtration_device](./elements/filtration_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filter type</strong> (Optional, Multivalued)</summary>

**Description:** Type of filter membrane or medium used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filter_type`](https://w3id.org/nfdi4cat/catcore/filter_type)

**Schema Reference:** [filter_type](./elements/filter_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FlameSprayPyrolysis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MechanochemicalSynthesis</strong></summary>

**Description:** Catalyst preparation by mechanical milling or grinding, optionally
combined with thermal treatment.

**CURIE:** [`catcore:MechanochemicalSynthesis`](https://w3id.org/nfdi4cat/catcore/MechanochemicalSynthesis)

**Schema Reference:** [MechanochemicalSynthesis](./elements/MechanochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>vessel volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume of the milling vessel.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_volume`](https://w3id.org/nfdi4cat/catcore/vessel_volume)

**Schema Reference:** [vessel_volume](./elements/vessel_volume.md)

**Unit:** mL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>size and material</strong> (Optional, Multivalued)</summary>

**Description:** Size and material of the milling vessel and components.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:size_and_material`](https://w3id.org/nfdi4cat/catcore/size_and_material)

**Schema Reference:** [size_and_material](./elements/size_and_material.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20size_and_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>milling speed</strong> (Optional, Multivalued)</summary>

**Description:** Rotational speed during milling.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:milling_speed`](https://w3id.org/nfdi4cat/catcore/milling_speed)

**Schema Reference:** [milling_speed](./elements/milling_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20milling_speed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>milling duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the milling process.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:milling_duration`](https://w3id.org/nfdi4cat/catcore/milling_duration)

**Schema Reference:** [milling_duration](./elements/milling_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20milling_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball material</strong> (Optional, Multivalued)</summary>

**Description:** Material of the milling balls (e.g. zirconia, stainless steel).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ball_material`](https://w3id.org/nfdi4cat/catcore/ball_material)

**Schema Reference:** [ball_material](./elements/ball_material.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_material target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball size</strong> (Optional, Multivalued)</summary>

**Description:** Diameter of the milling balls.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ball_size`](https://w3id.org/nfdi4cat/catcore/ball_size)

**Schema Reference:** [ball_size](./elements/ball_size.md)

**Unit:** mm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball to powder ratio</strong> (Optional, Multivalued)</summary>

**Description:** Mass ratio of milling balls to powder charge.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ball_to_powder_ratio`](https://w3id.org/nfdi4cat/catcore/ball_to_powder_ratio)

**Schema Reference:** [ball_to_powder_ratio](./elements/ball_to_powder_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_to_powder_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MechanochemicalSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Sublimation</strong></summary>

**Description:** Catalyst preparation by sublimation: a solid precursor is vaporised
and deposited onto a substrate without passing through a liquid phase.

**CURIE:** [`catcore:Sublimation`](https://w3id.org/nfdi4cat/catcore/Sublimation)

**Schema Reference:** [Sublimation](./elements/Sublimation.md)

**Slots**

<details markdown="1">
<summary><strong>synthesis pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure applied during synthesis (e.g. in autoclave or plasma reactor).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/synthesis_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the synthesis step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment or instrument used in a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction or synthesis vessel used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Sublimation target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MolecularSynthesis</strong></summary>

**Description:** Catalyst preparation by molecular (organometallic or coordination)
chemistry routes, including crystallisation and purification steps.

**CURIE:** [`catcore:MolecularSynthesis`](https://w3id.org/nfdi4cat/catcore/MolecularSynthesis)

**Schema Reference:** [MolecularSynthesis](./elements/MolecularSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>reaction vessel</strong> (Optional, Multivalued)</summary>

**Description:** Type of reaction vessel used (e.g. Schlenk flask, round-bottom flask).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:reaction_vessel`](https://w3id.org/nfdi4cat/catcore/reaction_vessel)

**Schema Reference:** [reaction_vessel](./elements/reaction_vessel.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reaction_vessel target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for mixing (e.g. magnetic stirrer, vortex mixer).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_device`](https://w3id.org/nfdi4cat/catcore/mixing_device)

**Schema Reference:** [mixing_device](./elements/mixing_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of stirring or agitation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirring_duration`](https://w3id.org/nfdi4cat/catcore/stirring_duration)

**Schema Reference:** [stirring_duration](./elements/stirring_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring speed</strong> (Optional, Multivalued)</summary>

**Description:** Rotational speed of stirring or agitation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirring_speed`](https://w3id.org/nfdi4cat/catcore/stirring_speed)

**Schema Reference:** [stirring_speed](./elements/stirring_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_speed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for filtration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration_device`](https://w3id.org/nfdi4cat/catcore/filtration_device)

**Schema Reference:** [filtration_device](./elements/filtration_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filter type</strong> (Optional, Multivalued)</summary>

**Description:** Type of filter membrane or medium used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filter_type`](https://w3id.org/nfdi4cat/catcore/filter_type)

**Schema Reference:** [filter_type](./elements/filter_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystallisation solvents</strong> (Optional, Multivalued)</summary>

**Description:** Solvent(s) used for crystallisation.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:crystallisation_solvents`](https://w3id.org/nfdi4cat/catcore/crystallisation_solvents)

**Schema Reference:** [crystallisation_solvents](./elements/crystallisation_solvents.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystallisation_solvents target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitation agent</strong> (Optional, Multivalued)</summary>

**Description:** Agent used to induce precipitation in molecular synthesis.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitation_agent`](https://w3id.org/nfdi4cat/catcore/precipitation_agent)

**Schema Reference:** [precipitation_agent](./elements/precipitation_agent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitation_agent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystallisation duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the crystallisation step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:crystallisation_duration`](https://w3id.org/nfdi4cat/catcore/crystallisation_duration)

**Schema Reference:** [crystallisation_duration](./elements/crystallisation_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystallisation_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used for washing or recrystallisation during purification.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:purification_solvent`](https://w3id.org/nfdi4cat/catcore/purification_solvent)

**Schema Reference:** [purification_solvent](./elements/purification_solvent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification_solvent target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature ramp</strong> (Optional, Multivalued)</summary>

**Description:** Temperature ramp rate applied during drying or activation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:temperature_ramp`](https://w3id.org/nfdi4cat/catcore/temperature_ramp)

**Schema Reference:** [temperature_ramp](./elements/temperature_ramp.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature_ramp target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment or atmospheric conditions during a process.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying (e.g. oven, rotary evaporator).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature applied during drying.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the drying step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere maintained during drying (e.g. air, N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolecularSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ExsolutionSynthesis</strong></summary>

**Description:** Catalyst preparation by exsolution: metal nanoparticles are grown on
a perovskite oxide surface by reduction/oxidation cycling.

**CURIE:** [`catcore:ExsolutionSynthesis`](https://w3id.org/nfdi4cat/catcore/ExsolutionSynthesis)

**Schema Reference:** [ExsolutionSynthesis](./elements/ExsolutionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final (target) temperature for calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Time held at the final calcination temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of repeated cycles in a process (e.g. ALD cycles, impregnation cycles).

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment maintained during calcination (e.g. air, H2/N2).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate maintained during calcination.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ExsolutionSynthesis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20realized_plan target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

