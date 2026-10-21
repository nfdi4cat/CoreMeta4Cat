# Excel Inbox

This folder is the drop-zone for vocabulary workbook contributions via pull request.

## Contributor workflow

1. Download the current vocabulary reference workbook from
   [`docs/assets/coremeta4cat_vocabulary.xlsx`](../docs/assets/coremeta4cat_vocabulary.xlsx).

2. Edit the workbook in Excel. You may add or adjust rows in the data sheets
   (`Synthesis`, `Characterization`, `Reaction`, `Simulation`).
   Do **not** rename sheets or change the column headers.

3. Open a pull request and place your edited file here as:

   ```
   inbox/coremeta4cat_vocabulary.xlsx
   ```

4. The **Excel inbox** GitHub Actions workflow runs automatically and:
   - Validates the workbook structure (sheet names, column headers).
   - Diffs every row against the current schema and plans the corresponding
     schema changes: modifying an existing field's M/R/O, description, URI,
     range, etc.; adding a genuinely new field or class (you can add a new
     field and the new class it points to in the same submission -- both
     are validated together); or flagging a field/class present in the
     schema but missing from your workbook as a deletion.
   - Posts the results as a comment on your PR: errors that must be fixed
     before anything is written, and warnings that need maintainer review
     (e.g. a deletion, or an edit to a field that is shared across multiple
     classes -- which lists every other class the edit also affects, since
     such a field has one single definition, not one per class).
   - If there are no errors, the resulting schema changes are committed
     directly to your PR branch, the regenerated `docs/assets/*.xlsx`
     workbook is committed alongside them, and the inbox copy is removed
     automatically. A maintainer then reviews the diff before merging.
   - If there are errors, nothing is written -- fix the workbook and push
     again.

## What's editable

Rows that appear in the workbook but are shown greyed-out (see the
**Legend** sheet) are inherited from chemdcat-ap, the underlying chemistry
model CoreMeta4Cat is built on. They're shown for reference so you can see
the full effective field set, but they cannot be added, changed, or removed
through this workflow -- open a schema issue instead.

## Notes

- Only one file named `coremeta4cat_vocabulary.xlsx` is expected.
- The `inbox/` folder is otherwise empty and tracked by `.gitkeep`.
- Do not place other files in this folder.
