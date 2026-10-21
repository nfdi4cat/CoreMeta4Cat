import yaml
from pathlib import Path
from typing import List, Set, Optional

_HERE = Path(__file__).parent
_ROOT = _HERE.parent

# coremeta4cat.yaml is loaded FIRST so its generic stubs (range: Plan, range: AgenticEntity)
# are overwritten by the specific ranges in the subprofile modules.
#
# EDITABLE_MODULE_FILES are the coremeta4cat-authored modules: everything a
# contributor can add/modify/delete via the Excel inbox workflow. This is the
# canonical, single source of truth for "editable" — also imported by
# inbox_to_schema.py for build_origin_index(), which must stay scoped to
# exactly these files.
#
# VENDORED_MODULE_FILES are the locally-vendored chemdcat-ap files. Classes/
# slots defined here (e.g. ChemicalReaction, Reactor) are loaded so that
# is_a-inheritance resolution (get_all_class_slots, get_subclasses) can see
# them, but they are NOT editable via the Excel inbox workflow — contributors
# only ever see them as inherited, read-only reference rows.
#
# ALL_MODULE_FILES is what actually gets merged into the in-memory schema
# dict used for slot/class resolution and rendering.
EDITABLE_MODULE_FILES = [
    "coremeta4cat.yaml",           # load first: generic stubs get overwritten by subprofiles
    "coremeta4cat_common.yaml",
    "coremeta4cat_synthesis_ap.yaml",
    "coremeta4cat_characterization_ap.yaml",
    "coremeta4cat_reaction_ap.yaml",
    "coremeta4cat_simulation_ap.yaml",
]

VENDORED_MODULE_FILES = [
    "chem_dcat_ap.yaml",
    "chemical_reaction_ap.yaml",
    "chemical_entities_ap.yaml",
    "material_entities_ap.yaml",
]

ALL_MODULE_FILES = EDITABLE_MODULE_FILES + VENDORED_MODULE_FILES


# ─────────────────────────────────────────────────────────────────────────────
# Schema loading & merging
# ─────────────────────────────────────────────────────────────────────────────

