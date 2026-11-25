# Feedback on TestDataSet_CoreMeta4Cat.xlsx (catalyst JLCAT03)

Thank you for the workbook. It converts into a valid CoreMeta4Cat record, with JSON and RDF
versions. This note lists what worked, what we need from you before publishing it as the
documentation example, and how the template could be set up so that the next workbook converts
without guesswork.

Every value we used, and why, is in `metadata/source_documentation.yaml`. The same questions, with
cell references, are in `metadata/parse_report.md`.

## Status after your answers (2026-11-24)

Thank you for answering (transcript: `source/provider_answers.md`). With your answers the record
validates without any placeholder, and all 13 questions below are settled. What changed:

- **Reduction step.** The "calcination" columns now describe a reduction step in 5 % H2/N2 (your
  answer to question 10). It is recorded as a separate step of the synthesis, because the schema's
  impregnation method has a calcination step but no reduction step.
- **PXRD rows 11, 12 and 22.** Their title, description and ID now belong to the PXRD measurement
  (question 8).
- **New values.** The units, the drying time, the diffractometer, the measured phase and oxygen as
  reactant are now in the record. So are the dataset's title, description, keywords and contact
  person.

Still open:

1. **Licence.** Under which licence may the example be published (e.g. CC BY 4.0)?
2. **Authors.** Who should be named as creators of the dataset, with ORCID? We did not assume
   that the contact person is an author.
3. **NTP.** "NTP" is defined in more than one way. NIST uses 20 °C and 1 atm, while the German
   normal litre (DIN 1343) refers to 0 °C and 1.01325 bar. Which applies to the 15 nl/h?
4. **Reaction type** (optional): an ontology term for the reaction type, e.g. an RXNO term for
   epoxidation.

The first-round feedback follows unchanged.

## What worked well

- **The vocabulary IDs are right.** All 39 voc4cat IDs in your headers exist and their labels match
  your column names. The other IDs (PROCO, AFE, NCIT, RO, CHMO, OBI, Allotrope) are also correct.
- **Units in their own row** (Synthesis and Reaction sheets) could be read without interpretation.
- **One catalyst ID in all three sheets** (`JLCAT03`) links synthesis, PXRD and catalytic test to
  the same catalyst. This is what makes the example an "interconnected workflow".
- **InChIs for every substance** give each chemical an unambiguous identity.
- **The numbers are consistent.** 100.9 mg Pt(NH3)4(NO3)2 on 957.9 mg Al2O3 gives 5.0 wt.% Pt,
  which matches the stated metal loading.

## Please answer before we publish

**Missing information the schema requires.** Without it, the record only validates with an
explicit "not stated" entry.

1. **PXRD instrument**: which diffractometer was used (make, model)? `Characterization` requires
   the instrument.
2. **Measured catalyst properties** (`catalyst_measured_properties`, required): did you measure
   anything on JLCAT03, for example the Pt content (ICP), BET surface area, or the phases seen in
   the PXRD? If nothing was measured, say so and we keep "none given".

**Missing units.** For the Reaction sheet we could deduce the unit; the Character sheet has no units
at all.

3. Character sheet: the unit of the **2θ range** "2 to 90" (we assume degrees), the **step size** 0.5
   (degrees 2θ?), the **sample spinning speed** 30 (rpm? rps?) and the **experiment duration** 80
   (min? s?). We recorded spinning speed and duration without a unit, because we cannot tell.
4. Reaction sheet, Z2: unit of the **reaction temperature** 100. We assumed °C, because your
   reactor temperature range is 50–100 °C.
5. Reaction sheet, AF2: unit of the **second yield** 22. We assumed %, like the first yield.

**Values we could not use as given.**

6. **Drying duration "over night"**: please give a number of hours. A duration has to be a number;
   for now the text is only kept in a description.
7. **Calcination gas flow "15 nl/h"**: we read this as normal litres per hour. Please confirm, and
   give the reference conditions (e.g. 0 °C and 1.01325 bar). The unit vocabulary we use (QUDT) has
   no normal-litre unit, so the record currently stores the value without a unit.

**Ambiguous placement.**

8. Character rows 11, 12 and 22 (title "PXRD of catalyst", description "PXRD of JLCAT03", id
   "JLCAT-PXRD-03") sit in the PowderXRD block, so we read them as the title, description and ID of
   the PXRD *protocol*. They sound like the title, description and ID of the *measurement* itself.
   Which did you mean?

## Please confirm

9. **Metal loading 5 wt.%**: nominal (calculated from the masses) or measured? We treated it as a
   property of the catalyst without claiming either. If it was measured, it also belongs under
   measured properties.
