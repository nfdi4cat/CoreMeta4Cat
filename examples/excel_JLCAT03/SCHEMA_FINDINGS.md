# What the JLCAT03 workbook revealed about the schema

Items 1–20 were found while mapping the workbook against the schema on `main` (commit 40a0e41,
2026-11-24). Items 21–22 come from adopting the schema of 2026-11-26 (`main` at 72525640a, after
#192 and #199); items 1 and 2 are fixed there. These are about the schema, not the data provider's
workbook. Each item gives the evidence and a possible
fix. Paths starting with `examples/output/` are relative to the repository root; `metadata/` is
this folder's.

## RDF output (affects every example, not only this one)

1. **Activities were typed with a string.** *Fixed by nfdi4cat/CoreMeta4Cat#199.*
   - The problem: `activity_designator` had `slot_uri: rdf:type` and `range: string`, so the
     Turtle said `coremeta4cat:SYN_JLCAT03 a "Synthesis"`, a literal as rdf:type, and the class IRI
     of the activity was not asserted at all. Seen in this record and every combined example.
   - What #199 did (per its diff, not its description): it removed `activity_designator` and
     `CatalysisDataGeneratingActivity`. Each kind of activity now has its own dataset slot
     (`was_generated_by_synthesis`, `_characterization`, `_simulation`, all prov:wasGeneratedBy),
     and `was_generated_by` lists the activities' ids.
   - The activities got their own class IRIs: Synthesis PROCO:0000001, Characterization
     OBI:0000070, Simulation PROCO:0000159, CatalyticReaction REX:0000051. This record now has
     `a PROCO:0000001` etc.
2. **`sample_preparation` was serialised as `<allotrope.quality:0001159>`**, which is not an IRI.
   *Fixed by #199.*
   - The prefix was declared only in `coremeta4cat_characterization_ap.yaml`.
   - #199 declares it, and the other module-only prefixes, in `coremeta4cat.yaml`;
     `tests/test_rdf_output.py` now checks that every CURIE expands.
   - This record's Turtle has no unexpanded CURIE left.
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
    The data provider meant the vessel alone (Q12), i.e. the slot's definition, yet the RDF
    predicate voc4cat:0000153 still carries voc4cat's definition.
11. **Calcination final temperature** (voc4cat:0000058) has no slot. Round 1 put it into
    `has_calcination_temperature_range.max_value`, leaving `min_value` empty. In this record the step
    turned out to be a reduction (item 18), but the gap remains for real calcinations. A dedicated
    slot, or a note in the range's description, would make the mapping explicit.
12. **Reaction temperature** (voc4cat:0007013) is not used. The reaction temperature lands in the
    generic `ChemicalReaction.has_temperature` (SIO:000008); a mapping to the voc4cat term would help.
13. **`ImpregnationTypeEnum` values have no `meaning`.** `incipient_wetness` could carry
    voc4cat:0007806; the RDF currently gets the literal "incipient_wetness".
14. **`step_size` is a bare float**, so its unit cannot be recorded. The provider gave degrees (Q3);
    the unit now sits in the protocol's description.

## Smaller observations

15. **"Recommended" is inherited by almost every slot** from generic DCAT-AP-PLUS parents (e.g.
    `has_quantitative_attribute`). The class pages show nearly every slot as recommended, and a
    check for empty recommended slots lists a `rdf_type` for every quantity. The parser therefore
    only reports recommended slots that the domain class lists itself.
16. **Required instrument for Characterization.** When the instrument is unknown, the requirement is
    met by a placeholder device ("Instrument not specified"). 32x1-99x6 does this, and so did this
    record until the provider named the diffractometer.
17. **Upstream voc4cat typo**: the prefLabel of voc4cat:0000056 is "calcincation gas flow rate".

## Found with the data provider's answers

18. **No reduction step in the preparation methods.** Impregnation, CoPrecipitation and the others
    offer drying and calcination slots, but nothing for a reduction in H2-containing gas. That is a
    common last step for supported metal catalysts, and the one used here (Q10).
    - The step became a generic Activity under `Synthesis.has_part`. Its parameters are typed
      attributes, with generic voc4cat terms where voc4cat has one: atmosphere 0007809, heating
      rate 0008116, gas flow rate 0008109.
    - voc4cat has no concept for a catalyst reduction step either, only the chemical "reduction"
      (0000098, used as the step's type), and no generic dwell-time term.
    - Impregnation also recommends its calcination slots when no calcination took place, so the
      empty-slot check lists them here.
    - Possible fix: a reduction (or general thermal treatment) mixin with atmosphere, temperature
      programme, heating rate, gas flow and hold time.
19. **A contact person cannot be recorded properly.** The range of `contact_point`, vcard:Kind, has
    no properties in DCAT-AP-PLUS. `Attribution` (`qualified_attribution`) has only a title and a
    description, with no agent and no role.
    - Here the contact person (Q17) is a `qualified_attribution` with the title "contact person" and
      the name as its description.
    - No other CoreMeta4Cat record uses either slot.
    - Upstream fix: vcard:fn and vcard:hasEmail on Kind, or prov:agent and dcat:hadRole on
      Attribution.
20. **A licence needs a Distribution.** In DCAT-AP the licence sits on `Distribution`, which
    requires an access URL. Once the provider names a licence, this example needs a distribution,
    e.g. pointing at this folder, just to carry it.

## Found while adopting nfdi4cat/CoreMeta4Cat#192 and #199

21. **Round-tripped data no longer validates.** Since #199, `was_generated_by` holds the activities'
    ids. After a round trip through the Python data model, LinkML writes them as `{"id": ...}`
    objects, which the schema rejects.
    - `linkml-convert` validates that round-tripped data by default and stops; it needs
      `--no-validate`.
    - The JSON in `examples/output/` (written via the data model) does not validate either. In
      `examples/output/CatalysisDataset-6mxw-xsrd.json` all 8 `was_generated_by` entries fail, and
      so do 3 `realized_plan` entries.
    - The JSON in `docs/assets/examples/`, written straight from the source data by
      `scripts/generate_example_outputs.py`, validates. This example writes its JSON the same way.
22. **The reaction type is now required** (#192), and a workbook rarely contains an ontology term
    for it. Here it was deduced from the reaction name: voc4cat:0000205 'epoxidation', confirmed to
    exist in voc4cat v2026-10-31. It was then flagged for the provider to confirm.
