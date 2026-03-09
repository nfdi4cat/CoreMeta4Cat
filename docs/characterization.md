# Characterization

The Characterization data class documents experimental techniques used to determine structural, electronic, compositional, and physicochemical properties of catalysts. It captures both measurement parameters and relevant contextual information required for interpretation and comparison.

The class follows a hierarchical structure in which selection of a characterization technique activates technique-specific metadata fields (e.g., radiation source for X-ray diffraction or solvent for nuclear magnetic resonance spectroscopy). Metadata on sample preparation and pre-treatment are also included, as these factors directly influence measurement outcomes.

**CURIE:** [`OBI:0000070`](OBI:0000070)

<iframe
    src="/CoreMeta4Cat/assets/metadata_characterization_hierarchy.html"
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
<summary><strong>sample state</strong> (Optional, Multivalued)</summary>

**Description:** Physical state of the sample during characterization.

**Data Type:** SampleStateEnum

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sample_state`](https://w3id.org/nfdi4cat/coremeta4cat/sample_state)

**Schema Reference:** [sample_state](./elements/slots/sample_state.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_state target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>sample description</strong> (Optional, Multivalued)</summary>

**Description:** Free-text description of the sample used in this characterization.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sample_description`](https://w3id.org/nfdi4cat/coremeta4cat/sample_description)

**Schema Reference:** [sample_description](./elements/slots/sample_description.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_description target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>sample preparation</strong> (Optional, Multivalued)</summary>

**Description:** Sample preparation steps applied immediately before measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFP:0001159`](http://purl.allotrope.org/ontologies/process#AFP_0001159)

**Schema Reference:** [sample_preparation](./elements/slots/sample_preparation.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_preparation target="_blank" class="md-button md-button--primary">
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
<summary><strong>detector type</strong> (Optional, Multivalued)</summary>

**Description:** Type of detector used in the measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000317`](http://purl.allotrope.org/ontologies/result#AFR_0000317)

**Schema Reference:** [detector_type](./elements/slots/detector_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20detector_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>realized plan</strong> (Mandatory)</summary>

**Description:** The CharacterizationTechnique (protocol) realized in this Characterization.

**Data Type:** CharacterizationTechnique

**Cardinality:**  Mandatory

**Schema Reference:** [realized_plan](./elements/slots/realized_plan.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>CharacterizationTechnique</strong></summary>

**Abstract Class**

**Description:** An abstract Plan describing the analytical protocol used to characterize
a catalyst. Concrete subclasses specify technique-specific parameters.
Linked from Characterization via realized_plan.

**CURIE:** [`OBI:0000272`](http://purl.obolibrary.org/obo/OBI_0000272)

**Schema Reference:** [CharacterizationTechnique](./elements/classes/CharacterizationTechnique.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CharacterizationTechnique target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of CharacterizationTechnique:**

<details markdown="1">
<summary><strong>PowderXRD</strong></summary>

**Description:** Powder X-ray diffraction for phase identification and structural analysis.

**CURIE:** [`CHMO:0000158`](http://purl.obolibrary.org/obo/CHMO_0000158)

**Schema Reference:** [PowderXRD](./elements/classes/PowderXRD.md)

**Slots**

<details markdown="1">
<summary><strong>minimum 2theta</strong> (Optional, Multivalued)</summary>

**Description:** Minimum 2theta angle in the diffraction scan.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_2theta`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_2theta)

**Schema Reference:** [minimum_2theta](./elements/slots/minimum_2theta.md)

**Unit:** deg

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_2theta target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum 2theta</strong> (Optional, Multivalued)</summary>

**Description:** Maximum 2theta angle in the diffraction scan.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_2theta`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_2theta)

**Schema Reference:** [maximum_2theta](./elements/slots/maximum_2theta.md)

**Unit:** deg

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_2theta target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for a scan (angle, wavelength, energy, or potential).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/slots/step_size.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of an instrument (e.g. transmission, reflection, AC, DC).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/slots/operation_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode target="_blank" class="md-button md-button--primary">
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
<summary><strong>sample spinning speed</strong> (Optional, Multivalued)</summary>

**Description:** Sample spinning speed during XRD measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sample_spinning_speed`](https://w3id.org/nfdi4cat/coremeta4cat/sample_spinning_speed)

**Schema Reference:** [sample_spinning_speed](./elements/slots/sample_spinning_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_spinning_speed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
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

<details markdown="1">
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used (e.g. Cu K-alpha, Mo K-alpha, synchrotron).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/slots/xray_source.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>monochromator</strong> (Optional, Multivalued)</summary>

**Description:** Monochromator type or configuration used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002120`](http://purl.obolibrary.org/obo/CHMO_0002120)

**Schema Reference:** [monochromator](./elements/slots/monochromator.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20monochromator target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PowderXRD target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SingleCrystalXRD</strong></summary>

**Description:** Single crystal X-ray diffraction for structure determination.

**CURIE:** [`CHMO:0000852`](http://purl.obolibrary.org/obo/CHMO_0000852)

**Schema Reference:** [SingleCrystalXRD](./elements/classes/SingleCrystalXRD.md)

**Slots**

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
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used (e.g. Cu K-alpha, Mo K-alpha, synchrotron).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/slots/xray_source.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>monochromator</strong> (Optional, Multivalued)</summary>

**Description:** Monochromator type or configuration used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002120`](http://purl.obolibrary.org/obo/CHMO_0002120)

**Schema Reference:** [monochromator](./elements/slots/monochromator.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20monochromator target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SingleCrystalXRD target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>XRayAbsorptionSpectroscopy</strong></summary>

**Description:** X-ray absorption spectroscopy (XAS/XANES/EXAFS) for electronic and local structure analysis.

**CURIE:** [`VOC4CAT:0000286`](https://w3id.org/nfdi4cat/voc4cat_0000286)

**Schema Reference:** [XRayAbsorptionSpectroscopy](./elements/classes/XRayAbsorptionSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of an instrument (e.g. transmission, reflection, AC, DC).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/slots/operation_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>element analyzed</strong> (Optional, Multivalued)</summary>

**Description:** Chemical element analysed (e.g. Fe, Cu, Pt).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:element_analyzed`](https://w3id.org/nfdi4cat/coremeta4cat/element_analyzed)

**Schema Reference:** [element_analyzed](./elements/slots/element_analyzed.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20element_analyzed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>absorption edge</strong> (Optional, Multivalued)</summary>

**Description:** X-ray absorption edge measured (e.g. K-edge, L3-edge).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:absorption_edge`](https://w3id.org/nfdi4cat/coremeta4cat/absorption_edge)

**Schema Reference:** [absorption_edge](./elements/slots/absorption_edge.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20absorption_edge target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy resolution</strong> (Optional, Multivalued)</summary>

**Description:** Energy resolution of the spectrometer or monochromator.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [energy_resolution](./elements/slots/energy_resolution.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_resolution target="_blank" class="md-button md-button--primary">
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
<summary><strong>beamline source</strong> (Optional, Multivalued)</summary>

**Description:** Synchrotron beamline or X-ray source identifier.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:beamline_source`](https://w3id.org/nfdi4cat/coremeta4cat/beamline_source)

**Schema Reference:** [beamline_source](./elements/slots/beamline_source.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20beamline_source target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>noise of measurement</strong> (Optional, Multivalued)</summary>

**Description:** Noise level of the XAS measurement (signal-to-noise ratio).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:noise_of_measurement`](https://w3id.org/nfdi4cat/coremeta4cat/noise_of_measurement)

**Schema Reference:** [noise_of_measurement](./elements/slots/noise_of_measurement.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20noise_of_measurement target="_blank" class="md-button md-button--primary">
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
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used (e.g. Cu K-alpha, Mo K-alpha, synchrotron).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/slots/xray_source.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>monochromator</strong> (Optional, Multivalued)</summary>

**Description:** Monochromator type or configuration used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002120`](http://purl.obolibrary.org/obo/CHMO_0002120)

**Schema Reference:** [monochromator](./elements/slots/monochromator.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20monochromator target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum energy</strong> (Optional, Multivalued)</summary>

**Description:** Minimum energy of the scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_energy`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_energy)

**Schema Reference:** [minimum_energy](./elements/slots/minimum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum energy</strong> (Optional, Multivalued)</summary>

**Description:** Maximum energy of the scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_energy`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_energy)

**Schema Reference:** [maximum_energy](./elements/slots/maximum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20XRayAbsorptionSpectroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>XPS</strong></summary>

**Description:** X-ray photoelectron spectroscopy for surface elemental and chemical state analysis.

**CURIE:** [`CHMO:0000404`](http://purl.obolibrary.org/obo/CHMO_0000404)

**Schema Reference:** [XPS](./elements/classes/XPS.md)

**Slots**

<details markdown="1">
<summary><strong>total acquisition time</strong> (Optional, Multivalued)</summary>

**Description:** Total time for XPS spectrum acquisition.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:total_acquisition_time`](https://w3id.org/nfdi4cat/coremeta4cat/total_acquisition_time)

**Schema Reference:** [total_acquisition_time](./elements/slots/total_acquisition_time.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20total_acquisition_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans or accumulations recorded.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_scans`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_scans)

**Schema Reference:** [number_of_scans](./elements/slots/number_of_scans.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for a scan (angle, wavelength, energy, or potential).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/slots/step_size.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pass energy</strong> (Optional, Multivalued)</summary>

**Description:** Analyser pass energy setting in XPS.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:pass_energy`](https://w3id.org/nfdi4cat/coremeta4cat/pass_energy)

**Schema Reference:** [pass_energy](./elements/slots/pass_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pass_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spot size</strong> (Optional, Multivalued)</summary>

**Description:** X-ray spot size on the sample surface.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:spot_size`](https://w3id.org/nfdi4cat/coremeta4cat/spot_size)

**Schema Reference:** [spot_size](./elements/slots/spot_size.md)

**Unit:** mm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spot_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>lense mode</strong> (Optional, Multivalued)</summary>

**Description:** Electron lens mode setting in XPS analyser.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [lense_mode](./elements/slots/lense_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20lense_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>charge compensation</strong> (Optional, Multivalued)</summary>

**Description:** Charge compensation method applied during XPS measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:charge_compensation`](https://w3id.org/nfdi4cat/coremeta4cat/charge_compensation)

**Schema Reference:** [charge_compensation](./elements/slots/charge_compensation.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20charge_compensation target="_blank" class="md-button md-button--primary">
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
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used (e.g. Cu K-alpha, Mo K-alpha, synchrotron).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/slots/xray_source.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>monochromator</strong> (Optional, Multivalued)</summary>

**Description:** Monochromator type or configuration used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002120`](http://purl.obolibrary.org/obo/CHMO_0002120)

**Schema Reference:** [monochromator](./elements/slots/monochromator.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20monochromator target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum energy</strong> (Optional, Multivalued)</summary>

**Description:** Minimum energy of the scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_energy`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_energy)

**Schema Reference:** [minimum_energy](./elements/slots/minimum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum energy</strong> (Optional, Multivalued)</summary>

**Description:** Maximum energy of the scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_energy`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_energy)

**Schema Reference:** [maximum_energy](./elements/slots/maximum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20XPS target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>EDX</strong></summary>

**Description:** Energy-dispersive X-ray spectroscopy for elemental mapping and quantification.

**CURIE:** [`CHMO:0000309`](http://purl.obolibrary.org/obo/CHMO_0000309)

**Schema Reference:** [EDX](./elements/classes/EDX.md)

**Slots**

<details markdown="1">
<summary><strong>primary energy</strong> (Optional, Multivalued)</summary>

**Description:** Primary electron beam energy for EDX excitation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:primary_energy`](https://w3id.org/nfdi4cat/coremeta4cat/primary_energy)

**Schema Reference:** [primary_energy](./elements/slots/primary_energy.md)

**Unit:** keV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20primary_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>counting time</strong> (Optional, Multivalued)</summary>

**Description:** X-ray counting time per point or spectrum.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:counting_time`](https://w3id.org/nfdi4cat/coremeta4cat/counting_time)

**Schema Reference:** [counting_time](./elements/slots/counting_time.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20counting_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>resolution</strong> (Optional, Multivalued)</summary>

**Description:** Resolution of a measurement or detector.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:resolution`](https://w3id.org/nfdi4cat/coremeta4cat/resolution)

**Schema Reference:** [resolution](./elements/slots/resolution.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20resolution target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calibration method</strong> (Optional, Multivalued)</summary>

**Description:** Calibration method applied during a measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:calibration_method`](https://w3id.org/nfdi4cat/coremeta4cat/calibration_method)

**Schema Reference:** [calibration_method](./elements/slots/calibration_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calibration_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20EDX target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>InfraredSpectroscopy</strong></summary>

**Description:** Infrared spectroscopy (FTIR/ATR) for functional group and surface species identification.

**CURIE:** [`coremeta4cat:InfraredSpectroscopy`](https://w3id.org/nfdi4cat/coremeta4cat/InfraredSpectroscopy)

**Schema Reference:** [InfraredSpectroscopy](./elements/classes/InfraredSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of an instrument (e.g. transmission, reflection, AC, DC).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/slots/operation_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum wavenumber</strong> (Optional, Multivalued)</summary>

**Description:** Minimum wavenumber of the IR scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_wavenumber`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_wavenumber)

**Schema Reference:** [minimum_wavenumber](./elements/slots/minimum_wavenumber.md)

**Unit:** cm-1

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_wavenumber target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum wavenumber</strong> (Optional, Multivalued)</summary>

**Description:** Maximum wavenumber of the IR scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_wavenumber`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_wavenumber)

**Schema Reference:** [maximum_wavenumber](./elements/slots/maximum_wavenumber.md)

**Unit:** cm-1

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_wavenumber target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for a scan (angle, wavelength, energy, or potential).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/slots/step_size.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size target="_blank" class="md-button md-button--primary">
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
<summary><strong>background correction</strong> (Optional, Multivalued)</summary>

**Description:** Background correction method applied to IR spectra.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFP:0003721`](http://purl.allotrope.org/ontologies/process#AFP_0003721)

**Schema Reference:** [background_correction](./elements/slots/background_correction.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20background_correction target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans or accumulations recorded.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_scans`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_scans)

**Schema Reference:** [number_of_scans](./elements/slots/number_of_scans.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans target="_blank" class="md-button md-button--primary">
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
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20InfraredSpectroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>DRIFTS</strong></summary>

**Description:** Diffuse reflectance infrared Fourier transform spectroscopy for in-situ
surface species identification under reactive gas conditions.

**CURIE:** [`CHMO:0000645`](http://purl.obolibrary.org/obo/CHMO_0000645)

**Schema Reference:** [DRIFTS](./elements/classes/DRIFTS.md)

**Slots**

<details markdown="1">
<summary><strong>adsorption gas</strong> (Optional, Multivalued)</summary>

**Description:** Probe gas adsorbed during in-situ DRIFTS measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:adsorption_gas`](https://w3id.org/nfdi4cat/coremeta4cat/adsorption_gas)

**Schema Reference:** [adsorption_gas](./elements/slots/adsorption_gas.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20adsorption_gas target="_blank" class="md-button md-button--primary">
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
<summary><strong>diluting reference</strong> (Optional, Multivalued)</summary>

**Description:** Reference material used to dilute the DRIFTS sample (e.g. KBr).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:diluting_reference`](https://w3id.org/nfdi4cat/coremeta4cat/diluting_reference)

**Schema Reference:** [diluting_reference](./elements/slots/diluting_reference.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20diluting_reference target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ratio reference sample</strong> (Optional, Multivalued)</summary>

**Description:** Mass ratio of reference material to catalyst sample in DRIFTS cup.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ratio_reference_sample`](https://w3id.org/nfdi4cat/coremeta4cat/ratio_reference_sample)

**Schema Reference:** [ratio_reference_sample](./elements/slots/ratio_reference_sample.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ratio_reference_sample target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for a scan (angle, wavelength, energy, or potential).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/slots/step_size.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>resolution</strong> (Optional, Multivalued)</summary>

**Description:** Resolution of a measurement or detector.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:resolution`](https://w3id.org/nfdi4cat/coremeta4cat/resolution)

**Schema Reference:** [resolution](./elements/slots/resolution.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20resolution target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>background correction method</strong> (Optional, Multivalued)</summary>

**Description:** Specific background correction method used in DRIFTS.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:background_correction_method`](https://w3id.org/nfdi4cat/coremeta4cat/background_correction_method)

**Schema Reference:** [background_correction_method](./elements/slots/background_correction_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20background_correction_method target="_blank" class="md-button md-button--primary">
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
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans or accumulations recorded.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_scans`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_scans)

**Schema Reference:** [number_of_scans](./elements/slots/number_of_scans.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DRIFTS target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>RamanSpectroscopy</strong></summary>

**Description:** Raman spectroscopy for vibrational and structural characterization.

**CURIE:** [`VOC4CAT:0000069`](https://w3id.org/nfdi4cat/voc4cat_0000069)

**Schema Reference:** [RamanSpectroscopy](./elements/classes/RamanSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>excitation laser wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Wavelength of excitation laser used in Raman spectroscopy.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001594`](http://purl.allotrope.org/ontologies/result#AFR_0001594)

**Schema Reference:** [excitation_laser_wavelength](./elements/slots/excitation_laser_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_laser_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>excitation laser power</strong> (Optional, Multivalued)</summary>

**Description:** Power of the excitation laser at the sample.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001595`](http://purl.allotrope.org/ontologies/result#AFR_0001595)

**Schema Reference:** [excitation_laser_power](./elements/slots/excitation_laser_power.md)

**Unit:** mW

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_laser_power target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>magnification setting</strong> (Optional, Multivalued)</summary>

**Description:** Magnification setting used for imaging.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002226`](http://purl.allotrope.org/ontologies/result#AFR_0002226)

**Schema Reference:** [magnification_setting](./elements/slots/magnification_setting.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20magnification_setting target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>integration time</strong> (Optional, Multivalued)</summary>

**Description:** Integration or acquisition time per measurement step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:integration_time`](https://w3id.org/nfdi4cat/coremeta4cat/integration_time)

**Schema Reference:** [integration_time](./elements/slots/integration_time.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20integration_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans or accumulations recorded.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_scans`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_scans)

**Schema Reference:** [number_of_scans](./elements/slots/number_of_scans.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans target="_blank" class="md-button md-button--primary">
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
<summary><strong>filter or grating</strong> (Optional, Multivalued)</summary>

**Description:** Optical filter or grating used in Raman spectrometer.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:filter_or_grating`](https://w3id.org/nfdi4cat/coremeta4cat/filter_or_grating)

**Schema Reference:** [filter_or_grating](./elements/slots/filter_or_grating.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_or_grating target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20RamanSpectroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>NMRSpectroscopy</strong></summary>

**Description:** Nuclear magnetic resonance spectroscopy for structure elucidation.
Note: for detailed liquid-state NMR minimum information, the dedicated
nmr_dcat_ap profile (MARGARITAS) should be used in combination with
this subprofile.

**CURIE:** [`VOC4CAT:0000073`](https://w3id.org/nfdi4cat/voc4cat_0000073)

**Schema Reference:** [NMRSpectroscopy](./elements/classes/NMRSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>nucleus</strong> (Optional, Multivalued)</summary>

**Description:** NMR-active nucleus observed (e.g. 1H, 13C, 31P).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:nucleus`](https://w3id.org/nfdi4cat/coremeta4cat/nucleus)

**Schema Reference:** [nucleus](./elements/slots/nucleus.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nucleus target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
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

<details markdown="1">
<summary><strong>irradiation frequency</strong> (Optional, Multivalued)</summary>

**Description:** Irradiation frequency of the NMR spectrometer.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:irradiation_frequency`](https://w3id.org/nfdi4cat/coremeta4cat/irradiation_frequency)

**Schema Reference:** [irradiation_frequency](./elements/slots/irradiation_frequency.md)

**Unit:** MHz

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20irradiation_frequency target="_blank" class="md-button md-button--primary">
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
<summary><strong>nmr pulse sequence</strong> (Optional, Multivalued)</summary>

**Description:** NMR pulse sequence used (e.g. zgpg30, dept).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:nmr_pulse_sequence`](https://w3id.org/nfdi4cat/coremeta4cat/nmr_pulse_sequence)

**Schema Reference:** [nmr_pulse_sequence](./elements/slots/nmr_pulse_sequence.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nmr_pulse_sequence target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>nmr sample tube</strong> (Optional, Multivalued)</summary>

**Description:** NMR sample tube type (e.g. 5mm standard, Shigemi tube).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:nmr_sample_tube`](https://w3id.org/nfdi4cat/coremeta4cat/nmr_sample_tube)

**Schema Reference:** [nmr_sample_tube](./elements/slots/nmr_sample_tube.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nmr_sample_tube target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans or accumulations recorded.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_scans`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_scans)

**Schema Reference:** [number_of_scans](./elements/slots/number_of_scans.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans target="_blank" class="md-button md-button--primary">
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
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20NMRSpectroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>TransmissionElectronMicroscopy</strong></summary>

**Description:** TEM for atomic-resolution imaging and diffraction of catalyst particles.

**CURIE:** [`VOC4CAT:0000078`](https://w3id.org/nfdi4cat/voc4cat_0000078)

**Schema Reference:** [TransmissionElectronMicroscopy](./elements/classes/TransmissionElectronMicroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of an instrument (e.g. transmission, reflection, AC, DC).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/slots/operation_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gun type</strong> (Optional, Multivalued)</summary>

**Description:** Type of electron gun (e.g. FEG, thermionic LaB6).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gun_type`](https://w3id.org/nfdi4cat/coremeta4cat/gun_type)

**Schema Reference:** [gun_type](./elements/slots/gun_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gun_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acceleration voltage</strong> (Optional, Multivalued)</summary>

**Description:** Acceleration voltage applied to the electron beam.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:acceleration_voltage`](https://w3id.org/nfdi4cat/coremeta4cat/acceleration_voltage)

**Schema Reference:** [acceleration_voltage](./elements/slots/acceleration_voltage.md)

**Unit:** kV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acceleration_voltage target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>magnification setting</strong> (Optional, Multivalued)</summary>

**Description:** Magnification setting used for imaging.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002226`](http://purl.allotrope.org/ontologies/result#AFR_0002226)

**Schema Reference:** [magnification_setting](./elements/slots/magnification_setting.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20magnification_setting target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20TransmissionElectronMicroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ScanningElectronMicroscopy</strong></summary>

**Description:** SEM for surface morphology and particle size/shape imaging.

**CURIE:** [`VOC4CAT:0000075`](https://w3id.org/nfdi4cat/voc4cat_0000075)

**Schema Reference:** [ScanningElectronMicroscopy](./elements/classes/ScanningElectronMicroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>image resolution</strong> (Optional, Multivalued)</summary>

**Description:** Spatial resolution of SEM images.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:image_resolution`](https://w3id.org/nfdi4cat/coremeta4cat/image_resolution)

**Schema Reference:** [image_resolution](./elements/slots/image_resolution.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20image_resolution target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>field emitter</strong> (Optional, Multivalued)</summary>

**Description:** Type of field emitter used in FE-SEM instrument.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:field_emitter`](https://w3id.org/nfdi4cat/coremeta4cat/field_emitter)

**Schema Reference:** [field_emitter](./elements/slots/field_emitter.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20field_emitter target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gun type</strong> (Optional, Multivalued)</summary>

**Description:** Type of electron gun (e.g. FEG, thermionic LaB6).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gun_type`](https://w3id.org/nfdi4cat/coremeta4cat/gun_type)

**Schema Reference:** [gun_type](./elements/slots/gun_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gun_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acceleration voltage</strong> (Optional, Multivalued)</summary>

**Description:** Acceleration voltage applied to the electron beam.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:acceleration_voltage`](https://w3id.org/nfdi4cat/coremeta4cat/acceleration_voltage)

**Schema Reference:** [acceleration_voltage](./elements/slots/acceleration_voltage.md)

**Unit:** kV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acceleration_voltage target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>magnification setting</strong> (Optional, Multivalued)</summary>

**Description:** Magnification setting used for imaging.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002226`](http://purl.allotrope.org/ontologies/result#AFR_0002226)

**Schema Reference:** [magnification_setting](./elements/slots/magnification_setting.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20magnification_setting target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ScanningElectronMicroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Thermogravimetry</strong></summary>

**Description:** Thermogravimetric analysis (TGA/DTG) for mass loss, decomposition, and oxidation state characterization.

**CURIE:** [`CHMO:0000690`](http://purl.obolibrary.org/obo/CHMO_0000690)

**Schema Reference:** [Thermogravimetry](./elements/classes/Thermogravimetry.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of an instrument (e.g. transmission, reflection, AC, DC).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/slots/operation_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode target="_blank" class="md-button md-button--primary">
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
<summary><strong>initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature at the start of a thermal analysis run.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C164644`](http://purl.obolibrary.org/obo/NCIT_C164644)

**Schema Reference:** [initial_temperature](./elements/slots/initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20initial_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature at the end of a thermal analysis run.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C164644`](http://purl.obolibrary.org/obo/NCIT_C164644)

**Schema Reference:** [final_temperature](./elements/slots/final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20final_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample mass</strong> (Optional, Multivalued)</summary>

**Description:** Mass of the sample used in a process or measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sample_mass`](https://w3id.org/nfdi4cat/coremeta4cat/sample_mass)

**Schema Reference:** [sample_mass](./elements/slots/sample_mass.md)

**Unit:** mg

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum (start) temperature in a temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_temperature)

**Schema Reference:** [minimum_temperature](./elements/slots/minimum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum (final) temperature in a temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_temperature)

**Schema Reference:** [maximum_temperature](./elements/slots/maximum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate at which temperature is increased during a process.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_rate`](https://w3id.org/nfdi4cat/coremeta4cat/heating_rate)

**Schema Reference:** [heating_rate](./elements/slots/heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating procedure</strong> (Optional, Multivalued)</summary>

**Description:** Description of the heating procedure applied.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_procedure`](https://w3id.org/nfdi4cat/coremeta4cat/heating_procedure)

**Schema Reference:** [heating_procedure](./elements/slots/heating_procedure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_procedure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Thermogravimetry target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>TPR</strong></summary>

**Description:** Temperature-programmed reduction for reducibility and metal-support interaction characterization.

**CURIE:** [`CHMO:0002908`](http://purl.obolibrary.org/obo/CHMO_0002908)

**Schema Reference:** [TPR](./elements/classes/TPR.md)

**Slots**

<details markdown="1">
<summary><strong>reducing gas composition</strong> (Optional, Multivalued)</summary>

**Description:** Composition of reducing gas used in TPR (e.g. 5% H2/Ar).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:reducing_gas_composition`](https://w3id.org/nfdi4cat/coremeta4cat/reducing_gas_composition)

**Schema Reference:** [reducing_gas_composition](./elements/slots/reducing_gas_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reducing_gas_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum (start) temperature in a temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_temperature)

**Schema Reference:** [minimum_temperature](./elements/slots/minimum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum (final) temperature in a temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_temperature)

**Schema Reference:** [maximum_temperature](./elements/slots/maximum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate at which temperature is increased during a process.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_rate`](https://w3id.org/nfdi4cat/coremeta4cat/heating_rate)

**Schema Reference:** [heating_rate](./elements/slots/heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating procedure</strong> (Optional, Multivalued)</summary>

**Description:** Description of the heating procedure applied.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_procedure`](https://w3id.org/nfdi4cat/coremeta4cat/heating_procedure)

**Schema Reference:** [heating_procedure](./elements/slots/heating_procedure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_procedure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20TPR target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>TPO</strong></summary>

**Description:** Temperature-programmed oxidation for coke quantification and reoxidation characterization.

**CURIE:** [`CHMO:0002907`](http://purl.obolibrary.org/obo/CHMO_0002907)

**Schema Reference:** [TPO](./elements/classes/TPO.md)

**Slots**

<details markdown="1">
<summary><strong>oxidizing gas composition</strong> (Optional, Multivalued)</summary>

**Description:** Composition of oxidising gas used in TPO (e.g. 5% O2/Ar).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:oxidizing_gas_composition`](https://w3id.org/nfdi4cat/coremeta4cat/oxidizing_gas_composition)

**Schema Reference:** [oxidizing_gas_composition](./elements/slots/oxidizing_gas_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20oxidizing_gas_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum (start) temperature in a temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_temperature)

**Schema Reference:** [minimum_temperature](./elements/slots/minimum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum (final) temperature in a temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_temperature)

**Schema Reference:** [maximum_temperature](./elements/slots/maximum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate at which temperature is increased during a process.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_rate`](https://w3id.org/nfdi4cat/coremeta4cat/heating_rate)

**Schema Reference:** [heating_rate](./elements/slots/heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating procedure</strong> (Optional, Multivalued)</summary>

**Description:** Description of the heating procedure applied.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_procedure`](https://w3id.org/nfdi4cat/coremeta4cat/heating_procedure)

**Schema Reference:** [heating_procedure](./elements/slots/heating_procedure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_procedure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20TPO target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>BET</strong></summary>

**Description:** Brunauer-Emmett-Teller analysis for specific surface area and pore size distribution.

**CURIE:** [`coremeta4cat:BET`](https://w3id.org/nfdi4cat/coremeta4cat/BET)

**Schema Reference:** [BET](./elements/classes/BET.md)

**Slots**

<details markdown="1">
<summary><strong>adsorbate gas</strong> (Optional, Multivalued)</summary>

**Description:** Adsorbate gas used in BET surface area measurement (e.g. N2, Ar).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:adsorbate_gas`](https://w3id.org/nfdi4cat/coremeta4cat/adsorbate_gas)

**Schema Reference:** [adsorbate_gas](./elements/slots/adsorbate_gas.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20adsorbate_gas target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>degassing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature at which sample is degassed before BET measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:degassing_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/degassing_temperature)

**Schema Reference:** [degassing_temperature](./elements/slots/degassing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20degassing_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>measurement temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature at which BET adsorption isotherm is measured (e.g. 77 K for N2).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:measurement_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/measurement_temperature)

**Schema Reference:** [measurement_temperature](./elements/slots/measurement_temperature.md)

**Unit:** K

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20measurement_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pore size distribution method</strong> (Optional, Multivalued)</summary>

**Description:** Method used for pore size distribution calculation (e.g. BJH, DFT, HK).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:pore_size_distribution_method`](https://w3id.org/nfdi4cat/coremeta4cat/pore_size_distribution_method)

**Schema Reference:** [pore_size_distribution_method](./elements/slots/pore_size_distribution_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pore_size_distribution_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample mass</strong> (Optional, Multivalued)</summary>

**Description:** Mass of the sample used in a process or measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sample_mass`](https://w3id.org/nfdi4cat/coremeta4cat/sample_mass)

**Schema Reference:** [sample_mass](./elements/slots/sample_mass.md)

**Unit:** mg

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_mass target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20BET target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ICPAES</strong></summary>

**Description:** Inductively coupled plasma atomic emission spectroscopy for bulk elemental composition.

**CURIE:** [`CHMO:0000267`](http://purl.obolibrary.org/obo/CHMO_0000267)

**Schema Reference:** [ICPAES](./elements/classes/ICPAES.md)

**Slots**

<details markdown="1">
<summary><strong>element analyzed</strong> (Optional, Multivalued)</summary>

**Description:** Chemical element analysed (e.g. Fe, Cu, Pt).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:element_analyzed`](https://w3id.org/nfdi4cat/coremeta4cat/element_analyzed)

**Schema Reference:** [element_analyzed](./elements/slots/element_analyzed.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20element_analyzed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calibration method</strong> (Optional, Multivalued)</summary>

**Description:** Calibration method applied during a measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:calibration_method`](https://w3id.org/nfdi4cat/coremeta4cat/calibration_method)

**Schema Reference:** [calibration_method](./elements/slots/calibration_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calibration_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>detection limit</strong> (Optional, Multivalued)</summary>

**Description:** Detection limit of the analytical method.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C105701`](http://purl.obolibrary.org/obo/NCIT_C105701)

**Schema Reference:** [detection_limit](./elements/slots/detection_limit.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20detection_limit target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>matrix effect correction</strong> (Optional, Multivalued)</summary>

**Description:** Method used to correct for matrix effects in ICP-AES.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:matrix_effect_correction`](https://w3id.org/nfdi4cat/coremeta4cat/matrix_effect_correction)

**Schema Reference:** [matrix_effect_correction](./elements/slots/matrix_effect_correction.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20matrix_effect_correction target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ICPAES target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ElementalAnalysis</strong></summary>

**Description:** Combustion elemental analysis (CHNS/O) for carbon, hydrogen, nitrogen, sulfur content.

**CURIE:** [`CHMO:0001075`](http://purl.obolibrary.org/obo/CHMO_0001075)

**Schema Reference:** [ElementalAnalysis](./elements/classes/ElementalAnalysis.md)

**Slots**

<details markdown="1">
<summary><strong>elements analyzed</strong> (Optional, Multivalued)</summary>

**Description:** List of elements analysed by combustion elemental analysis (e.g. C, H, N, S).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:elements_analyzed`](https://w3id.org/nfdi4cat/coremeta4cat/elements_analyzed)

**Schema Reference:** [elements_analyzed](./elements/slots/elements_analyzed.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20elements_analyzed target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>combustion temperature</strong> (Optional, Multivalued)</summary>

**Description:** Combustion furnace temperature for elemental analysis.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:combustion_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/combustion_temperature)

**Schema Reference:** [combustion_temperature](./elements/slots/combustion_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20combustion_temperature target="_blank" class="md-button md-button--primary">
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
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElementalAnalysis target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>UVVisSpectroscopy</strong></summary>

**Description:** UV-Vis spectroscopy for electronic transitions, band gap, and concentration determination.

**CURIE:** [`VOC4CAT:0000079`](https://w3id.org/nfdi4cat/voc4cat_0000079)

**Schema Reference:** [UVVisSpectroscopy](./elements/classes/UVVisSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>minimum wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Minimum wavelength of the UV-Vis scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_wavelength`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_wavelength)

**Schema Reference:** [minimum_wavelength](./elements/slots/minimum_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Maximum wavelength of the UV-Vis scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_wavelength`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_wavelength)

**Schema Reference:** [maximum_wavelength](./elements/slots/maximum_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>path length</strong> (Optional, Multivalued)</summary>

**Description:** Optical path length of the measurement cell.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFQ:0000268`](http://purl.allotrope.org/ontologies/quality#AFQ_0000268)

**Schema Reference:** [path_length](./elements/slots/path_length.md)

**Unit:** cm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20path_length target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
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

<details markdown="1">
<summary><strong>concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of a substance in a sample or solution.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:concentration`](https://w3id.org/nfdi4cat/coremeta4cat/concentration)

**Schema Reference:** [concentration](./elements/slots/concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20UVVisSpectroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PhotoluminescenceSpectroscopy</strong></summary>

**Description:** Photoluminescence spectroscopy for defect and charge carrier characterization.

**CURIE:** [`coremeta4cat:PhotoluminescenceSpectroscopy`](https://w3id.org/nfdi4cat/coremeta4cat/PhotoluminescenceSpectroscopy)

**Schema Reference:** [PhotoluminescenceSpectroscopy](./elements/classes/PhotoluminescenceSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>emission range</strong> (Optional, Multivalued)</summary>

**Description:** Wavelength range over which emission is detected.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:emission_range`](https://w3id.org/nfdi4cat/coremeta4cat/emission_range)

**Schema Reference:** [emission_range](./elements/slots/emission_range.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20emission_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>slit width</strong> (Optional, Multivalued)</summary>

**Description:** Spectrometer entrance or exit slit width.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:slit_width`](https://w3id.org/nfdi4cat/coremeta4cat/slit_width)

**Schema Reference:** [slit_width](./elements/slots/slit_width.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20slit_width target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for a scan (angle, wavelength, energy, or potential).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/slots/step_size.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>integration time</strong> (Optional, Multivalued)</summary>

**Description:** Integration or acquisition time per measurement step.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:integration_time`](https://w3id.org/nfdi4cat/coremeta4cat/integration_time)

**Schema Reference:** [integration_time](./elements/slots/integration_time.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20integration_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>excitation wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Excitation wavelength used in photoluminescence measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002479`](http://purl.allotrope.org/ontologies/result#AFR_0002479)

**Schema Reference:** [excitation_wavelength](./elements/slots/excitation_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>emission wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Emission wavelength detected in photoluminescence measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C204101`](http://purl.obolibrary.org/obo/NCIT_C204101)

**Schema Reference:** [emission_wavelength](./elements/slots/emission_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20emission_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>optical filter</strong> (Optional, Multivalued)</summary>

**Description:** Optical filter used in the emission or excitation path.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:optical_filter`](https://w3id.org/nfdi4cat/coremeta4cat/optical_filter)

**Schema Reference:** [optical_filter](./elements/slots/optical_filter.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20optical_filter target="_blank" class="md-button md-button--primary">
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

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PhotoluminescenceSpectroscopy target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PhotoluminescenceLifetime</strong></summary>

**Description:** Time-resolved photoluminescence for charge carrier lifetime and recombination dynamics.

**CURIE:** [`coremeta4cat:PhotoluminescenceLifetime`](https://w3id.org/nfdi4cat/coremeta4cat/PhotoluminescenceLifetime)

**Schema Reference:** [PhotoluminescenceLifetime](./elements/classes/PhotoluminescenceLifetime.md)

**Slots**

<details markdown="1">
<summary><strong>lifetime fitting model</strong> (Optional, Multivalued)</summary>

**Description:** Mathematical model used for fluorescence lifetime fitting (e.g. mono-exponential, bi-exponential).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:lifetime_fitting_model`](https://w3id.org/nfdi4cat/coremeta4cat/lifetime_fitting_model)

**Schema Reference:** [lifetime_fitting_model](./elements/slots/lifetime_fitting_model.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20lifetime_fitting_model target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of shots</strong> (Optional, Multivalued)</summary>

**Description:** Number of laser shots accumulated per measurement point.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_shots`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_shots)

**Schema Reference:** [number_of_shots](./elements/slots/number_of_shots.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_shots target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>excitation wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Excitation wavelength used in photoluminescence measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002479`](http://purl.allotrope.org/ontologies/result#AFR_0002479)

**Schema Reference:** [excitation_wavelength](./elements/slots/excitation_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>emission wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Emission wavelength detected in photoluminescence measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C204101`](http://purl.obolibrary.org/obo/NCIT_C204101)

**Schema Reference:** [emission_wavelength](./elements/slots/emission_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20emission_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>optical filter</strong> (Optional, Multivalued)</summary>

**Description:** Optical filter used in the emission or excitation path.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:optical_filter`](https://w3id.org/nfdi4cat/coremeta4cat/optical_filter)

**Schema Reference:** [optical_filter](./elements/slots/optical_filter.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20optical_filter target="_blank" class="md-button md-button--primary">
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

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PhotoluminescenceLifetime target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CyclicVoltammetry</strong></summary>

**Description:** Cyclic voltammetry for electrochemical activity, redox potential, and capacitance characterization.

**CURIE:** [`CHMO:0000025`](http://purl.obolibrary.org/obo/CHMO_0000025)

**Schema Reference:** [CyclicVoltammetry](./elements/classes/CyclicVoltammetry.md)

**Slots**

<details markdown="1">
<summary><strong>scan rate</strong> (Optional, Multivalued)</summary>

**Description:** Potential scan rate in cyclic voltammetry.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007213`](https://w3id.org/nfdi4cat/voc4cat_0007213)

**Schema Reference:** [scan_rate](./elements/slots/scan_rate.md)

**Unit:** mV/s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20scan_rate target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum potential</strong> (Optional, Multivalued)</summary>

**Description:** Lower potential limit in cyclic voltammetry.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_potential`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_potential)

**Schema Reference:** [minimum_potential](./elements/slots/minimum_potential.md)

**Unit:** V

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_potential target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum potential</strong> (Optional, Multivalued)</summary>

**Description:** Upper potential limit in cyclic voltammetry.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_potential`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_potential)

**Schema Reference:** [maximum_potential](./elements/slots/maximum_potential.md)

**Unit:** V

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_potential target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size potential</strong> (Optional, Multivalued)</summary>

**Description:** Potential step size in cyclic voltammetry.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007218`](https://w3id.org/nfdi4cat/voc4cat_0007218)

**Schema Reference:** [step_size_potential](./elements/slots/step_size_potential.md)

**Unit:** mV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size_potential target="_blank" class="md-button md-button--primary">
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
<summary><strong>reference electrode</strong> (Optional, Multivalued)</summary>

**Description:** Reference electrode used in electrochemical cell (e.g. Ag/AgCl, RHE).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007204`](https://w3id.org/nfdi4cat/voc4cat_0007204)

**Schema Reference:** [reference_electrode](./elements/slots/reference_electrode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_electrode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>working electrode</strong> (Optional, Multivalued)</summary>

**Description:** Working electrode used in electrochemical cell.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007202`](https://w3id.org/nfdi4cat/voc4cat_0007202)

**Schema Reference:** [working_electrode](./elements/slots/working_electrode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20working_electrode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>counter electrode</strong> (Optional, Multivalued)</summary>

**Description:** Counter electrode used in electrochemical cell.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007203`](https://w3id.org/nfdi4cat/voc4cat_0007203)

**Schema Reference:** [counter_electrode](./elements/slots/counter_electrode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20counter_electrode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>electrolyte composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the electrolyte solution.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:electrolyte_composition`](https://w3id.org/nfdi4cat/coremeta4cat/electrolyte_composition)

**Schema Reference:** [electrolyte_composition](./elements/slots/electrolyte_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrolyte_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>electrolyte concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of the electrolyte.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:electrolyte_concentration`](https://w3id.org/nfdi4cat/coremeta4cat/electrolyte_concentration)

**Schema Reference:** [electrolyte_concentration](./elements/slots/electrolyte_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrolyte_concentration target="_blank" class="md-button md-button--primary">
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

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CyclicVoltammetry target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ConductivityMeasurement</strong></summary>

**Description:** Electrical conductivity measurement for ionic and electronic transport characterization.

**CURIE:** [`coremeta4cat:ConductivityMeasurement`](https://w3id.org/nfdi4cat/coremeta4cat/ConductivityMeasurement)

**Schema Reference:** [ConductivityMeasurement](./elements/classes/ConductivityMeasurement.md)

**Slots**

<details markdown="1">
<summary><strong>electrode configuration</strong> (Optional, Multivalued)</summary>

**Description:** Configuration of electrodes used in conductivity measurement (e.g. 2-probe, 4-probe).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:electrode_configuration`](https://w3id.org/nfdi4cat/coremeta4cat/electrode_configuration)

**Schema Reference:** [electrode_configuration](./elements/slots/electrode_configuration.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrode_configuration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ac frequency</strong> (Optional, Multivalued)</summary>

**Description:** Frequency of AC signal applied in impedance or conductivity measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007239`](https://w3id.org/nfdi4cat/voc4cat_0007239)

**Schema Reference:** [ac_frequency](./elements/slots/ac_frequency.md)

**Unit:** Hz

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ac_frequency target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ac dc mode</strong> (Optional, Multivalued)</summary>

**Description:** AC or DC measurement mode used in conductivity measurement.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ac_dc_mode`](https://w3id.org/nfdi4cat/coremeta4cat/ac_dc_mode)

**Schema Reference:** [ac_dc_mode](./elements/slots/ac_dc_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ac_dc_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample geometry</strong> (Optional, Multivalued)</summary>

**Description:** Geometry of the sample used in conductivity measurement (e.g. pellet, thin film).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sample_geometry`](https://w3id.org/nfdi4cat/coremeta4cat/sample_geometry)

**Schema Reference:** [sample_geometry](./elements/slots/sample_geometry.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_geometry target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reference electrode</strong> (Optional, Multivalued)</summary>

**Description:** Reference electrode used in electrochemical cell (e.g. Ag/AgCl, RHE).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007204`](https://w3id.org/nfdi4cat/voc4cat_0007204)

**Schema Reference:** [reference_electrode](./elements/slots/reference_electrode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_electrode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>working electrode</strong> (Optional, Multivalued)</summary>

**Description:** Working electrode used in electrochemical cell.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007202`](https://w3id.org/nfdi4cat/voc4cat_0007202)

**Schema Reference:** [working_electrode](./elements/slots/working_electrode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20working_electrode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>counter electrode</strong> (Optional, Multivalued)</summary>

**Description:** Counter electrode used in electrochemical cell.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007203`](https://w3id.org/nfdi4cat/voc4cat_0007203)

**Schema Reference:** [counter_electrode](./elements/slots/counter_electrode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20counter_electrode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>electrolyte composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the electrolyte solution.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:electrolyte_composition`](https://w3id.org/nfdi4cat/coremeta4cat/electrolyte_composition)

**Schema Reference:** [electrolyte_composition](./elements/slots/electrolyte_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrolyte_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>electrolyte concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of the electrolyte.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:electrolyte_concentration`](https://w3id.org/nfdi4cat/coremeta4cat/electrolyte_concentration)

**Schema Reference:** [electrolyte_concentration](./elements/slots/electrolyte_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrolyte_concentration target="_blank" class="md-button md-button--primary">
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

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ConductivityMeasurement target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>DynamicLightScattering</strong></summary>

**Description:** Dynamic light scattering for hydrodynamic particle size distribution in suspension.

**CURIE:** [`CHMO:0000167`](http://purl.obolibrary.org/obo/CHMO_0000167)

**Schema Reference:** [DynamicLightScattering](./elements/classes/DynamicLightScattering.md)

**Slots**

<details markdown="1">
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

<details markdown="1">
<summary><strong>concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of a substance in a sample or solution.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:concentration`](https://w3id.org/nfdi4cat/coremeta4cat/concentration)

**Schema Reference:** [concentration](./elements/slots/concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>light wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Wavelength of the laser used in DLS measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000176`](https://w3id.org/nfdi4cat/voc4cat_0000176)

**Schema Reference:** [light_wavelength](./elements/slots/light_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20light_wavelength target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>scattering angle</strong> (Optional, Multivalued)</summary>

**Description:** Scattering angle at which intensity is detected in DLS.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:scattering_angle`](https://w3id.org/nfdi4cat/coremeta4cat/scattering_angle)

**Schema Reference:** [scattering_angle](./elements/slots/scattering_angle.md)

**Unit:** deg

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20scattering_angle target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>refractive index</strong> (Optional, Multivalued)</summary>

**Description:** Refractive index of the solvent used in DLS measurement.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:refractive_index`](https://w3id.org/nfdi4cat/coremeta4cat/refractive_index)

**Schema Reference:** [refractive_index](./elements/slots/refractive_index.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20refractive_index target="_blank" class="md-button md-button--primary">
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
<summary><strong>measurement duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of a single DLS acquisition.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:measurement_duration`](https://w3id.org/nfdi4cat/coremeta4cat/measurement_duration)

**Schema Reference:** [measurement_duration](./elements/slots/measurement_duration.md)

**Unit:** s

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20measurement_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DynamicLightScattering target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ElectroSprayIonizationMassSpectrometry</strong></summary>

**Description:** Electrospray ionisation mass spectrometry for molecular mass and identity determination.

**CURIE:** [`CHMO:0000482`](http://purl.obolibrary.org/obo/CHMO_0000482)

**Schema Reference:** [ElectroSprayIonizationMassSpectrometry](./elements/classes/ElectroSprayIonizationMassSpectrometry.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of an instrument (e.g. transmission, reflection, AC, DC).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/slots/operation_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spray voltage</strong> (Optional, Multivalued)</summary>

**Description:** Spray voltage applied in electrospray ionisation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002792`](http://purl.obolibrary.org/obo/CHMO_0002792)

**Schema Reference:** [spray_voltage](./elements/slots/spray_voltage.md)

**Unit:** kV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spray_voltage target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>capillary temperature</strong> (Optional, Multivalued)</summary>

**Description:** Capillary or desolvation temperature in ESI source.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:capillary_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/capillary_temperature)

**Schema Reference:** [capillary_temperature](./elements/slots/capillary_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20capillary_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvent composition</strong> (Optional, Multivalued)</summary>

**Description:** Solvent composition used for ESI spray solution.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent_composition](./elements/slots/solvent_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent_composition target="_blank" class="md-button md-button--primary">
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

<details markdown="1">
<summary><strong>concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of a substance in a sample or solution.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:concentration`](https://w3id.org/nfdi4cat/coremeta4cat/concentration)

**Schema Reference:** [concentration](./elements/slots/concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20concentration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz minimum</strong> (Optional, Multivalued)</summary>

**Description:** Minimum m/z value in the mass scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002652`](http://purl.allotrope.org/ontologies/result#AFR_0002652)

**Schema Reference:** [mz_minimum](./elements/slots/mz_minimum.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_minimum target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz maximum</strong> (Optional, Multivalued)</summary>

**Description:** Maximum m/z value in the mass scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002653`](http://purl.allotrope.org/ontologies/result#AFR_0002653)

**Schema Reference:** [mz_maximum](./elements/slots/mz_maximum.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_maximum target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectroSprayIonizationMassSpectrometry target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>GCMS</strong></summary>

**Description:** Gas chromatography-mass spectrometry for volatile compound identification and quantification.

**CURIE:** [`CHMO:0000497`](http://purl.obolibrary.org/obo/CHMO_0000497)

**Schema Reference:** [GCMS](./elements/classes/GCMS.md)

**Slots**

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

<details markdown="1">
<summary><strong>carrier gas purity</strong> (Optional, Multivalued)</summary>

**Description:** Purity grade of the carrier gas used in GC.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:carrier_gas_purity`](https://w3id.org/nfdi4cat/coremeta4cat/carrier_gas_purity)

**Schema Reference:** [carrier_gas_purity](./elements/slots/carrier_gas_purity.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas_purity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>inlet temperature</strong> (Optional, Multivalued)</summary>

**Description:** GC inlet temperature.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:inlet_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/inlet_temperature)

**Schema Reference:** [inlet_temperature](./elements/slots/inlet_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inlet_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum oven temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum oven temperature in GC temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:minimum_oven_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/minimum_oven_temperature)

**Schema Reference:** [minimum_oven_temperature](./elements/slots/minimum_oven_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_oven_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum oven temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum oven temperature in GC temperature programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:maximum_oven_temperature`](https://w3id.org/nfdi4cat/coremeta4cat/maximum_oven_temperature)

**Schema Reference:** [maximum_oven_temperature](./elements/slots/maximum_oven_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_oven_temperature target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating ramp</strong> (Optional, Multivalued)</summary>

**Description:** Temperature ramp rate in GC oven programme.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_ramp`](https://w3id.org/nfdi4cat/coremeta4cat/heating_ramp)

**Schema Reference:** [heating_ramp](./elements/slots/heating_ramp.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_ramp target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating procedure</strong> (Optional, Multivalued)</summary>

**Description:** Description of the heating procedure applied.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:heating_procedure`](https://w3id.org/nfdi4cat/coremeta4cat/heating_procedure)

**Schema Reference:** [heating_procedure](./elements/slots/heating_procedure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_procedure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acquisition mode</strong> (Optional, Multivalued)</summary>

**Description:** Mass spectrometer acquisition mode (e.g. full scan, SIM, SRM).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:acquisition_mode`](https://w3id.org/nfdi4cat/coremeta4cat/acquisition_mode)

**Schema Reference:** [acquisition_mode](./elements/slots/acquisition_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acquisition_mode target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvent delay</strong> (Optional, Multivalued)</summary>

**Description:** Solvent delay time before MS acquisition begins.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:solvent_delay`](https://w3id.org/nfdi4cat/coremeta4cat/solvent_delay)

**Schema Reference:** [solvent_delay](./elements/slots/solvent_delay.md)

**Unit:** min

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent_delay target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>trace ion detection</strong> (Optional, Multivalued)</summary>

**Description:** Trace ion detection setting or threshold.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:trace_ion_detection`](https://w3id.org/nfdi4cat/coremeta4cat/trace_ion_detection)

**Schema Reference:** [trace_ion_detection](./elements/slots/trace_ion_detection.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20trace_ion_detection target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>split ratio</strong> (Optional, Multivalued)</summary>

**Description:** Split ratio at the GC injector.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:split_ratio`](https://w3id.org/nfdi4cat/coremeta4cat/split_ratio)

**Schema Reference:** [split_ratio](./elements/slots/split_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20split_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>column type</strong> (Optional, Multivalued)</summary>

**Description:** Type of chromatographic column used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:column_type`](https://w3id.org/nfdi4cat/coremeta4cat/column_type)

**Schema Reference:** [column_type](./elements/slots/column_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20column_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>eluent</strong> (Optional, Multivalued)</summary>

**Description:** Eluent or mobile phase used in chromatography.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFRL:0000011`](http://purl.allotrope.org/ontologies/role#AFRL_0000011)

**Schema Reference:** [eluent](./elements/slots/eluent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20eluent target="_blank" class="md-button md-button--primary">
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
<summary><strong>injection volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume injected in a chromatographic or mass spectrometric experiment.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:injection_volume`](https://w3id.org/nfdi4cat/coremeta4cat/injection_volume)

**Schema Reference:** [injection_volume](./elements/slots/injection_volume.md)

**Unit:** uL

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20injection_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>external standard</strong> (Optional, Multivalued)</summary>

**Description:** External standard used for quantification or calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:external_standard`](https://w3id.org/nfdi4cat/coremeta4cat/external_standard)

**Schema Reference:** [external_standard](./elements/slots/external_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20external_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>internal standard</strong> (Optional, Multivalued)</summary>

**Description:** Internal standard used for quantification or calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:internal_standard`](https://w3id.org/nfdi4cat/coremeta4cat/internal_standard)

**Schema Reference:** [internal_standard](./elements/slots/internal_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20internal_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz minimum</strong> (Optional, Multivalued)</summary>

**Description:** Minimum m/z value in the mass scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002652`](http://purl.allotrope.org/ontologies/result#AFR_0002652)

**Schema Reference:** [mz_minimum](./elements/slots/mz_minimum.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_minimum target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz maximum</strong> (Optional, Multivalued)</summary>

**Description:** Maximum m/z value in the mass scan range.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002653`](http://purl.allotrope.org/ontologies/result#AFR_0002653)

**Schema Reference:** [mz_maximum](./elements/slots/mz_maximum.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_maximum target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20GCMS target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SizeExclusionChromatography</strong></summary>

**Description:** Size exclusion chromatography for molecular weight distribution determination.

**CURIE:** [`AFP:0000843`](http://purl.allotrope.org/ontologies/process#AFP_0000843)

**Schema Reference:** [SizeExclusionChromatography](./elements/classes/SizeExclusionChromatography.md)

**Slots**

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
<summary><strong>calibration standard</strong> (Optional, Multivalued)</summary>

**Description:** Calibration standard used for molecular weight or retention time calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:calibration_standard`](https://w3id.org/nfdi4cat/coremeta4cat/calibration_standard)

**Schema Reference:** [calibration_standard](./elements/slots/calibration_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calibration_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>column type</strong> (Optional, Multivalued)</summary>

**Description:** Type of chromatographic column used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:column_type`](https://w3id.org/nfdi4cat/coremeta4cat/column_type)

**Schema Reference:** [column_type](./elements/slots/column_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20column_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>eluent</strong> (Optional, Multivalued)</summary>

**Description:** Eluent or mobile phase used in chromatography.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFRL:0000011`](http://purl.allotrope.org/ontologies/role#AFRL_0000011)

**Schema Reference:** [eluent](./elements/slots/eluent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20eluent target="_blank" class="md-button md-button--primary">
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
<summary><strong>injection volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume injected in a chromatographic or mass spectrometric experiment.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:injection_volume`](https://w3id.org/nfdi4cat/coremeta4cat/injection_volume)

**Schema Reference:** [injection_volume](./elements/slots/injection_volume.md)

**Unit:** uL

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20injection_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>external standard</strong> (Optional, Multivalued)</summary>

**Description:** External standard used for quantification or calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:external_standard`](https://w3id.org/nfdi4cat/coremeta4cat/external_standard)

**Schema Reference:** [external_standard](./elements/slots/external_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20external_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>internal standard</strong> (Optional, Multivalued)</summary>

**Description:** Internal standard used for quantification or calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:internal_standard`](https://w3id.org/nfdi4cat/coremeta4cat/internal_standard)

**Schema Reference:** [internal_standard](./elements/slots/internal_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20internal_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SizeExclusionChromatography target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>HighPerformanceLiquidChromatographyMassSpectrometry</strong></summary>

**Description:** High-performance liquid chromatography-mass spectrometry for compound identification and quantification.

**CURIE:** [`CHMO:0000796`](http://purl.obolibrary.org/obo/CHMO_0000796)

**Schema Reference:** [HighPerformanceLiquidChromatographyMassSpectrometry](./elements/classes/HighPerformanceLiquidChromatographyMassSpectrometry.md)

**Slots**

<details markdown="1">
<summary><strong>gradient program</strong> (Optional, Multivalued)</summary>

**Description:** Gradient elution programme used in HPLC-MS.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gradient_program`](https://w3id.org/nfdi4cat/coremeta4cat/gradient_program)

**Schema Reference:** [gradient_program](./elements/slots/gradient_program.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gradient_program target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ionization mode</strong> (Optional, Multivalued)</summary>

**Description:** Ionisation mode used in HPLC-MS (e.g. positive, negative, APCI, ESI).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ionization_mode`](https://w3id.org/nfdi4cat/coremeta4cat/ionization_mode)

**Schema Reference:** [ionization_mode](./elements/slots/ionization_mode.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ionization_mode target="_blank" class="md-button md-button--primary">
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
<summary><strong>column type</strong> (Optional, Multivalued)</summary>

**Description:** Type of chromatographic column used.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:column_type`](https://w3id.org/nfdi4cat/coremeta4cat/column_type)

**Schema Reference:** [column_type](./elements/slots/column_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20column_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>eluent</strong> (Optional, Multivalued)</summary>

**Description:** Eluent or mobile phase used in chromatography.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFRL:0000011`](http://purl.allotrope.org/ontologies/role#AFRL_0000011)

**Schema Reference:** [eluent](./elements/slots/eluent.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20eluent target="_blank" class="md-button md-button--primary">
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
<summary><strong>injection volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume injected in a chromatographic or mass spectrometric experiment.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:injection_volume`](https://w3id.org/nfdi4cat/coremeta4cat/injection_volume)

**Schema Reference:** [injection_volume](./elements/slots/injection_volume.md)

**Unit:** uL

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20injection_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>external standard</strong> (Optional, Multivalued)</summary>

**Description:** External standard used for quantification or calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:external_standard`](https://w3id.org/nfdi4cat/coremeta4cat/external_standard)

**Schema Reference:** [external_standard](./elements/slots/external_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20external_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>internal standard</strong> (Optional, Multivalued)</summary>

**Description:** Internal standard used for quantification or calibration.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:internal_standard`](https://w3id.org/nfdi4cat/coremeta4cat/internal_standard)

**Schema Reference:** [internal_standard](./elements/slots/internal_standard.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20internal_standard target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20HighPerformanceLiquidChromatographyMassSpectrometry target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20realized_plan target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

