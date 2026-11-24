## CatalysisDataset-001
### Input
```yaml
description:
- Dataset covering preparation of Cu/ZnO/Al2O3 methanol synthesis catalyst by incipient
  wetness impregnation and catalytic performance in CO2 hydrogenation at 50 bar, 200-300
  deg C.
id: coremeta4cat:DS_001_MeOH_synthesis_CuZnO
is_about_entity:
- description: 63 wt% CuO, 24 wt% ZnO, 13 wt% Al2O3 (calcined precursor)
  id: coremeta4cat:CAT_001_CuZnO_Al2O3
  title: Cu/ZnO/Al2O3 methanol synthesis catalyst
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
title:
- 'Methanol synthesis over Cu/ZnO/Al2O3: synthesis and catalytic performance dataset'
was_generated_by:
- activity_designator: Synthesis
  catalyst_measured_properties:
  - 'BET surface area: 185 m2/g, Pt particle size: 2.3 nm (TEM), Pt loading: 4.8 wt%
    (ICP-AES)'
  catalyst_support:
  - gamma-Al2O3, Sasol Puralox, 200 m2/g
  had_input_entity:
  - id: coremeta4cat:PREC_001_H2PtCl6
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.0485
    title: chloroplatinic acid hexahydrate
  has_sample_pretreatment:
  - value: reduction in H2 at 400 deg C for 2 hours prior to catalytic testing
  id: coremeta4cat:SYNTH_001_Pt_Al2O3
  nominal_composition:
  - 5 wt% Pt/Al2O3
  realized_plan:
    description: incipient_wetness, 25 deg C, 12 h
    id: coremeta4cat:SYNTH_001_impregnation_method
    title: incipient wetness impregnation
  solvent:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/962
    title: deionized water
  storage_conditions:
  - stored in desiccator under argon atmosphere at room temperature
- activity_designator: Characterization
  carried_out_by:
  - id: coremeta4cat:DEV_001_Micromeritics_ASAP2020
    title: Micromeritics ASAP 2020 surface area and porosimetry analyzer
  evaluated_entity:
  - description: 63 wt% CuO, 24 wt% ZnO, 13 wt% Al2O3 (calcined precursor)
    id: coremeta4cat:CAT_001_CuZnO_Al2O3
    title: Cu/ZnO/Al2O3 methanol synthesis catalyst
  id: coremeta4cat:CHAR_001_BET_CuZnO_Al2O3
  realized_plan:
    description: N2 physisorption at 77 K, degassing at 300 deg C for 3 h under vacuum
      prior to measurement
    id: coremeta4cat:CHAR_001_BET_method
    title: BET surface area measurement
- activity_designator: Characterization
  carried_out_by:
  - id: coremeta4cat:DEV_002_Bruker_D8_Advance
    title: Bruker D8 Advance diffractometer with Cu K-alpha radiation (1.5406 Ang)
  evaluated_entity:
  - description: 63 wt% CuO, 24 wt% ZnO, 13 wt% Al2O3 (calcined precursor)
    id: coremeta4cat:CAT_001_CuZnO_Al2O3
    title: Cu/ZnO/Al2O3 methanol synthesis catalyst
  id: coremeta4cat:CHAR_002_XRD_CuZnO_Al2O3
  realized_plan:
    description: Cu K-alpha, 2theta range 5 to 80 deg, step size 0.02 deg, scan rate
      1 deg/min, Rietveld refinement for phase quantification
    id: coremeta4cat:CHAR_002_XRD_method
    title: powder X-ray diffraction

```
## CatalysisDataset-002
### Input
```yaml
description:
- 'Dataset covering the full lifecycle of a 15 wt% NiO/CeO2 dry reforming catalyst:
  (1) co-precipitation synthesis with precipitation parameters and calcination protocol;
  (2) XPS surface composition and oxidation state analysis; (3) H2-TPR reducibility
  profiling; (4) catalytic performance in CH4+CO2 dry reforming at 600-800 deg C over
  20 h; (5) ReaxFF molecular dynamics of the Ni/CeO2(111) interface at 800 deg C to
  rationalise metal-support interaction.'
id: coremeta4cat:DS_002_DRM_NiO_CeO2
is_about_activity:
- catalyst_form:
  - supported
  catalyst_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/GM
    value: 0.2
  catalyst_type:
  - heterogeneous_catalysis
  experiment_pressure:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/ATM
    value: 1.0
  feed_composition_range:
  - description: 'stoichiometric DRM: CH4/CO2 = 1:1 (molar)'
  - description: 'CO2-rich condition: CH4/CO2 = 1:1.5 to suppress carbon deposition'
  had_input_entity:
  - description: 'CH4 flow: 45 mL/min (STP); calibrated Brooks SLA5850 MFC'
    id: coremeta4cat:FEED_004_CH4_DRM
    title: methane feed (99.995%, Linde)
  - description: 'CO2 flow: 45 mL/min (STP); calibrated Brooks SLA5850 MFC'
    id: coremeta4cat:FEED_005_CO2_DRM
    title: CO2 feed (99.998%, Linde)
  - description: 'N2 flow: 10 mL/min (STP); used as internal standard for GC molar
      balance'
    id: coremeta4cat:FEED_006_N2_standard
    title: N2 internal standard (99.999%, Linde)
  has_atmosphere:
  - value: CH4/CO2/N2 = 45:45:10 vol%, total flow 100 mL/min (STP), GHSV = 30000 mL/(g*h)
  has_experiment_duration:
    has_quantity_type: http://qudt.org/vocab/quantitykind/Time
    unit: https://qudt.org/vocab/unit/HR
    value: 20.0
  id: coremeta4cat:REAC_002_DRM_NiCeO2
  product_identification_method:
  - description: 'Shimadzu GC-2014 with TCD detector (Ar carrier gas); column 1: HayeSep
      D (2 m x 1/8 in) for CO2, CH4 separation; column 2: Molecular Sieve 5A (2 m
      x 1/8 in) for CO, H2, N2, CH4 separation; 10-port Valco valve for column switching;
      oven temperature: 50 deg C isothermal; TCD temperature: 250 deg C; injection:
      automated gas sampling valve, 1 mL loop; analysis cycle: 10 min; calibration:
      certified gas standard (Air Liquide CRYSTAL mixture: H2 5%, CO 5%, CH4 5%, CO2
      10%, N2 balance); CH4 conversion, CO2 conversion, H2/CO ratio, and carbon balance
      calculated from N2-normalised molar flows'
    id: coremeta4cat:REAC_002_GC_method
    title: online dual-column gas chromatography (TCD)
  rdf_type:
    id: CHMO:0001446
    title: catalytic reforming
  reactor_temperature_range:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 800
    min_value: 600
    unit: https://qudt.org/vocab/unit/DEG_C
  title:
  - dry methane reforming catalytic activity test (600-800 deg C, 20 h)
  used_catalyst:
  - description: Ni0 after in situ reduction of NiO/CeO2
    id: coremeta4cat:CAT_002_NiCeO2
    title: Ni/CeO2
  used_reactant:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/297
    title: CH4 (99.995% purity, Linde)
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/280
    title: CO2 (99.998% purity, Linde)
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/947
    title: N2 balance (99.999% purity, internal standard for GC quantification)
  used_reactor:
  - description: 'quartz tube reactor, 8 mm inner diameter, 30 cm length; catalyst
      bed: 200 mg NiO/CeO2 (250-500 um sieve fraction) diluted 1:2 (mass) with inert
      SiC chips (500 um); thermocouple inserted into catalyst bed centre; backpressure
      regulator at outlet (1 bar); reactor surrounded by ceramic-fibre furnace with
      PID temperature controller; mass flow controllers (Brooks SLA5850) for CH4,
      CO2, N2'
    id: coremeta4cat:REACT_003_FixedBed_DRM
    title: quartz fixed-bed plug-flow reactor (DRM)
is_about_entity:
- description: 15 wt% NiO on CeO2 support, co-precipitated at pH 8.5, calcined 500
    deg C / 4 h, active phase Ni0 formed by in situ reduction
  id: coremeta4cat:CAT_002_NiO_CeO2
  title: NiO/CeO2 dry reforming catalyst
- description: 13-atom cuboctahedral Ni cluster on 6-layer CeO2(111) p(4x4) periodic
    slab; ReaxFF MD model representing Ni/CeO2 metal-support interface
  id: coremeta4cat:SLAB_002_CeO2_111_Ni13
  title: Ni13/CeO2(111) computational model
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
title:
- 'NiO/CeO2 dry methane reforming catalyst: co-precipitation synthesis, multi-technique
  characterization, catalytic performance, and computational interface study'
was_generated_by:
- activity_designator: Synthesis
  catalyst_measured_properties:
  - 'BET surface area: 42 m2/g'
  - 'NiO crystallite size: 8.4 nm (Scherrer, XRD)'
  - 'Ni loading: 14.7 wt% (ICP-AES)'
  - 'reducibility onset: 280 deg C, completion at 600 deg C (H2-TPR)'
  had_input_entity:
  - id: coremeta4cat:PREC_004_Ni_NO3_6H2O
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 8.72
    title: nickel(II) nitrate hexahydrate (Sigma-Aldrich, purity 99%)
  - id: coremeta4cat:PREC_005_Ce_NO3_6H2O
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 13.03
    title: cerium(III) nitrate hexahydrate (Sigma-Aldrich, purity 99.5%)
  - id: coremeta4cat:PREC_006_Na2CO3
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 5.3
    title: sodium carbonate precipitating agent (anhydrous, Sigma-Aldrich, purity
      99.5%)
  had_output_entity:
  - description: 15 wt% NiO on CeO2 support, co-precipitated at pH 8.5, calcined 500
      deg C / 4 h, sieved to 250-500 um
    id: coremeta4cat:CAT_002_NiO_CeO2
    title: NiO/CeO2 dry reforming catalyst (calcined precursor)
  has_sample_pretreatment:
  - value: 'in situ reduction: 5 vol% H2/N2 at 700 deg C for 1 h (10 deg C/min ramp)
      before DRM tests'
  id: coremeta4cat:SYNTH_002_NiO_CeO2
  nominal_composition:
  - 15 wt% NiO/CeO2
  realized_plan:
    description: 'aqueous solutions of Ni(NO3)2 (0.5 M) and Ce(NO3)3 (0.5 M) mixed
      in stoichiometric ratio; precipitant: 1 M Na2CO3 solution added dropwise at
      2 mL/min; target pH 8.5 maintained by feedback addition; mixing: 600 rpm mechanical
      stirring at 60 deg C for 2 h; aging: 12 h at 60 deg C without stirring; filtration:
      vacuum filtration through Whatman grade 4 filter paper; washing: 5 successive
      deionized water washes until conductivity < 5 uS/cm (Na+ removal); drying: 120
      deg C for 12 h in static air oven; calcination: 5 deg C/min ramp to 500 deg
      C, isothermal hold for 4 h in static air, natural cooling'
    id: coremeta4cat:SYNTH_002_coprecipitation_method
    title: co-precipitation
  solvent:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/962
    title: deionized water (18.2 MOhm cm, MilliQ)
  storage_conditions:
  - sealed glass vial in desiccator, ambient temperature, protected from moisture
- activity_designator: Characterization
  carried_out_by:
  - id: coremeta4cat:DEV_003_Thermo_KAlpha_XPS
    title: Thermo Scientific K-Alpha+ XPS spectrometer
  - id: coremeta4cat:DEV_004_AlKalpha_source
    title: Al K-alpha monochromatic X-ray source (1486.6 eV, 72 W)
  detector_type:
  - 128-channel 2D delay-line detector (DLD)
  evaluated_entity:
  - description: 15 wt% NiO on CeO2 support, calcined at 500 deg C
    id: coremeta4cat:CAT_002_NiO_CeO2
    title: NiO/CeO2 dry reforming catalyst (calcined)
  has_sample_pretreatment:
  - value: outgassed in XPS load-lock chamber at < 1e-7 mbar for 12 h before transfer
      to analysis chamber (< 5e-9 mbar)
  id: coremeta4cat:CHAR_003_XPS_NiO_CeO2
  realized_plan:
    description: 'monochromatic Al K-alpha (1486.6 eV); base pressure 5e-9 mbar; survey
      scan: 0-1350 eV, 1.0 eV step, 50 ms dwell, 3 scans, pass energy 200 eV; high-resolution
      regions: Ni 2p3/2 (845-895 eV), Ce 3d (875-935 eV), O 1s (525-540 eV), C 1s
      (280-295 eV); step size 0.1 eV, 20 scans each, pass energy 50 eV; spot size
      400 um; lens mode: large area XL; charge compensation: dual-beam flood gun (1
      eV electrons + 10 eV Ar+); binding energy scale calibrated to C 1s adventitious
      carbon at 284.8 eV; Shirley background subtraction; peak fitting: Voigt profiles
      (CasaXPS v2.3.25); atomic concentrations from Scofield sensitivity factors corrected
      for transmission function'
    id: coremeta4cat:CHAR_003_XPS_method
    title: X-ray photoelectron spectroscopy (XPS)
  sample_description:
  - NiO/CeO2 co-precipitated catalyst (SYNTH_002), calcined at 500 deg C, as-prepared
    (non-reduced), ca. 10 mg pressed into indium foil
  sample_preparation:
  - lightly pressed into indium foil to obtain flat surface; mounted on sample stub
    with copper tape; no Ar+ sputtering performed
  sample_state:
  - powder
- activity_designator: Characterization
  carried_out_by:
  - id: coremeta4cat:DEV_005_Micromeritics_AutoChem
    title: Micromeritics AutoChem II 2920 chemisorption analyzer
  detector_type:
  - thermal conductivity detector (TCD), Ar carrier gas reference channel
  evaluated_entity:
  - description: 15 wt% NiO on CeO2, calcined at 500 deg C / 4 h
    id: coremeta4cat:CAT_002_NiO_CeO2
    title: NiO/CeO2 dry reforming catalyst (calcined)
  has_sample_pretreatment:
  - value: 'oxidative pretreatment: 10 vol% O2/Ar (50 mL/min) at 300 deg C for 30
      min; cool to 50 deg C under Ar purge'
  id: coremeta4cat:CHAR_004_TPR_NiO_CeO2
  realized_plan:
    description: 'reducing gas: 5 vol% H2/Ar, total flow 50 mL/min (calibrated Brooks
      MFC); temperature programme: 50 deg C to 900 deg C at 10 deg C/min; isothermal
      hold: 30 min at 900 deg C; H2O trap: molecular sieve 3A between reactor outlet
      and TCD to prevent TCD signal interference; baseline: Ar flow for 30 min at
      50 deg C before switching to H2/Ar; H2 consumption quantified by integration
      of TCD signal, calibrated against CuO reference standard (99.9%, 10 mg, single
      reduction peak at 310 deg C); NiO reduction: expected peaks at 280-350 deg C
      (NiO weakly interacting with CeO2) and 400-600 deg C (NiO strongly interacting);
      CeO2 surface reduction: 600-900 deg C'
    id: coremeta4cat:CHAR_004_TPR_method
    title: H2 temperature-programmed reduction (H2-TPR)
  sample_description:
  - NiO/CeO2 calcined at 500 deg C; 50 mg packed in quartz U-tube reactor (4 mm ID);
    quartz wool plugs above and below bed
- activity_designator: Simulation
  calculated_property:
  - description: CeO2(111) cleavage surface energy (clean slab without Ni cluster,
      computed from relaxed DFT-D3 reference at 0 K, used as force field validation
      benchmark)
    value: 1.52 J/m2
  - description: time-averaged Ni-CeO2 adhesion energy per Ni atom (13-atom cluster)
      relative to bulk Ni cohesive energy and clean CeO2(111) slab; computed from
      800 ps production trajectory
    value: -1.83 eV/atom
  - description: first-shell Ni-O coordination distance at Ni cluster / CeO2 interface
      (peak of Ni-O radial distribution function, production trajectory average)
    value: 3.8 Ang
  - description: fraction of Ni atoms in direct contact with CeO2 surface (Ni-O bond
      order > 0.3) averaged over production trajectory; measures cluster wetting /
      spreading
    value: '0.42'
  evaluated_entity:
  - description: 6-layer CeO2(111) p(4x4) slab (256 CeO2 formula units, 768 atoms
      total); bottom 3 layers fixed during MD; 13-atom cuboctahedral Ni cluster adsorbed
      on three-fold hollow O site; 20 Ang vacuum layer; 3D periodic boundary conditions
    id: coremeta4cat:SLAB_002_CeO2_111_Ni13
    title: CeO2(111) surface slab with supported 13-atom Ni cluster
  id: coremeta4cat:SIM_002_MD_Ni_CeO2_111
  realized_plan:
    description: 'force field: ReaxFF C/H/Ni/O parametrisation (van Duin et al. 2012,
      DOI: 10.1021/jp210484t); ensemble: NVT with Nose-Hoover thermostat (tau = 100
      fs) at 800 deg C (1073 K); integration timestep: 0.5 fs; total simulation time:
      1 ns (2,000,000 steps); equilibration phase: 200 ps (400,000 steps) discarded;
      production phase: 800 ps (1,600,000 steps) used for analysis; sampling interval:
      every 1000 steps (0.5 ps); bond order cutoff: C-O 0.3, Ni-O 0.3 (fix reax/c/bonds);
      radial distribution functions computed with OVITO using 0.05 Ang bin width;
      common-neighbour analysis (CNA) to track Ni cluster crystallographic ordering'
    id: coremeta4cat:SIM_002_MD_method
    title: ReaxFF molecular dynamics (NVT, 800 deg C)
  software_package:
  - LAMMPS (29 Sep 2021 stable release, OpenMP build)
  - OVITO 3.7.11 (structure analysis, RDF, CNA, cluster tracking)

```
## CatalysisDataset-2d6m-exeb
### Input
```yaml
creator:
- name:
  - Schmider, Daniel
- name:
  - Maier, Lubow
- name:
  - Deutschmann, Olaf
dataset_distribution:
- access_URL:
  - id: https://hdl.handle.net/21.11165/4cat/2d6m-exeb
    title: Repository landing page
  description:
  - Repository landing page providing access to the per-experiment CSV/JSON data files.
  licence:
    id: https://creativecommons.org/licenses/by/4.0/
    title: CC BY 4.0
description:
- 'Steady-state methanation kinetics screening dataset covering 16 valid experimental
  runs (Exp2,3,4,7,8,9,11,12,13,14,15,16,17,18,19,20 -- Exp1, Exp5, Exp6, Exp10 excluded
  by the data providers, see ReadMe.txt) over 16 distinct supported Ni catalysts (Al2O3,
  SiO2, ZrO2, TiO2, MgAl2O4 supports; 5-40.8 wt% Ni) in isothermal cylindrical fixed-bed
  reactors. Three reaction types were studied depending on feed gas composition: CO
  methanation (4 runs), CO2 methanation (8 runs), and mixed CO/CO2 co-methanation
  (4 runs). Conversion was determined from outlet gas composition analysis. Related
  publication: DOI 10.1021/acs.iecr.1c00389.'
id: hdl:21.11165/4cat/2d6m-exeb
is_about_activity:
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Catalytic CO methanation (CO + 3H2 -> CH4 + H2O) screened over 4 supported Ni
    catalysts (Al2O3, SiO2, ZrO2 supports; 10-20 wt% Ni) in cylindrical isothermal
    fixed-bed reactors (radius 3-10 mm across runs). Steady-state CO conversion measured
    as a function of superficial velocity and temperature. Source runs: Exp2, Exp3,
    Exp4, Exp12 (Ni/Al2O3 x2, Ni/SiO2, Ni/ZrO2). Total pressure ~100-101.3 kPa in
    all four runs.'
  experiment_pressure:
  - description: ~100-101.3 kPa in all 4 runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/KiloPA
    value: 100.0
  id: coremeta4cat:REAC_2d6m-exeb_CO_methanation
  other_identifier:
  - description: Related publication DOI
    notation: doi:10.1021/acs.iecr.1c00389
  product_identification_method:
  - description: CO conversion (dimensionless, 0-1) calculated from inlet and outlet
      CO concentrations. Specific analytical instrument not stated in dataset files;
      gas chromatography is the standard method for this reaction.
    id: coremeta4cat:REAC_2d6m-exeb_CO_product_id
    title: CO conversion from outlet gas composition
  rdf_type:
    id: voc4cat:0000260
    title: hydrogenation
  reaction_name:
  - CO methanation
  reactor_temperature_range:
  - description: Overall temperature range explored across all 4 CO methanation runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 874.6
    min_value: 423.0
    unit: https://qudt.org/vocab/unit/K
  title:
  - CO methanation catalyst screening (4 Ni catalysts)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp2_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 20.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp2_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp2_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 630.0
    - description: 'BET specific surface area (Exp2_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 14.0
    - description: 'Catalyst bed mass (Exp2_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.5
    id: coremeta4cat:CAT_2d6m-exeb_Exp2
    title: 20 wt% Ni/Al2O3 (Exp2)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp3_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 20.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp3_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp3_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 375.0
    - description: 'BET specific surface area (Exp3_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 3.56
    - description: 'Catalyst bed mass (Exp3_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.2
    id: coremeta4cat:CAT_2d6m-exeb_Exp3
    title: 20 wt% Ni/Al2O3 (Exp3)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp4_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 10.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp4_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp4_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 265.0
    - description: 'BET specific surface area (Exp4_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 2.81
    - description: 'Catalyst bed mass (Exp4_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.05
    id: coremeta4cat:CAT_2d6m-exeb_Exp4
    title: 10 wt% Ni/SiO2 (Exp4)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp12_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 10.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp12_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp12_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 265.0
    - description: 'BET specific surface area (Exp12_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 3.06
    - description: 'Catalyst bed mass (Exp12_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.05
    id: coremeta4cat:CAT_2d6m-exeb_Exp12
    title: 10 wt% Ni/ZrO2 (Exp12)
  used_reactant:
  - has_concentration:
    - description: Feed CO mole fraction ranges 1-25% across the 4 runs (Exp2, Exp3,
        Exp4, Exp12 inlet.mole_fractions.CO)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.0
    id: coremeta4cat:REAC_2d6m-exeb_CO
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - has_concentration:
    - description: Feed H2 mole fraction ranges 50-75% across the 4 runs
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 50.0
    id: coremeta4cat:REAC_2d6m-exeb_H2
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Cylindrical fixed-bed reactors, radius 3-10 mm across the 4 runs,
      isothermal operation.
    id: coremeta4cat:REAC_2d6m-exeb_CO_reactor
    title: isothermal cylindrical fixed-bed reactors
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Catalytic CO2 methanation (CO2 + 4H2 -> CH4 + 2H2O) screened over 8 supported
    Ni catalysts (Al2O3, SiO2, ZrO2, MgAl2O4 supports; 10-40.8 wt% Ni) in cylindrical
    isothermal fixed-bed reactors (radius 3-10 mm across runs). Steady-state CO2 conversion
    measured as a function of superficial velocity and temperature. Source runs: Exp7,
    Exp8, Exp9, Exp13, Exp14, Exp15, Exp16, Exp17 (Ni/Al2O3 x4, Ni/MgAl2O4 x2, Ni/ZrO2,
    Ni/SiO2). Total pressure ~100-101.3 kPa in all runs except Exp9 (800 kPa, an outlier
    within this series).'
  experiment_pressure:
  - description: ~100-101.3 kPa in 7 of the 8 runs; Exp9 used 800 kPa (see used_catalyst
      description)
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/KiloPA
    value: 100.0
  id: coremeta4cat:REAC_2d6m-exeb_CO2_methanation
  other_identifier:
  - description: Related publication DOI
    notation: doi:10.1021/acs.iecr.1c00389
  product_identification_method:
  - description: CO2 conversion (dimensionless, 0-1) calculated from inlet and outlet
      CO2 concentrations. Specific analytical instrument not stated in dataset files;
      gas chromatography is the standard method for this reaction.
    id: coremeta4cat:REAC_2d6m-exeb_CO2_product_id
    title: CO2 conversion from outlet gas composition
  rdf_type:
    id: voc4cat:0000259
    title: CO2 hydrogenation
  reaction_name:
  - CO2 methanation
  reactor_temperature_range:
  - description: Overall temperature range explored across all 8 CO2 methanation runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 1114.4
    min_value: 405.1
    unit: https://qudt.org/vocab/unit/K
  title:
  - CO2 methanation catalyst screening (8 Ni catalysts)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp7_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 10.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp7_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp7_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 335.0
    - description: 'BET specific surface area (Exp7_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 4.55
    - description: 'Catalyst bed mass (Exp7_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 1.2
    id: coremeta4cat:CAT_2d6m-exeb_Exp7
    title: 10 wt% Ni/MgAl2O4 (Exp7)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp8_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 20.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp8_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp8_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 375.0
    - description: 'BET specific surface area (Exp8_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 3.56
    - description: 'Catalyst bed mass (Exp8_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.2
    id: coremeta4cat:CAT_2d6m-exeb_Exp8
    title: 20 wt% Ni/Al2O3 (Exp8)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp9_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 40.8
      id: coremeta4cat:CAT_2d6m-exeb_Exp9_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    description: High Ni-loading Al2O3-supported catalyst; this run also used an elevated
      feed pressure of 800 kPa, an outlier relative to the other runs in this series
      (~100-101.3 kPa).
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp9_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 175.0
    - description: 'BET specific surface area (Exp9_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 8.28
    - description: 'Catalyst bed mass (Exp9_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.025
    id: coremeta4cat:CAT_2d6m-exeb_Exp9
    title: 40.8 wt% Ni/Al2O3 (Exp9)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp13_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 10.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp13_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp13_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 265.0
    - description: 'BET specific surface area (Exp13_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 3.06
    - description: 'Catalyst bed mass (Exp13_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.05
    id: coremeta4cat:CAT_2d6m-exeb_Exp13
    title: 10 wt% Ni/ZrO2 (Exp13)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp14_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 10.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp14_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp14_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 265.0
    - description: 'BET specific surface area (Exp14_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 2.81
    - description: 'Catalyst bed mass (Exp14_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.05
    id: coremeta4cat:CAT_2d6m-exeb_Exp14
    title: 10 wt% Ni/SiO2 (Exp14)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp15_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 20.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp15_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp15_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 750.0
    - description: 'Catalyst bed mass (Exp15_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 1.76
    id: coremeta4cat:CAT_2d6m-exeb_Exp15
    title: 20 wt% Ni/Al2O3 (Exp15)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp16_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 15.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp16_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp16_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 630.0
    - description: 'BET specific surface area (Exp16_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 8.72
    - description: 'Catalyst bed mass (Exp16_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.3
    id: coremeta4cat:CAT_2d6m-exeb_Exp16
    title: 15 wt% Ni/Al2O3 (Exp16)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp17_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 10.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp17_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp17_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 335.0
    - description: 'BET specific surface area (Exp17_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 3.84
    - description: 'Catalyst bed mass (Exp17_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 1.2
    id: coremeta4cat:CAT_2d6m-exeb_Exp17
    title: 10 wt% Ni/MgAl2O4 (Exp17)
  used_reactant:
  - has_concentration:
    - description: Feed CO2 mole fraction ranges 1-22.2% across the 8 runs (inlet.mole_fractions.CO2)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.0
    id: coremeta4cat:REAC_2d6m-exeb_CO2
    rdf_type:
      id: CHEBI:16526
      title: carbon dioxide
    title: carbon dioxide
  - has_concentration:
    - description: Feed H2 mole fraction ranges 5.1-77.8% across the 8 runs
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.1
    id: coremeta4cat:REAC_2d6m-exeb_H2_CO2series
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Cylindrical fixed-bed reactors, radius 3-10 mm across the 8 runs,
      isothermal operation.
    id: coremeta4cat:REAC_2d6m-exeb_CO2_reactor
    title: isothermal cylindrical fixed-bed reactors
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Catalytic co-methanation of a mixed CO/CO2 feed (CO + 3H2 -> CH4 + H2O; CO2 +
    4H2 -> CH4 + 2H2O) screened over 4 supported Ni catalysts (ZrO2, SiO2, TiO2, Al2O3
    supports; 5 wt% Ni in all 4) in cylindrical isothermal fixed-bed reactors (radius
    3.77-6.5 mm across runs). Steady-state CO and CO2 conversion measured as a function
    of superficial velocity and temperature. Source runs: Exp11, Exp18, Exp19, Exp20.
    Total pressure ~100 kPa in all four runs.'
  experiment_pressure:
  - description: ~100 kPa in all 4 runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/KiloPA
    value: 100.0
  id: coremeta4cat:REAC_2d6m-exeb_mixed_methanation
  other_identifier:
  - description: Related publication DOI
    notation: doi:10.1021/acs.iecr.1c00389
  product_identification_method:
  - description: CO and CO2 conversion (dimensionless, 0-1) calculated from inlet
      and outlet gas concentrations. Specific analytical instrument not stated in
      dataset files; gas chromatography is the standard method for this reaction.
    id: coremeta4cat:REAC_2d6m-exeb_mixed_product_id
    title: CO and CO2 conversion from outlet gas composition
  rdf_type:
    id: voc4cat:0000260
    title: hydrogenation
  reaction_name:
  - CO/CO2 co-methanation
  reactor_temperature_range:
  - description: Overall temperature range explored across all 4 mixed CO/CO2 methanation
      runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 672.2
    min_value: 428.3
    unit: https://qudt.org/vocab/unit/K
  title:
  - Mixed CO+CO2 methanation catalyst screening (4 Ni catalysts)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp11_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp11_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp11_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 220.0
    - description: 'BET specific surface area (Exp11_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 1.826
    - description: 'Catalyst bed mass (Exp11_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.15
    id: coremeta4cat:CAT_2d6m-exeb_Exp11
    title: 5 wt% Ni/ZrO2 (Exp11)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp18_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp18_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp18_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 3000.0
    - description: 'BET specific surface area (Exp18_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 1.1
    - description: 'Catalyst bed mass (Exp18_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.18
    id: coremeta4cat:CAT_2d6m-exeb_Exp18
    title: 5 wt% Ni/SiO2 (Exp18)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp19_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp19_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp19_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 630.0
    - description: 'BET specific surface area (Exp19_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 14.0
    - description: 'Catalyst bed mass (Exp19_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.15
    id: coremeta4cat:CAT_2d6m-exeb_Exp19
    title: 5 wt% Ni/TiO2 (Exp19)
  - composed_of:
    - has_quantitative_attribute:
      - description: 'Loading (Exp20_metadata.json: catalyst.metal_loading)'
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_2d6m-exeb_Exp20_Ni
      rdf_type:
        id: CHEBI:28112
        title: nickel atom
      title: nickel
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Particle diameter (Exp20_metadata.json: catalyst.particles_mean_diameter)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MicroM
      value: 220.0
    - description: 'BET specific surface area (Exp20_metadata.json: catalyst.specific_surface_area)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 0.897
    - description: 'Catalyst bed mass (Exp20_metadata.json: catalyst.mass)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.15
    id: coremeta4cat:CAT_2d6m-exeb_Exp20
    title: 5 wt% Ni/Al2O3 (Exp20)
  used_reactant:
  - has_concentration:
    - description: Feed CO mole fraction; 0.6% in 3 of 4 runs, 6% in Exp18
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 0.6
    id: coremeta4cat:REAC_2d6m-exeb_CO_mixed
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - has_concentration:
    - description: Feed CO2 mole fraction ranges 6-17% across the 4 runs
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 6.0
    id: coremeta4cat:REAC_2d6m-exeb_CO2_mixed
    rdf_type:
      id: CHEBI:16526
      title: carbon dioxide
    title: carbon dioxide
  - has_concentration:
    - description: Feed H2 mole fraction ranges 57-88% across the 4 runs
      has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 57.0
    id: coremeta4cat:REAC_2d6m-exeb_H2_mixed
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Cylindrical fixed-bed reactors, radius 3.77-6.5 mm across the 4 runs,
      isothermal operation.
    id: coremeta4cat:REAC_2d6m-exeb_mixed_reactor
    title: isothermal cylindrical fixed-bed reactors
is_about_entity:
- description: Supported Ni catalysts on Al2O3, SiO2, ZrO2, TiO2, and MgAl2O4, Ni
    loading 5-40.8 wt%. See used_catalyst under is_about_activity above for per-sample
    detail (particle size, BET surface area, catalyst mass).
  id: coremeta4cat:CAT_2d6m-exeb_all
  title: 16 supported Ni catalyst samples (this screening series)
keyword:
- Chemistry
- Catalysis
- Heterogeneous catalysis
- CO methanation
- CO2 methanation
- Nickel catalyst
- Fixed-bed reactor
other_identifier:
- notation: https://hdl.handle.net/21.11165/4cat/2d6m-exeb
- description: Related publication DOI
  notation: doi:10.1021/acs.iecr.1c00389
publisher:
  name:
  - NFDI4Cat Central Data Repository
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
title:
- 'Dataset for Publication: Reaction Kinetics of CO and CO2 Methanation over Nickel'
was_generated_by:
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_2d6m-exeb_GC
    title: gas chromatograph
  description:
  - 'Steady-state outlet gas composition analysis used to determine CO/CO2 conversion
    for all 16 catalyst screening runs (CO methanation: Exp2, 3, 4, 12; CO2 methanation:
    Exp7, 8, 9, 13, 14, 15, 16, 17; mixed CO/CO2 methanation: Exp11, 18, 19, 20).
    Dataset files do not name a specific instrument model; gas chromatography is the
    standard analytical method for this reaction class and is assumed here.'
  evaluated_entity:
  - description: 'Supported Ni catalysts on Al2O3, SiO2, ZrO2, TiO2, and MgAl2O4,
      Ni loading 5-40.8 wt%, screened for CO methanation, CO2 methanation, and mixed
      CO/CO2 methanation (see the corresponding CatalyticReaction entries for per-catalyst
      detail: used_catalyst in coremeta4cat:REAC_2d6m-exeb_CO_methanation, coremeta4cat:REAC_2d6m-exeb_CO2_methanation,
      coremeta4cat:REAC_2d6m-exeb_mixed_methanation).'
    id: coremeta4cat:CAT_2d6m-exeb_all
    title: 16 supported Ni catalyst samples (this screening series)
  id: coremeta4cat:CHAR_2d6m-exeb_outlet_gas_analysis
  other_identifier:
  - description: Related publication DOI
    notation: doi:10.1021/acs.iecr.1c00389
  rdf_type:
    id: voc4cat:0000130
    title: gas chromatography
  realized_plan:
    description: Analytical protocol for determining reactant/product mole fractions
      from the reactor outlet stream. Method parameters not specified in the source
      dataset files.
    id: coremeta4cat:CHAR_2d6m-exeb_GC_method
    title: Outlet gas GC method
  title:
  - Outlet gas composition analysis (all 16 runs)

```
## CatalysisDataset-32x1-99x6
### Input
```yaml
creator:
- name:
  - Rang, Fabian
- name:
  - Hanf, Schirin
- name:
  - Holtermann, Birger
- name:
  - Eggeler, Yolita
- name:
  - Barth, Simon
- name:
  - Grunwaldt, Jan-Dierk
dataset_distribution:
- access_URL:
  - id: https://hdl.handle.net/21.11165/4cat/32x1-99x6
    title: Repository landing page
  description:
  - Repository landing page providing access to the characterization and catalytic
    testing data files.
  licence:
    id: https://creativecommons.org/licenses/by/4.0/
    title: CC BY 4.0
description:
- Catalyst characterization (BET, ICP-AES, PXRD, DRIFT, IR) and catalytic testing
  data for a series of Pd/P catalysts (nominal 2 wt% Pd, 0-5 wt% P) on Al2O3 and SiO2
  supports, investigating how phosphorus modification of the support tunes the Pd-catalyzed
  selective hydrogenation of cinnamyl alcohol (CAL) and citral. Catalytic performance
  was screened via Central Composite Design (Al2O3/CAL, 27 runs) and full-factorial
  designs (SiO2/CAL, Al2O3/citral, SiO2/citral; 9 runs each) varying temperature (30-70
  C), pressure (1-9 bar), phosphorus loading, and reaction time. TEM is mentioned
  in the original repository description but no TEM data files are included in the
  deposited dataset.
id: hdl:21.11165/4cat/32x1-99x6
is_about_activity:
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - Selective hydrogenation of cinnamyl alcohol (CAL) over 6 Pd/P/Al2O3 catalysts
    (P loading 0-5 wt%, ~2 wt% Pd) in a Central Composite Design (27 runs) exploring
    temperature, pressure, phosphorus loading, and time. An initial fixed-condition
    screening (50C/5bar/30min, hot-filtration leaching test) gave CAL conversion/HCAL
    yield of 32/30% (Pd/Al2O3) and 45/42% (Pd/3P/Al2O3). Conversion ranged 6-96%,
    yield 6-90% across the 27-run design (catalytic_data.xlsx, 'Pd-XPAl2O3_CCD_CAL').
  experiment_pressure:
  - description: Minimum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 1.0
  - description: Maximum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 9.0
  id: coremeta4cat:REAC_32x1-99x6_CAL_Al2O3
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  product_identification_method:
  - description: Substrate conversion and product yield (%) reported with standard
      deviations in catalytic_data.xlsx. Specific analytical instrument not stated
      in the source dataset files; GC is the standard method for this reaction class.
    id: coremeta4cat:REAC_32x1-99x6_CAL_Al2O3_product_id
    title: Conversion/yield quantification
  rdf_type:
    id: voc4cat:0000260
    title: hydrogenation
  reaction_name:
  - selective hydrogenation of cinnamyl alcohol
  reactor_temperature_range:
  - description: Temperature range explored in the design of experiments (catalytic_data.xlsx)
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 343.15
    min_value: 303.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Selective hydrogenation of cinnamyl alcohol over Pd-P/Al2O3 catalysts
  used_catalyst:
  - description: Pd on Al2O3 support, unmodified (P-free) reference catalyst
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 119.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_0P
    title: Pd/Al2O3
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.8
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 0.8
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3 (nominal 1 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 2 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 116.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P
    title: Pd/2P/Al2O3 (nominal 2 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.8
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.5
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 105.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3 (nominal 3 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 3.7
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 4 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 112.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P
    title: Pd/4P/Al2O3 (nominal 4 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.9
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 4.6
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 108.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P
    title: Pd/5P/Al2O3 (nominal 5 wt% P)
  used_reactant:
  - id: coremeta4cat:REAC_32x1-99x6_CAL_Al2O3_substrate
    rdf_type:
      id: CHEBI:15554
      title: cinnamyl alcohol
    title: cinnamyl alcohol
  - id: coremeta4cat:REAC_32x1-99x6_CAL_Al2O3_H2
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Batch pressurised reactor (autoclave or similar sealed vessel), inferred
      from the 1-9 bar working pressure range and hot-filtration leaching test noted
      in catalytic_data.xlsx. Specific reactor model not stated in the source dataset
      files.
    id: coremeta4cat:REAC_32x1-99x6_CAL_Al2O3_reactor
    title: batch pressurized reactor
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - Selective hydrogenation of cinnamyl alcohol (CAL) over 4 Pd/P/SiO2 catalysts (P
    loading 0-5 wt%, ~2 wt% Pd) in a full factorial design (9 runs) exploring temperature,
    pressure, phosphorus loading, and time. An initial fixed-condition screening (50C/5bar/30min,
    hot-filtration leaching test) gave CAL conversion/HCAL yield of 23/22% (Pd/SiO2)
    and 78/40% (Pd/3P/SiO2). Conversion ranged 12-100%, yield 9-56% across the 9-run
    design (catalytic_data.xlsx, 'Pd-XPSiO2_FF_CAL').
  experiment_pressure:
  - description: Minimum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 1.0
  - description: Maximum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 9.0
  id: coremeta4cat:REAC_32x1-99x6_CAL_SiO2
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  product_identification_method:
  - description: Substrate conversion and product yield (%) reported with standard
      deviations in catalytic_data.xlsx. Specific analytical instrument not stated
      in the source dataset files; GC is the standard method for this reaction class.
    id: coremeta4cat:REAC_32x1-99x6_CAL_SiO2_product_id
    title: Conversion/yield quantification
  rdf_type:
    id: voc4cat:0000260
    title: hydrogenation
  reaction_name:
  - selective hydrogenation of cinnamyl alcohol
  reactor_temperature_range:
  - description: Temperature range explored in the design of experiments (catalytic_data.xlsx)
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 343.15
    min_value: 303.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Selective hydrogenation of cinnamyl alcohol over Pd-P/SiO2 catalysts
  used_catalyst:
  - description: Pd on SiO2 support, unmodified (P-free) reference catalyst
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 126.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_0P
    title: Pd/SiO2
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_SiO2_1P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.1
      id: coremeta4cat:CAT_32x1-99x6_SiO2_1P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on SiO2 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2 (nominal 1 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.8
      id: coremeta4cat:CAT_32x1-99x6_SiO2_3P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.6
      id: coremeta4cat:CAT_32x1-99x6_SiO2_3P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on SiO2 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 98.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2 (nominal 3 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_SiO2_5P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 4.8
      id: coremeta4cat:CAT_32x1-99x6_SiO2_5P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on SiO2 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 72.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_5P
    title: Pd/5P/SiO2 (nominal 5 wt% P)
  used_reactant:
  - id: coremeta4cat:REAC_32x1-99x6_CAL_SiO2_substrate
    rdf_type:
      id: CHEBI:15554
      title: cinnamyl alcohol
    title: cinnamyl alcohol
  - id: coremeta4cat:REAC_32x1-99x6_CAL_SiO2_H2
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Batch pressurised reactor (autoclave or similar sealed vessel), inferred
      from the 1-9 bar working pressure range and hot-filtration leaching test noted
      in catalytic_data.xlsx. Specific reactor model not stated in the source dataset
      files.
    id: coremeta4cat:REAC_32x1-99x6_CAL_SiO2_reactor
    title: batch pressurized reactor
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - Selective hydrogenation of citral over 3 Pd/P/Al2O3 catalysts (1, 3, 5 wt% nominal
    P loading, ~2 wt% Pd) in a full factorial design (9 runs) exploring temperature,
    pressure, phosphorus loading, and time. Conversion ranged 15-85%, yield 15-65%
    across the 9-run design (catalytic_data.xlsx, 'Pd-XPAl2O3_FF_Citral').
  experiment_pressure:
  - description: Minimum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 1.0
  - description: Maximum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 9.0
  id: coremeta4cat:REAC_32x1-99x6_Citral_Al2O3
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  product_identification_method:
  - description: Substrate conversion and product yield (%) reported with standard
      deviations in catalytic_data.xlsx. Specific analytical instrument not stated
      in the source dataset files; GC is the standard method for this reaction class.
    id: coremeta4cat:REAC_32x1-99x6_Citral_Al2O3_product_id
    title: Conversion/yield quantification
  rdf_type:
    id: voc4cat:0000260
    title: hydrogenation
  reaction_name:
  - selective hydrogenation of citral
  reactor_temperature_range:
  - description: Temperature range explored in the design of experiments (catalytic_data.xlsx)
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 343.15
    min_value: 303.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Selective hydrogenation of citral over Pd-P/Al2O3 catalysts
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.8
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 0.8
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3 (nominal 1 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.8
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.5
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 105.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3 (nominal 3 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.9
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 4.6
      id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on Al2O3 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 108.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P
    title: Pd/5P/Al2O3 (nominal 5 wt% P)
  used_reactant:
  - id: coremeta4cat:REAC_32x1-99x6_Citral_Al2O3_substrate
    rdf_type:
      id: CHEBI:29085
      title: citral
    title: citral
  - id: coremeta4cat:REAC_32x1-99x6_Citral_Al2O3_H2
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Batch pressurised reactor (autoclave or similar sealed vessel), inferred
      from the 1-9 bar working pressure range and hot-filtration leaching test noted
      in catalytic_data.xlsx. Specific reactor model not stated in the source dataset
      files.
    id: coremeta4cat:REAC_32x1-99x6_Citral_Al2O3_reactor
    title: batch pressurized reactor
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - Selective hydrogenation of citral over 3 Pd/P/SiO2 catalysts (1, 3, 5 wt% nominal
    P loading, ~2 wt% Pd) in a full factorial design (9 runs) exploring temperature,
    pressure, phosphorus loading, and time. Conversion ranged 11-100%, yield 11-84%
    across the 9-run design (catalytic_data.xlsx, 'Pd-XPSiO2_FF_Citral').
  experiment_pressure:
  - description: Minimum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 1.0
  - description: Maximum pressure in the design space
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 9.0
  id: coremeta4cat:REAC_32x1-99x6_Citral_SiO2
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  product_identification_method:
  - description: Substrate conversion and product yield (%) reported with standard
      deviations in catalytic_data.xlsx. Specific analytical instrument not stated
      in the source dataset files; GC is the standard method for this reaction class.
    id: coremeta4cat:REAC_32x1-99x6_Citral_SiO2_product_id
    title: Conversion/yield quantification
  rdf_type:
    id: voc4cat:0000260
    title: hydrogenation
  reaction_name:
  - selective hydrogenation of citral
  reactor_temperature_range:
  - description: Temperature range explored in the design of experiments (catalytic_data.xlsx)
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 343.15
    min_value: 303.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Selective hydrogenation of citral over Pd-P/SiO2 catalysts
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_SiO2_1P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.1
      id: coremeta4cat:CAT_32x1-99x6_SiO2_1P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on SiO2 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2 (nominal 1 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.8
      id: coremeta4cat:CAT_32x1-99x6_SiO2_3P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.6
      id: coremeta4cat:CAT_32x1-99x6_SiO2_3P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on SiO2 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 98.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2 (nominal 3 wt% P)
  - composed_of:
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 2.0
      id: coremeta4cat:CAT_32x1-99x6_SiO2_5P_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    - has_quantitative_attribute:
      - description: ICP-AES measured loading (icp_results.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 4.8
      id: coremeta4cat:CAT_32x1-99x6_SiO2_5P_P
      rdf_type:
        id: CHEBI:28659
        title: phosphorus atom
      title: phosphorus
    description: Pd on SiO2 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 72.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_5P
    title: Pd/5P/SiO2 (nominal 5 wt% P)
  used_reactant:
  - id: coremeta4cat:REAC_32x1-99x6_Citral_SiO2_substrate
    rdf_type:
      id: CHEBI:29085
      title: citral
    title: citral
  - id: coremeta4cat:REAC_32x1-99x6_Citral_SiO2_H2
    rdf_type:
      id: CHEBI:18276
      title: molecular hydrogen
    title: hydrogen
  used_reactor:
  - description: Batch pressurised reactor (autoclave or similar sealed vessel), inferred
      from the 1-9 bar working pressure range and hot-filtration leaching test noted
      in catalytic_data.xlsx. Specific reactor model not stated in the source dataset
      files.
    id: coremeta4cat:REAC_32x1-99x6_Citral_SiO2_reactor
    title: batch pressurized reactor
is_about_entity:
- description: Pd catalysts (nominal 2 wt% Pd) with 0-5 wt% nominal phosphorus loading
    on Al2O3 (6 samples) and SiO2 (4 samples) supports. See used_catalyst under is_about_activity
    and evaluated_entity under was_generated_by above for per-sample detail (ICP-AES
    loading, BET surface area).
  id: coremeta4cat:CAT_32x1-99x6_all
  title: 10 Pd/P catalyst samples (Al2O3 and SiO2 supports)
keyword:
- Chemistry
- Engineering
- Catalysis
- Heterogeneous catalysis
- Palladium catalyst
- Phosphorus modification
- Selective hydrogenation
- Cinnamyl alcohol
- Citral
other_identifier:
- notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
- description: Methodology reference cited for the DRIFT pseudo-absorbance conversion
    (not this dataset's own publication)
  notation: doi:10.1021/ac0702802
publisher:
  name:
  - NFDI4Cat Central Data Repository
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
release_date: '2026-03-11'
title:
- "Support Engineering with Phosphorus: Tuning the Palladium-Catalyzed Selective Hydrogenation\
  \ of \u03B1,\u03B2-Unsaturated Aldehydes"
was_generated_by:
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_32x1-99x6_BET
    title: BET surface area analyser
  description:
  - Brunauer-Emmett-Teller specific surface area determination for all 10 Pd/P-Al2O3
    and Pd/P-SiO2 catalysts (0-5 wt% nominal P loading). Surface area ranged 72-126
    m2/g, generally decreasing with increasing P loading (bet_results.txt).
  evaluated_entity:
  - description: Pd on Al2O3, P-free reference
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_0P
    title: Pd/Al2O3
  - description: Pd on Al2O3, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3
  - description: Pd on Al2O3, nominal 2 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P
    title: Pd/2P/Al2O3
  - description: Pd on Al2O3, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3
  - description: Pd on Al2O3, nominal 4 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P
    title: Pd/4P/Al2O3
  - description: Pd on Al2O3, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P
    title: Pd/5P/Al2O3
  - description: Pd on SiO2, P-free reference
    id: coremeta4cat:CAT_32x1-99x6_SiO2_0P
    title: Pd/SiO2
  - description: Pd on SiO2, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2
  - description: Pd on SiO2, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2
  - description: Pd on SiO2, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_5P
    title: Pd/5P/SiO2
  id: coremeta4cat:CHAR_32x1-99x6_BET
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  rdf_type:
    id: enm:0000064
    title: BET analysis
  realized_plan:
    description: Standard N2 physisorption at liquid-nitrogen temperature (-196C),
      Brunauer-Emmett-Teller analysis. Adsorbate gas and measurement temperature not
      explicitly stated in bet_results.txt; assumed standard BET convention.
    id: coremeta4cat:CHAR_32x1-99x6_BET_method
    title: N2 physisorption BET method
  title:
  - BET surface area analysis (10 catalysts)
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_32x1-99x6_DRIFT
    title: FTIR spectrometer with DRIFT accessory
  description:
  - Diffuse reflectance infrared Fourier transform spectroscopy of CO adsorbed at
    room temperature, for 4 catalysts (Pd/Al2O3, Pd/3P/Al2O3, Pd/SiO2, Pd/3P/SiO2).
    Spectra converted to pseudo-absorbance (log(1/reflectance)) per Anal. Chem. 2007,
    79, 10, 3912-3918 (DOI 10.1021/ac0702802) and baseline-corrected (info_drifts.txt);
    OriginPro 2023 used for analysis/plotting.
  evaluated_entity:
  - description: Pd on Al2O3, P-free reference
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_0P
    title: Pd/Al2O3
  - description: Pd on Al2O3, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3
  - description: Pd on SiO2, P-free reference
    id: coremeta4cat:CAT_32x1-99x6_SiO2_0P
    title: Pd/SiO2
  - description: Pd on SiO2, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2
  id: coremeta4cat:CHAR_32x1-99x6_DRIFT
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  rdf_type:
    id: CHMO:0000645
    title: diffuse reflectance infrared Fourier transform spectroscopy
  realized_plan:
    description: CO adsorption at room temperature; pseudo-absorbance = log(1/reflectance).
    id: coremeta4cat:CHAR_32x1-99x6_DRIFT_method
    title: CO-adsorption DRIFT method
  title:
  - DRIFT CO-adsorption spectroscopy (4 catalysts)
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_32x1-99x6_ICPAES
    title: ICP-AES spectrometer
  description:
  - Inductively coupled plasma atomic emission spectroscopy for bulk Pd and P content
    of the 8 P-modified catalysts (measured Pd 1.8-2.0 wt%, P 0.8-4.8 wt%, deviating
    somewhat from nominal loadings; icp_results.txt). P-free reference catalysts (Pd/Al2O3,
    Pd/SiO2) were not analysed by ICP-AES.
  evaluated_entity:
  - description: Pd on Al2O3, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3
  - description: Pd on Al2O3, nominal 2 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P
    title: Pd/2P/Al2O3
  - description: Pd on Al2O3, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3
  - description: Pd on Al2O3, nominal 4 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P
    title: Pd/4P/Al2O3
  - description: Pd on Al2O3, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P
    title: Pd/5P/Al2O3
  - description: Pd on SiO2, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2
  - description: Pd on SiO2, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2
  - description: Pd on SiO2, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_5P
    title: Pd/5P/SiO2
  id: coremeta4cat:CHAR_32x1-99x6_ICPAES
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  rdf_type:
    id: CHMO:0000267
    title: inductively coupled plasma atomic emission spectroscopy
  realized_plan:
    description: 'Elements analyzed: Pd, P. Results reported in wt% (icp_results.txt).'
    id: coremeta4cat:CHAR_32x1-99x6_ICPAES_method
    title: ICP-AES elemental analysis method
  title:
  - ICP-AES elemental composition analysis (8 catalysts)
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_32x1-99x6_IR
    title: FTIR spectrometer
  description:
  - Infrared spectroscopy of the 6 P-modified catalysts (1, 3, 5 wt% nominal P on
    Al2O3 and SiO2). Wavenumber range ~400-3599 cm-1, 3319 data points per file, pseudo-absorbance
    convention consistent with the DRIFT data.
  evaluated_entity:
  - description: Pd on Al2O3, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3
  - description: Pd on Al2O3, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3
  - description: Pd on Al2O3, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P
    title: Pd/5P/Al2O3
  - description: Pd on SiO2, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2
  - description: Pd on SiO2, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2
  - description: Pd on SiO2, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_5P
    title: Pd/5P/SiO2
  id: coremeta4cat:CHAR_32x1-99x6_IR
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  rdf_type:
    id: CHMO:0000630
    title: infrared spectroscopy
  realized_plan:
    description: Wavenumber range ~400-3599 cm-1; pseudo-absorbance units.
    id: coremeta4cat:CHAR_32x1-99x6_IR_method
    title: Infrared spectroscopy method
  title:
  - Infrared spectroscopy (6 catalysts)
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_32x1-99x6_PXRD
    title: X-ray diffractometer
  description:
  - Powder X-ray diffraction for phase identification of all 10 Pd/P-Al2O3 and Pd/P-SiO2
    catalysts, plus a P/SiO2 support-only reference sample without Pd (file PXRD_1PSiO2.xy).
    Two-theta range ~2-92 degrees, step size 0.015 degrees (most files); two files
    (nominal 5 wt% P samples) cover a shorter range ~2-63.5 degrees.
  evaluated_entity:
  - description: Pd on Al2O3, P-free reference
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_0P
    title: Pd/Al2O3
  - description: Pd on Al2O3, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3
  - description: Pd on Al2O3, nominal 2 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P
    title: Pd/2P/Al2O3
  - description: Pd on Al2O3, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3
  - description: Pd on Al2O3, nominal 4 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P
    title: Pd/4P/Al2O3
  - description: Pd on Al2O3, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_5P
    title: Pd/5P/Al2O3
  - description: Pd on SiO2, P-free reference
    id: coremeta4cat:CAT_32x1-99x6_SiO2_0P
    title: Pd/SiO2
  - description: Pd on SiO2, nominal 1 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2
  - description: Pd on SiO2, nominal 3 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2
  - description: Pd on SiO2, nominal 5 wt% P
    id: coremeta4cat:CAT_32x1-99x6_SiO2_5P
    title: Pd/5P/SiO2
  id: coremeta4cat:CHAR_32x1-99x6_PXRD
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/32x1-99x6
  rdf_type:
    id: CHMO:0000158
    title: powder X-ray diffraction
  realized_plan:
    description: Two-theta scan, ~2-92 degrees, step size 0.015 degrees. One file
      (PXRD_1PSiO2.xy) is a Pd-free P/SiO2 support reference; one file (PXRD_Pd5Al2O3.xy)
      is missing the 'P' in its name but is interpreted as the nominal 5 wt% P/Al2O3
      sample based on the file series context (matches ICP sample FR507).
    id: coremeta4cat:CHAR_32x1-99x6_PXRD_method
    title: Powder XRD measurement method
  title:
  - Powder XRD phase analysis (10 catalysts)

```
## CatalysisDataset-6mxw-xsrd
### Input
```yaml
creator:
- name:
  - Weber, Sebastian
dataset_distribution:
- access_URL:
  - id: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
    title: Repository landing page
  licence:
    id: https://creativecommons.org/licenses/by/4.0/
    title: CC BY 4.0
description:
- 'Data from Weber et al., ACS Catal. 2025, 15, 18857: DFT and machine-learned-potential
  (EquiformerV2/OCP, MACE-MPA-0) binding energies of OH and CO used to screen active
  phases; nominal and XRF compositions of 76 co-precipitated Cu-Ga-Al hydrotalcite-like
  precursors; the 13 compositions of the initial activity screening; calcination temperatures
  of the seven optimized catalysts; and the 17-condition test protocol for CO2/CO
  hydrogenation to methanol and dimethyl ether at 80 bar in a 16-fold fixed-bed reactor.
  Catalytic results (conversions, yields) and further characterization (PXRD, N2 sorption,
  TPR, N2O-RFC, TEM) are reported in the article but not deposited.'
id: hdl:21.11165/4cat/6mxw-xsrd
is_about_activity:
- catalyst_form:
  - bulk
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Gas-phase testing of the first-generation (Cu0.465Ga0.07Al0.465, calcined at
    500, 600 and 700 C) and second-generation (Cu0.85Al0.15 with 1 wt% Ga, two calcination
    steps) catalysts under all 17 conditions of the test protocol: 80 bar, 225-300
    C, GHSV 3000 and 6000 h-1, CO2 13-27.1 vol%, CO 0-15.8 vol%, H2 36.7-76 vol%,
    5 vol% Ar, balance N2 (0-26.7 vol%), H2/COx 1.2-4. Pretreatment: 2 h at 300 C
    and 20 bar under 10 vol% Ar in N2 (GHSV 6000 h-1, 48 L/h), then in-situ reduction
    in the syngas feed. Products are methanol and dimethyl ether, with methane as
    a minor by-product. Conversions and yields are reported in the article''s figures
    only; they are not deposited.'
  experiment_pressure:
  - description: Constant across all 17 conditions
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 80.0
  feed_composition_range:
  - description: CO2 in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 27.1
    min_value: 13.0
    unit: https://qudt.org/vocab/unit/PERCENT
  - description: CO in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 15.8
    min_value: 0.0
    unit: https://qudt.org/vocab/unit/PERCENT
  - description: H2 in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 76.0
    min_value: 36.7
    unit: https://qudt.org/vocab/unit/PERCENT
  - description: Ar in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 5.0
    min_value: 5.0
    unit: https://qudt.org/vocab/unit/PERCENT
  - description: N2 balance, computed as 100 minus the listed components
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 26.7
    min_value: 0.0
    unit: https://qudt.org/vocab/unit/PERCENT
  generated_product:
  - id: coremeta4cat:PROD_6mxw-xsrd_MeOH
    rdf_type:
      id: CHEBI:17790
      title: methanol
    title: methanol
  - id: coremeta4cat:PROD_6mxw-xsrd_DME
    rdf_type:
      id: CHEBI:28887
      title: methoxymethane
    title: dimethyl ether
  - id: coremeta4cat:PROD_6mxw-xsrd_CH4
    rdf_type:
      id: CHEBI:16183
      title: methane
    title: methane (by-product)
  id: coremeta4cat:REAC_6mxw-xsrd_CO2_hydrogenation
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  rdf_type:
    id: voc4cat:0000259
    title: CO2 hydrogenation
  reaction_name:
  - hydrogenation of CO2/CO to methanol and dimethyl ether
  reactor_temperature_range:
  - description: 225-300 C (article Table 1)
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 573.15
    min_value: 498.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - CO2/CO hydrogenation over optimized Cu-Ga-Al mixed metal oxides (17 conditions,
    7 catalysts)
  used_catalyst:
  - description: First generation, calcined at 500 C
    id: coremeta4cat:CAT_6mxw-xsrd_G1_500
    title: Cu0.465Ga0.07Al0.465(500)
  - description: First generation, calcined at 600 C
    id: coremeta4cat:CAT_6mxw-xsrd_G1_600
    title: Cu0.465Ga0.07Al0.465(600)
  - description: First generation, calcined at 700 C
    id: coremeta4cat:CAT_6mxw-xsrd_G1_700
    title: Cu0.465Ga0.07Al0.465(700)
  - description: Second generation; Cu0.85Al0.1(...) in the deposited sample names
    id: coremeta4cat:CAT_6mxw-xsrd_G2_450_250
    title: Cu0.85Al0.15(450)-1wt.%Ga(250)
  - description: Second generation
    id: coremeta4cat:CAT_6mxw-xsrd_G2_450_350
    title: Cu0.85Al0.15(450)-1wt.%Ga(350)
  - description: Second generation
    id: coremeta4cat:CAT_6mxw-xsrd_G2_550_250
    title: Cu0.85Al0.15(550)-1wt.%Ga(250)
  - description: Second generation
    id: coremeta4cat:CAT_6mxw-xsrd_G2_550_350
    title: Cu0.85Al0.15(550)-1wt.%Ga(350)
  used_reactant:
  - id: coremeta4cat:REAC_6mxw-xsrd_CO2
    rdf_type:
      id: CHEBI:16526
      title: carbon dioxide
    title: carbon dioxide
  - id: coremeta4cat:REAC_6mxw-xsrd_CO
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - id: coremeta4cat:REAC_6mxw-xsrd_H2
    rdf_type:
      id: CHEBI:18276
      title: dihydrogen
    title: dihydrogen
  - description: 5 vol% in every feed
    id: coremeta4cat:REAC_6mxw-xsrd_Ar
    rdf_type:
      id: CHEBI:49475
      title: argon atom
    title: argon
  - description: Balance gas (article, Table 1 footnote)
    id: coremeta4cat:REAC_6mxw-xsrd_N2
    rdf_type:
      id: CHEBI:17997
      title: dinitrogen
    title: dinitrogen
  used_reactor:
  - catalyst_bed_diameter:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MilliM
      value: 4.5
    catalyst_bed_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      unit: https://qudt.org/vocab/unit/MilliL
      value: 0.5
    description: Stainless steel 1.4571 tubes, 4.5 mm inner diameter, 290 mm long;
      0.5 mL catalyst, sieve fraction 250-315 um (tablets pressed at 9 t, crushed
      and sieved), pre- and post-bed of corundum.
    id: coremeta4cat:REAC_6mxw-xsrd_reactor
    reactor_designator: coremeta4cat:FixedBedReactor
    title: 16-fold parallel fixed-bed reactor system (hte GmbH)
- catalyst_form:
  - bulk
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Initial activity screening of 13 compositions calcined at 600 C (Cu 0.15-0.6,
    Al 0-0.78, Ga 0-0.6 metal fractions) under conditions 1-8 of the test protocol:
    80 bar, 225-300 C, GHSV 3000 h-1 (condition 1: 6000 h-1), CO2 13-27.1 vol%, CO
    0-15.8 vol%, H2 63.3-76 vol%, 5 vol% Ar, N2 balance. Same 16-fold fixed-bed reactor
    and pretreatment as the optimized catalysts. The highest combined MeOH + DME yields
    were found for Cu0.40Ga0.07Al0.53 and Cu0.33Ga0.07Al0.60 (article, section 3.3);
    yields are not deposited.'
  experiment_pressure:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 80.0
  feed_composition_range:
  - description: CO2 in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 27.1
    min_value: 13.0
    unit: https://qudt.org/vocab/unit/PERCENT
  - description: CO in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 15.8
    min_value: 0.0
    unit: https://qudt.org/vocab/unit/PERCENT
  - description: H2 in the feed
    has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
    max_value: 76.0
    min_value: 63.3
    unit: https://qudt.org/vocab/unit/PERCENT
  generated_product:
  - id: coremeta4cat:PROD_6mxw-xsrd_MeOH
    rdf_type:
      id: CHEBI:17790
      title: methanol
    title: methanol
  - id: coremeta4cat:PROD_6mxw-xsrd_DME
    rdf_type:
      id: CHEBI:28887
      title: methoxymethane
    title: dimethyl ether
  - id: coremeta4cat:PROD_6mxw-xsrd_CH4
    rdf_type:
      id: CHEBI:16183
      title: methane
    title: methane (by-product, yield below 2%)
  id: coremeta4cat:REAC_6mxw-xsrd_screening
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  rdf_type:
    id: voc4cat:0000259
    title: CO2 hydrogenation
  reaction_name:
  - hydrogenation of CO2/CO to methanol and dimethyl ether
  reactor_temperature_range:
  - description: 225-300 C, conditions 1-8
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 573.15
    min_value: 498.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Activity screening of 13 Cu-Ga-Al mixed metal oxides for CO2/CO hydrogenation
    (8 conditions)
  used_catalyst:
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.15Ga0.07Al0.78
    title: Cu0.15Ga0.07Al0.78 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.25Ga0.07Al0.68
    title: Cu0.25Ga0.07Al0.68 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.25Ga0.25Al0.50
    title: Cu0.25Ga0.25Al0.50 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.25Ga0.50Al0.25
    title: Cu0.25Ga0.50Al0.25 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.33Ga0.07Al0.60
    title: Cu0.33Ga0.07Al0.60 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_Cu0.33Ga0.33Al0.33
    title: Cu0.33Ga0.33Al0.33 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.33Ga0.60Al0.07
    title: Cu0.33Ga0.60Al0.07 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.40Ga0.07Al0.53
    title: Cu0.40Ga0.07Al0.53 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.40Ga0.20Al0.40
    title: Cu0.40Ga0.20Al0.40 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.50Ga0.25Al0.25
    title: Cu0.50Ga0.25Al0.25 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.60Al0.40
    title: Cu0.60Al0.40 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.60Ga0.20Al0.20
    title: Cu0.60Ga0.20Al0.20 (600)
  - id: coremeta4cat:CAT_6mxw-xsrd_S_Cu0.60Ga0.40
    title: Cu0.60Ga0.40 (600)
  used_reactant:
  - id: coremeta4cat:REAC_6mxw-xsrd_CO2
    rdf_type:
      id: CHEBI:16526
      title: carbon dioxide
    title: carbon dioxide
  - id: coremeta4cat:REAC_6mxw-xsrd_CO
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - id: coremeta4cat:REAC_6mxw-xsrd_H2
    rdf_type:
      id: CHEBI:18276
      title: dihydrogen
    title: dihydrogen
  - id: coremeta4cat:REAC_6mxw-xsrd_Ar
    rdf_type:
      id: CHEBI:49475
      title: argon atom
    title: argon
  - id: coremeta4cat:REAC_6mxw-xsrd_N2
    rdf_type:
      id: CHEBI:17997
      title: dinitrogen
    title: dinitrogen (balance)
  used_reactor:
  - catalyst_bed_diameter:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/MilliM
      value: 4.5
    catalyst_bed_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      unit: https://qudt.org/vocab/unit/MilliL
      value: 0.5
    description: 'As for the optimized catalysts: 4.5 mm inner diameter, 0.5 mL catalyst,
      250-315 um.'
    id: coremeta4cat:REAC_6mxw-xsrd_reactor
    reactor_designator: coremeta4cat:FixedBedReactor
    title: 16-fold parallel fixed-bed reactor system (hte GmbH)
is_about_entity:
- description: 76 HTC precursors characterized by XRF; 13 screening catalysts and
    7 optimized catalysts tested; 17 doped oxide sites (DFT) and 37 intermetallic
    and elemental compositions (machine-learned potentials). See was_generated_by
    and is_about_activity for detail.
  id: coremeta4cat:CAT_6mxw-xsrd_all
  title: Cu-Ga-Al mixed metal oxides and computational surface models
is_referenced_by:
- id: https://doi.org/10.1021/acscatal.5c03876
  title: Weber et al., ACS Catal. 2025, 15, 18857-18876
keyword:
- CO2 hydrogenation
- mixed-metal-oxide catalyst
- machine learning
- machine learning interatomic potentials
- density functional theory
- reaction mechanism
other_identifier:
- notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
publisher:
  name:
  - NFDI4Cat Central Data Repository
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
title:
- Copper Gallium Aluminum Mixed Metal Oxides as Alternative Catalyst Candidates for
  Efficient Conversion of Carbon Dioxide to Methanol and Dimethyl Ether
was_generated_by:
- activity_designator: Synthesis
  catalyst_measured_properties:
  - No measured properties of these three samples are deposited; the article reports
    XRD, N2 sorption, TPR, N2O-RFC and TEM results for the first generation in figures
    and the SI.
  had_input_entity:
  - id: coremeta4cat:PREC_6mxw-xsrd_CuNO3
    title: "copper(II) nitrate trihydrate, Cu(NO3)2\xB73H2O (Sigma-Aldrich, 98.8%)"
  - id: coremeta4cat:PREC_6mxw-xsrd_AlNO3
    title: "aluminium nitrate nonahydrate, Al(NO3)3\xB79H2O (Sigma-Aldrich, 99.9%)"
  - id: coremeta4cat:PREC_6mxw-xsrd_GaNO3
    title: "gallium(III) nitrate hydrate, Ga(NO3)3\xB7xH2O (Sigma-Aldrich, 99.9%)"
  had_output_entity:
  - id: coremeta4cat:CAT_6mxw-xsrd_G1_500
    title: Cu0.465Ga0.07Al0.465(500)
  - id: coremeta4cat:CAT_6mxw-xsrd_G1_600
    title: Cu0.465Ga0.07Al0.465(600)
  - id: coremeta4cat:CAT_6mxw-xsrd_G1_700
    title: Cu0.465Ga0.07Al0.465(700)
  id: coremeta4cat:SYN_6mxw-xsrd_gen1
  nominal_composition:
  - Cu0.465Ga0.07Al0.465 (metal fractions Cu 0.465, Al 0.465, Ga 0.07)
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  realized_plan:
    description: Same route as the library (precipitant 1.6 M NaOH / 0.2 M Na2CO3,
      pH 9, ageing 2 h at 65 C, freeze-drying, see the library-example record). One
      precursor batch, calcined 4 h at 4 C/min in clean dry air at 500, 600 or 700
      C.
    has_calcination_atmosphere:
    - value: clean dry air
    has_calcination_dwelling_time:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 4
    has_calcination_heating_rate:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/TemperaturePerTime
      unit: https://qudt.org/vocab/unit/K-PER-MIN
      value: 4
    has_calcination_temperature_range:
    - description: 500, 600 and 700 C, one sample each
      has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      max_value: 973.15
      min_value: 773.15
      unit: https://qudt.org/vocab/unit/K
    id: coremeta4cat:SYN_6mxw-xsrd_gen1_method
    plan_designator: voc4cat:0007795
    title: automated co-precipitation at pH 9, ageing, freeze-drying, calcination
      at 500/600/700 C
  title:
  - Cu0.465Ga0.07Al0.465 mixed metal oxide, three calcination temperatures
- activity_designator: Synthesis
  catalyst_measured_properties:
  - No measured properties of the intermediate oxides are deposited.
  had_input_entity:
  - id: coremeta4cat:PREC_6mxw-xsrd_CuNO3
    title: "copper(II) nitrate trihydrate, Cu(NO3)2\xB73H2O (Sigma-Aldrich, 98.8%)"
  - id: coremeta4cat:PREC_6mxw-xsrd_AlNO3
    title: "aluminium nitrate nonahydrate, Al(NO3)3\xB79H2O (Sigma-Aldrich, 99.9%)"
  had_output_entity:
  - id: coremeta4cat:INT_6mxw-xsrd_Cu0.85Al0.15_450
    title: Cu0.85Al0.15 oxide calcined at 450 C
  - id: coremeta4cat:INT_6mxw-xsrd_Cu0.85Al0.15_550
    title: Cu0.85Al0.15 oxide calcined at 550 C
  id: coremeta4cat:SYN_6mxw-xsrd_gen2_step1
  nominal_composition:
  - Cu0.85Al0.15 (metal fractions Cu 0.85, Al 0.15)
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  realized_plan:
    description: Same route as the library (precipitant 1.6 M NaOH / 0.2 M Na2CO3,
      pH 9, ageing 2 h at 65 C, freeze-drying, see Synthesis-6mxw-xsrd-library-example.yaml).
      Calcined 4 h at 4 C/min in clean dry air at 450 or 550 C (Tcalc,1).
    has_calcination_atmosphere:
    - value: clean dry air
    has_calcination_dwelling_time:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 4
    has_calcination_heating_rate:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/TemperaturePerTime
      unit: https://qudt.org/vocab/unit/K-PER-MIN
      value: 4
    has_calcination_temperature_range:
    - description: 450 or 550 C
      has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      max_value: 823.15
      min_value: 723.15
      unit: https://qudt.org/vocab/unit/K
    id: coremeta4cat:SYN_6mxw-xsrd_gen2_step1_method
    plan_designator: voc4cat:0007795
    title: automated co-precipitation at pH 9, ageing, freeze-drying, calcination
      at 450/550 C
  title:
  - Co-precipitated Cu0.85Al0.15 precursor, calcined at 450 or 550 C
- activity_designator: Synthesis
  catalyst_measured_properties:
  - No measured properties of these four samples are deposited.
  had_input_entity:
  - id: coremeta4cat:INT_6mxw-xsrd_Cu0.85Al0.15_450
    title: Cu0.85Al0.15 oxide calcined at 450 C (output of step 1)
  - id: coremeta4cat:INT_6mxw-xsrd_Cu0.85Al0.15_550
    title: Cu0.85Al0.15 oxide calcined at 550 C (output of step 1)
  - id: coremeta4cat:PREC_6mxw-xsrd_GaNO3
    title: "gallium(III) nitrate hydrate, Ga(NO3)3\xB7xH2O (Sigma-Aldrich, 99.9%),\
      \ aqueous solution"
  had_output_entity:
  - id: coremeta4cat:CAT_6mxw-xsrd_G2_450_250
    title: Cu0.85Al0.15(450)-1wt.%Ga(250)
  - id: coremeta4cat:CAT_6mxw-xsrd_G2_450_350
    title: Cu0.85Al0.15(450)-1wt.%Ga(350)
  - id: coremeta4cat:CAT_6mxw-xsrd_G2_550_250
    title: Cu0.85Al0.15(550)-1wt.%Ga(250)
  - id: coremeta4cat:CAT_6mxw-xsrd_G2_550_350
    title: Cu0.85Al0.15(550)-1wt.%Ga(350)
  id: coremeta4cat:SYN_6mxw-xsrd_gen2_step2
  nominal_composition:
  - Cu0.85Al0.15 mixed oxide with 1 wt% Ga (target loading)
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  realized_plan:
    description: Aqueous Ga(NO3)3 to a target of 1 wt% Ga, drying at 80 C, calcination
      4 h at 4 C/min in clean dry air at 250 or 350 C (Tcalc,2).
    has_calcination_atmosphere:
    - value: clean dry air
    has_calcination_dwelling_time:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 4
    has_calcination_heating_rate:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/TemperaturePerTime
      unit: https://qudt.org/vocab/unit/K-PER-MIN
      value: 4
    has_calcination_temperature_range:
    - description: 250 or 350 C
      has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      max_value: 623.15
      min_value: 523.15
      unit: https://qudt.org/vocab/unit/K
    has_drying_temperature:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      unit: https://qudt.org/vocab/unit/K
      value: 353.15
    id: coremeta4cat:SYN_6mxw-xsrd_gen2_step2_method
    impregnation_type:
    - incipient_wetness
    plan_designator: voc4cat:0007028
    title: incipient wetness impregnation with Ga(NO3)3, drying, calcination at 250/350
      C
  title:
  - 1 wt% Ga on Cu0.85Al0.15 oxide by incipient wetness impregnation, calcined at
    250 or 350 C
- activity_designator: Synthesis
  catalyst_measured_properties:
  - 'XRF of the HTC precursor: Cu 0.42, Al 0.22, Ga 0.36 (metal fractions; nominal
    0.33/0.33/0.34)'
  had_input_entity:
  - id: coremeta4cat:PREC_6mxw-xsrd_CuNO3
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 5.25
    title: "copper(II) nitrate trihydrate, Cu(NO3)2\xB73H2O (Sigma-Aldrich, 98.8%)"
  - id: coremeta4cat:PREC_6mxw-xsrd_AlNO3
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 8.37
    title: "aluminium nitrate nonahydrate, Al(NO3)3\xB79H2O (Sigma-Aldrich, 99.9%)"
  - description: Water content x not stated.
    id: coremeta4cat:PREC_6mxw-xsrd_GaNO3
    precursor_quantity:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 8.92
    title: "gallium(III) nitrate hydrate, Ga(NO3)3\xB7xH2O (Sigma-Aldrich, 99.9%)"
  had_output_entity:
  - description: One of the 13 screening samples (calcined at 600 C).
    id: coremeta4cat:CAT_6mxw-xsrd_Cu0.33Ga0.33Al0.33
    title: Cu0.33Ga0.33Al0.33 mixed metal oxide
  id: coremeta4cat:SYN_6mxw-xsrd_CuAlGaO4
  nominal_composition:
  - CuAlGaO4 (metal fractions Cu 0.33, Al 0.33, Ga 0.33)
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  realized_plan:
    description: Metal nitrate solution fed at 1.6 mL/min into a glass reactor prefilled
      with 200 mL water, overhead stirrer at 500 rpm, ambient temperature; precipitant
      dosed to hold pH 9 +- 0.1. Suspension aged 2 h at 65 C at 500 rpm, cooled, filtered,
      washed to pH 7 +- 0.3, freeze-dried at -10 C and 3 mbar for 12 h to the HTC
      precursor. Calcination 4 h at 4 C/min in clean dry air; the library was calcined
      at 400, 500, 600, 700 and 900 C, the screening samples at 600 C. In-house computer-controlled
      precipitation plant.
    drying_device:
    - freeze dryer (-10 C, 3 mbar)
    filtration:
    - suction filter
    has_aging_duration:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 2
    has_aging_temperature:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      unit: https://qudt.org/vocab/unit/K
      value: 338.15
    has_calcination_atmosphere:
    - value: clean dry air
    has_calcination_dwelling_time:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 4
    has_calcination_heating_rate:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/TemperaturePerTime
      unit: https://qudt.org/vocab/unit/K-PER-MIN
      value: 4
    has_calcination_temperature_range:
    - description: 400-900 C across the library; screening samples at 600 C
      has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      max_value: 1173.15
      min_value: 673.15
      unit: https://qudt.org/vocab/unit/K
    has_drying_duration:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 12
    has_drying_temperature:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      unit: https://qudt.org/vocab/unit/K
      value: 263.15
    has_mixing_speed:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AngularVelocity
      unit: https://qudt.org/vocab/unit/REV-PER-MIN
      value: 500
    has_ph_value:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/PH
      unit: https://qudt.org/vocab/unit/PH
      value: 9.0
    id: coremeta4cat:SYN_6mxw-xsrd_coprecipitation_method
    order_of_addition:
    - metal nitrate solution pumped into prefilled water; precipitant added to keep
      pH 9
    plan_designator: voc4cat:0007795
    precipitating_agent:
    - id: CHEBI:32145
      title: sodium hydroxide
    - id: CHEBI:29377
      title: sodium carbonate
    precipitating_concentration:
    - description: NaOH
      has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration
      unit: https://qudt.org/vocab/unit/MOL-PER-L
      value: 1.6
    - description: Na2CO3
      has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration
      unit: https://qudt.org/vocab/unit/MOL-PER-L
      value: 0.2
    purification:
    - washed with deionised water until pH 7 +- 0.3
    title: automated co-precipitation at constant pH, ageing, freeze-drying, calcination
  solvent:
  - id: coremeta4cat:SOLV_6mxw-xsrd_water
    title: deionised water (150 mL for the metal nitrates; reactor prefilled with
      200 mL)
  title:
  - Co-precipitation of the CuAlGaO4 hydrotalcite-like precursor and calcination
- activity_designator: Characterization
  carried_out_by:
  - description: Rh X-ray tube; ESPRIT software (article, section 2.1.4).
    id: coremeta4cat:DEV_6mxw-xsrd_XRF
    title: Bruker M4 TORNADO micro-XRF spectrometer
  description:
  - X-ray fluorescence analysis of 76 Cu-Ga-Al compositions spanning the Cu/Al/Ga
    ternary (Cu 0-1, Al 0-1, Ga 0-1, metal fractions normalised to 1), including the
    three single-metal end members. According to the article (section 3.2), XRF was
    measured on the freeze-dried hydrotalcite-like (HTC) precursors, i.e. before calcination.
    Measured Cu, Al and Ga fractions are reported next to the nominal fractions.
  evaluated_entity:
  - description: Co-precipitated, freeze-dried HTC precursors of the Cu-Ga-Al mixed
      metal oxides; individual samples are identified only by their composition, not
      by a sample ID.
    id: coremeta4cat:CAT_6mxw-xsrd_HTC_library
    title: Cu-Ga-Al hydrotalcite-like precursor library (76 compositions)
  id: coremeta4cat:CHAR_6mxw-xsrd_XRF
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  rdf_type:
    id: VOC4CAT:0000067
    title: X-ray fluorescence
  realized_plan:
    description: Elemental composition by the fundamental parameter method in ESPRIT;
      metal fractions of Cu, Al and Ga normalised to their sum. Sample preparation
      and measurement conditions are not stated in the main text of the article.
    id: coremeta4cat:CHAR_6mxw-xsrd_XRF_method
    title: XRF determination of Cu, Al and Ga metal fractions
  title:
  - XRF elemental analysis (76 Cu-Ga-Al hydrotalcite-like precursors)
- activity_designator: Simulation
  calculated_property:
  - adsorbate:
    - OH
    description: Range over all sites (Ga2O3-Zn lowest, CuGa2O4-Cu highest); the reference
      state is not defined in the main text.
    material_composition:
    - CuGa2O4, pristine and doped with Al, Co, Cu, Ge, In, Ni or Sn
    - Ga2O3, pristine and doped with Al, Pd, Pt, Rh, Ru, Sn, Zn or Zr
    property_designator: coremeta4cat:AdsorptionEnergetics
    title: OH binding energy
    value: -1.87 to 1.41 eV (17 sites)
  - adsorbate:
    - CO
    description: Range over all sites (Ga2O3-Ru lowest, pristine Ga2O3 highest).
    energy_reference:
    - CO(g)
    material_composition:
    - CuGa2O4, pristine and doped with Al, Co, Cu, Ge, In, Ni or Sn
    - Ga2O3, pristine and doped with Al, Pd, Pt, Rh, Ru, Sn, Zn or Zr
    property_designator: coremeta4cat:AdsorptionEnergetics
    title: CO binding energy
    value: -2.20 to 0.51 eV (17 sites)
  description:
  - 'Density functional theory binding energies of OH and CO at 17 sites: pristine
    CuGa2O4 and CuGa2O4 doped with Al, Co, Cu, Ge, In, Ni or Sn, and pristine Ga2O3
    and Ga2O3 doped with Al, Pd, Pt, Rh, Ru, Sn, Zn or Zr. Site notation in the source
    file is <host>-<dopant>, e.g. CuGa2O4-Co. Part of the theory-based prediction
    that led to the Cu-Ga-Al system (article, section 3.1).'
  evaluated_entity:
  - description: Dopants Al, Co, Cu, Ge, In, Ni, Sn. Facet and slab model are in the
      article's SI.
    id: coremeta4cat:SLAB_6mxw-xsrd_CuGa2O4_sites
    title: CuGa2O4 surface models, pristine and with 7 dopants
  - description: Dopants Al, Pd, Pt, Rh, Ru, Sn, Zn, Zr. Facet, polymorph and slab
      model are in the article's SI.
    id: coremeta4cat:SLAB_6mxw-xsrd_Ga2O3_sites
    title: Ga2O3 surface models, pristine and with 8 dopants
  id: coremeta4cat:SIM_6mxw-xsrd_DFT_active_sites
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  rdf_type:
    id: VOC4CAT:0000215
    title: density functional theory
  realized_plan:
    description: Vienna Ab initio Simulation Package with the PBE functional and projector
      augmented waves. The article uses PBE-D3 when verifying the machine-learned
      potentials; whether D3 was applied for this table is not stated in the main
      text. Cut-off, k-points and convergence criteria are in the SI.
    exchange_correlation_functional:
    - PBE
    id: coremeta4cat:SIM_6mxw-xsrd_DFT_method
    plan_designator: coremeta4cat:DFT
    title: periodic DFT, PBE, PAW
  software_package:
  - VASP
  - Atomic Simulation Environment (ASE), structure generation
  - pymatgen, structure generation
  title:
  - DFT binding energies of OH and CO at 17 oxide surface sites
- activity_designator: Simulation
  calculated_property:
  - adsorbate:
    - OH
    description: Range over all compositions (Al4Cu9 lowest, Fe and GaNi3 highest).
    property_designator: coremeta4cat:AdsorptionEnergetics
    title: OH binding energy
    value: -1.50 to 2.91 eV (31 compositions)
  - adsorbate:
    - CO
    description: Range over all compositions (Ir lowest, Fe highest).
    property_designator: coremeta4cat:AdsorptionEnergetics
    title: CO binding energy
    value: -2.51 to 1.14 eV (31 compositions)
  description:
  - Binding energies of OH and CO computed with the MACE-MPA-0 machine-learned interatomic
    potential for 31 elemental and intermetallic compositions, as a second model next
    to the OCP screening; both serve as prescreening and sampling for DFT calculations,
    with DFT verification at the PBE-D3 level (Weber et al., ACS Catal. 2025, Table
    2 and section 3.1). Surface facets, adsorption sites and the reference states
    of the binding energies are in the article's SI, not in the main text.
  evaluated_entity:
  - description: Ag9In4, Al, Al4Cu9, CuFe3, Co, CoGa3, CoIn3, CoMn3, Cu, Cu3Ga, Cu3Mn,
      Cu3Rh, Cu7In3, Cu9Ga4, CuGa2, CuNi, Fe, FeNi, Ga3Ni5, GaMn, GaNi3, In, InRh,
      InSb, Ir, Mn, Ni, Pd, Rh, Sn, Zn. All 31 were also computed with the OCP model,
      partly under a different spelling of the formula. Facets and slab models not
      stated.
    id: coremeta4cat:SLAB_6mxw-xsrd_MACE_compositions
    title: 31 elemental and intermetallic surface models
  id: coremeta4cat:SIM_6mxw-xsrd_MLIP_MACE
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  realized_plan:
    description: Single-point or relaxation protocol, adsorbate placement and reference
      energies not stated in the deposited files.
    id: coremeta4cat:SIM_6mxw-xsrd_MLIP_MACE_method
    title: machine-learned interatomic potential (MACE-MPA-0)
  software_package:
  - MACE-MPA-0 foundation model (article, Table 2)
  title:
  - MACE-MPA-0 binding-energy screening of OH and CO (31 compositions)
- activity_designator: Simulation
  calculated_property:
  - adsorbate:
    - OH
    description: Range over all compositions (InSb lowest, Pd highest).
    property_designator: coremeta4cat:AdsorptionEnergetics
    title: OH binding energy
    value: -5.35 to 0.79 eV (37 compositions)
  - adsorbate:
    - CO
    description: Range over all compositions (InSb lowest, Al highest).
    property_designator: coremeta4cat:AdsorptionEnergetics
    title: CO binding energy
    value: -5.12 to -0.13 eV (37 compositions)
  description:
  - Binding energies of OH and CO computed with an Open Catalyst Project (OCP) machine-learned
    interatomic potential for 37 elemental and intermetallic compositions, as prescreening
    and sampling for DFT calculations (article, Table 2). Surface facets, adsorption
    sites and the reference states of the binding energies are in the article's SI,
    not in the main text.
  evaluated_entity:
  - description: Al, Al4Cu9, Co, Cu, Cu3Rh, CuNi, Fe, Fe3Cu, FeNi, Ga2Cu, Ga3Co, Ga3Ni5,
      Ga4Cu9, GaCu3, GaNi3, In, In3Co, In3Cu7, In3Ga, In4Ag9, InRh, InSb, Ir, Mn,
      Mn3Co, Mn3In, MnCu3, MnGa, Ni, Pd, Rh, Sn, Zn, Zn2Pd, Zn3Sn, ZnGa3, ZnIn3. Facets
      and slab models not stated.
    id: coremeta4cat:SLAB_6mxw-xsrd_OCP_compositions
    title: 37 elemental and intermetallic surface models
  id: coremeta4cat:SIM_6mxw-xsrd_MLIP_OCP
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/6mxw-xsrd
  realized_plan:
    description: Single-point or relaxation protocol, adsorbate placement and reference
      energies not stated in the deposited files.
    id: coremeta4cat:SIM_6mxw-xsrd_MLIP_OCP_method
    title: machine-learned interatomic potential (OCP model)
  software_package:
  - EquiformerV2-31M-S2EF-OC20-All+MD (Open Catalyst Project); inferred from article
    Table 2
  title:
  - OCP binding-energy screening of OH and CO (37 compositions)

```
## CatalysisDataset-8ppb-aeky
### Input
```yaml
creator:
- name:
  - Doerr, Mark
- name:
  - Weigmann, Konstantin
- name:
  - Schulig, Lukas
dataset_distribution:
- access_URL:
  - id: https://hdl.handle.net/21.11165/4cat/8ppb-aeky
    title: Repository landing page
  licence:
    id: https://creativecommons.org/licenses/by/4.0/
    title: CC BY 4.0
description:
- 'Computational part of Weigmann et al., ACS Catal. (2025): protein preparation of
  the Ruegeria sp. amine transaminase variant 3FCR-4M, induced-fit docking of the
  PLP-bound substrate (S)-1-(2-chlorophenyl)ethanamine, Desmond molecular dynamics
  of the complex in 3FCR-4M and the mutants S19V/P423F (4M-N15) and G151A/P423F (4M-N16),
  and Prime MM/GBSA relative binding free energies. All results are in 17 software
  archives (about 33 GB). The enzyme kinetics and preparative reactions of the article
  are not part of this dataset.'
id: hdl:21.11165/4cat/8ppb-aeky
is_about_entity:
- description: 3FCR-4M (Y59W/Y87F/Y152F/T231A), 4M-N15 (S19V/P423F), 4M-N16 (G151A/P423F).
    See was_generated_by for detail.
  id: coremeta4cat:ENZ_8ppb-aeky_all
  title: Amine transaminase 3FCR-4M and two mutants with the PLP-bound substrate 2a
is_referenced_by:
- id: https://doi.org/10.1021/acscatal.5c04248
  title: Weigmann et al., ACS Catal. (2025), doi:10.1021/acscatal.5c04248
keyword:
- biocatalysis
- amine transaminase
- molecular dynamics
- MM/GBSA
- docking
- protein engineering
other_identifier:
- notation: https://hdl.handle.net/21.11165/4cat/8ppb-aeky
publisher:
  name:
  - NFDI4Cat Central Data Repository
rdf_type:
- id: voc4cat:0000204
  title: biocatalysis
title:
- 'Datasets for Publication: Navigating the Sequence-Function Landscape: AI-Driven
  Discovery of Unseen and SynergisticMutations in an Amine Transaminase - Molecular
  Dynamic Simulations'
was_generated_by:
- activity_designator: Simulation
  description:
  - Desmond molecular dynamics of the docked substrate-cofactor complex in 3FCR-4M
    and the mutants S19V/P423F (4M-N15, deposit M1) and G151A/P423F (4M-N16, deposit
    M2), run to investigate why these mutations change the kinetic parameters. Each
    variant has a system setup, a minimisation, an equilibration and a production
    run (12 archives, about 32 GB). The production runs extend beyond 100 ns; trajectories
    were analysed with the Simulation Interaction Diagram and in-house scripts using
    the Schrodinger Python API, and frames after 100 ns were used for MM/GBSA.
  evaluated_entity:
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M_complex
    title: 3FCR-4M with cofactor-bound substrate 2a
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M-M1_complex
    title: 4M-N15 = 3FCR-4M-S19V/P423F (deposit M1) with cofactor-bound substrate
      2a
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M-M2_complex
    title: 4M-N16 = 3FCR-4M-G151A/P423F (deposit M2) with cofactor-bound substrate
      2a
  id: coremeta4cat:SIM_8ppb-aeky_MD
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/8ppb-aeky
  realized_plan:
    description: Force field, water model, ensemble, temperature, timestep and simulation
      length are in the article's SI and the Desmond configuration files inside the
      archives; neither was read.
    id: coremeta4cat:SIM_8ppb-aeky_MD_method
    plan_designator: NCIT:C18097
    title: 'molecular dynamics: setup, minimisation, equilibration, production'
  software_package:
  - Desmond (Schrodinger suite)
  - Simulation Interaction Diagram and Schrodinger Python API, analysis
  title:
  - Molecular dynamics of the substrate-cofactor complex in 3FCR-4M, 4M-N15 and 4M-N16
- activity_designator: Simulation
  calculated_property:
  - description: Relative binding free energy (ddG) of 4M-N15 (S19V/P423F) vs. 3FCR-4M
    value: -1.86 kcal/mol
  - description: Relative binding free energy (ddG) of 4M-N16 (G151A/P423F) vs. 3FCR-4M
    value: -1.11 kcal/mol
  description:
  - Prime MM/GBSA end-point calculations of the binding free energy of the cofactor-bound
    substrate 2a ((S)-1-(2-chlorophenyl)ethanamine bound to PLP) in 3FCR-4M and the
    mutants S19V/P423F (4M-N15, deposit M1) and G151A/P423F (4M-N16, deposit M2).
    Frames taken from the molecular dynamics runs after 100 ns, every 200th frame,
    both binding sites of the dimer, giving 50 absolute values per complex. Relative
    values are the mean of each mutant minus the mean of 3FCR-4M. The article reports
    them as consistent in magnitude and trend with the experimentally determined KM
    values.
  evaluated_entity:
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M_complex
    title: 3FCR-4M with cofactor-bound substrate 2a
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M-M1_complex
    title: 4M-N15 = 3FCR-4M-S19V/P423F (deposit M1) with cofactor-bound substrate
      2a
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M-M2_complex
    title: 4M-N16 = 3FCR-4M-G151A/P423F (deposit M2) with cofactor-bound substrate
      2a
  id: coremeta4cat:SIM_8ppb-aeky_MMGBSA
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/8ppb-aeky
  realized_plan:
    description: Minimization approach, VSGB solvation model, OPLS4 force field; residues
      within 5 A of the ligands flexible; frames after 100 ns, every 200th frame;
      both binding sites of the dimer.
    id: coremeta4cat:SIM_8ppb-aeky_MMGBSA_method
    title: MM/GBSA end-point free energy on MD frames
  software_package:
  - Prime MM-GBSA (Schrodinger suite)
  title:
  - MM/GBSA binding free energy of the substrate-cofactor complex in 3FCR-4M, 4M-N15
    and 4M-N16
- activity_designator: Simulation
  description:
  - Induced-fit docking with Glide to predict the initial binding mode of the cofactor-bound
    substrate in 3FCR-4M, the starting structure for molecular dynamics. The substrate
    is 2a, (S)-1-(2-chlorophenyl)ethanamine, bound to pyridoxal 5'-phosphate (PLP);
    the article shows the resulting poses as "substrate-cofactor complexes ((S)-2)"
    (Figure 4). "CPEA" in the archive name is taken to abbreviate this amine.
  evaluated_entity:
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M
    title: amine transaminase 3FCR-4M (Ruegeria sp., PDB 3FCR, Y59W/Y87F/Y152F/T231A)
  - id: coremeta4cat:LIG_8ppb-aeky_2a_PLP
    title: (S)-1-(2-chlorophenyl)ethanamine bound to pyridoxal 5'-phosphate
  id: coremeta4cat:SIM_8ppb-aeky_induced_fit_docking
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/8ppb-aeky
  realized_plan:
    description: Glide Induced Fit; settings in the article's SI, not read from the
      archive.
    id: coremeta4cat:SIM_8ppb-aeky_induced_fit_docking_method
    title: induced-fit ligand docking
  software_package:
  - Glide, Induced Fit docking protocol (Schrodinger suite)
  title:
  - Induced-fit docking of the substrate-cofactor complex into 3FCR-4M
- activity_designator: Simulation
  description:
  - Preparation of the initial structure of 3FCR-4M for docking and molecular dynamics
    with the Protein Preparation Wizard. 3FCR-4M is the amine transaminase from Ruegeria
    sp. (PDB 3FCR) with the four mutations Y59W, Y87F, Y152F and T231A. The file descriptions
    of the deposit spell it 3CFR; the file names and the article use 3FCR.
  evaluated_entity:
  - id: coremeta4cat:ENZ_8ppb-aeky_3FCR-4M
    title: amine transaminase 3FCR-4M (Ruegeria sp., PDB 3FCR, Y59W/Y87F/Y152F/T231A)
  id: coremeta4cat:SIM_8ppb-aeky_protein_preparation
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/8ppb-aeky
  realized_plan:
    description: Protein Preparation Wizard workflow; settings in the article's SI,
      not read from the archive.
    id: coremeta4cat:SIM_8ppb-aeky_protein_preparation_method
    title: protein structure preparation
  software_package:
  - Protein Preparation Wizard (Schrodinger suite)
  title:
  - Protein preparation of the amine transaminase variant 3FCR-4M

```
## CatalysisDataset-arp5-s69r
### Input
```yaml
creator:
- name:
  - Neyyathala, Arjun
- name:
  - Jung, Felix
- name:
  - Barth, Simon
- name:
  - Feldmann, Claus
- name:
  - Grunwaldt, Jan-Dierk
- name:
  - Jevtovik, Ivana
- name:
  - Schunk, Stephan A.
- name:
  - Dolcet, Paolo
- name:
  - Gross, Silvia
- name:
  - Hanf, Schirin
dataset_distribution:
- access_URL:
  - id: https://hdl.handle.net/21.11165/4cat/arp5-s69r
    title: Repository landing page
  description:
  - Repository landing page providing access to the characterization and catalytic
    testing data files.
  licence:
    id: https://creativecommons.org/licenses/by/4.0/
    title: CC BY 4.0
description:
- 'Catalyst characterization (PXRD, DRIFT, CO chemisorption, XPS, STEM) and catalytic
  testing data for Pd3P/SiO2 (a phosphorus-modified palladium phosphide catalyst,
  internal code ARNE01) compared against an unmodified Pd/SiO2 reference (ARNE02),
  for Pd-catalyzed carbonylation reactions of aryl iodides. 31 batch reactor runs
  span three reaction types: alkoxycarbonylation (27 runs; mainly iodobenzene + ethanol
  -> ethyl benzoate, exploring reaction time, base, temperature, and substrate/nucleophile
  scope), phenoxycarbonylation (1 run, phenol nucleophile), and aminocarbonylation
  (3 runs, aniline nucleophile, 100-140 C). PXRD additionally covers two further Pd3P/SiO2
  loading variants (1 wt% and 10 wt% Pd), and STEM additionally covers a recycled/spent
  Pd3P/SiO2 sample recovered after catalytic testing; STEM method details are documented
  but no STEM image/data files are included in the deposited dataset.'
id: hdl:21.11165/4cat/arp5-s69r
is_about_activity:
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - Pd-catalyzed aminocarbonylation of iodobenzene with aniline as the nucleophile
    (in toluene, triethylamine base) to form benzanilide, over Pd3P/SiO2. 3 runs at
    100, 120, and 140 C (5 h, CO 10 bar); yield/conversion increased with temperature
    from 10% to 78%.
  experiment_pressure:
  - description: Initial CO pressure, constant across the 3 runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 10.0
  id: coremeta4cat:REAC_arp5-s69r_Aminocarbonylation
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  product_identification_method:
  - description: Gas chromatography-mass spectrometry with n-decane internal standard.
    id: coremeta4cat:REAC_arp5-s69r_Amino_product_id
    title: GC-MS product quantification
  rdf_type:
    id: voc4cat:0000247
    title: carbonylation
  reaction_name:
  - Pd-catalyzed aminocarbonylation of iodobenzene
  reactor_temperature_range:
  - description: 100-140 C across the 3 runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 413.15
    min_value: 373.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Aminocarbonylation of iodobenzene over Pd3P/SiO2 (3 runs)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: Loading (Overview Reaction Description-2.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    description: Palladium phosphide (Pd3P) nanoparticles supported on silica, 5 wt%
      Pd, 0.5 mol% metal loading.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Catalyst mass used per batch test
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.01
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, internal code ARNE01)
  used_reactant:
  - id: coremeta4cat:REAC_arp5-s69r_CO
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - id: coremeta4cat:REAC_arp5-s69r_Amino_iodobenzene
    title: iodobenzene
  - id: coremeta4cat:REAC_arp5-s69r_Amino_aniline
    title: aniline
  used_reactor:
  - description: Batch autoclave, cylindrical stainless steel reaction chamber (25
      mL, 25.4 x 50.8 mm ID), overhead stirrer at 1000 rpm, electric heating.
    id: coremeta4cat:REAC_arp5-s69r_reactor
    title: Parr 5500 series compact reactor
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - Pd-catalyzed alkoxycarbonylation (CO insertion + alcohol trapping) of aryl iodides
    to form aryl esters, mainly iodobenzene + ethanol -> ethyl benzoate. 24 runs used
    Pd3P/SiO2 (ARNE01), exploring reaction time (5 min - 3 h, series A), base screening
    (triethylamine, sodium acetate, potassium hydroxide, potassium carbonate, or no
    base, series B), temperature-time kinetics grid (60-80 C x 0.5-1 h, series k),
    and substrate/nucleophile scope (methanol, isopropanol, and aryl iodide substrates
    bromoiodobenzene/iodotoluene/iodoanisole, series S1-S5). 3 further runs (series
    C) repeated the time-course on Pd/SiO2 (ARNE02, P-free reference) for comparison.
    Conversion/yield ranged 7-100% across all 27 runs. Batch reactor, CO 6 bar, ethanol
    solvent (except S1 methanol, S2 isopropanol).
  experiment_pressure:
  - description: Initial CO pressure, constant across all 27 runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 6.0
  id: coremeta4cat:REAC_arp5-s69r_Carbonylation
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  product_identification_method:
  - description: Gas chromatography-mass spectrometry with n-decane internal standard;
      conversion/yield/selectivity computed from GC-MS peak areas.
    id: coremeta4cat:REAC_arp5-s69r_Carbonylation_product_id
    title: GC-MS product quantification
  rdf_type:
    id: voc4cat:0000247
    title: carbonylation
  reaction_name:
  - Pd-catalyzed alkoxycarbonylation of aryl iodides
  reactor_temperature_range:
  - description: 60-100 C across the 27 runs
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 373.15
    min_value: 333.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Alkoxycarbonylation of aryl iodides over Pd3P/SiO2 and Pd/SiO2 (27 runs)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: Loading (Overview Reaction Description-2.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    description: Palladium phosphide (Pd3P) nanoparticles supported on silica, 5 wt%
      Pd, 0.5 mol% metal loading.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Catalyst mass used per batch test
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.01
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, internal code ARNE01)
  - composed_of:
    - has_quantitative_attribute:
      - description: Loading (Overview Reaction Description-2.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    description: Unmodified (phosphorus-free) palladium nanoparticles supported on
      silica, 5 wt% Pd, 0.5 mol% metal loading -- reference catalyst for comparison
      against the Pd3P phosphide.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Catalyst mass used per batch test
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.01
    id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt
    title: Pd/SiO2 (5 wt% Pd, internal code ARNE02)
  used_reactant:
  - id: coremeta4cat:REAC_arp5-s69r_CO
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - description: Iodobenzene in most runs; bromoiodobenzene (S3), iodotoluene (S4),
      and iodoanisole (S5) in the substrate-scope runs.
    id: coremeta4cat:REAC_arp5-s69r_Carbonylation_substrate
    title: aryl iodide substrate
  - description: Ethanol in most runs (also the reaction solvent); methanol (S1) and
      isopropanol (S2) in the nucleophile-scope runs.
    id: coremeta4cat:REAC_arp5-s69r_Carbonylation_alcohol
    title: alcohol nucleophile
  - description: Triethylamine in most runs; sodium acetate, potassium hydroxide,
      potassium carbonate, or no base in the base-screening runs (series B).
    id: coremeta4cat:REAC_arp5-s69r_Carbonylation_base
    title: base
  used_reactor:
  - description: Batch autoclave, cylindrical stainless steel reaction chamber (25
      mL, 25.4 x 50.8 mm ID), overhead stirrer at 1000 rpm, electric heating.
    id: coremeta4cat:REAC_arp5-s69r_reactor
    title: Parr 5500 series compact reactor
- catalyst_form:
  - supported
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Pd-catalyzed phenoxycarbonylation of iodobenzene with phenol as the nucleophile
    (in toluene, triethylamine base) to form phenyl benzoate, over Pd3P/SiO2. Single
    run: 100 C, 7 h, CO 6 bar, yield/conversion 30%.'
  experiment_pressure:
  - description: Initial CO pressure
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 6.0
  id: coremeta4cat:REAC_arp5-s69r_Phenoxycarbonylation
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  product_identification_method:
  - description: Gas chromatography-mass spectrometry with n-decane internal standard.
    id: coremeta4cat:REAC_arp5-s69r_Phenoxy_product_id
    title: GC-MS product quantification
  rdf_type:
    id: voc4cat:0000247
    title: carbonylation
  reaction_name:
  - Pd-catalyzed phenoxycarbonylation of iodobenzene
  reactor_temperature_range:
  - description: 100 C, single run
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 373.15
    min_value: 373.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - Phenoxycarbonylation of iodobenzene over Pd3P/SiO2 (1 run)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: Loading (Overview Reaction Description-2.txt)
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 5.0
      id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt_Pd
      rdf_type:
        id: CHEBI:33363
        title: palladium atom
      title: palladium
    description: Palladium phosphide (Pd3P) nanoparticles supported on silica, 5 wt%
      Pd, 0.5 mol% metal loading.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Catalyst mass used per batch test
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.01
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, internal code ARNE01)
  used_reactant:
  - id: coremeta4cat:REAC_arp5-s69r_CO
    rdf_type:
      id: CHEBI:17245
      title: carbon monoxide
    title: carbon monoxide
  - id: coremeta4cat:REAC_arp5-s69r_Phenoxy_iodobenzene
    title: iodobenzene
  - id: coremeta4cat:REAC_arp5-s69r_Phenoxy_phenol
    title: phenol
  used_reactor:
  - description: Batch autoclave, cylindrical stainless steel reaction chamber (25
      mL, 25.4 x 50.8 mm ID), overhead stirrer at 1000 rpm, electric heating.
    id: coremeta4cat:REAC_arp5-s69r_reactor
    title: Parr 5500 series compact reactor
is_about_entity:
- description: Palladium phosphide (Pd3P) and unmodified palladium catalysts supported
    on silica (5 wt% Pd, plus 1 and 10 wt% Pd3P loading variants characterized by
    PXRD only, and a recycled/spent Pd3P/SiO2 sample characterized by STEM only).
    See used_catalyst under is_about_activity and evaluated_entity under was_generated_by
    above for per-sample detail.
  id: coremeta4cat:CAT_arp5-s69r_all
  title: Pd3P/SiO2 and Pd/SiO2 catalyst samples
keyword:
- Chemistry
- Catalysis
- Heterogeneous catalysis
- Palladium catalyst
- Palladium phosphide
- Carbonylation
- Active-site engineering
other_identifier:
- notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
publisher:
  name:
  - NFDI4Cat Central Data Repository
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
title:
- Carbonylation catalysis of aryl halides through active-site engineering
was_generated_by:
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_arp5-s69r_COChemisorption
    title: Pulse chemisorption analyser
  description:
  - Pulse CO chemisorption at room temperature (25 C) for Pd3P/SiO2 and Pd/SiO2 (2
    replicate runs each), used to determine active surface Pd site density / dispersion
    by comparing CO uptake between the phosphide and the unmodified reference catalyst.
  evaluated_entity:
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, ARNE01)
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt
    title: Pd/SiO2 (5 wt% Pd, ARNE02)
  id: coremeta4cat:CHAR_arp5-s69r_COChemisorption
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  realized_plan:
    description: CO pulses at room temperature; peak areas integrated to determine
      total CO uptake.
    id: coremeta4cat:CHAR_arp5-s69r_COChemisorption_method
    title: Pulse CO chemisorption method
  title:
  - CO chemisorption analysis (2 catalysts)
- activity_designator: Characterization
  carried_out_by:
  - description: VERTEX 70 FTIR spectrometer (Bruker) equipped with Praying Mantis
      diffuse reflection optics (Harrick) and a liquid-nitrogen-cooled mercury cadmium
      telluride (MCT) detector.
    id: coremeta4cat:DEV_arp5-s69r_DRIFT
    title: VERTEX 70 FTIR spectrometer (Bruker)
  description:
  - 'Diffuse reflectance infrared Fourier transform spectroscopy of CO adsorbed on
    Pd3P/SiO2 and Pd/SiO2, at 30 C and 100 C (4 spectra total). Atmosphere: 4000 ppm
    CO, balance Ar, 50 mL/min flow; Ar flush between measurements. Sample: 50 mg,
    100-200 micron sieve fraction, in a Harrick in-situ cell with CaF2 windows.'
  evaluated_entity:
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, ARNE01)
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt
    title: Pd/SiO2 (5 wt% Pd, ARNE02)
  id: coremeta4cat:CHAR_arp5-s69r_DRIFT
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  rdf_type:
    id: CHMO:0000645
    title: diffuse reflectance infrared Fourier transform spectroscopy
  realized_plan:
    description: Reflectance mode; scanner velocity 20 kHz; aperture 6 mm; MIR source,
      KBr beamsplitter.
    id: coremeta4cat:CHAR_arp5-s69r_DRIFT_method
    title: CO-adsorption DRIFT method
  title:
  - DRIFT CO-adsorption spectroscopy (2 catalysts, 2 temperatures)
- activity_designator: Characterization
  carried_out_by:
  - description: Stoe STADI-MP powder diffractometer, Cu X-ray source (lambda=1.54178
      A), Ge monochromator.
    id: coremeta4cat:DEV_arp5-s69r_PXRD
    title: Stoe STADI-MP diffractometer
  description:
  - Powder X-ray diffraction for phase identification of Pd/SiO2 (5 wt%, ARNE01/ICSD
    85525=Pd3P phase reference, ARNE02/ICSD 52251=Pd phase reference) and two further
    Pd3P/SiO2 loading variants (1 wt% and 10 wt%), transmission geometry, 2theta 2-90
    degrees, ~80 min total measurement per sample.
  evaluated_entity:
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, ARNE01)
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt
    title: Pd/SiO2 (5 wt% Pd, ARNE02)
  - description: Lower-loading Pd3P/SiO2 variant, PXRD-only sample.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_1wt
    title: Pd3P/SiO2 (1 wt% Pd)
  - description: Higher-loading Pd3P/SiO2 variant, PXRD-only sample.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_10wt
    title: Pd3P/SiO2 (10 wt% Pd)
  id: coremeta4cat:CHAR_arp5-s69r_PXRD
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  rdf_type:
    id: CHMO:0000158
    title: powder X-ray diffraction
  realized_plan:
    description: Transmission geometry, air atmosphere, ambient temperature; software
      INSTPAR.
    id: coremeta4cat:CHAR_arp5-s69r_PXRD_method
    title: Powder XRD measurement method
  title:
  - Powder XRD phase analysis (4 catalysts)
- activity_designator: Characterization
  carried_out_by:
  - description: FEI/Thermo Fisher Osiris ChemiSTEM, combined TEM and STEM with ChemiSTEM
      EDX detector, Schottky field emission gun, 200 kV high tension, magnification
      160-800 kx.
    id: coremeta4cat:DEV_arp5-s69r_STEM
    title: FEI Osiris ChemiSTEM
  description:
  - 'Transmission electron microscopy (HRTEM), scanning TEM (HAADF-STEM), and STEM-EDX
    elemental mapping of Pd3P/SiO2 (ARNE01), Pd/SiO2 (ARNE02), and a recycled/spent
    Pd3P/SiO2 sample recovered after catalytic testing (ARNE03), for particle size
    distribution, chemical composition, and crystal structure. Note: STEM-Meta-2.txt
    documents the method in detail but no image/data files for this technique are
    included in the deposited dataset.'
  evaluated_entity:
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, ARNE01)
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt
    title: Pd/SiO2 (5 wt% Pd, ARNE02)
  - description: Spent Pd3P/SiO2 catalyst recovered after catalytic testing, examined
      by STEM for post-reaction stability.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt_recycled
    title: Pd3P/SiO2 (5 wt% Pd, recycled, ARNE03)
  id: coremeta4cat:CHAR_arp5-s69r_STEM
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  rdf_type:
    id: voc4cat:0000078
    title: transmission electron microscopy
  realized_plan:
    description: HRTEM (Digital Micrograph/Gatan) and HAADF-STEM/STEM-EDXS (TEM Imaging
      and Microscopy/FEI, Esprit/Bruker); Cliff-Lorimer quantification for EDXS.
    id: coremeta4cat:CHAR_arp5-s69r_STEM_method
    title: STEM/TEM imaging and EDX mapping method
  title:
  - STEM/TEM imaging and EDX mapping (3 catalyst samples)
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not specified in the source dataset files.
    id: coremeta4cat:DEV_arp5-s69r_XPS
    title: XPS spectrometer
  description:
  - XPS binding energy scans of the Pd 3d core level for Pd/SiO2 and Pd3P/SiO2, and
    the P 2p core level for Pd3P/SiO2, to compare Pd electronic structure/oxidation
    state between the phosphide and the unmodified reference catalyst.
  evaluated_entity:
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, ARNE01)
  - description: See CatalyticReaction files for full detail.
    id: coremeta4cat:CAT_arp5-s69r_Pd_SiO2_5wt
    title: Pd/SiO2 (5 wt% Pd, ARNE02)
  id: coremeta4cat:CHAR_arp5-s69r_XPS
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/arp5-s69r
  rdf_type:
    id: CHMO:0000404
    title: X-ray photoelectron spectroscopy
  realized_plan:
    description: Pd 3d scans for both catalysts; P 2p scan additionally for Pd3P/SiO2.
    id: coremeta4cat:CHAR_arp5-s69r_XPS_method
    title: XPS core-level measurement method
  title:
  - X-ray photoelectron spectroscopy (2 catalysts, Pd 3d and P 2p)

```
## CatalysisDataset-b74m-m6rp
### Input
```yaml
creator:
- name:
  - Davari, Sadaf
- name:
  - Chacko, Rinu
- name:
  - Bastek, Tim
- name:
  - Lott, Patrick
- name:
  - Dailly, Julian
- name:
  - Angeli, Sofia
- name:
  - Deutschmann, Olaf
dataset_distribution:
- access_URL:
  - id: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
    title: Repository landing page
  licence:
    id: https://creativecommons.org/licenses/by/4.0/
    title: CC BY 4.0
description:
- 'Data from Davari et al., Appl. Catal. A 708 (2025) 120571: H2-TPR of the Ni-BCZY
  cermet; NH3 decomposition light-off curves of six Ru/Ba catalysts on Ni-BCZY, Ni-YSZ
  and YSZ at 500-3000 ppm NH3 in a packed bed (1 bar, GHSV 50,000 h-1); and DETCHEM
  microkinetic packed-bed simulations: comparison with the experiments for literature
  and optimized parameters, axial and surface-coverage profiles, turnover frequencies,
  and variation of inlet NH3, GHSV and pressure. File names follow the figures of
  a version of the article; from Fig6 on they do not match the published figure numbers.'
id: hdl:21.11165/4cat/b74m-m6rp
is_about_activity:
- catalyst_form:
  - supported
  catalyst_mass:
  - description: Catalyst granulate per test, mixed with 700 mg silica
    has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 300
  catalyst_type:
  - heterogeneous_catalysis
  description:
  - 'Thermocatalytic decomposition of ammonia (2 NH3 -> N2 + 3 H2) measured as light-off
    curves in a packed bed: NH3 in Ar at 1 bar, GHSV 50,000 h-1, temperature ramped
    from 473 to 873 K at 2 K/min, after 1.5 h pretreatment at 873 K in 5% H2/Ar and
    1 h Ar purge at 473 K. Six catalysts at 1000 ppm NH3 (Fig. 2); 0.5Ru/1Ba/Ni-BCZY
    and Ni-BCZY also at 500 and 3000 ppm (Fig. 3 and simulation comparisons). Article
    Table 3 gives T10/T50: Ni-BCZY 656/717 K, 1Ru/Ni-BCZY 621/675 K, 0.5Ru/1Ba/Ni-BCZY
    615/675 K, 0.5Ru/0.5Ba/Ni-BCZY 621/676 K, 1Ru/1Ba/YSZ 536/589 K, 1Ru/1Ba/Ni-YSZ
    621/688 K. The deposited curve for 0.5Ru/0.5Ba/Ni-BCZY is unreadable (lost decimal
    separators); its T10/T50 survive only in the article.'
  experiment_pressure:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 1.0
  feed_composition_range:
  - description: NH3 at the inlet (500, 1000, 3000 ppm), balance Ar
    has_quantity_type: http://qudt.org/vocab/quantitykind/MoleFraction
    max_value: 3000.0
    min_value: 500.0
    unit: https://qudt.org/vocab/unit/PPM
  generated_product:
  - id: coremeta4cat:PROD_b74m-m6rp_N2
    rdf_type:
      id: CHEBI:17997
      title: dinitrogen
    title: dinitrogen
  - id: coremeta4cat:PROD_b74m-m6rp_H2
    rdf_type:
      id: CHEBI:18276
      title: dihydrogen
    title: dihydrogen
  id: coremeta4cat:REAC_b74m-m6rp_NH3_decomposition
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
  product_identification_method:
  - description: MKS Instruments MG2030 FTIR spectrometer, continuous analysis of
      the effluent gas
    id: coremeta4cat:REAC_b74m-m6rp_FTIR
    title: online FTIR gas analysis
  rdf_type:
    id: SIO:010511
    title: decomposition reaction
  reaction_name:
  - thermocatalytic ammonia decomposition
  reactor_temperature_range:
  - description: Ramp 473-873 K at 2 K/min; deposited inlet temperature 200-601 C
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    max_value: 873.15
    min_value: 473.15
    unit: https://qudt.org/vocab/unit/K
  title:
  - NH3 decomposition light-off over Ru/Ni-BCZY and reference catalysts (6 catalysts,
    3 inlet concentrations)
  used_catalyst:
  - composed_of:
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 0.5
      id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-1Ba_Ni-BCZY_Ru
      rdf_type:
        id: CHEBI:30682
        title: ruthenium atom
      title: ruthenium
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.0
      id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-1Ba_Ni-BCZY_Ba
      rdf_type:
        id: CHEBI:32594
        title: barium atom
      title: barium
    description: 0.5 wt% Ru and 1 wt% Ba on crushed Ni-BCZY cermet; 500, 1000, 3000
      ppm NH3
    id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-1Ba_Ni-BCZY
    title: 0.5Ru/1Ba/Ni-BCZY
  - composed_of:
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 0.5
      id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-0.5Ba_Ni-BCZY_Ru
      rdf_type:
        id: CHEBI:30682
        title: ruthenium atom
      title: ruthenium
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 0.5
      id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-0.5Ba_Ni-BCZY_Ba
      rdf_type:
        id: CHEBI:32594
        title: barium atom
      title: barium
    description: 1000 ppm NH3; the deposited file lost its decimal separators
    id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-0.5Ba_Ni-BCZY
    title: 0.5Ru/0.5Ba/Ni-BCZY
  - composed_of:
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.0
      id: coremeta4cat:CAT_b74m-m6rp_1Ru_Ni-BCZY_Ru
      rdf_type:
        id: CHEBI:30682
        title: ruthenium atom
      title: ruthenium
    description: 1000 ppm NH3
    id: coremeta4cat:CAT_b74m-m6rp_1Ru_Ni-BCZY
    title: 1Ru/Ni-BCZY
  - description: Bare cermet (NiO:BCZY811 = 60:40 by weight before reduction); 500,
      1000, 3000 ppm NH3
    id: coremeta4cat:CAT_b74m-m6rp_Ni-BCZY
    title: Ni-BCZY cermet
  - composed_of:
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.0
      id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_Ni-YSZ_Ru
      rdf_type:
        id: CHEBI:30682
        title: ruthenium atom
      title: ruthenium
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.0
      id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_Ni-YSZ_Ba
      rdf_type:
        id: CHEBI:32594
        title: barium atom
      title: barium
    description: 1000 ppm NH3
    id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_Ni-YSZ
    title: 1Ru/1Ba/Ni-YSZ
  - composed_of:
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.0
      id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_YSZ_Ru
      rdf_type:
        id: CHEBI:30682
        title: ruthenium atom
      title: ruthenium
    - has_quantitative_attribute:
      - description: Nominal loading
        has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.0
      id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_YSZ_Ba
      rdf_type:
        id: CHEBI:32594
        title: barium atom
      title: barium
    description: 1000 ppm NH3; Ni-free YSZ support
    id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_YSZ
    title: 1Ru/1Ba/YSZ
  used_reactant:
  - id: coremeta4cat:REAC_b74m-m6rp_NH3
    rdf_type:
      id: CHEBI:16134
      title: ammonia
    title: ammonia
  - id: coremeta4cat:REAC_b74m-m6rp_Ar
    rdf_type:
      id: CHEBI:49475
      title: argon atom
    title: argon (balance)
  used_reactor:
  - catalyst_bed_diameter:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/CentiM
      value: 0.8
    catalyst_bed_height:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Length
      unit: https://qudt.org/vocab/unit/CentiM
      value: 1.2
    catalyst_dilution_material:
    - silica particles, 700 mg, 120-250 um
    description: 0.8 cm inner diameter, 100 cm long, in a furnace; bed fixed by quartz
      wool, about 1.2 cm long; catalyst and silica sieve fraction 120-250 um; Bronkhorst
      mass flow controllers; two type N thermocouples about 2 mm up- and downstream
      of the bed.
    id: coremeta4cat:REAC_b74m-m6rp_reactor
    reactor_designator: coremeta4cat:FixedBedReactor
    title: quartz glass tubular packed-bed reactor
is_about_entity:
- description: 'Six catalysts: Ni-BCZY, 1Ru/Ni-BCZY, 0.5Ru/1Ba/Ni-BCZY, 0.5Ru/0.5Ba/Ni-BCZY,
    1Ru/1Ba/YSZ, 1Ru/1Ba/Ni-YSZ. See is_about_activity for per-catalyst detail.'
  id: coremeta4cat:CAT_b74m-m6rp_all
  title: Ru/Ba catalysts on Ni-BCZY, Ni-YSZ and YSZ
is_referenced_by:
- id: https://doi.org/10.1016/j.apcata.2025.120571
  title: Davari et al., Appl. Catal. A 708 (2025) 120571
keyword:
- Ammonia decomposition
- Ru catalyst
- Ni-BCZY
- Hydrogen production/generation
- Protonic Ceramic Cell
- Thermo-catalytic experiments
- Microkinetic modeling
other_identifier:
- notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
publisher:
  name:
  - NFDI4Cat Central Data Repository
rdf_type:
- id: voc4cat:0007001
  title: heterogeneous catalysis
title:
- 'Dataset for Publication: Experimental and Microkinetic Investigation of Thermo-Catalytic
  Ammonia Decomposition over a Ba-promoted Ru/Ni-BCZY Catalyst for Use in Ammonia-fed
  Protonic Ceramic Cells'
was_generated_by:
- activity_designator: Synthesis
  catalyst_measured_properties:
  - Ru distribution and nanoparticle size of 0.5Ru/1Ba/Ni-BCZY by SEM/EDX (article
    Figs. 4-5; images not deposited)
  had_input_entity:
  - id: coremeta4cat:PREC_b74m-m6rp_RuNO_NO3
    title: ruthenium(III) nitrosyl nitrate, aqueous solution (Alfa Aesar)
  - id: coremeta4cat:PREC_b74m-m6rp_BaNO3
    title: barium nitrate, Ba(NO3)2 (Alfa Aesar), dissolved in deionised water
  - description: Output of SYN_b74m-m6rp_cermet_supports
    id: coremeta4cat:SUP_b74m-m6rp_supports
    title: crushed Ni-BCZY, Ni-YSZ and YSZ supports
  had_output_entity:
  - id: coremeta4cat:CAT_b74m-m6rp_1Ru_Ni-BCZY
    title: 1Ru/Ni-BCZY
  - id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-1Ba_Ni-BCZY
    title: 0.5Ru/1Ba/Ni-BCZY
  - id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-0.5Ba_Ni-BCZY
    title: 0.5Ru/0.5Ba/Ni-BCZY
  - id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_YSZ
    title: 1Ru/1Ba/YSZ
  - id: coremeta4cat:CAT_b74m-m6rp_1Ru-1Ba_Ni-YSZ
    title: 1Ru/1Ba/Ni-YSZ
  id: coremeta4cat:SYN_b74m-m6rp_Ru_Ba_IWI
  nominal_composition:
  - '1Ru/Ni-BCZY: 1.0 wt% Ru'
  - '0.5Ru/1Ba/Ni-BCZY: 0.5 wt% Ru, 1.0 wt% Ba'
  - '0.5Ru/0.5Ba/Ni-BCZY: 0.5 wt% Ru, 0.5 wt% Ba'
  - '1Ru/1Ba/YSZ: 1.0 wt% Ru, 1.0 wt% Ba'
  - '1Ru/1Ba/Ni-YSZ: 1.0 wt% Ru, 1.0 wt% Ba'
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
  realized_plan:
    description: Because of the low pore volume of the cermets the precursor solution
      was added in 100 uL steps, each followed by drying at 348 K for 15 min, until
      the target loading was reached. Nitrates decomposed by calcination for 5 h at
      873 K in static air; granulated to 120-250 um.
    has_calcination_atmosphere:
    - value: static air
    has_calcination_dwelling_time:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/HR
      value: 5
    has_calcination_temperature_range:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      max_value: 873.15
      min_value: 873.15
      unit: https://qudt.org/vocab/unit/K
    has_drying_duration:
      has_quantity_type: http://qudt.org/vocab/quantitykind/Time
      unit: https://qudt.org/vocab/unit/MIN
      value: 15
    has_drying_temperature:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      unit: https://qudt.org/vocab/unit/K
      value: 348.15
    id: coremeta4cat:SYN_b74m-m6rp_IWI_method
    impregnation_type:
    - incipient_wetness
    plan_designator: voc4cat:0007028
    title: stepwise incipient wetness impregnation, calcination, granulation
  title:
  - Ru and Ba on Ni-BCZY, Ni-YSZ and YSZ by stepwise incipient wetness impregnation
- activity_designator: Synthesis
  catalyst_measured_properties:
  - 'BET surface area: NiO-BCZY (oxidized) 1.1 m2/g, YSZ powder 14.1 m2/g (article
    Table 2)'
  - Ni dispersion of Ni-BCZY 3.17% (H2-TPD)
  had_input_entity:
  - id: coremeta4cat:PREC_b74m-m6rp_BCZY811
    title: BaCe0.8Zr0.1Y0.1O3-d powder (BCZY811, CerPoTech)
  - id: coremeta4cat:PREC_b74m-m6rp_8YSZ
    title: 8 mol% yttria-stabilised zirconia powder (8-YSZ, Tosoh)
  - id: coremeta4cat:PREC_b74m-m6rp_NiO
    title: NiO powder (J.T. Baker)
  - id: coremeta4cat:PREC_b74m-m6rp_graphite
    title: graphite pore former (TimCal)
  - id: coremeta4cat:PREC_b74m-m6rp_tape_organics
    title: ethanol and methyl ethyl ketone (solvents, dispersant), polyvinyl butyral
      (binder), PEG and TEG-EH (plasticizers, Eastman)
  had_output_entity:
  - id: coremeta4cat:SUP_b74m-m6rp_Ni-BCZY
    title: crushed Ni-BCZY cermet powder
  - id: coremeta4cat:SUP_b74m-m6rp_Ni-YSZ
    title: crushed Ni-YSZ cermet powder
  - id: coremeta4cat:SUP_b74m-m6rp_YSZ
    title: crushed YSZ powder
  id: coremeta4cat:SYN_b74m-m6rp_cermet_supports
  nominal_composition:
  - 'Ni-BCZY cermet: NiO and BaCe0.8Zr0.1Y0.1O3-d (BCZY811), 60:40 by weight before
    reduction'
  - 'Ni-YSZ cermet: NiO and 8-YSZ, 60:40 by weight before reduction'
  - YSZ (8-YSZ, Ni-free)
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
  realized_plan:
    description: Ceramic powder (and NiO for the cermets) slurried with graphite,
      ethanol and MEK in a TURBULA 3D shaker for 24 h; PVB, PEG and TEG-EH added,
      mixed 3 h, rested 24 h, de-aired under vacuum; cast with a ZAA 2300 film applicator
      onto silicone-coated PET; dried 12 h at room temperature and 10 min at 773 K;
      sintered 9 h at 1673 K (heating 1 K/min, cooling 3 K/min); crushed to a fine
      powder.
    id: coremeta4cat:SYN_b74m-m6rp_tape_casting_method
    title: tape casting, sintering and crushing
  title:
  - Ni-BCZY, Ni-YSZ and YSZ supports from sintered tapes
- activity_designator: Characterization
  carried_out_by:
  - description: Instrument model not stated in the article.
    id: coremeta4cat:DEV_b74m-m6rp_TCD
    title: TPR set-up with quartz reactor and thermal conductivity detector
  description:
  - Temperature-programmed reduction of about 0.1 g Ni-BCZY powder in a quartz reactor,
    from room temperature to 1223 K at 10 K/min in 10% H2/Ar (50 mL/min); H2 consumption
    followed by a thermal conductivity detector. Deposited signal 38-951 C.
  evaluated_entity:
  - id: coremeta4cat:CAT_b74m-m6rp_Ni-BCZY
    title: Ni-BCZY cermet powder
  id: coremeta4cat:CHAR_b74m-m6rp_TCD
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
  rdf_type:
    id: CHMO:0002908
    title: temperature-programmed reduction
  realized_plan:
    description: About 0.1 g sample, 10% H2 in Ar at 50 mL/min, TCD detection.
    has_heating_rate:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/TemperaturePerTime
      unit: https://qudt.org/vocab/unit/K-PER-MIN
      value: 10
    has_temperature_range:
    - description: room temperature to 1223 K (the article gives 1223 K as the end
        point)
      has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
      max_value: 1223.15
      min_value: 298.15
      unit: https://qudt.org/vocab/unit/K
    id: coremeta4cat:CHAR_b74m-m6rp_TCD_method
    plan_designator: CHMO:0002908
    reducing_gas_composition:
    - 10% H2 in Ar, 50 mL/min
    title: H2-TPR, 10 K/min to 1223 K
  title:
  - H2-TPR of the Ni-BCZY cermet (article Fig. 1)
- activity_designator: Simulation
  calculated_property:
  - description: Turnover frequency of NH3 decomposition, deposit Fig11_Ni+Ru.tab
      (article Fig. 10); Ni-only and Ru-only in Fig11_Ni.tab and Fig11_Ru.tab
    value: TOF 3.2e-4 to 0.37 s-1 (Ni+Ru sites, 498-848 K)
  - description: Deposit Fig10_615K.csv, Fig10_818K.csv (article Fig. 9)
    value: surface coverages of 12 surface species along the bed at 615 and 818 K
  - description: Deposit Fig12b, Fig12d, Fig12f; TOF at 615 K vs. the same parameters
      in Fig12_a, Fig12c, Fig12e (article Fig. 11 shows 100-10,000 ppm and 0.5-5 bar)
    value: NH3 conversion vs. temperature for inlet NH3 100 ppm-100%, GHSV 100-100,000
      h-1, pressure 0.5-10 bar
  description:
  - 'Simulations with the optimized microkinetic mechanism: axial NH3 and conversion
    profiles over the 12 mm bed at 618-818 K (article Fig. 8); spatially resolved
    surface coverages at 615 and 818 K (Fig. 9); turnover frequency of the Ru-only,
    Ni-only and combined models at 498-848 K, computed without reactor effects (Fig.
    10); and variation of inlet NH3, GHSV (100-100,000 h-1) and pressure at 615 K
    or as a function of temperature (Fig. 11). Base case: 1000 ppm NH3 in Ar, 1 bar,
    GHSV 50,000 h-1, 615 K (= T10 of 0.5Ru/1Ba/Ni-BCZY).'
  evaluated_entity:
  - id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-1Ba_Ni-BCZY
    title: 0.5Ru/1Ba/Ni-BCZY (modelled as Ru and Ni surface sites)
  id: coremeta4cat:SIM_b74m-m6rp_MKM_parametric
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
  realized_plan:
    description: 'Mechanism with the optimized Ru and Ni parameters (article Table
      4). Varied inputs: inlet NH3 mole fraction, GHSV, pressure, temperature.'
    id: coremeta4cat:SIM_b74m-m6rp_MKM_parametric_method
    plan_designator: coremeta4cat:Microkinetics
    title: optimized microkinetic packed-bed model, parameter variation
  software_package:
  - DETCHEM-PBR (DETCHEM package), reactor simulations
  - DETCHEM-SURFPROBE, surface coverages and TOF without reactor effects
  title:
  - 'Microkinetic NH3 decomposition: reactor profiles, TOF and parameter variation'
- activity_designator: Simulation
  calculated_property:
  - description: Deposit Fig6a-c (0.5Ru/1Ba/Ni-BCZY, original), Fig7a-c (Ni-BCZY,
      original and optimized), Fig8a-c (0.5Ru/1Ba/Ni-BCZY, optimized)
    value: NH3 conversion vs. surface temperature, 498-848 K, 9 simulated curves
  description:
  - 'One-dimensional packed-bed reactor simulation (negligible axial diffusion) with
    a mean-field surface mechanism on Ru and Ni sites, compared with the measured
    light-off curves at 500, 1000 and 3000 ppm NH3 in Ar, 1 bar, GHSV 50,000 h-1,
    ramp 2 K/min. Ni steps start from Zhu et al. (Int. J. Green Energy 19 (2022) 1568),
    Ru steps from Zhang et al. (ACS Sustain. Chem. Eng. 7 (2019) 18038, Ba-promoted
    Ru on YSZ, coverage-dependent activation energies). Both parameter sets were re-optimized
    against the 1000 ppm data and validated with the 500 and 3000 ppm data; the optimized
    set is article Table 4. Surface species: Ru, H-Ru, N-Ru, NH-Ru, NH2-Ru, NH3-Ru,
    Ni, H-Ni, N-Ni, NH-Ni, NH2-Ni, NH3-Ni.'
  evaluated_entity:
  - id: coremeta4cat:CAT_b74m-m6rp_0.5Ru-1Ba_Ni-BCZY
    title: 0.5Ru/1Ba/Ni-BCZY (modelled as Ru and Ni surface sites)
  - id: coremeta4cat:CAT_b74m-m6rp_Ni-BCZY
    title: Ni-BCZY (modelled as Ni surface sites)
  id: coremeta4cat:SIM_b74m-m6rp_MKM_validation
  other_identifier:
  - notation: https://hdl.handle.net/21.11165/4cat/b74m-m6rp
  realized_plan:
    description: Modified Arrhenius rate expressions with coverage-dependent activation
      energies; catalytic area scaled by F_cat/geo from the metal dispersion. Parameter
      optimization in 5% steps with two dependent parameters fixed by thermodynamic
      consistency.
    id: coremeta4cat:SIM_b74m-m6rp_MKM_method
    plan_designator: coremeta4cat:Microkinetics
    title: microkinetic packed-bed model, literature and optimized parameters
  software_package:
  - DETCHEM-PBR (DETCHEM package)
  - CaRMeN (Catalytic Reaction Mechanisms Network)
  - DETCHEM-ADJUST (thermodynamic consistency during optimization)
  title:
  - Microkinetic simulation of NH3 decomposition light-off on Ni-BCZY and 0.5Ru/1Ba/Ni-BCZY

```
## CatalyticReaction-001
### Input
```yaml
catalyst_form:
- supported
catalyst_mass:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
  unit: https://qudt.org/vocab/unit/GM
  value: 0.5
catalyst_type:
- heterogeneous_catalysis
experiment_pressure:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
  unit: https://qudt.org/vocab/unit/BAR
  value: 50.0
feed_composition_range:
- description: H2/CO2 = 3:1, CO2 concentration 20 vol%
had_input_entity:
- description: H2/CO2 molar ratio 3:1, total flow 100 mL/min
  id: coremeta4cat:FEED_001_CO2_H2
  title: CO2/H2 feed gas mixture
has_atmosphere:
- value: H2/CO2 = 3:1 (molar), GHSV = 10000 mL/(g*h)
id: coremeta4cat:REAC_001_CO2_hydrogenation
product_identification_method:
- description: 'GC (Agilent 7890B) with TCD and FID detectors; columns: Molecular
    Sieve 5A and Poraplot Q; products: MeOH, CO, CH4, H2O quantified'
  id: coremeta4cat:REAC_001_GC_method
  title: online gas chromatography
rdf_type:
  id: voc4cat:0000259
  title: CO2 hydrogenation
reactor_temperature_range:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  max_value: 300
  min_value: 200
  unit: https://qudt.org/vocab/unit/DEG_C
used_reactant:
- id: https://pubchem.ncbi.nlm.nih.gov/compound/280
  title: CO2 (99.998% purity, 20 vol% in H2)
- id: https://pubchem.ncbi.nlm.nih.gov/compound/783
  title: H2 (99.999% purity)
used_reactor:
- description: 10 mm inner diameter, 30 cm length, 0.5 g catalyst diluted with SiC
  id: coremeta4cat:REACT_001_FixedBed
  title: stainless steel fixed-bed plug-flow reactor

```
## CatalyticReaction-002
### Input
```yaml
catalyst_form:
- supported
catalyst_mass:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
  unit: https://qudt.org/vocab/unit/GM
  value: 0.2
catalyst_type:
- heterogeneous_catalysis
experiment_pressure:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
  unit: https://qudt.org/vocab/unit/ATM
  value: 1.0
feed_composition_range:
- description: 'stoichiometric DRM: CH4/CO2 = 1:1 (molar)'
- description: 'CO2-rich condition: CH4/CO2 = 1:1.5 to suppress carbon deposition'
had_input_entity:
- description: 'CH4 flow: 45 mL/min (STP); calibrated Brooks SLA5850 MFC'
  id: coremeta4cat:FEED_004_CH4_DRM
  title: methane feed (99.995%, Linde)
- description: 'CO2 flow: 45 mL/min (STP); calibrated Brooks SLA5850 MFC'
  id: coremeta4cat:FEED_005_CO2_DRM
  title: CO2 feed (99.998%, Linde)
- description: 'N2 flow: 10 mL/min (STP); used as internal standard for GC molar balance'
  id: coremeta4cat:FEED_006_N2_standard
  title: N2 internal standard (99.999%, Linde)
has_atmosphere:
- value: CH4/CO2/N2 = 45:45:10 vol%, total flow 100 mL/min (STP), GHSV = 30000 mL/(g*h)
has_experiment_duration:
  has_quantity_type: http://qudt.org/vocab/quantitykind/Time
  unit: https://qudt.org/vocab/unit/HR
  value: 20.0
id: coremeta4cat:REAC_002_DRM_NiCeO2
product_identification_method:
- description: 'Shimadzu GC-2014 with TCD detector (Ar carrier gas); column 1: HayeSep
    D (2 m x 1/8 in) for CO2, CH4 separation; column 2: Molecular Sieve 5A (2 m x
    1/8 in) for CO, H2, N2, CH4 separation; 10-port Valco valve for column switching;
    oven temperature: 50 deg C isothermal; TCD temperature: 250 deg C; injection:
    automated gas sampling valve, 1 mL loop; analysis cycle: 10 min; calibration:
    certified gas standard (Air Liquide CRYSTAL mixture: H2 5%, CO 5%, CH4 5%, CO2
    10%, N2 balance); CH4 conversion, CO2 conversion, H2/CO ratio, and carbon balance
    calculated from N2-normalised molar flows'
  id: coremeta4cat:REAC_002_GC_method
  title: online dual-column gas chromatography (TCD)
rdf_type:
  id: CHMO:0001446
  title: catalytic reforming
reactor_temperature_range:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  max_value: 800
  min_value: 600
  unit: https://qudt.org/vocab/unit/DEG_C
used_catalyst:
- description: Ni0 after in situ reduction of NiO/CeO2
  id: coremeta4cat:CAT_002_NiCeO2
  title: Ni/CeO2
used_reactant:
- id: https://pubchem.ncbi.nlm.nih.gov/compound/297
  title: CH4 (99.995% purity, Linde)
- id: https://pubchem.ncbi.nlm.nih.gov/compound/280
  title: CO2 (99.998% purity, Linde)
- id: https://pubchem.ncbi.nlm.nih.gov/compound/947
  title: N2 balance (99.999% purity, internal standard for GC quantification)
used_reactor:
- description: 'quartz tube reactor, 8 mm inner diameter, 30 cm length; catalyst bed:
    200 mg NiO/CeO2 (250-500 um sieve fraction) diluted 1:2 (mass) with inert SiC
    chips (500 um); thermocouple inserted into catalyst bed centre; backpressure regulator
    at outlet (1 bar); reactor surrounded by ceramic-fibre furnace with PID temperature
    controller; mass flow controllers (Brooks SLA5850) for CH4, CO2, N2'
  id: coremeta4cat:REACT_003_FixedBed_DRM
  title: quartz fixed-bed plug-flow reactor (DRM)

```
## Characterization-001
### Input
```yaml
carried_out_by:
- id: coremeta4cat:DEV_001_Micromeritics_ASAP2020
  title: Micromeritics ASAP 2020 surface area and porosimetry analyzer
evaluated_entity:
- description: 63 wt% CuO, 24 wt% ZnO, 13 wt% Al2O3 (calcined precursor)
  id: coremeta4cat:CAT_001_CuZnO_Al2O3
  title: Cu/ZnO/Al2O3 methanol synthesis catalyst
id: coremeta4cat:CHAR_001_BET_CuZnO_Al2O3
realized_plan:
  description: N2 physisorption at 77 K, degassing at 300 deg C for 3 h under vacuum
    prior to measurement
  id: coremeta4cat:CHAR_001_BET_method
  title: BET surface area measurement

```
## Characterization-002
### Input
```yaml
carried_out_by:
- id: coremeta4cat:DEV_002_Bruker_D8_Advance
  title: Bruker D8 Advance diffractometer with Cu K-alpha radiation (1.5406 Ang)
evaluated_entity:
- description: 63 wt% CuO, 24 wt% ZnO, 13 wt% Al2O3 (calcined precursor)
  id: coremeta4cat:CAT_001_CuZnO_Al2O3
  title: Cu/ZnO/Al2O3 methanol synthesis catalyst
id: coremeta4cat:CHAR_002_XRD_CuZnO_Al2O3
realized_plan:
  description: Cu K-alpha, 2theta range 5 to 80 deg, step size 0.02 deg, scan rate
    1 deg/min, Rietveld refinement for phase quantification
  id: coremeta4cat:CHAR_002_XRD_method
  title: powder X-ray diffraction

```
## Characterization-003
### Input
```yaml
carried_out_by:
- id: coremeta4cat:DEV_003_Thermo_KAlpha_XPS
  title: Thermo Scientific K-Alpha+ XPS spectrometer
- id: coremeta4cat:DEV_004_AlKalpha_source
  title: Al K-alpha monochromatic X-ray source (1486.6 eV, 72 W)
detector_type:
- 128-channel 2D delay-line detector (DLD)
evaluated_entity:
- description: 15 wt% NiO on CeO2 support, calcined at 500 deg C
  id: coremeta4cat:CAT_002_NiO_CeO2
  title: NiO/CeO2 dry reforming catalyst (calcined)
has_sample_pretreatment:
- value: outgassed in XPS load-lock chamber at < 1e-7 mbar for 12 h before transfer
    to analysis chamber (< 5e-9 mbar)
id: coremeta4cat:CHAR_003_XPS_NiO_CeO2
realized_plan:
  description: 'monochromatic Al K-alpha (1486.6 eV); base pressure 5e-9 mbar; survey
    scan: 0-1350 eV, 1.0 eV step, 50 ms dwell, 3 scans, pass energy 200 eV; high-resolution
    regions: Ni 2p3/2 (845-895 eV), Ce 3d (875-935 eV), O 1s (525-540 eV), C 1s (280-295
    eV); step size 0.1 eV, 20 scans each, pass energy 50 eV; spot size 400 um; lens
    mode: large area XL; charge compensation: dual-beam flood gun (1 eV electrons
    + 10 eV Ar+); binding energy scale calibrated to C 1s adventitious carbon at 284.8
    eV; Shirley background subtraction; peak fitting: Voigt profiles (CasaXPS v2.3.25);
    atomic concentrations from Scofield sensitivity factors corrected for transmission
    function'
  id: coremeta4cat:CHAR_003_XPS_method
  title: X-ray photoelectron spectroscopy (XPS)
sample_description:
- NiO/CeO2 co-precipitated catalyst (SYNTH_002), calcined at 500 deg C, as-prepared
  (non-reduced), ca. 10 mg pressed into indium foil
sample_preparation:
- lightly pressed into indium foil to obtain flat surface; mounted on sample stub
  with copper tape; no Ar+ sputtering performed
sample_state:
- powder

```
## Characterization-004
### Input
```yaml
carried_out_by:
- id: coremeta4cat:DEV_005_Micromeritics_AutoChem
  title: Micromeritics AutoChem II 2920 chemisorption analyzer
detector_type:
- thermal conductivity detector (TCD), Ar carrier gas reference channel
evaluated_entity:
- description: 15 wt% NiO on CeO2, calcined at 500 deg C / 4 h
  id: coremeta4cat:CAT_002_NiO_CeO2
  title: NiO/CeO2 dry reforming catalyst (calcined)
has_sample_pretreatment:
- value: 'oxidative pretreatment: 10 vol% O2/Ar (50 mL/min) at 300 deg C for 30 min;
    cool to 50 deg C under Ar purge'
id: coremeta4cat:CHAR_004_TPR_NiO_CeO2
realized_plan:
  description: 'reducing gas: 5 vol% H2/Ar, total flow 50 mL/min (calibrated Brooks
    MFC); temperature programme: 50 deg C to 900 deg C at 10 deg C/min; isothermal
    hold: 30 min at 900 deg C; H2O trap: molecular sieve 3A between reactor outlet
    and TCD to prevent TCD signal interference; baseline: Ar flow for 30 min at 50
    deg C before switching to H2/Ar; H2 consumption quantified by integration of TCD
    signal, calibrated against CuO reference standard (99.9%, 10 mg, single reduction
    peak at 310 deg C); NiO reduction: expected peaks at 280-350 deg C (NiO weakly
    interacting with CeO2) and 400-600 deg C (NiO strongly interacting); CeO2 surface
    reduction: 600-900 deg C'
  id: coremeta4cat:CHAR_004_TPR_method
  title: H2 temperature-programmed reduction (H2-TPR)
sample_description:
- NiO/CeO2 calcined at 500 deg C; 50 mg packed in quartz U-tube reactor (4 mm ID);
  quartz wool plugs above and below bed

```
## Simulation-001
### Input
```yaml
calculated_property:
- adsorbate:
  - CO
  adsorption_energy:
  - -0.67
  adsorption_site:
  - fcc hollow
  description: CO adsorption energy on hollow fcc site of Cu(111) relative to gas-phase
    CO
  energy_reference:
  - CO(g)
  material_composition:
  - Cu
  miller_indices:
  - (111)
  property_designator: coremeta4cat:AdsorptionEnergetics
  title: CO adsorption energy
  value: -0.67 eV
- description: C-O bond length of adsorbed CO
  value: 1.157 Ang
- description: Cu-C bond length at hollow adsorption site
  value: 2.312 Ang
evaluated_entity:
- description: 4-layer Cu(111) p(3x3) slab, bottom 2 layers fixed, 15 Ang vacuum
  id: coremeta4cat:SLAB_001_Cu111
  title: Cu(111) surface slab model
id: coremeta4cat:SIM_001_DFT_Cu111_CO_ads
realized_plan:
  description: PBE functional, PAW pseudopotentials, 400 eV cutoff, 4x4x1 Monkhorst-Pack
    k-mesh, D3 dispersion correction, spin-unpolarized
  id: coremeta4cat:SIM_001_DFT_method
  title: periodic plane-wave DFT
software_package:
- VASP 6.3.0
- VESTA 3.5.8 (structure visualization)

```
## Simulation-002
### Input
```yaml
calculated_property:
- description: CeO2(111) cleavage surface energy (clean slab without Ni cluster, computed
    from relaxed DFT-D3 reference at 0 K, used as force field validation benchmark)
  value: 1.52 J/m2
- description: time-averaged Ni-CeO2 adhesion energy per Ni atom (13-atom cluster)
    relative to bulk Ni cohesive energy and clean CeO2(111) slab; computed from 800
    ps production trajectory
  value: -1.83 eV/atom
- description: first-shell Ni-O coordination distance at Ni cluster / CeO2 interface
    (peak of Ni-O radial distribution function, production trajectory average)
  value: 3.8 Ang
- description: fraction of Ni atoms in direct contact with CeO2 surface (Ni-O bond
    order > 0.3) averaged over production trajectory; measures cluster wetting / spreading
  value: '0.42'
evaluated_entity:
- description: 6-layer CeO2(111) p(4x4) slab (256 CeO2 formula units, 768 atoms total);
    bottom 3 layers fixed during MD; 13-atom cuboctahedral Ni cluster adsorbed on
    three-fold hollow O site; 20 Ang vacuum layer; 3D periodic boundary conditions
  id: coremeta4cat:SLAB_002_CeO2_111_Ni13
  title: CeO2(111) surface slab with supported 13-atom Ni cluster
id: coremeta4cat:SIM_002_MD_Ni_CeO2_111
realized_plan:
  description: 'force field: ReaxFF C/H/Ni/O parametrisation (van Duin et al. 2012,
    DOI: 10.1021/jp210484t); ensemble: NVT with Nose-Hoover thermostat (tau = 100
    fs) at 800 deg C (1073 K); integration timestep: 0.5 fs; total simulation time:
    1 ns (2,000,000 steps); equilibration phase: 200 ps (400,000 steps) discarded;
    production phase: 800 ps (1,600,000 steps) used for analysis; sampling interval:
    every 1000 steps (0.5 ps); bond order cutoff: C-O 0.3, Ni-O 0.3 (fix reax/c/bonds);
    radial distribution functions computed with OVITO using 0.05 Ang bin width; common-neighbour
    analysis (CNA) to track Ni cluster crystallographic ordering'
  id: coremeta4cat:SIM_002_MD_method
  title: ReaxFF molecular dynamics (NVT, 800 deg C)
software_package:
- LAMMPS (29 Sep 2021 stable release, OpenMP build)
- OVITO 3.7.11 (structure analysis, RDF, CNA, cluster tracking)

```
## Synthesis-001
### Input
```yaml
catalyst_measured_properties:
- 'BET surface area: 185 m2/g, Pt particle size: 2.3 nm (TEM), Pt loading: 4.8 wt%
  (ICP-AES)'
catalyst_support:
- gamma-Al2O3, Sasol Puralox, 200 m2/g
had_input_entity:
- id: coremeta4cat:PREC_001_H2PtCl6
  precursor_quantity:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/GM
    value: 0.0485
  title: chloroplatinic acid hexahydrate
has_sample_pretreatment:
- value: reduction in H2 at 400 deg C for 2 hours prior to catalytic testing
id: coremeta4cat:SYNTH_001_Pt_Al2O3
nominal_composition:
- 5 wt% Pt/Al2O3
realized_plan:
  description: incipient_wetness, 25 deg C, 12 h
  id: coremeta4cat:SYNTH_001_impregnation_method
  title: incipient wetness impregnation
solvent:
- id: https://pubchem.ncbi.nlm.nih.gov/compound/962
  title: deionized water
storage_conditions:
- stored in desiccator under argon atmosphere at room temperature

```
## Synthesis-002
### Input
```yaml
catalyst_measured_properties:
- 'BET surface area: 42 m2/g'
- 'NiO crystallite size: 8.4 nm (Scherrer, XRD)'
- 'Ni loading: 14.7 wt% (ICP-AES)'
- 'reducibility onset: 280 deg C, completion at 600 deg C (H2-TPR)'
had_input_entity:
- id: coremeta4cat:PREC_004_Ni_NO3_6H2O
  precursor_quantity:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/GM
    value: 8.72
  title: nickel(II) nitrate hexahydrate (Sigma-Aldrich, purity 99%)
- id: coremeta4cat:PREC_005_Ce_NO3_6H2O
  precursor_quantity:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/GM
    value: 13.03
  title: cerium(III) nitrate hexahydrate (Sigma-Aldrich, purity 99.5%)
- id: coremeta4cat:PREC_006_Na2CO3
  precursor_quantity:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/GM
    value: 5.3
  title: sodium carbonate precipitating agent (anhydrous, Sigma-Aldrich, purity 99.5%)
had_output_entity:
- description: 15 wt% NiO on CeO2 support, co-precipitated at pH 8.5, calcined 500
    deg C / 4 h, sieved to 250-500 um
  id: coremeta4cat:CAT_002_NiO_CeO2
  title: NiO/CeO2 dry reforming catalyst (calcined precursor)
has_sample_pretreatment:
- value: 'in situ reduction: 5 vol% H2/N2 at 700 deg C for 1 h (10 deg C/min ramp)
    before DRM tests'
id: coremeta4cat:SYNTH_002_NiO_CeO2
nominal_composition:
- 15 wt% NiO/CeO2
realized_plan:
  description: 'aqueous solutions of Ni(NO3)2 (0.5 M) and Ce(NO3)3 (0.5 M) mixed in
    stoichiometric ratio; precipitant: 1 M Na2CO3 solution added dropwise at 2 mL/min;
    target pH 8.5 maintained by feedback addition; mixing: 600 rpm mechanical stirring
    at 60 deg C for 2 h; aging: 12 h at 60 deg C without stirring; filtration: vacuum
    filtration through Whatman grade 4 filter paper; washing: 5 successive deionized
    water washes until conductivity < 5 uS/cm (Na+ removal); drying: 120 deg C for
    12 h in static air oven; calcination: 5 deg C/min ramp to 500 deg C, isothermal
    hold for 4 h in static air, natural cooling'
  id: coremeta4cat:SYNTH_002_coprecipitation_method
  title: co-precipitation
solvent:
- id: https://pubchem.ncbi.nlm.nih.gov/compound/962
  title: deionized water (18.2 MOhm cm, MilliQ)
storage_conditions:
- sealed glass vial in desiccator, ambient temperature, protected from moisture

```
