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
  catalyst_quantity:
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
    id: VOC4CAT:0007010
    title: CO methanation
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp2_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 20.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp3_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 20.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp4_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 10.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp12_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 10.0
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
    id: VOC4CAT:0007011
    title: CO2 methanation
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp7_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 10.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp8_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 20.0
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
  - description: High Ni-loading Al2O3-supported catalyst; this run also used an elevated
      feed pressure of 800 kPa, an outlier relative to the other runs in this series
      (~100-101.3 kPa).
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp9_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 40.8
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp13_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 10.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp14_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 10.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp15_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 20.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp16_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 15.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp17_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 10.0
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
    id: VOC4CAT:0007010
    title: CO methanation
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp11_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp18_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp19_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
  - has_physical_state: SOLID
    has_quantitative_attribute:
    - description: 'Ni loading (Exp20_metadata.json: catalyst.metal_loading)'
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
  id: VOC4CAT:0007001
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
    id: VOC4CAT:0000130
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
    id: VOC4CAT:0000260
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
  - description: Pd on Al2O3 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.8
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 0.8
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3 (nominal 1 wt% P)
  - description: Pd on Al2O3 support, nominal 2 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 116.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_2P
    title: Pd/2P/Al2O3 (nominal 2 wt% P)
  - description: Pd on Al2O3 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.8
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.5
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 105.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3 (nominal 3 wt% P)
  - description: Pd on Al2O3 support, nominal 4 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 3.7
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 112.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_4P
    title: Pd/4P/Al2O3 (nominal 4 wt% P)
  - description: Pd on Al2O3 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.9
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 4.6
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
    id: VOC4CAT:0000260
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
  - description: Pd on SiO2 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.1
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2 (nominal 1 wt% P)
  - description: Pd on SiO2 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.8
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.6
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 98.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2 (nominal 3 wt% P)
  - description: Pd on SiO2 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 4.8
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
    id: VOC4CAT:0000260
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
  - description: Pd on Al2O3 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.8
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 0.8
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_1P
    title: Pd/1P/Al2O3 (nominal 1 wt% P)
  - description: Pd on Al2O3 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.8
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.5
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 105.0
    id: coremeta4cat:CAT_32x1-99x6_Al2O3_3P
    title: Pd/3P/Al2O3 (nominal 3 wt% P)
  - description: Pd on Al2O3 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.9
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 4.6
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
    id: VOC4CAT:0000260
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
  - description: Pd on SiO2 support, nominal 1 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.1
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 118.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_1P
    title: Pd/1P/SiO2 (nominal 1 wt% P)
  - description: Pd on SiO2 support, nominal 3 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.8
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.6
    - description: BET specific surface area (bet_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/SpecificArea
      unit: https://qudt.org/vocab/unit/M2-PER-GM
      value: 98.0
    id: coremeta4cat:CAT_32x1-99x6_SiO2_3P
    title: Pd/3P/SiO2 (nominal 3 wt% P)
  - description: Pd on SiO2 support, nominal 5 wt% P (phosphorus modifier)
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: ICP-AES measured Pd loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2.0
    - description: ICP-AES measured P loading (icp_results.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 4.8
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
  id: VOC4CAT:0007001
  title: heterogeneous catalysis
release_date: '2026-03-11'
title:
- "Support Engineering with Phosphorus: Tuning the Palladium-Catalyzed Selective Hydrogenation\
  \ of \xCE\xB1,\xCE\xB2-Unsaturated Aldehydes"
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
    id: ENM:0000064
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
    id: VOC4CAT:0000247
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
  - description: Palladium phosphide (Pd3P) nanoparticles supported on silica, 5 wt%
      Pd, 0.5 mol% metal loading.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Pd loading (Overview Reaction Description-2.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
    id: VOC4CAT:0000247
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
  - description: Palladium phosphide (Pd3P) nanoparticles supported on silica, 5 wt%
      Pd, 0.5 mol% metal loading.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Pd loading (Overview Reaction Description-2.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
    - description: Catalyst mass used per batch test
      has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      unit: https://qudt.org/vocab/unit/GM
      value: 0.01
    id: coremeta4cat:CAT_arp5-s69r_Pd3P_SiO2_5wt
    title: Pd3P/SiO2 (5 wt% Pd, internal code ARNE01)
  - description: Unmodified (phosphorus-free) palladium nanoparticles supported on
      silica, 5 wt% Pd, 0.5 mol% metal loading -- reference catalyst for comparison
      against the Pd3P phosphide.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Pd loading (Overview Reaction Description-2.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
    id: VOC4CAT:0000247
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
  - description: Palladium phosphide (Pd3P) nanoparticles supported on silica, 5 wt%
      Pd, 0.5 mol% metal loading.
    has_physical_state: SOLID
    has_quantitative_attribute:
    - description: Pd loading (Overview Reaction Description-2.txt)
      has_quantity_type: http://qudt.org/vocab/quantitykind/MassFraction
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 5.0
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
  id: VOC4CAT:0007001
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
    id: VOC4CAT:0000078
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
## CatalyticReaction-001
### Input
```yaml
catalyst_form:
- supported
catalyst_quantity:
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
catalyst_quantity:
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
- description: CO adsorption energy on hollow fcc site of Cu(111) relative to gas-phase
    CO
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