10. **Calcination under 5 % H2/N2**: this is a reducing gas. Was the step a calcination, or a
    reduction? The schema's impregnation method has a calcination step but no separate reduction
    step.
11. **Calcination programme**: only the final temperature (700 °C) is given. What was the starting
    temperature (room temperature?)?
12. **Reaction chamber volume 10 mL**: the voc4cat term you used includes connected pipes and
    valves. Is the 10 mL the vessel alone, or vessel plus connections?
13. **Oxygen**: you listed it as the atmosphere (1 bar). If it is the oxidant of the epoxidation,
    it can also be listed as a reactant (`used_reactant`, recommended by the schema).

## Optional fields the schema recommends

Fill these only where you know them:

- **Reaction**: an ontology term for the reaction type (e.g. an RXNO term for epoxidation).
- **PXRD**: measurement temperature, detector type.
- **Autoclave**: reaction chamber material, vessel material, batch duration.
- **Dataset**: title, description, authors (with ORCID), contact person, licence, keywords, and a
  related publication if there is one. There is no place for these in the workbook yet. We
  composed a title from your values and took the description from your e-mail, but authorship and
  licence have to come from you.

## How to set up the template next time

The conversion needed one hand-written mapping entry per column or row, partly because the three
sheets use different layouts and conventions. These changes would make a workbook convertible
almost mechanically.

1. **Use one layout for every sheet: one record per row.** The Characterization sheet is laid out
   vertically, with class rows (bold) mixed with field rows. Values sometimes sit on the class row
   (OperationMode, Atmosphere), sometimes on the field row, sometimes on both (Duration repeats
   "has experiment duration"). A table like the Synthesis sheet avoids this, with one row per
   measurement.

2. **Put name, term ID and unit in three separate header rows**, and never inside the header text:

   | (row 1) field | impregnation_temperature | has_drying_duration | has_drying_atmosphere |
   |---|---|---|---|
   | (row 2) term | voc4cat:0008121 | voc4cat:0008206 | voc4cat:0008208 |
   | (row 3) unit | °C | h | |
   | (row 4+) data | 25 | a number, e.g. 16 | air |

   Use the CoreMeta4Cat field name (e.g. `has_calcination_atmosphere`) in row 1, not only a term
   ID. Some IDs are shared: `SIO:000008`, the ID you gave for the calcination atmosphere, belongs to
   dozens of fields, and `voc4cat:0008113` (stirrer type) to both a synthesis field and a reactor
   field.

3. **Give every numeric column a unit**, written the same way throughout (`mL`, not sometimes `ml`).
   For gas flows at normal conditions, use `L/h` and add a column for the reference conditions.

4. **One value per cell, numbers only in numeric columns.**
   - "over night" → a number of hours.
   - "50-100" or "2 to 90" → two columns, minimum and maximum.
   - "Autoclave (NCIT:C93052)" → `Autoclave`, with the ID in the term row or a pick-list.

5. **Use pick-lists (Excel data validation) for controlled values**, with the values the schema
   accepts: catalyst type `heterogeneous_catalysis`, catalyst form `powdered`, impregnation type
   `incipient_wetness`, sample state `solid`, preparation method `Impregnation`, reactor `Autoclave`.
   We currently translate "heterogeneous", "powder" and "incipient wetness impregnation
   (voc4cat:0007806)" by hand.

6. **Move repeating groups to their own sheet.** Instead of "Precursor 1 / Precursor 2" and
   "generated product 1 / 2" column groups, use a Precursors sheet (catalyst ID, substance, InChI,
   quantity, unit) and a Products sheet (test ID, product, InChI, yield, unit). The current groups
   drift apart: Precursor 2 has no InChI column, and product 2 has no unit cell.

7. **Keep the IDs, and add the missing ones.** The catalyst ID as the link between sheets is
   exactly right. Give each measurement its own ID column (like `JLCAT-PXRD-03`), and give
   instruments an ID too (as for the reactor, `MBR01`).

8. **Add a "Dataset" sheet** with title, description, authors (name and ORCID), contact, licence,
   keywords, research field and related publication.

9. **Add instrument fields to every measurement and analysis**: diffractometer, GC-MS (make, model,
   ID).

10. **Small things that cost time:**
    - Write term IDs one way: lowercase prefix (`voc4cat:`, not `VOC4CAT:`), colon form (`AFR:0002018`,
      not `AFR_0002018`).
    - Spelling: "yeild" → "yield".
    - Trailing spaces in values ("water ", "Impregnation ", "grinding ").
    - Formatting (bold) used to carry meaning.
    - Values repeated in two rows.

11. **For chemicals, an InChIKey or a PubChem CID / ChEBI ID** next to the InChI would let us link
    each substance to a public identifier instead of minting a local one.
