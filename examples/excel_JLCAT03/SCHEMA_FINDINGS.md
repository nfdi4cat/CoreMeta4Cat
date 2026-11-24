# What the JLCAT03 workbook revealed about the schema

Found while mapping the workbook against the schema on `main` (commit 40a0e41, 2026-11-24). These
are about the schema, not the data provider's workbook. Each item gives the evidence and a possible
fix. Paths starting with `examples/output/` are relative to the repository root; `metadata/` is
this folder's.

## RDF output (affects every example, not only this one)

1. **Activities are typed with a string.** `activity_designator` has `slot_uri: rdf:type` and
   `range: string`, so the Turtle says `coremeta4cat:SYN_JLCAT03 a "Synthesis"`, a literal as
   rdf:type. The class IRI of Synthesis/Characterization (OBI:0000070) is not asserted at all.
   - Evidence: `metadata/CatalysisDataset-JLCAT03.ttl`; also `examples/output/CatalysisDataset-001.ttl`
     (lines 17, 23, 42) and 8 times in `CatalysisDataset-6mxw-xsrd.ttl`.
   - Fix: not simply range `uriorcurie` as for `plan_designator`. Synthesis and Characterization
     share class_uri OBI:0000070, so an IRI designator could not tell them apart. Options: distinct
     class_uris for the two, or a designator slot_uri other than rdf:type, which keeps it out of the
     type assertions.
2. **`sample_preparation` is serialised as `<allotrope.quality:0001159>`**, which is not an IRI. The
   prefix `allotrope.quality` is declared only in `coremeta4cat_characterization_ap.yaml`;
   `allotrope.result` is declared in `coremeta4cat_common.yaml` too, and it expands.
   - Evidence: this record; also `examples/output/CatalysisDataset-002.ttl` and `Characterization-003.ttl`.
   - Fix: declare the prefix in `coremeta4cat.yaml` or `coremeta4cat_common.yaml`.
3. **QUDT unit namespace.** Every example uses `https://qudt.org/vocab/unit/...` (227 times in
   CoreMeta4Cat; DCAT-AP-PLUS's `QUDTUnitEnum` also names `https://`). QUDT itself declares
   `http://qudt.org/vocab/unit/` (checked on qudt.org v3.5.4), so the unit IRIs in our RDF do not
   match QUDT's. Quantity kinds already use `http://`. This needs one project-wide decision; this
   example follows the current convention.

## Missing or contradictory slots

4. **No slot for metal loading** (voc4cat:0008106) or catalyst identifier (voc4cat:0008134), both of
   which have voc4cat terms. Here they became a generic quantity on the CatalystSample, typed by
   `rdf_type`, and an `other_identifier`. `tests/data/valid/CatalysisDataset-arp5-s69r.yaml` already
   stores Pd loading the same way (a generic MassFraction quantity on the catalyst). A dedicated
   slot would also let the schema cap mass fractions at 100 %.
5. **The amount of support has no place.** `catalyst_support` is a string, and
   `Synthesis.had_input_entity` accepts only `Precursor`. The support (957.9 mg Al2O3, with its InChI)
   therefore had to be listed as a Precursor. Possible fixes: a support object with a quantity, or
   allow `MaterialSample` inputs.
6. **Chemical identity sits in three places, depending on the class.**
   - `ChemicalEntity.inchi` (synthesis solvent).
   - `composed_of[].inchi` (reaction chemicals, via `ChemicalSubstanceMixin`).
   - Nowhere for `Precursor`, a MaterialSample without `composed_of`. Here the InChI became a
     generic attribute typed CHEMINF:000113.

   Giving Precursor the `ChemicalSubstanceMixin` would make precursors look like the other
   chemicals.
7. **A yield cannot be linked to its product.** `has_yield` is on the reaction (chem-dcat-ap). With
   two products, the product is only named in the yield's description. This is an upstream
   chem-dcat-ap issue.
8. **`product_identification_method` cannot be GCMS.** Its description says to "reference a
   CharacterizationTechnique instance (e.g. GCMS, HPLC_MS)". But the range is
   `ProductIdentificationMethod`, whose `plan_designator` allows only OBI:0000272. GCMS is therefore
   given as `rdf_type` CHMO:0000497. Possible fix: range `CharacterizationTechnique`.
9. **Operation mode means two things.** voc4cat:0000108 "operation mode" is defined as how
   reactants enter and products leave the reaction chamber (batch, continuous). The schema uses it as
   the class_uri of `OperationMode` for instrument modes (PXRD "transmission"). Meanwhile neither
   `CatalyticReaction` nor `ChemicalReactor` has a slot for the batch/continuous mode the term
   describes; here it became a typed generic attribute of the reactor.
10. **voc4cat:0000153 contradicts `reactor_working_volume`.** voc4cat defines the reaction chamber
    volume as including connected pipes and valves. The slot's description says they are excluded.
11. **Calcination final temperature** (voc4cat:0000058) has no slot. It goes into
    `has_calcination_temperature_range.max_value`, leaving `min_value` empty. A dedicated slot, or a
    note in the range's description, would make this mapping explicit.
12. **Reaction temperature** (voc4cat:0007013) is not used. The reaction temperature lands in the
    generic `ChemicalReaction.has_temperature` (SIO:000008); a mapping to the voc4cat term would help.
13. **`ImpregnationTypeEnum` values have no `meaning`.** `incipient_wetness` could carry
    voc4cat:0007806; the RDF currently gets the literal "incipient_wetness".
14. **`step_size` is a bare float**, so its unit cannot be recorded.

## Smaller observations

15. **"Recommended" is inherited by almost every slot** from generic DCAT-AP-PLUS parents (e.g.
    `has_quantitative_attribute`). The class pages show nearly every slot as recommended, and a
    check for empty recommended slots lists a `rdf_type` for every quantity. The parser therefore
    only reports recommended slots that the domain class lists itself.
16. **Required instrument for Characterization.** When the instrument is unknown, the requirement is
    met by a placeholder device ("Instrument not specified"), as in 32x1-99x6 and this record.
17. **Upstream voc4cat typo**: the prefLabel of voc4cat:0000056 is "calcincation gas flow rate".
