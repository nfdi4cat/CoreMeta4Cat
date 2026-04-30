# CoreMeta4Cat Schema Alignment Fixes — 2026-04-29

## What was done

This session identified and fixed schema alignment issues between CoreMeta4Cat and ChemDCAT-AP that accumulated during the previous alignment session (2026-04-27). The previous session updated the synthesis, characterisation, and reaction APs but **left the simulation AP untouched**, causing the schema to fail to load entirely.

---

## Fixes applied

### 1. Critical: undefined `temperature` slots in simulation AP

**File:** `src/coremeta4cat/schema/coremeta4cat_simulation_ap.yaml`

Three classes referenced a `temperature` slot that does not exist anywhere in the schema. The correct slot is `has_temperature` (defined in `material_entities_ap.yaml`, range: `Temperature`).

| Class | Before | After |
|-------|--------|-------|
| `Microkinetics` | `- temperature` | `- has_temperature` |
| `MonteCarlo` | `- temperature` | `- has_temperature` |
| `AqueousStability` | `- temperature` | `- has_temperature` |

**Effect:** The schema failed to load at all before this fix (`ValueError: unknown slot: "temperature"`).

---

### 2. `pressure` alignment in simulation AP

**File:** `src/coremeta4cat/schema/coremeta4cat_simulation_ap.yaml`

The `Microkinetics` class used a locally-defined `pressure` slot with `range: float` and a unit annotation. This breaks the ChemDCAT-AP pattern where pressure is represented as `has_pressure → Pressure` (a `QuantitativeAttribute` instance, not a float).

- **`Microkinetics` slots:** `- pressure` → `- has_pressure`
- **Removed slot definition:**
  ```yaml
  pressure:
    range: float
    unit: {ucum_code: bar}
  ```

---

### 3. `set_temperature` range in synthesis AP

**File:** `src/coremeta4cat/schema/coremeta4cat_synthesis_ap.yaml`

The `set_temperature` slot (used by `CombustionSynthesis`) still used `range: float` with an inline `unit:` annotation, inconsistent with all other temperature slots in the schema.

```yaml
# Before
set_temperature:
  range: float
  unit: {ucum_code: Cel}

# After
set_temperature:
  range: Temperature
  inlined_as_list: true
```

---

### 4. `rdf_type` not available on `CatalysisDataset`

**File:** `src/coremeta4cat/schema/coremeta4cat.yaml`

`CatalysisDataset` uses `rdf_type` in `slot_usage` to classify the catalysis research field. The `rdf_type` slot comes from `ClassifierMixin` (DCAT-AP-PLUS). However, the parent class `Dataset` does not include `ClassifierMixin` in its inheritance chain (unlike `DataGeneratingActivity` and `EvaluatedActivity` which do). The linter reported this as an error.

**Fix:** Added `ClassifierMixin` explicitly to `CatalysisDataset`:
```yaml
CatalysisDataset:
  is_a: Dataset
  class_uri: dcat:Dataset
  mixins:
    - ClassifierMixin
```

---

### 5. Unicode characters causing Windows encoding failure

**Files:** `coremeta4cat_common.yaml`, `coremeta4cat_characterization_ap.yaml`

The Windows shell redirect (`>`) uses `cp1252` encoding. Characters outside cp1252 cause `UnicodeEncodeError` when `gen-pydantic` writes output. Two rounds of fixes were applied.

**Round 1:** Six occurrences of `→` (U+2192, right arrow) — replaced with `->`:

| File | Slot | Description excerpt |
|------|------|---------------------|
| `coremeta4cat_common.yaml` | `has_calcination_temperature_range` | `initial -> final temperature` |
| `coremeta4cat_characterization_ap.yaml` | `has_energy_range` | `minimum -> maximum` |
| `coremeta4cat_characterization_ap.yaml` | `has_temperature_range` | `start -> final temperature` |
| `coremeta4cat_characterization_ap.yaml` | `has_mz_range` | `minimum -> maximum m/z` |
| `coremeta4cat_characterization_ap.yaml` | `has_two_theta_range` | `minimum -> maximum 2theta` |
| `coremeta4cat_characterization_ap.yaml` | `has_wavenumber_range` | `minimum -> maximum cm-1` |

