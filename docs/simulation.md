# Simulation

The Simulation data class captures metadata describing theoretical and computational studies in catalysis. It documents methodological background, computational settings, and modeling approaches required to interpret simulation results.

Computational approaches are organized under the parent field simulation method, which includes techniques such as density functional theory, molecular dynamics, microkinetic modeling, and Monte Carlo simulations. Selection of a specific method activates the corresponding method-specific metadata fields necessary to describe model setup and computational parameters.

**CURIE:** [`NCIT:C48936`](NCIT:C48936)

<iframe
    src="/CoreMeta4Cat/assets/metadata_simulation_hierarchy.html"
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
<summary><strong>software package</strong> (Mandatory, Multivalued)</summary>

**Description:** Software package or code used for the simulation (e.g. VASP, Quantum ESPRESSO,
LAMMPS, CP2K, ORCA, Zacros). Include version number where possible.

**Data Type:** string

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:software_package`](https://w3id.org/nfdi4cat/coremeta4cat/software_package)

**Schema Reference:** [software_package](./elements/slots/software_package.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20software_package target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>calculated property</strong> (Mandatory, Multivalued)</summary>

**Description:** A property computed by this Simulation, provided as a CalculatedProperty
instance. Multiple properties may be computed in a single simulation run.

**Data Type:** CalculatedProperty

**Cardinality:**  Mandatory, Multivalued

**CURIE:** [`coremeta4cat:calculated_property`](https://w3id.org/nfdi4cat/coremeta4cat/calculated_property)

**Schema Reference:** [calculated_property](./elements/slots/calculated_property.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>CalculatedProperty</strong></summary>

**Abstract Class**

**Description:** Abstract QualitativeAttribute representing a property computed by a
Simulation. Concrete subclasses carry the property-specific output
values and the computational settings used to produce them.
Linked from Simulation via the calculated_property slot.

**CURIE:** [`coremeta4cat:CalculatedProperty`](https://w3id.org/nfdi4cat/coremeta4cat/CalculatedProperty)

**Schema Reference:** [CalculatedProperty](./elements/classes/CalculatedProperty.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CalculatedProperty target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of CalculatedProperty:**

<details markdown="1">
<summary><strong>ThermodynamicStability</strong></summary>

**Description:** Thermodynamic stability of a material or phase, characterised by formation
energy, convex hull distance, and competing phases. Used to screen catalyst
stability and predict synthesis feasibility.

**CURIE:** [`coremeta4cat:ThermodynamicStability`](https://w3id.org/nfdi4cat/coremeta4cat/ThermodynamicStability)

**Schema Reference:** [ThermodynamicStability](./elements/classes/ThermodynamicStability.md)

**Slots**

<details markdown="1">
<summary><strong>formation energy</strong> (Optional, Multivalued)</summary>

**Description:** Formation energy per atom relative to elemental reference states.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:formation_energy`](https://w3id.org/nfdi4cat/coremeta4cat/formation_energy)

**Schema Reference:** [formation_energy](./elements/slots/formation_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20formation_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reference energies</strong> (Optional, Multivalued)</summary>

**Description:** Elemental reference energies used to compute formation energies
(e.g. DFT total energies of elemental ground-state structures).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:reference_energies`](https://w3id.org/nfdi4cat/coremeta4cat/reference_energies)

**Schema Reference:** [reference_energies](./elements/slots/reference_energies.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_energies target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy above hull</strong> (Optional, Multivalued)</summary>

**Description:** Distance above the convex hull of stable phases (thermodynamic stability
metric). Zero for phases on the hull; positive values indicate metastability.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:energy_above_hull`](https://w3id.org/nfdi4cat/coremeta4cat/energy_above_hull)

**Schema Reference:** [energy_above_hull](./elements/slots/energy_above_hull.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_above_hull target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>phase diagram type</strong> (Optional, Multivalued)</summary>

**Description:** Type of phase diagram constructed (e.g. binary, ternary, quaternary).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:phase_diagram_type`](https://w3id.org/nfdi4cat/coremeta4cat/phase_diagram_type)

**Schema Reference:** [phase_diagram_type](./elements/slots/phase_diagram_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20phase_diagram_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>competing phases</strong> (Optional, Multivalued)</summary>

**Description:** List of stable competing phases used in convex hull construction
(e.g. "Fe2O3, Fe3O4, FeO, Fe").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:competing_phases`](https://w3id.org/nfdi4cat/coremeta4cat/competing_phases)

**Schema Reference:** [competing_phases](./elements/slots/competing_phases.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20competing_phases target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ThermodynamicStability target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Piezoelectricity</strong></summary>

**Description:** Piezoelectric response of a non-centrosymmetric material, described by the
piezoelectric tensor. Relevant for piezocatalysis applications.

**CURIE:** [`coremeta4cat:Piezoelectricity`](https://w3id.org/nfdi4cat/coremeta4cat/Piezoelectricity)

**Schema Reference:** [Piezoelectricity](./elements/classes/Piezoelectricity.md)

**Slots**

<details markdown="1">
<summary><strong>piezoelectric tensor</strong> (Optional, Multivalued)</summary>

**Description:** Components of the piezoelectric tensor e_ij (C/m²) or d_ij (pC/N),
describing the coupling between stress and electric polarization.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:piezoelectric_tensor`](https://w3id.org/nfdi4cat/coremeta4cat/piezoelectric_tensor)

**Schema Reference:** [piezoelectric_tensor](./elements/slots/piezoelectric_tensor.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20piezoelectric_tensor target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal symmetry</strong> (Optional, Multivalued)</summary>

**Description:** Point group or space group symmetry of the crystal structure.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:crystal_symmetry`](https://w3id.org/nfdi4cat/coremeta4cat/crystal_symmetry)

**Schema Reference:** [crystal_symmetry](./elements/slots/crystal_symmetry.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_symmetry target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>strain applied</strong> (Optional, Multivalued)</summary>

**Description:** Magnitude of applied strain in the piezoelectric calculation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:strain_applied`](https://w3id.org/nfdi4cat/coremeta4cat/strain_applied)

**Schema Reference:** [strain_applied](./elements/slots/strain_applied.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20strain_applied target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ionic electronic contributions</strong> (Optional, Multivalued)</summary>

**Description:** Decomposition of the piezoelectric or dielectric response into ionic
(nuclear) and electronic contributions.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ionic_electronic_contributions`](https://w3id.org/nfdi4cat/coremeta4cat/ionic_electronic_contributions)

**Schema Reference:** [ionic_electronic_contributions](./elements/slots/ionic_electronic_contributions.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ionic_electronic_contributions target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Piezoelectricity target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ElasticConstants</strong></summary>

**Description:** Elastic mechanical properties of a material derived from the elastic tensor,
including bulk modulus, shear modulus, and Young's modulus.

**CURIE:** [`coremeta4cat:ElasticConstants`](https://w3id.org/nfdi4cat/coremeta4cat/ElasticConstants)

**Schema Reference:** [ElasticConstants](./elements/classes/ElasticConstants.md)

**Slots**

<details markdown="1">
<summary><strong>elastic tensor</strong> (Optional, Multivalued)</summary>

**Description:** Full Voigt-notation elastic tensor C_ij (GPa) describing the linear
elastic response of the material.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:elastic_tensor`](https://w3id.org/nfdi4cat/coremeta4cat/elastic_tensor)

**Schema Reference:** [elastic_tensor](./elements/slots/elastic_tensor.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20elastic_tensor target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bulk modulus</strong> (Optional, Multivalued)</summary>

**Description:** Bulk modulus (resistance to uniform compression).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:bulk_modulus`](https://w3id.org/nfdi4cat/coremeta4cat/bulk_modulus)

**Schema Reference:** [bulk_modulus](./elements/slots/bulk_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bulk_modulus target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>shear modulus</strong> (Optional, Multivalued)</summary>

**Description:** Shear modulus (resistance to shear deformation).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:shear_modulus`](https://w3id.org/nfdi4cat/coremeta4cat/shear_modulus)

**Schema Reference:** [shear_modulus](./elements/slots/shear_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20shear_modulus target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>poisson ratio</strong> (Optional, Multivalued)</summary>

**Description:** Poisson's ratio (ratio of transverse to axial strain under uniaxial load).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:poisson_ratio`](https://w3id.org/nfdi4cat/coremeta4cat/poisson_ratio)

**Schema Reference:** [poisson_ratio](./elements/slots/poisson_ratio.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20poisson_ratio target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>young modulus</strong> (Optional, Multivalued)</summary>

**Description:** Young's modulus (stiffness under uniaxial tension or compression).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:young_modulus`](https://w3id.org/nfdi4cat/coremeta4cat/young_modulus)

**Schema Reference:** [young_modulus](./elements/slots/young_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20young_modulus target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElasticConstants target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Surfaces</strong></summary>

**Description:** Surface properties of a catalyst computed from a periodic slab model,
including surface energy, Miller index, slab thickness, and vacuum spacing.
Central to heterogeneous catalysis modelling.

**CURIE:** [`coremeta4cat:Surfaces`](https://w3id.org/nfdi4cat/coremeta4cat/Surfaces)

**Schema Reference:** [Surfaces](./elements/classes/Surfaces.md)

**Slots**

<details markdown="1">
<summary><strong>surface energy</strong> (Optional, Multivalued)</summary>

**Description:** Cleavage energy per unit area required to create the surface from the bulk.
A lower value indicates a more stable surface facet.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:surface_energy`](https://w3id.org/nfdi4cat/coremeta4cat/surface_energy)

**Schema Reference:** [surface_energy](./elements/slots/surface_energy.md)

**Unit:** J/m2

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surface_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>miller indices</strong> (Optional, Multivalued)</summary>

**Description:** Miller indices of the modelled surface facet (e.g. "(111)", "(110)", "(100)").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:miller_indices`](https://w3id.org/nfdi4cat/coremeta4cat/miller_indices)

**Schema Reference:** [miller_indices](./elements/slots/miller_indices.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20miller_indices target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>slab thickness</strong> (Optional, Multivalued)</summary>

**Description:** Thickness of the periodic slab model used to represent the surface.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:slab_thickness`](https://w3id.org/nfdi4cat/coremeta4cat/slab_thickness)

**Schema Reference:** [slab_thickness](./elements/slots/slab_thickness.md)

**Unit:** Ao

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20slab_thickness target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vacuum spacing</strong> (Optional, Multivalued)</summary>

**Description:** Vacuum layer thickness added above the slab to prevent spurious
periodic interactions between slab images.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:vacuum_spacing`](https://w3id.org/nfdi4cat/coremeta4cat/vacuum_spacing)

**Schema Reference:** [vacuum_spacing](./elements/slots/vacuum_spacing.md)

**Unit:** Ao

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vacuum_spacing target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surface termination method</strong> (Optional, Multivalued)</summary>

**Description:** Method used to terminate the slab and handle dangling bonds
(e.g. H-passivation, OH-termination, dipole correction).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:surface_termination_method`](https://w3id.org/nfdi4cat/coremeta4cat/surface_termination_method)

**Schema Reference:** [surface_termination_method](./elements/slots/surface_termination_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surface_termination_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Surfaces target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>DielectricTensors</strong></summary>

**Description:** Dielectric tensor computed from density functional perturbation theory (DFPT).
Characterises the optical and static dielectric response of a material.

**CURIE:** [`coremeta4cat:DielectricTensors`](https://w3id.org/nfdi4cat/coremeta4cat/DielectricTensors)

**Schema Reference:** [DielectricTensors](./elements/classes/DielectricTensors.md)

**Slots**

<details markdown="1">
<summary><strong>dielectric tensor</strong> (Optional, Multivalued)</summary>

**Description:** Components of the static and/or high-frequency dielectric tensor epsilon_ij,
computed from DFPT.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:dielectric_tensor`](https://w3id.org/nfdi4cat/coremeta4cat/dielectric_tensor)

**Schema Reference:** [dielectric_tensor](./elements/slots/dielectric_tensor.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20dielectric_tensor target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>born effective charges</strong> (Optional, Multivalued)</summary>

**Description:** Born effective charge tensors Z*_ij for each atom, describing how
the polarization changes with atomic displacements.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:born_effective_charges`](https://w3id.org/nfdi4cat/coremeta4cat/born_effective_charges)

**Schema Reference:** [born_effective_charges](./elements/slots/born_effective_charges.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20born_effective_charges target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Plane-wave kinetic energy cutoff for the basis set expansion.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:energy_cutoff`](https://w3id.org/nfdi4cat/coremeta4cat/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/slots/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence thresholds applied during self-consistent field (SCF) and/or
geometry optimisation (e.g. energy < 1e-5 eV, forces < 0.02 eV/Å).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:convergence_criteria`](https://w3id.org/nfdi4cat/coremeta4cat/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/slots/convergence_criteria.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** Monkhorst-Pack k-point mesh used for Brillouin zone sampling
(e.g. "4×4×1" for a surface slab, "8×8×8" for a bulk cell).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:k_point_mesh`](https://w3id.org/nfdi4cat/coremeta4cat/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/slots/k_point_mesh.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DielectricTensors target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PhononDispersion</strong></summary>

**Description:** Phonon dispersion relations computed from interatomic force constants,
providing access to vibrational frequencies, thermodynamic quantities,
and dynamical stability (imaginary modes).

**CURIE:** [`coremeta4cat:PhononDispersion`](https://w3id.org/nfdi4cat/coremeta4cat/PhononDispersion)

**Schema Reference:** [PhononDispersion](./elements/classes/PhononDispersion.md)

**Slots**

<details markdown="1">
<summary><strong>force constant method</strong> (Optional, Multivalued)</summary>

**Description:** Method used to compute the interatomic force constants (e.g. finite
differences / supercell method, DFPT/linear response).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:force_constant_method`](https://w3id.org/nfdi4cat/coremeta4cat/force_constant_method)

**Schema Reference:** [force_constant_method](./elements/slots/force_constant_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20force_constant_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>kq point mesh</strong> (Optional, Multivalued)</summary>

**Description:** k/q-point mesh for phonon Brillouin zone sampling (e.g. "8×8×8").
Distinct from the electronic k-point mesh.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:kq_point_mesh`](https://w3id.org/nfdi4cat/coremeta4cat/kq_point_mesh)

**Schema Reference:** [kq_point_mesh](./elements/slots/kq_point_mesh.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20kq_point_mesh target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>smearing parameter</strong> (Optional, Multivalued)</summary>

**Description:** Smearing or broadening parameter applied to the phonon density of states.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:smearing_parameter`](https://w3id.org/nfdi4cat/coremeta4cat/smearing_parameter)

**Schema Reference:** [smearing_parameter](./elements/slots/smearing_parameter.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smearing_parameter target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>imaginary modes</strong> (Optional, Multivalued)</summary>

**Description:** Whether imaginary (soft) phonon modes are present in the dispersion.
Imaginary modes indicate dynamical instability of the structure.

**Data Type:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:imaginary_modes`](https://w3id.org/nfdi4cat/coremeta4cat/imaginary_modes)

**Schema Reference:** [imaginary_modes](./elements/slots/imaginary_modes.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20imaginary_modes target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PhononDispersion target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>EquationsOfState</strong></summary>

**Description:** Equation of state relating energy (or enthalpy) to volume, fitted to a
parametric model (e.g. Birch-Murnaghan). Used to extract equilibrium
volume, bulk modulus, and its pressure derivative.

**CURIE:** [`coremeta4cat:EquationsOfState`](https://w3id.org/nfdi4cat/coremeta4cat/EquationsOfState)

**Schema Reference:** [EquationsOfState](./elements/classes/EquationsOfState.md)

**Slots**

<details markdown="1">
<summary><strong>fit method</strong> (Optional, Multivalued)</summary>

**Description:** Parametric model used to fit the energy-volume curve
(e.g. Birch-Murnaghan 3rd order, Vinet, Murnaghan).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:fit_method`](https://w3id.org/nfdi4cat/coremeta4cat/fit_method)

**Schema Reference:** [fit_method](./elements/slots/fit_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fit_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bulk modulus</strong> (Optional, Multivalued)</summary>

**Description:** Bulk modulus (resistance to uniform compression).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:bulk_modulus`](https://w3id.org/nfdi4cat/coremeta4cat/bulk_modulus)

**Schema Reference:** [bulk_modulus](./elements/slots/bulk_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bulk_modulus target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pressure derivative</strong> (Optional, Multivalued)</summary>

**Description:** Pressure derivative of the bulk modulus B' (dimensionless).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:pressure_derivative`](https://w3id.org/nfdi4cat/coremeta4cat/pressure_derivative)

**Schema Reference:** [pressure_derivative](./elements/slots/pressure_derivative.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pressure_derivative target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fit residuals</strong> (Optional, Multivalued)</summary>

**Description:** Root-mean-square residuals of the energy-volume fit.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:fit_residuals`](https://w3id.org/nfdi4cat/coremeta4cat/fit_residuals)

**Schema Reference:** [fit_residuals](./elements/slots/fit_residuals.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fit_residuals target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Plane-wave kinetic energy cutoff for the basis set expansion.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:energy_cutoff`](https://w3id.org/nfdi4cat/coremeta4cat/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/slots/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence thresholds applied during self-consistent field (SCF) and/or
geometry optimisation (e.g. energy < 1e-5 eV, forces < 0.02 eV/Å).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:convergence_criteria`](https://w3id.org/nfdi4cat/coremeta4cat/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/slots/convergence_criteria.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** Monkhorst-Pack k-point mesh used for Brillouin zone sampling
(e.g. "4×4×1" for a surface slab, "8×8×8" for a bulk cell).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:k_point_mesh`](https://w3id.org/nfdi4cat/coremeta4cat/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/slots/k_point_mesh.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20EquationsOfState target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>AqueousStability</strong></summary>

**Description:** Electrochemical (Pourbaix) stability of a catalyst in aqueous solution as
a function of pH and electrode potential. Critical for electrocatalyst
stability screening.

**CURIE:** [`coremeta4cat:AqueousStability`](https://w3id.org/nfdi4cat/coremeta4cat/AqueousStability)

**Schema Reference:** [AqueousStability](./elements/classes/AqueousStability.md)

**Slots**

<details markdown="1">
<summary><strong>ph range</strong> (Optional, Multivalued)</summary>

**Description:** pH range covered in the Pourbaix stability diagram (e.g. "0–14").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ph_range`](https://w3id.org/nfdi4cat/coremeta4cat/ph_range)

**Schema Reference:** [ph_range](./elements/slots/ph_range.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ph_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>potential range</strong> (Optional, Multivalued)</summary>

**Description:** Electrode potential range covered in the Pourbaix diagram
(e.g. "-2 to +2 V vs SHE").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:potential_range`](https://w3id.org/nfdi4cat/coremeta4cat/potential_range)

**Schema Reference:** [potential_range](./elements/slots/potential_range.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20potential_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvation model</strong> (Optional, Multivalued)</summary>

**Description:** Implicit solvation model used to account for aqueous environment
(e.g. VASPsol, SCCS/Environ, COSMO).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:solvation_model`](https://w3id.org/nfdi4cat/coremeta4cat/solvation_model)

**Schema Reference:** [solvation_model](./elements/slots/solvation_model.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvation_model target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ionic strength</strong> (Optional, Multivalued)</summary>

**Description:** Ionic strength of the electrolyte solution modelled.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ionic_strength`](https://w3id.org/nfdi4cat/coremeta4cat/ionic_strength)

**Schema Reference:** [ionic_strength](./elements/slots/ionic_strength.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ionic_strength target="_blank" class="md-button md-button--primary">
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
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AqueousStability target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>GrainBoundaries</strong></summary>

**Description:** Grain boundary structure and energetics from atomistic simulation.
Relevant for understanding polycrystalline catalyst behaviour,
sintering, and charge/defect segregation.

**CURIE:** [`coremeta4cat:GrainBoundaries`](https://w3id.org/nfdi4cat/coremeta4cat/GrainBoundaries)

**Schema Reference:** [GrainBoundaries](./elements/classes/GrainBoundaries.md)

**Slots**

<details markdown="1">
<summary><strong>grain boundary plane</strong> (Optional, Multivalued)</summary>

**Description:** Crystallographic plane of the grain boundary, expressed using
Miller indices (e.g. "Sigma5 (310)[001]").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:grain_boundary_plane`](https://w3id.org/nfdi4cat/coremeta4cat/grain_boundary_plane)

**Schema Reference:** [grain_boundary_plane](./elements/slots/grain_boundary_plane.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20grain_boundary_plane target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>misorientation angle</strong> (Optional, Multivalued)</summary>

**Description:** Misorientation angle between adjacent grains at the boundary.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:misorientation_angle`](https://w3id.org/nfdi4cat/coremeta4cat/misorientation_angle)

**Schema Reference:** [misorientation_angle](./elements/slots/misorientation_angle.md)

**Unit:** deg

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20misorientation_angle target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>grain boundary energy</strong> (Optional, Multivalued)</summary>

**Description:** Excess energy per unit area of the grain boundary.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:grain_boundary_energy`](https://w3id.org/nfdi4cat/coremeta4cat/grain_boundary_energy)

**Schema Reference:** [grain_boundary_energy](./elements/slots/grain_boundary_energy.md)

**Unit:** J/m2

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20grain_boundary_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation cell size</strong> (Optional, Multivalued)</summary>

**Description:** Dimensions of the simulation cell used to model the grain boundary
(e.g. "10×10×30 nm").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:simulation_cell_size`](https://w3id.org/nfdi4cat/coremeta4cat/simulation_cell_size)

**Schema Reference:** [simulation_cell_size](./elements/slots/simulation_cell_size.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_cell_size target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gb excess volume</strong> (Optional, Multivalued)</summary>

**Description:** Excess volume per unit area associated with the grain boundary.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gb_excess_volume`](https://w3id.org/nfdi4cat/coremeta4cat/gb_excess_volume)

**Schema Reference:** [gb_excess_volume](./elements/slots/gb_excess_volume.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gb_excess_volume target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gb structural units</strong> (Optional, Multivalued)</summary>

**Description:** Description of the structural units (repeating atomic motifs) that
constitute the grain boundary structure.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gb_structural_units`](https://w3id.org/nfdi4cat/coremeta4cat/gb_structural_units)

**Schema Reference:** [gb_structural_units](./elements/slots/gb_structural_units.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gb_structural_units target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>charge defect segregation</strong> (Optional, Multivalued)</summary>

**Description:** Data describing charge carrier or point defect segregation behaviour
at the grain boundary (e.g. segregation energy per defect type).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:charge_defect_segregation`](https://w3id.org/nfdi4cat/coremeta4cat/charge_defect_segregation)

**Schema Reference:** [charge_defect_segregation](./elements/slots/charge_defect_segregation.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20charge_defect_segregation target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20GrainBoundaries target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>ElectronicStructure</strong></summary>

**Description:** Electronic band structure and density of states, characterising the
electronic properties of a catalyst relevant to activity descriptors
(d-band centre, band gap, Fermi energy).

**CURIE:** [`coremeta4cat:ElectronicStructure`](https://w3id.org/nfdi4cat/coremeta4cat/ElectronicStructure)

**Schema Reference:** [ElectronicStructure](./elements/classes/ElectronicStructure.md)

**Slots**

<details markdown="1">
<summary><strong>smearing method</strong> (Optional, Multivalued)</summary>

**Description:** Electronic smearing scheme and width used in the SCF calculation
(e.g. Methfessel-Paxton order 1 with sigma=0.2 eV, Gaussian with sigma=0.05 eV).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:smearing_method`](https://w3id.org/nfdi4cat/coremeta4cat/smearing_method)

**Schema Reference:** [smearing_method](./elements/slots/smearing_method.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smearing_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spin polarized</strong> (Optional, Multivalued)</summary>

**Description:** Whether the electronic structure calculation is spin-polarized
(accounts for spin-up and spin-down electrons separately).

**Data Type:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:spin_polarized`](https://w3id.org/nfdi4cat/coremeta4cat/spin_polarized)

**Schema Reference:** [spin_polarized](./elements/slots/spin_polarized.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spin_polarized target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>band path</strong> (Optional, Multivalued)</summary>

**Description:** High-symmetry k-path through the Brillouin zone used to plot the
band structure (e.g. "Gamma-X-M-Gamma-R" for cubic, following SeeK-path convention).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:band_path`](https://w3id.org/nfdi4cat/coremeta4cat/band_path)

**Schema Reference:** [band_path](./elements/slots/band_path.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20band_path target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fermi energy</strong> (Optional, Multivalued)</summary>

**Description:** Fermi energy (chemical potential of electrons) in the calculated system.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:fermi_energy`](https://w3id.org/nfdi4cat/coremeta4cat/fermi_energy)

**Schema Reference:** [fermi_energy](./elements/slots/fermi_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fermi_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Plane-wave kinetic energy cutoff for the basis set expansion.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:energy_cutoff`](https://w3id.org/nfdi4cat/coremeta4cat/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/slots/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence thresholds applied during self-consistent field (SCF) and/or
geometry optimisation (e.g. energy < 1e-5 eV, forces < 0.02 eV/Å).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:convergence_criteria`](https://w3id.org/nfdi4cat/coremeta4cat/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/slots/convergence_criteria.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** Monkhorst-Pack k-point mesh used for Brillouin zone sampling
(e.g. "4×4×1" for a surface slab, "8×8×8" for a bulk cell).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:k_point_mesh`](https://w3id.org/nfdi4cat/coremeta4cat/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/slots/k_point_mesh.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectronicStructure target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Ferroelectrics</strong></summary>

**Description:** Ferroelectric properties computed from DFT, including spontaneous
polarization, switching barrier, and coercive field. Relevant for
ferroelectric-photocatalyst design.

**CURIE:** [`coremeta4cat:Ferroelectrics`](https://w3id.org/nfdi4cat/coremeta4cat/Ferroelectrics)

**Schema Reference:** [Ferroelectrics](./elements/classes/Ferroelectrics.md)

**Slots**

<details markdown="1">
<summary><strong>polarization direction</strong> (Optional, Multivalued)</summary>

**Description:** Crystallographic direction of the spontaneous electric polarization
(e.g. "[001]" for tetragonal BaTiO_3).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:polarization_direction`](https://w3id.org/nfdi4cat/coremeta4cat/polarization_direction)

**Schema Reference:** [polarization_direction](./elements/slots/polarization_direction.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20polarization_direction target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spontaneous polarization</strong> (Optional, Multivalued)</summary>

**Description:** Magnitude of the spontaneous electric polarization.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:spontaneous_polarization`](https://w3id.org/nfdi4cat/coremeta4cat/spontaneous_polarization)

**Schema Reference:** [spontaneous_polarization](./elements/slots/spontaneous_polarization.md)

**Unit:** uC/cm2

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spontaneous_polarization target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reference structure</strong> (Optional, Multivalued)</summary>

**Description:** Reference (paraelectric/centrosymmetric) structure used as the zero-
polarization endpoint in the Berry-phase polarization calculation.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:reference_structure`](https://w3id.org/nfdi4cat/coremeta4cat/reference_structure)

**Schema Reference:** [reference_structure](./elements/slots/reference_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>switching barrier</strong> (Optional, Multivalued)</summary>

**Description:** Energy barrier for polarization switching between equivalent states.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:switching_barrier`](https://w3id.org/nfdi4cat/coremeta4cat/switching_barrier)

**Schema Reference:** [switching_barrier](./elements/slots/switching_barrier.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20switching_barrier target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>coercive field</strong> (Optional, Multivalued)</summary>

**Description:** Electric field required to reverse the polarization direction.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:coercive_field`](https://w3id.org/nfdi4cat/coremeta4cat/coercive_field)

**Schema Reference:** [coercive_field](./elements/slots/coercive_field.md)

**Unit:** kV/cm

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20coercive_field target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature dependence</strong> (Optional, Multivalued)</summary>

**Description:** Description of how the ferroelectric properties vary with temperature.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:temperature_dependence`](https://w3id.org/nfdi4cat/coremeta4cat/temperature_dependence)

**Schema Reference:** [temperature_dependence](./elements/slots/temperature_dependence.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature_dependence target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Ferroelectrics target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>BandGap</strong></summary>

**Description:** Electronic band gap and its character (direct/indirect), with optional
many-body (GW) or excitonic corrections. Critical for photocatalyst
and semiconductor catalyst screening.

**CURIE:** [`coremeta4cat:BandGap`](https://w3id.org/nfdi4cat/coremeta4cat/BandGap)

**Schema Reference:** [BandGap](./elements/classes/BandGap.md)

**Slots**

<details markdown="1">
<summary><strong>material sample</strong> (Optional, Multivalued)</summary>

**Description:** Reference to the material or MaterialSample being characterised by this
calculated band gap.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`VOC4CAT:0005056`](https://w3id.org/nfdi4cat/voc4cat_0005056)

**Schema Reference:** [material_sample](./elements/slots/material_sample.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_sample target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>structure model</strong> (Optional, Multivalued)</summary>

**Description:** Model structure used in the band gap calculation (e.g. bulk unit cell,
surface slab, defect supercell).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:structure_model`](https://w3id.org/nfdi4cat/coremeta4cat/structure_model)

**Schema Reference:** [structure_model](./elements/slots/structure_model.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20structure_model target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>smearing broadening</strong> (Optional, Multivalued)</summary>

**Description:** Gaussian or Lorentzian broadening applied to the simulated spectrum.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:smearing_broadening`](https://w3id.org/nfdi4cat/coremeta4cat/smearing_broadening)

**Schema Reference:** [smearing_broadening](./elements/slots/smearing_broadening.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smearing_broadening target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>direct indirect</strong> (Optional, Multivalued)</summary>

**Description:** Band gap character: "direct" (VBM and CBM at same k-point) or
"indirect" (VBM and CBM at different k-points).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:direct_indirect`](https://w3id.org/nfdi4cat/coremeta4cat/direct_indirect)

**Schema Reference:** [direct_indirect](./elements/slots/direct_indirect.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20direct_indirect target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>experimental reference</strong> (Optional, Multivalued)</summary>

**Description:** Experimental band gap value used for benchmarking the calculation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:experimental_reference`](https://w3id.org/nfdi4cat/coremeta4cat/experimental_reference)

**Schema Reference:** [experimental_reference](./elements/slots/experimental_reference.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experimental_reference target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gw hybrid correction</strong> (Optional, Multivalued)</summary>

**Description:** Whether a many-body GW correction or hybrid functional (e.g. HSE06)
was applied to correct the DFT band gap underestimation.

**Data Type:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:gw_hybrid_correction`](https://w3id.org/nfdi4cat/coremeta4cat/gw_hybrid_correction)

**Schema Reference:** [gw_hybrid_correction](./elements/slots/gw_hybrid_correction.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gw_hybrid_correction target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>excitonic correction</strong> (Optional, Multivalued)</summary>

**Description:** Excitonic correction (from Bethe-Salpeter equation) applied to the
optical band gap.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:excitonic_correction`](https://w3id.org/nfdi4cat/coremeta4cat/excitonic_correction)

**Schema Reference:** [excitonic_correction](./elements/slots/excitonic_correction.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitonic_correction target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Chemical composition of the simulated material (e.g. "Fe2O3", "Pt/CeO2").
Use empirical formula or SMILES for molecular systems.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:material_composition`](https://w3id.org/nfdi4cat/coremeta4cat/material_composition)

**Schema Reference:** [material_composition](./elements/slots/material_composition.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure of the simulated material, including space group and
lattice parameters (e.g. "Fm-3m, a=3.92 Å for Pt").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/slots/crystal_structure.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Plane-wave kinetic energy cutoff for the basis set expansion.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:energy_cutoff`](https://w3id.org/nfdi4cat/coremeta4cat/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/slots/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence thresholds applied during self-consistent field (SCF) and/or
geometry optimisation (e.g. energy < 1e-5 eV, forces < 0.02 eV/Å).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:convergence_criteria`](https://w3id.org/nfdi4cat/coremeta4cat/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/slots/convergence_criteria.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** Monkhorst-Pack k-point mesh used for Brillouin zone sampling
(e.g. "4×4×1" for a surface slab, "8×8×8" for a bulk cell).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:k_point_mesh`](https://w3id.org/nfdi4cat/coremeta4cat/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/slots/k_point_mesh.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20BandGap target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calculated_property target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1" open>
<summary><strong>realized plan</strong> (Mandatory, Multivalued)</summary>

**Description:** The SimulationMethod (protocol) realized in this Simulation.

**Data Type:** SimulationMethod

**Cardinality:**  Mandatory, Multivalued

**Schema Reference:** [realized_plan](./elements/slots/realized_plan.md)

**Data Type Class Details:**

<details markdown="1" open>
<summary><strong>SimulationMethod</strong></summary>

**Abstract Class**

**Description:** Abstract Plan describing the computational method (protocol) used in a
Simulation. Concrete subclasses carry method-specific parameter slots.
Linked from Simulation via realized_plan.

**CURIE:** [`OBI:0000272`](http://purl.obolibrary.org/obo/OBI_0000272)

**Schema Reference:** [SimulationMethod](./elements/classes/SimulationMethod.md)

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SimulationMethod target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of SimulationMethod:**

<details markdown="1">
<summary><strong>DFT</strong></summary>

**Description:** Density functional theory — a quantum mechanical method for calculating
the electronic structure of atoms, molecules, and periodic solids.
The most widely used ab initio method in computational catalysis.

**CURIE:** [`coremeta4cat:DFT`](https://w3id.org/nfdi4cat/coremeta4cat/DFT)

**Schema Reference:** [DFT](./elements/classes/DFT.md)

**Slots**

<details markdown="1">
<summary><strong>exchange correlation functional</strong> (Optional, Multivalued)</summary>

**Description:** Exchange-correlation functional used (e.g. PBE, PBEsol, RPBE, B3LYP,
HSE06). The choice of functional directly affects accuracy.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:exchange_correlation_functional`](https://w3id.org/nfdi4cat/coremeta4cat/exchange_correlation_functional)

**Schema Reference:** [exchange_correlation_functional](./elements/slots/exchange_correlation_functional.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20exchange_correlation_functional target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Plane-wave kinetic energy cutoff for the basis set expansion.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:energy_cutoff`](https://w3id.org/nfdi4cat/coremeta4cat/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/slots/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence thresholds applied during self-consistent field (SCF) and/or
geometry optimisation (e.g. energy < 1e-5 eV, forces < 0.02 eV/Å).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:convergence_criteria`](https://w3id.org/nfdi4cat/coremeta4cat/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/slots/convergence_criteria.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>dft u parameters</strong> (Optional, Multivalued)</summary>

**Description:** Hubbard U correction parameters (DFT+U). Specify element, orbital, and
U value (e.g. "Fe d: U=4.0 eV, J=0.0 eV").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:dft_u_parameters`](https://w3id.org/nfdi4cat/coremeta4cat/dft_u_parameters)

**Schema Reference:** [dft_u_parameters](./elements/slots/dft_u_parameters.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20dft_u_parameters target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spin polarization</strong> (Optional, Multivalued)</summary>

**Description:** Whether spin polarization (collinear magnetism) is included in the DFT
calculation. Set to true for systems containing magnetic elements.

**Data Type:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:spin_polarization`](https://w3id.org/nfdi4cat/coremeta4cat/spin_polarization)

**Schema Reference:** [spin_polarization](./elements/slots/spin_polarization.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spin_polarization target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>total energy per atom</strong> (Optional, Multivalued)</summary>

**Description:** Total DFT ground-state energy divided by number of atoms in the unit cell.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:total_energy_per_atom`](https://w3id.org/nfdi4cat/coremeta4cat/total_energy_per_atom)

**Schema Reference:** [total_energy_per_atom](./elements/slots/total_energy_per_atom.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20total_energy_per_atom target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DFT target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MolecularDynamics</strong></summary>

**Description:** Molecular dynamics simulation — a method for computing the time evolution
of a system of interacting particles by integrating the equations of motion.
Used to study diffusion, reaction kinetics, and thermal properties.

**CURIE:** [`NCIT:C18097`](http://purl.obolibrary.org/obo/NCIT_C18097)

**Schema Reference:** [MolecularDynamics](./elements/classes/MolecularDynamics.md)

**Slots**

<details markdown="1">
<summary><strong>force field</strong> (Optional, Multivalued)</summary>

**Description:** Force field or interatomic potential used (e.g. ReaxFF, CHARMM, Tersoff,
EAM). Include parametrisation source or reference.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:force_field`](https://w3id.org/nfdi4cat/coremeta4cat/force_field)

**Schema Reference:** [force_field](./elements/slots/force_field.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20force_field target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation timestep</strong> (Optional, Multivalued)</summary>

**Description:** Integration timestep used in molecular dynamics.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`APOLLO_SV:00000012`](http://purl.obolibrary.org/obo/APOLLO_SV_00000012)

**Schema Reference:** [simulation_timestep](./elements/slots/simulation_timestep.md)

**Unit:** fs

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_timestep target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation time</strong> (Optional, Multivalued)</summary>

**Description:** Total simulated physical time of the MD trajectory.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:simulation_time`](https://w3id.org/nfdi4cat/coremeta4cat/simulation_time)

**Schema Reference:** [simulation_time](./elements/slots/simulation_time.md)

**Unit:** ps

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_time target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ensemble type</strong> (Optional, Multivalued)</summary>

**Description:** Statistical ensemble used in MD (e.g. NVE, NVT, NPT). Determines which
thermodynamic quantities are conserved.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:ensemble_type`](https://w3id.org/nfdi4cat/coremeta4cat/ensemble_type)

**Schema Reference:** [ensemble_type](./elements/slots/ensemble_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ensemble_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of atoms</strong> (Optional, Multivalued)</summary>

**Description:** Number of atoms in the simulation cell or supercell.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_atoms`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_atoms)

**Schema Reference:** [number_of_atoms](./elements/slots/number_of_atoms.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_atoms target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolecularDynamics target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Microkinetics</strong></summary>

**Description:** Microkinetic modelling — a mean-field kinetic approach that integrates
elementary reaction steps and their rate constants to predict catalytic
activity and selectivity under reaction conditions.

**CURIE:** [`coremeta4cat:Microkinetics`](https://w3id.org/nfdi4cat/coremeta4cat/Microkinetics)

**Schema Reference:** [Microkinetics](./elements/classes/Microkinetics.md)

**Slots**

<details markdown="1">
<summary><strong>rate constants</strong> (Optional, Multivalued)</summary>

**Description:** Rate constants or Arrhenius parameters (pre-exponential factor and
activation energy) for each elementary step in the reaction network.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C94967`](http://purl.obolibrary.org/obo/NCIT_C94967)

**Schema Reference:** [rate_constants](./elements/slots/rate_constants.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20rate_constants target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solver type</strong> (Optional, Multivalued)</summary>

**Description:** Numerical solver used for the microkinetic rate equations (e.g. LSODA,
stiff ODE solver, steady-state Newton method).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:solver_type`](https://w3id.org/nfdi4cat/coremeta4cat/solver_type)

**Schema Reference:** [solver_type](./elements/slots/solver_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solver_type target="_blank" class="md-button md-button--primary">
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
<summary><strong>pressure</strong> (Optional, Multivalued)</summary>

**Description:** Total pressure used in microkinetic or Monte Carlo simulation.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:pressure`](https://w3id.org/nfdi4cat/coremeta4cat/pressure)

**Schema Reference:** [pressure](./elements/slots/pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surface coverage</strong> (Optional, Multivalued)</summary>

**Description:** Surface coverage of adsorbed species (fraction of surface sites occupied).

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:surface_coverage`](https://w3id.org/nfdi4cat/coremeta4cat/surface_coverage)

**Schema Reference:** [surface_coverage](./elements/slots/surface_coverage.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surface_coverage target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>activation energy</strong> (Optional, Multivalued)</summary>

**Description:** Activation energy for each elementary step in the reaction mechanism.

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:activation_energy`](https://w3id.org/nfdi4cat/coremeta4cat/activation_energy)

**Schema Reference:** [activation_energy](./elements/slots/activation_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20activation_energy target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Microkinetics target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>MonteCarlo</strong></summary>

**Description:** Monte Carlo simulation — a stochastic method that samples configuration
space using random moves accepted or rejected according to a statistical
criterion (e.g. Metropolis). Used for adsorption isotherms, phase diagrams,
and lattice-based kinetics.

**CURIE:** [`coremeta4cat:MonteCarlo`](https://w3id.org/nfdi4cat/coremeta4cat/MonteCarlo)

**Schema Reference:** [MonteCarlo](./elements/classes/MonteCarlo.md)

**Slots**

<details markdown="1">
<summary><strong>interaction potential</strong> (Optional, Multivalued)</summary>

**Description:** Interaction potential or Hamiltonian used to compute energies in MC moves.

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:interaction_potential`](https://w3id.org/nfdi4cat/coremeta4cat/interaction_potential)

**Schema Reference:** [interaction_potential](./elements/slots/interaction_potential.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20interaction_potential target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of steps</strong> (Optional, Multivalued)</summary>

**Description:** Total number of Monte Carlo moves or trial configurations generated.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:number_of_steps`](https://w3id.org/nfdi4cat/coremeta4cat/number_of_steps)

**Schema Reference:** [number_of_steps](./elements/slots/number_of_steps.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_steps target="_blank" class="md-button md-button--primary">
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
<summary><strong>lattice size type</strong> (Optional, Multivalued)</summary>

**Description:** Lattice geometry and dimensions used in lattice-based MC (e.g.
"100×100 square lattice", "hexagonal 50×50").

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:lattice_size_type`](https://w3id.org/nfdi4cat/coremeta4cat/lattice_size_type)

**Schema Reference:** [lattice_size_type](./elements/slots/lattice_size_type.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20lattice_size_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acceptance criteria</strong> (Optional, Multivalued)</summary>

**Description:** Criterion for accepting or rejecting MC moves (e.g. Metropolis,
Kawasaki, heat-bath algorithm).

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:acceptance_criteria`](https://w3id.org/nfdi4cat/coremeta4cat/acceptance_criteria)

**Schema Reference:** [acceptance_criteria](./elements/slots/acceptance_criteria.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acceptance_criteria target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equilibration steps</strong> (Optional, Multivalued)</summary>

**Description:** Number of MC steps used for equilibration before data collection begins.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:equilibration_steps`](https://w3id.org/nfdi4cat/coremeta4cat/equilibration_steps)

**Schema Reference:** [equilibration_steps](./elements/slots/equilibration_steps.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equilibration_steps target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sampling interval</strong> (Optional, Multivalued)</summary>

**Description:** Interval between successive MC snapshots used for property averaging.

**Data Type:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`coremeta4cat:sampling_interval`](https://w3id.org/nfdi4cat/coremeta4cat/sampling_interval)

**Schema Reference:** [sampling_interval](./elements/slots/sampling_interval.md)

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sampling_interval target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MonteCarlo target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20realized_plan target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

