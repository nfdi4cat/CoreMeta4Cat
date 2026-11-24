# Examples of using CatCore

This folder contains examples using the datamodel.

The source of the data used in the example is [tests/data](../tests/data/).

The command `just test` creates different representations of the data in [tests/data](../tests/data/) and writes them to the subfolder `output`.
It also generates a markdown documentation of the examples which is not very useful in its current form.
Hence, the `output` sub-folder is git-ignored.

[excel_JLCAT03](excel_JLCAT03/) is a separate, hand-made worked example: a laboratory Excel workbook turned into a CoreMeta4Cat record, with the parser written for it. See its README.
