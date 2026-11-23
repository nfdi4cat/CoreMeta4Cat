# Excel Inbox

This folder is the drop-zone for vocabulary workbook contributions via pull request.

## Contributor workflow

1. Download the current vocabulary workbook built from `main`:
   [dev workbook](https://nfdi4cat.github.io/CoreMeta4Cat/dev/assets/coremeta4cat_vocabulary.xlsx).
   Always start from a downloaded copy: it carries a hidden `_baseline`
   sheet recording how it looked when it was generated, which is how the
   check tells your edits apart from changes merged after your download.

2. Edit the workbook in Excel. You may add, adjust or delete rows in the data
   sheets (`Synthesis`, `Characterization`, `Reaction`, `Simulation`).
   Do **not** rename sheets or change the column headers.

3. Open a pull request and place your edited file here as:

   ```
   inbox/coremeta4cat_vocabulary.xlsx
   ```

4. The **Excel inbox** GitHub Actions workflow runs automatically and:
   - Validates the workbook structure (sheet names, column headers) and the
     values you entered (M/R/O, ranges, URI prefixes, UCUM units, cells Excel
     turned into errors).
   - Compares every row with the hidden `_baseline` copy and applies **only
     what you changed**: modifying an existing field's M/R/O (for that class
     only), description, URI, range, multivalued, unit; adding a genuinely
     new field or class (you can add a new field and the new class it points
     to in the same submission -- both are validated together); or removing
     a field whose row you deleted. Rows you did not touch keep their current
     value, even if the schema changed after your download.
   - Checks afterwards that every change really took effect; if anything did
     not, nothing is written.
   - Posts the results as a comment on your PR: errors that must be fixed
     before anything is written, and warnings that need maintainer review
     (e.g. a deletion, an edit that could not be applied, an edit to a field
     that changed on `main` since your download, or an edit to a field that
     is shared across multiple classes -- which lists every other class the
     edit also affects, since such a field has one single definition).
   - If there are no errors, the resulting schema changes are committed
     directly to your PR branch and the inbox copy is removed automatically.
     A maintainer then reviews the diff before merging; `docs/assets/*.xlsx`
     is regenerated after the merge.
   - If there are errors, nothing is written -- fix the workbook and push
     again.

   Workbooks made from an older template (without the `_baseline` sheet)
   are rejected: download the current workbook and copy your edits into it.

## What's editable

Rows that appear in the workbook but are shown greyed-out (see the
**Legend** sheet) are inherited from chemdcat-ap, the underlying chemistry
model CoreMeta4Cat is built on. They're shown for reference so you can see
the full effective field set, but they cannot be added, changed, or removed
through this workflow -- open a schema issue instead. The same goes for the
`CoreMeta4Cat` sheet. Edits there are listed in the PR comment as not applied.

The M/R/O, range and multivalued columns show the values LinkML actually
uses, including what a field inherits from the more general field it is
based on (e.g. most measured quantities are recommended and multivalued).

## Notes

- Only one file named `coremeta4cat_vocabulary.xlsx` is expected.
- The `inbox/` folder is otherwise empty and tracked by `.gitkeep`.
- Do not place other files in this folder.