def load_yaml_file(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        print(f"  [WARNING] Module not found, skipping: {file_path}")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def merge_schemas(modules: List[dict]) -> dict:
    """
    Merge all module dicts into one flat schema.
    Later modules win on key collision, so subprofile modules (loaded last)
    correctly override the generic stubs in coremeta4cat.yaml (loaded first).
    """
    merged: dict = {"prefixes": {}, "classes": {}, "slots": {}, "enums": {}}

    for module in modules:
        if not module:
            continue
        for key in ("id", "name", "title", "description", "license",
                    "version", "default_prefix", "default_range"):
            if key not in merged and key in module:
                merged[key] = module[key]

        for section in ("prefixes", "classes", "slots", "enums"):
            section_data = module.get(section) or {}
            for name, definition in section_data.items():
                if section == "classes" and name in merged["classes"]:
                    existing = merged["classes"][name]
                    incoming = definition or {}
                    # slot_usage: merge entry by entry; incoming wins per key
                    if "slot_usage" in incoming:
                        existing.setdefault("slot_usage", {})
                        existing["slot_usage"].update(incoming["slot_usage"])
                    # slots list: union (incoming appends new names)
                    if "slots" in incoming:
                        existing_slots = existing.get("slots", [])
                        for s in incoming["slots"]:
                            if s not in existing_slots:
                                existing_slots.append(s)
                        existing["slots"] = existing_slots
                    # all other keys: incoming wins
                    for k, v in incoming.items():
                        if k not in ("slot_usage", "slots"):
                            existing[k] = v
                else:
                    merged[section][name] = (
                        dict(definition) if isinstance(definition, dict) else definition
                    )
    return merged


def load_merged_schema(schema_dir: str) -> dict:
    schema_dir_path = Path(schema_dir)
    modules = []
    for filename in ALL_MODULE_FILES:
        full_path = schema_dir_path / filename
        print(f"  Loading: {full_path}")
        modules.append(load_yaml_file(str(full_path)))
    merged = merge_schemas(modules)
    print(f"  Merged schema: {len(merged.get('classes', {}))} classes, "
          f"{len(merged.get('slots', {}))} slots\n")
    return merged


def build_origin_index(schema_dir) -> tuple[dict, dict]:
    """
    Return (slot_origin, class_origin): maps each slot/class name to the
    editable-module YAML file that defines it.

    Only scans EDITABLE_MODULE_FILES (never the vendored chemdcat-ap files),
    so a name's presence here is exactly the "is this editable via the Excel
    inbox workflow" predicate, used consistently by both schema_to_excel.py
    (to render inherited/vendored rows as read-only) and inbox_to_schema.py
    (to decide what can be modified or deleted).
    """
    schema_dir_path = Path(schema_dir)
    slot_origin:  dict = {}
    class_origin: dict = {}

    for fname in EDITABLE_MODULE_FILES:
        fpath = schema_dir_path / fname
        doc = load_yaml_file(str(fpath))
        for name in (doc.get("slots") or {}):
            slot_origin[name] = fpath
        for name in (doc.get("classes") or {}):
            class_origin[name] = fpath

    return slot_origin, class_origin


# ─────────────────────────────────────────────────────────────────────────────
# Mixin-aware slot resolution
# ─────────────────────────────────────────────────────────────────────────────

def get_all_class_slots(schema: dict, class_name: str,
                        _seen: Optional[Set[str]] = None) -> List[str]:
    """Return all slots on a class, including those inherited via is_a and
    those contributed by mixins.

    is_a resolution climbs into the merged schema (which now also includes
    the vendored chemdcat-ap modules, see ALL_MODULE_FILES) and stops
    silently at any class name not present there -- e.g. an external,
    unvendored dcat-ap-plus root like EvaluatedActivity or Device. That
    class is simply treated as an inheritance root with no further slots
    to add, mirroring how an unknown mixin name already degrades
    gracefully today.
    """
    if _seen is None:
        _seen = set()
    if class_name in _seen:
        return []
    _seen.add(class_name)
    class_def   = schema.get("classes", {}).get(class_name, {})
    own_slots   = class_def.get("slots", []) or []

    parent_name  = class_def.get("is_a")
    parent_slots: List[str] = []
    if parent_name and parent_name in schema.get("classes", {}):
        parent_slots = get_all_class_slots(schema, parent_name, _seen.copy())

    mixin_names = class_def.get("mixins", []) or []
    mixin_slots: List[str] = []
    for mixin_name in mixin_names:
        for s in get_all_class_slots(schema, mixin_name, _seen.copy()):
            if s not in mixin_slots:
                mixin_slots.append(s)
    combined = list(own_slots)
    for s in parent_slots:
        if s not in combined:
            combined.append(s)
    for s in mixin_slots:
        if s not in combined:
            combined.append(s)
    return combined


def get_class_ranged_slot_usage(schema: dict, class_name: str,
                                exclude: Optional[Set[str]] = None) -> List[tuple]:
    """
    Return (slot_name, synthetic_slot_def) pairs for every slot_usage entry
    whose range points to a class defined in the merged schema.

    These are the 'gateway' slots that expand into nested class/subclass docs
    for slot_usage entries that narrow an inherited slot NOT otherwise reachable
    via the class's own/inherited `slots:` lists (get_all_class_slots):
      Synthesis        → realized_plan:PreparationMethod, had_input_entity:Precursor, had_output_entity:CatalystSample
      Characterization → realized_plan:CharacterizationTechnique
      Simulation       → realized_plan:SimulationMethod

    `exclude` should be the set of slot names already covered by
    get_all_class_slots() for this class -- any slot_usage entry for a name
    already in that set is skipped here, since it will already be rendered
    (with the slot_usage-narrowed cardinality/range applied via
    get_slot_cardinality/format_slot_markdown) as part of the regular slot
    list. Without this check, a slot that is both explicitly listed in a
    class's `slots:` and separately narrowed via `slot_usage` with a
    class-valued range (e.g. Reaction's product_identification_method) would
    be rendered twice under the same name.
    """
    classes    = schema.get("classes", {})
    slots_dict = schema.get("slots", {})
    class_def  = classes.get(class_name, {})
    slot_usage = class_def.get("slot_usage", {}) or {}
    exclude    = exclude or set()

    result = []
    for su_name, su_def in slot_usage.items():
        if not su_def:
            continue
        if su_name in exclude:
            continue
        rng = su_def.get("range")
        if not rng or rng not in classes:
            continue
        if classes.get(rng, {}).get("mixin"):
            continue
        # Build synthetic slot def: base slot (if any) + slot_usage overrides
        base = dict(slots_dict.get(su_name, {}))
        base.update({k: v for k, v in su_def.items() if v is not None})
        if not base.get("description"):
            base["description"] = f"Link to {rng} — see subclasses for details."
        base["range"] = rng
        result.append((su_name, base))
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Standard helpers
# ─────────────────────────────────────────────────────────────────────────────

def is_mixin(schema: dict, class_name: str) -> bool:
    return bool(schema.get("classes", {}).get(class_name, {}).get("mixin", False))


def get_subclasses(schema: dict, parent_class: str) -> List[str]:
    """Return all (recursive) non-mixin subclasses of parent_class."""
    subclasses = []
    for class_name, class_def in schema.get("classes", {}).items():
        if class_def.get("is_a") == parent_class and not is_mixin(schema, class_name):
            subclasses.append(class_name)
            subclasses.extend(get_subclasses(schema, class_name))
    return subclasses


def get_slot_details(schema: dict, slot_name: str) -> dict:
    return schema.get("slots", {}).get(slot_name, {})


def is_class_in_schema(schema: dict, class_name: str) -> bool:
    return class_name in schema.get("classes", {})


def snake_to_readable(text: str) -> str:
    return text.replace("_", " ")


def expand_curie(schema: dict, value: str) -> str:
    if ":" not in value or value.startswith("http"):
        return value
    prefix, local = value.split(":", 1)
    entry = schema.get("prefixes", {}).get(prefix)
    if not entry:
        return value
    if isinstance(entry, str):
        base = entry
    elif isinstance(entry, dict):
        base = entry.get("prefix_reference") or entry.get("uri") or entry.get("prefix") or ""
    else:
        return value
    if not base:
        return value
    return base + local if base.endswith(("/", "#")) else base + local


def get_slot_cardinality(schema: dict, class_name: str,
                         slot_name: str, slot_details: dict) -> str:
    class_def = schema.get("classes", {}).get(class_name, {})
    usage = (class_def.get("slot_usage", {}) or {}).get(slot_name, {}) or {}
    required    = usage.get("required",    slot_details.get("required",    False))
    recommended = usage.get("recommended", slot_details.get("recommended", False))
    multivalued = usage.get("multivalued", slot_details.get("multivalued", False))
    parts = ["Mandatory" if required else ("Recommended" if recommended else "Optional")]
    if multivalued:
        parts.append("Multivalued")
    return ", ".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Markdown formatters
# ─────────────────────────────────────────────────────────────────────────────

def format_class_markdown(schema: dict, class_name: str, level: int = 3,
                          processed_classes: Optional[Set[str]] = None,
                          parent_class: Optional[str] = None,
                          rendered: Optional[dict] = None) -> str:
    """Render a class as a <details> block.

    `rendered` is a page-wide (not per-branch) name -> anchor-id map, shared
    across the whole recursive walk for one output page. A class that is
    reached from multiple slots/paths (e.g. Temperature, Pressure,
    ChemicalEntity -- common once CatalyticReaction inherits ChemicalReaction's
    full slot set) is fully expanded only the first time; later occurrences
    link back to that first rendering instead of re-expanding its entire slot
    subtree again, which would otherwise multiply page size with every
    additional path that reaches the same shared class.
    """
    if processed_classes is None:
        processed_classes = set()
    if class_name in processed_classes:
        return ""
    processed_classes.add(class_name)
    if rendered is None:
        rendered = {}

    class_def   = schema.get("classes", {}).get(class_name, {})
    description = class_def.get("description", "No description available")
    class_uri   = class_def.get("class_uri", "")
    is_abstract = class_def.get("abstract", False)

    if class_name in rendered:
        anchor = rendered[class_name]
        md  = '<details markdown="1">\n'
        md += f'<summary><strong>{snake_to_readable(class_name)}</strong></summary>\n\n'
        md += f"**Description:** {description}\n\n"
        if class_uri:
            md += f"**CURIE:** [`{class_uri}`]({expand_curie(schema, class_uri)})\n\n"
        md += (f"*Full field list already shown [earlier on this page](#{anchor}) "
               f"-- this class is reached from multiple fields.*\n\n")
        md += "</details>\n\n"
        return md

    anchor = f"schema-class-{class_name}"
    rendered[class_name] = anchor

    open_attr = " open" if level == 3 else ""
    md  = f'<details markdown="1"{open_attr} id="{anchor}">\n'
    md += f'<summary><strong>{snake_to_readable(class_name)}</strong></summary>\n\n'
    if is_abstract:
        md += "**Abstract Class**\n\n"
    md += f"**Description:** {description}\n\n"
    if class_uri:
        md += f"**CURIE:** [`{class_uri}`]({expand_curie(schema, class_uri)})\n\n"
    md += f"**Schema Reference:** [{class_name}](./elements/classes/{class_name}.md)\n\n"

    slots = get_all_class_slots(schema, class_name)
    if slots:
        md += "**Slots**\n\n"
        for slot_name in slots:
            slot_details = get_slot_details(schema, slot_name)
            md += format_slot_markdown(schema, slot_name, slot_details, level + 2,
                                       processed_classes.copy(), class_name, rendered)

    md += (f"<p>\n      <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new"
           f"?template=term_improvement.yaml&title=Term%20Feedback:%20{class_name}"
           f' target="_blank" class="md-button md-button--primary">\n'
           f"        💡 Submit Term Feedback\n      </a>\n    </p>")
    md += "</details>\n\n"
    return md


def format_slot_markdown(schema: dict, slot_name: str, slot_details: dict,
                         level: int = 3, processed_classes: Optional[Set[str]] = None,
                         parent_class: Optional[str] = None,
                         rendered: Optional[dict] = None) -> str:
    if processed_classes is None:
        processed_classes = set()
    if rendered is None:
        rendered = {}

    description = slot_details.get("description", "No description available")
    range_type  = slot_details.get("range", "string")
    slot_uri    = slot_details.get("slot_uri", "")
    unit        = slot_details.get("unit", {})

    cardinality = striped = ""
    if parent_class:
        cardinality = f" ({get_slot_cardinality(schema, parent_class, slot_name, slot_details)})"
        striped     = cardinality.replace("(", "").replace(")", "")

    open_attr = " open" if level == 3 else ""
    md  = f'<details markdown="1"{open_attr}>\n'
    md += f"<summary><strong>{snake_to_readable(slot_name)}</strong>{cardinality}</summary>\n\n"
    md += f"**Description:** {description}\n\n"
    md += f"**Data Type:** {range_type}\n\n"
    md += f"**Cardinality:** {striped}\n\n"
    if slot_uri:
        md += f"**CURIE:** [`{slot_uri}`]({expand_curie(schema, slot_uri)})\n\n"
    md += f"**Schema Reference:** [{slot_name}](./elements/slots/{slot_name}.md)\n\n"
    if unit and unit.get("ucum_code"):
        md += f"**Unit:** {unit['ucum_code']}\n\n"

    # If the range is a known schema class, expand it inline with all subclasses
    if is_class_in_schema(schema, range_type) and not is_mixin(schema, range_type):
        md += "**Data Type Class Details:**\n\n"
        md += format_class_markdown(schema, range_type, level, processed_classes, None, rendered)
        # Subclasses already fully rendered elsewhere on the page (tracked in
        # `rendered`) are skipped here -- re-listing them adds an "already
        # shown earlier" stub with nothing new to say. This matters for
        # self-referential relations (e.g. has_reaction_step: range
        # ChemicalReaction, whose only subclass is the page's own main class):
        # without this filter every such slot would print a "Possible
        # Subclasses" section whose sole entry immediately points back to the
        # top of the page.
        subclasses = [s for s in get_subclasses(schema, range_type) if s not in rendered]
        if subclasses:
            md += f"**Possible Subclasses / Enumerations of {snake_to_readable(range_type)}:**\n\n"
            for subclass in subclasses:
                if subclass not in processed_classes:
                    md += format_class_markdown(schema, subclass, level + 1,
                                                processed_classes, None, rendered)

    md += (f"<p>\n  <a href=https://github.com/nfdi4cat/CoreMeta4Cat/issues/new"
           f"?template=term_improvement.yaml&title=Term%20Feedback:%20{slot_name}"
           f' target="_blank" class="md-button md-button--primary">\n'
           f"    💡 Submit Term Feedback\n  </a>\n</p>")
    md += "</details>\n\n"
    return md

LEGEND = """\
<details markdown="1"><summary markdown="1"> **Legend** </summary>

- **Description:**A short description for Comprehension purposes

- **Data Type:** This specifies exactly what kind of information belongs in this field. Most simply, it could be a direct value, such as a number (float) or a piece of text (string). However, the Data Type can also point to another Class in the schema. When this happens, the field is not just a single value; it becomes a structured container. Designating a Class as the Data Type causes the field to contain a complete structured record, defined entirely by its own comprehensive collection of specific fields. Consequently, this allows for the systematic construction of complex data structures via organized, nested information layers within the broader schema architecture.

- **Cardinality:** This controls how many entries a specific data field must have. It defines if a field is required or optional, and whether it can accept a single value versus a list of multiple values.

- **CURIE:** A CURIE (Compact URI) is a short, easy-to-read reference that acts as a useful shortcut for a long, complex web address. Instead of seeing a full URL, you will see a two-part reference like gene:symbol, where the parts are separated by a colon. The first part is the prefix (a short code for the source website), and the second is the local identifier for the specific item. This structure is much easier to read and type, making the schema less cluttered and reducing errors. The full web link (URI) for the CURIE is always available if you click the provided link.

- **Schema Reference:** This link directs you to the complete, technical documentation for this part of the schema. This detailed view is generated automatically by LinkML's documentation tool and provides all underlying rules, data types, and complex relationships for expert users and developers.

- **Slots:** A Slot represents an individual data field or attribute that belongs to a specific Class (entity type) within the schema. If a Class defines an entity like 'Book', the Slots define the individual pieces of information about that book, such as the 'title', 'author', and 'ISBN'. Essentially, Slots are the essential building blocks that define the characteristics and permissible data for every record in the schema.

- **Enumerations:** Often called an Enum, Enumerations are a predefined, fixed list of permissible values that a Slot can accept. It is used to strictly limit the available choices for a data field to ensure consistency and prevent errors. For example, a 'Status' field might be restricted to the Enumeration list of only 'Active', 'Inactive', or 'Pending'. Any data entered that is not on this limited list is considered invalid by the schema.

</details>"""

# Maps schema class names to their simplified display names used in documentation.
# Needed where the schema uses a fully qualified name to avoid clashes with
# identically named classes in top-level profiles (e.g. chemdcat-ap).
DISPLAY_NAMES: dict[str, str] = {
    "CatalyticReaction": "Reaction",
}

# ── Per-class introductory text shown below the page title ────────────────────
# Edit these strings to replace the placeholder "test description" sections.
# Keys must match the schema class name (not the display name).
CLASS_DESCRIPTIONS: dict = {
    "Synthesis":          """The Synthesis data class captures metadata required to document catalyst preparation procedures in a structured and reproducible manner. It defines the minimum information necessary to describe synthesis routes and their relevant parameters.

Metadata are organized hierarchically based on the selected synthesis method. Method-specific child fields are activated depending on the preparation approach (e.g., co-precipitation requiring fields such as precipitating agent, synthesis pH, aging time, and aging temperature). In addition, method-independent fields—such as precursor identity, precursor quantity, and storage conditions—are included to ensure consistent documentation across synthesis strategies.
""",
    "Characterization":   """The Characterization data class documents experimental techniques used to determine structural, electronic, compositional, and physicochemical properties of catalysts. It captures both measurement parameters and relevant contextual information required for interpretation and comparison.

The class follows a hierarchical structure in which selection of a characterization technique activates technique-specific metadata fields (e.g., radiation source for X-ray diffraction or solvent for nuclear magnetic resonance spectroscopy). Metadata on sample preparation and pre-treatment are also included, as these factors directly influence measurement outcomes.""",
    "CatalyticReaction":  """The Reaction data class defines metadata required to document catalytic testing procedures, reactor configurations, operating conditions, and analytical methods. It provides structured descriptors necessary to contextualize catalytic performance data.

Core fields include reactor design type, operational parameters, and product identification and quantification methods. The class also specifies metadata required to report and evaluate catalyst performance metrics, enabling structured comparison across experimental studies.""",
    "Simulation":         """The Simulation data class captures metadata describing theoretical and computational studies in catalysis. It documents methodological background, computational settings, and modeling approaches required to interpret simulation results.

Computational approaches are organized under the parent field simulation method, which includes techniques such as density functional theory, molecular dynamics, microkinetic modeling, and Monte Carlo simulations. Selection of a specific method activates the corresponding method-specific metadata fields necessary to describe model setup and computational parameters.""",
}


def generate_markdown_for_main_class(schema: dict, main_class: str, output_file: str):
    classes        = schema.get("classes", {})
    main_class_def = classes.get(main_class, {})
    class_uri      = main_class_def.get("class_uri", "")
    is_abstract    = main_class_def.get("abstract", False)

    display_name = DISPLAY_NAMES.get(main_class, main_class)
    description  = CLASS_DESCRIPTIONS.get(main_class, "test description")
    md  = f"# {snake_to_readable(display_name)}\n\n"

    # Warning admonition for classes whose schema name differs from the display name
    if main_class != display_name:
        md += (f'!!! note "Schema class name"\n'
               f'    In the CoreMeta4Cat schema this class is named **`{main_class}`** '
               f'(not `{display_name}`) to avoid name conflicts with identically named '
               f'classes in top-level profiles such as chemdcat-ap. '
               f'The simplified name **{display_name}** is used throughout this documentation '
               f'for readability. When writing data files or referencing the class programmatically, '
               f'always use the full schema name `{main_class}`.\n\n')

    md += f"{description}\n\n"

    if is_abstract:
        md += "**Abstract Class**\n\n"
    if class_uri:
        md += f"**CURIE:** [`{class_uri}`]({class_uri})\n\n"

    md += (f'<iframe\n    src="../assets/metadata_{display_name.lower()}_hierarchy.html"\n'
           f'    width="100%"\n    height= "470vh"\n'
           f'    style="border: 2px solid #5C88DA; background-color: #F0F8FF;\n    "\n'
           f'    allowfullscreen\n></iframe>')

    # Slots section: direct/mixin slots first, then class-ranged slot_usage entries
    direct_slots    = get_all_class_slots(schema, main_class)
    class_ranged_su = get_class_ranged_slot_usage(schema, main_class, exclude=set(direct_slots))

    if direct_slots or class_ranged_su:
        md += LEGEND + "\n## Slots\n\n"
        processed: Set[str] = set()
        # Page-wide dedup map, shared across every slot on this page. Pre-seed
        # with main_class itself pointing at the page title -- otherwise a
        # self-referential slot (e.g. CatalyticReaction's inherited
        # has_reaction_step: range ChemicalReaction, whose own subclasses
        # include CatalyticReaction) would fully re-render this entire page
        # nested inside itself.
        rendered: dict = {main_class: display_name.lower().replace(" ", "-")}
        for slot_name in direct_slots:
            md += format_slot_markdown(schema, slot_name,
                                       get_slot_details(schema, slot_name),
                                       3, processed.copy(), main_class, rendered)
        for slot_name, synthetic in class_ranged_su:
            md += format_slot_markdown(schema, slot_name, synthetic,
                                       3, processed.copy(), main_class, rendered)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  OK {output_file}")



# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main(schema_dir: str, output_dir: str = "."):
    print(f"\nLoading CoreMeta4Cat modules from: {schema_dir}")
    schema = load_merged_schema(schema_dir)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    main_classes = {
        "Synthesis":         "synthesis.md",
        "Characterization":  "characterization.md",
        "CatalyticReaction": "reaction.md",
        "Simulation":        "simulation.md",
    }

    print(f"Generating Markdown docs in: {output_dir}")
    for main_class, filename in main_classes.items():
        generate_markdown_for_main_class(schema, main_class, str(output_path / filename))

    print(f"\nDone -- {len(main_classes)} files written to '{output_dir}'.")


if __name__ == "__main__":
    schema_dir = str(_ROOT / "src" / "coremeta4cat" / "schema")
    output_dir = str(_ROOT / "docs")
    main(schema_dir, output_dir)
