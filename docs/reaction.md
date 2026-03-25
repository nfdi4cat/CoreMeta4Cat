# Reaction

The Reaction data class defines metadata required to document catalytic testing procedures, reactor configurations, operating conditions, and analytical methods. It provides structured descriptors necessary to contextualize catalytic performance data.

Core fields include reactor design type, operational parameters, and product identification and quantification methods. The class also specifies metadata required to report and evaluate catalyst performance metrics, enabling structured comparison across experimental studies.

**CURIE:** [`SIO:010345`](SIO:010345)

<iframe
    src="/CoreMeta4Cat/assets/metadata_reaction_hierarchy.html"
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
<summary><strong>catalyst quantity</strong> (Mandatory, Multivalued)</summary>

**Description:** Mass of catalyst loaded into the reactor.

**Data Type:** float

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:catalyst_quantity`](https://w3id.org/nfdi4cat/coremeta4cat/catalyst_quantity)

**Schema Reference:** [catalyst_quantity](./elements/slots/catalyst_quantity.md)

**Unit:** g

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_quantity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>reactant</strong> (Mandatory, Multivalued)</summary>

**Description:** Reactant(s) used in the reaction. Provide compound name, CAS number,
or SMILES. For feeds, include composition and flow rate where known.

**Data Type:** string

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`VOC4CAT:0000101`](https://w3id.org/nfdi4cat/voc4cat_0000101)

**Schema Reference:** [reactant](./elements/slots/reactant.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactant target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>catalyst type</strong> (Recommended, Multivalued)</summary>

**Description:** Type of catalyst used (e.g. heterogeneous, homogeneous, biocatalyst).
For heterogeneous catalysts, use voc4cat terms where available.

**Data Type:** string

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`VOC4CAT:0007014`](https://w3id.org/nfdi4cat/voc4cat_0007014)

**Schema Reference:** [catalyst_type](./elements/slots/catalyst_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>reactor temperature range</strong> (Optional, Multivalued)</summary>

**Description:** Temperature range used in the reactor during the reaction, expressed
as a string range (e.g. "200–400 °C") or a single set-point.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007032`](https://w3id.org/nfdi4cat/voc4cat_0007032)

**Schema Reference:** [reactor_temperature_range](./elements/slots/reactor_temperature_range.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_temperature_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
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

<details markdown="1" open>
<summary><strong>experiment pressure</strong> (Optional, Multivalued)</summary>

**Description:** Total pressure in the reactor during the experiment.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000118`](https://w3id.org/nfdi4cat/voc4cat_0000118)

**Schema Reference:** [experiment_pressure](./elements/slots/experiment_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>feed composition range</strong> (Optional, Multivalued)</summary>

**Description:** Feed gas or liquid composition range studied (e.g. "1–10 vol% CO in N2").
Record as a string; for individual component concentrations use reactant.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:feed_composition_range`](https://w3id.org/nfdi4cat/coremeta4cat/feed_composition_range)

**Schema Reference:** [feed_composition_range](./elements/slots/feed_composition_range.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20feed_composition_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>experiment duration</strong> (Optional, Multivalued)</summary>

**Description:** Total duration of the experiment or measurement run.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002455`](http://purl.allotrope.org/ontologies/result#AFR_0002455)

**Schema Reference:** [experiment_duration](./elements/slots/experiment_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_duration target="_blank" class="md-button md-button--primary">
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

<details markdown="1" open>
<summary><strong>ProductIdentificationMethod</strong></summary>

**Description:** Abstract Plan representing the method used to identify and quantify reaction
products. In practice, users should reference a concrete CharacterizationTechnique
subclass from coremeta4cat_characterization_ap (e.g. GCMS, HPLC_MS, NMRSpectroscopy).

This abstract class is retained for backward compatibility with the original
CoreMeta4Cat monolith. It is a subclass of Plan (prov:Plan / OBI:0000272) so that
it can participate in the realized_plan slot if needed.

**CURIE:** [`OBI:0000272`](http://purl.obolibrary.org/obo/OBI_0000272)

**Schema Reference:** [ProductIdentificationMethod](./elements/classes/ProductIdentificationMethod.md)

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
<summary><strong>carried out by</strong> (Mandatory, Multivalued)</summary>

**Description:** The reactor in which the Reaction takes place, provided as a
ReactorDesignType (Device) instance.

**Data Type:** ReactorDesignType

**Cardinality:**  Mandatory, Multivalued

**Schema Reference:** [carried_out_by](./elements/slots/carried_out_by.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>ReactorDesignType</strong></summary>

**Abstract Class**

**Description:** Abstract Device representing the type of reactor used in a catalytic experiment.
Concrete subclasses specify the reactor geometry and operating mode.
Linked from Reaction via carried_out_by.

**CURIE:** [`VOC4CAT:0007018`](https://w3id.org/nfdi4cat/voc4cat_0007018)

**Schema Reference:** [ReactorDesignType](./elements/classes/ReactorDesignType.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ReactorDesignType target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of ReactorDesignType:**

<details markdown="1">
<summary><strong>ElectrochemicalReactor</strong></summary>

**Description:** Electrochemical reactor used in electrocatalytic experiments, including
H-cells, flow cells, and membrane electrode assemblies.

**CURIE:** [`VOC4CAT:0000193`](https://w3id.org/nfdi4cat/voc4cat_0000193)

**Schema Reference:** [ElectrochemicalReactor](./elements/classes/ElectrochemicalReactor.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectrochemicalReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CSTR</strong></summary>

**Description:** Continuous stirred tank reactor (CSTR) — a well-mixed, continuous-flow
reactor operating at steady state.

**CURIE:** [`VOC4CAT:0007019`](https://w3id.org/nfdi4cat/voc4cat_0007019)

**Schema Reference:** [CSTR](./elements/classes/CSTR.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CSTR target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PlugFlowReactor</strong></summary>

**Description:** Plug flow reactor (PFR) — a tubular reactor in which reactant composition
varies along the axis with no axial mixing.

**CURIE:** [`VOC4CAT:0007102`](https://w3id.org/nfdi4cat/voc4cat_0007102)

**Schema Reference:** [PlugFlowReactor](./elements/classes/PlugFlowReactor.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlugFlowReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Autoclave</strong></summary>

**Description:** Autoclave reactor — a sealed pressure vessel for batch reactions at
elevated temperature and/or pressure.

**CURIE:** [`NCIT:C93052`](http://purl.obolibrary.org/obo/NCIT_C93052)

**Schema Reference:** [Autoclave](./elements/classes/Autoclave.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Autoclave target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SlurryReactor</strong></summary>

**Description:** Slurry reactor — a three-phase reactor in which catalyst particles are
suspended in a liquid phase through which gas is bubbled.

**CURIE:** [`coremeta4cat:SlurryReactor`](https://w3id.org/nfdi4cat/coremeta4cat/SlurryReactor)

**Schema Reference:** [SlurryReactor](./elements/classes/SlurryReactor.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SlurryReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Microreactor</strong></summary>

**Description:** Microreactor — a miniaturised flow reactor with characteristic dimensions
in the sub-millimetre range, enabling precise thermal control and rapid
screening.

**CURIE:** [`VOC4CAT:0000234`](https://w3id.org/nfdi4cat/voc4cat_0000234)

**Schema Reference:** [Microreactor](./elements/classes/Microreactor.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Microreactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>FixedBedReactor</strong></summary>

**Description:** Fixed bed reactor — a tubular reactor packed with a stationary catalyst bed.
The most common reactor type in heterogeneous catalysis testing.

**CURIE:** [`coremeta4cat:FixedBedReactor`](https://w3id.org/nfdi4cat/coremeta4cat/FixedBedReactor)

**Schema Reference:** [FixedBedReactor](./elements/classes/FixedBedReactor.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FixedBedReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
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

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FluidizedBedReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carried_out_by target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>product identification method</strong> (Mandatory, Multivalued)</summary>

**Description:** The analytical method used to identify and/or quantify reaction products.
Should reference a CharacterizationTechnique instance (e.g. a GCMS or
HPLC_MS object from coremeta4cat_characterization_ap). The abstract stub
ProductIdentificationMethod is retained for backward compatibility.

**Data Type:** ProductIdentificationMethod

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:product_identification_method`](https://w3id.org/nfdi4cat/coremeta4cat/product_identification_method)

**Schema Reference:** [product_identification_method](./elements/slots/product_identification_method.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>ProductIdentificationMethod</strong></summary>

**Description:** Abstract Plan representing the method used to identify and quantify reaction
products. In practice, users should reference a concrete CharacterizationTechnique
subclass from coremeta4cat_characterization_ap (e.g. GCMS, HPLC_MS, NMRSpectroscopy).

This abstract class is retained for backward compatibility with the original
CoreMeta4Cat monolith. It is a subclass of Plan (prov:Plan / OBI:0000272) so that
it can participate in the realized_plan slot if needed.

**CURIE:** [`OBI:0000272`](http://purl.obolibrary.org/obo/OBI_0000272)

**Schema Reference:** [ProductIdentificationMethod](./elements/classes/ProductIdentificationMethod.md)

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