**Round 2:** Full scan of all schema YAML files for non-ASCII characters (69 total). Only three Unicode code points lie outside cp1252: U+2082 `₂` (subscript 2), U+03B8 `θ` (theta), and U+207B `⁻` (superscript minus). Theta and superscript-minus were already eliminated in Round 1. Subscript-2 remained in two `Atmosphere` class descriptions:

| File | Class/Field | Before | After |
|------|-------------|--------|-------|
| `coremeta4cat_common.yaml` | `Atmosphere.description` | `"air", "N₂", "5% H₂/Ar"` | `"air", "N2", "5% H2/Ar"` |
| `coremeta4cat_common.yaml` | `CalcinationGaseousEnvironment.description` | `"N₂", "10% O₂/N₂"` | `"N2", "10% O2/N2"` |

All remaining non-ASCII characters in the schema files (em dashes `—`, ellipses `…`, degree symbol `°`) are within cp1252 and are safe.

---

### 6. SHACL generator excluded from config

**File:** `config.yaml`

`gen-project` crashed in the SHACL generator with `KeyError: 'dcat-ap-plus'`. Root cause: LinkML's `SchemaView.schema_map` keys schemas by import identifier string (e.g. `dcatapplus:latest/schema/dcat_ap_plus`) but `in_schema()` returns the schema's `name:` field (e.g. `dcat-ap-plus`). This mismatch causes a lookup failure for any slot inherited from the external DCAT-AP-PLUS schema. This is a **LinkML 1.9.6 bug** — not a CoreMeta4Cat schema issue.

**Fix:** Added `shacl` to the `excludes` list in `config.yaml`.

---

## Validation results after all fixes

| Check | Result | Notes |
|-------|--------|-------|
| `just _test-schema` | **PASS** | Only pre-existing upstream warnings from DCAT-AP-PLUS |
| `linkml-lint` | **PASS** (no errors) | 5 warnings remain — all from upstream DCAT-AP-PLUS (SIO prefix namespace, URL slot naming) |
| `gen-pydantic` | **PASS** | Unicode fix resolved the Windows encoding error |
| `gen-project` (overall) | **FAIL** at `mv project/*.py` | Pre-existing justfile issue: LinkML 1.9.6 `gen-project` does not output Python files to `project/` root; the `mv` step is a dead line that has never worked in this setup |
| `just site` | Blocked by above | `gen-doc` step itself would pass if `gen-project` succeeded |

---

## Remaining known issues (out of scope for this session)

### Pre-existing justfile bug
`gen-project` fails at `mv project/*.py src/coremeta4cat/datamodel` because LinkML 1.9.6's `gen-project` doesn't write Python files to the output root directory. This predates all changes in this session. The Python model is generated correctly by the separate `gen-pydantic` step.

### Remaining raw `float` slots (Group D)
Several slots in the synthesis and simulation APs still use `range: float` with inline `unit:` annotations instead of a proper `QuantitativeAttribute` subclass. These are not schema errors but are misaligned with the ChemDCAT-AP QUDT pattern. They are deferred to a follow-up session.

**synthesis AP:** `pulse_time`, `purging_duration`, `power`, `sonication_power`, `sonication_duration`, `filling_volume`, `vessel_volume`, `milling_speed`, `milling_duration`, `ball_size`, `capillary_pressure`, `crystallisation_duration`, `temperature_ramp`

**simulation AP:** `simulation_timestep`, `simulation_time`, `activation_energy`, `ionic_strength`

---

## Files changed in this session

| File | Changes |
|------|---------|
| `src/coremeta4cat/schema/coremeta4cat_simulation_ap.yaml` | `temperature` → `has_temperature` (×3); `pressure` → `has_pressure` in Microkinetics; removed local `pressure: float` slot |
| `src/coremeta4cat/schema/coremeta4cat_synthesis_ap.yaml` | `set_temperature: range: float` → `range: Temperature` |
| `src/coremeta4cat/schema/coremeta4cat.yaml` | Added `mixins: [ClassifierMixin]` to `CatalysisDataset` |
| `src/coremeta4cat/schema/coremeta4cat_common.yaml` | `→` → `->` in 1 description; `₂` → `2` in 2 class descriptions |
| `src/coremeta4cat/schema/coremeta4cat_characterization_ap.yaml` | `→` → `->` in 5 descriptions; `θ` → `theta`, `⁻¹` → `-1` |
| `config.yaml` | Added `shacl` to `excludes` |
