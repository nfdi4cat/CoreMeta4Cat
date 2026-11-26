# Answers from the data provider (2026-11-24)

Verbatim transcript of `provider_answers_2026-11-24.docx`. After the first parse of the workbook
we sent the data provider our questions, and they wrote their answers into a copy of them.
Questions and headings are ours, answers (quoted) are theirs, unchanged; the transcript was
generated from the .docx, not retyped. The record's provenance cites the answers by question
number (Q1–Q17).

## Missing information the schema requires. Without it, the record only validates with an explicit "not stated" entry.

**Q1.** PXRD instrument: which diffractometer was used (make, model)? Characterization requires the instrument.

> Stoe STADI-MP diffractometer

**Q2.** Measured catalyst properties (catalyst_measured_properties, required): did you measure anything on JLCAT03, for example the Pt content (ICP), BET surface area, or the phases seen in the PXRD? If nothing was measured, say so and we keep "none given".

> Phase seen in PXRD is Pt

## Missing units. For the Reaction sheet we could deduce the unit; the Character sheet has no units at all.

**Q3.** Character sheet: the unit of the 2θ range "2 to 90" (we assume degrees), the step size 0.5 (degrees 2θ?), the sample spinning speed 30 (rpm? rps?) and the experiment duration 80 (min? s?). We recorded spinning speed and duration without a unit, because we cannot tell.

> 2theta ranges and step size in degree, sample spinning speed 30 rpm, experiment duration is 80 min

**Q4.** Reaction sheet, Z2: unit of the reaction temperature 100. We assumed °C, because your reactor temperature range is 50–100 °C.

> yes

**Q5.** Reaction sheet, AF2: unit of the second yield 22. We assumed %, like the first yield.

>  yes

## Values we could not use as given.

**Q6.** Drying duration "over night": please give a number of hours. A duration has to be a number; for now the text is only kept in a description.

> 12 hours

**Q7.** Calcination gas flow "15 nl/h": we read this as normal litres per hour. Please confirm, and give the reference conditions (e.g. 0 °C and 1.01325 bar). The unit vocabulary we use (QUDT) has no normal-litre unit, so the record currently stores the value without a unit.

> NTP conditions

## Ambiguous placement.

**Q8.** Character rows 11, 12 and 22 (title "PXRD of catalyst", description "PXRD of JLCAT03", id "JLCAT-PXRD-03") sit in the PowderXRD block, so we read them as the title, description and ID of the PXRD protocol. They sound like the title, description and ID of the measurement itself. Which did you mean?

> Title, description and ID of the measurement

## Please confirm

**Q9.** Metal loading 5 wt.%: nominal (calculated from the masses) or measured? We treated it as a property of the catalyst without claiming either. If it was measured, it also belongs under measured properties.

> Nominal

**Q10.** Calcination under 5 % H2/N2: this is a reducing gas. Was the step a calcination, or a reduction? The schema's impregnation method has a calcination step but no separate reduction step.

> Reduction process only used. No calcination in air involved.

**Q11.** Calcination programme: only the final temperature (700 °C) is given. What was the starting temperature (room temperature?)?

> Starting temperature is room temperature, 25 degC

**Q12.** Reaction chamber volume 10 mL: the voc4cat term you used includes connected pipes and valves. Is the 10 mL the vessel alone, or vessel plus connections?

> Just vessel, no volume of the fittings or connection involved

**Q13.** Oxygen: you listed it as the atmosphere (1 bar). If it is the oxidant of the epoxidation, it can also be listed as a reactant (used_reactant, recommended by the schema).

> Oxygen is a reactant

## Optional fields the schema recommends

## Fill these only where you know them:

**Q14.** Reaction: an ontology term for the reaction type (e.g. an RXNO term for epoxidation).

> *(no answer)*

**Q15.** PXRD: measurement temperature, detector type.

> Temperature: room temperature, 25 degC, detector type: dectris mythen 1K

**Q16.** Autoclave: reaction chamber material, vessel material, batch duration.

> Reaction chamber and vessel material: stainless steel, batch duration: 12 h

**Q17.** Dataset: title, description, authors (with ORCID), contact person, licence, keywords, and a related publication if there is one. There is no place for these in the workbook yet. We composed a title from your values and took the description from your e-mail, but authorship and licence have to come from you.

> Title: Supported Pt catalyst for the epoxidation of styrene

> Description: Alumina supported Pt catalyst was synthesized with incipient wetness impregnation and applied in the liquid phase epoxidation reaction of styrene.

> Contact person: Arjun Neyyathala

> Key words: epoxidation, supported catalyst, styrene oxide
