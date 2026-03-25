"""
generate_charts.py

Generates Plotly sunburst hierarchy charts for the four CoreMeta4Cat data
classes (Synthesis, Characterization, Reaction, Simulation) directly from the
merged LinkML schema.

Output files (written to docs/assets/):
  metadata_synthesis_hierarchy.html
  metadata_characterization_hierarchy.html
  metadata_reaction_hierarchy.html
  metadata_simulation_hierarchy.html

These files are embedded as iframes in the schema documentation pages
produced by generate_schema_docs.py.

Run:
    just gen-charts
  or directly:
    uv run python scripts/generate_charts.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

import plotly.express as px
from plotly.io import to_html

# ── locate project root and import shared schema loader ──────────────────────
_HERE = Path(__file__).parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_HERE))

from generate_schema_docs import (  # noqa: E402
    get_all_class_slots,
    get_class_ranged_slot_usage,
    get_slot_details,
    get_subclasses,
    is_mixin,
    load_merged_schema,
)

# ─────────────────────────────────────────────────────────────────────────────
# Visual design — matches the original Excel-based charts
# ─────────────────────────────────────────────────────────────────────────────

BASE_COLORS: dict[str, dict[str, str]] = {
    "synthesis":        {"M": "#d73027", "R": "#f46d43", "O": "#fdae61"},
    "characterization": {"M": "#4575b4", "R": "#74add1", "O": "#abd9e9"},
    "reaction":         {"M": "#1a9850", "R": "#66bd63", "O": "#a6d96a"},
    "simulation":       {"M": "#984ea3", "R": "#b358cb", "O": "#e082ea"},
    "coremeta4cat":     {"M": "#e66101", "R": "#fdb863", "O": "#fddbc7"},
}

# ─────────────────────────────────────────────────────────────────────────────
# M / R / O classification
# ─────────────────────────────────────────────────────────────────────────────

def _slot_mro(schema: dict, class_name: str, slot_name: str) -> str:
    """Return 'M', 'R', or 'O' for a slot within a given class context."""
    class_def = schema.get("classes", {}).get(class_name, {})
    usage = (class_def.get("slot_usage") or {}).get(slot_name) or {}
    slot_def = get_slot_details(schema, slot_name)

    required    = usage.get("required",    slot_def.get("required",    False))
    recommended = usage.get("recommended", slot_def.get("recommended", False))

    if required:
        return "M"
    if recommended:
        return "R"
    return "O"


# ─────────────────────────────────────────────────────────────────────────────
# Tree builder
# ─────────────────────────────────────────────────────────────────────────────

def _add_node(
    ids: list, names: list, parents: list, colors: list, hover: list,
    node_id: str, label: str, parent_id: str, color: str, hover_text: str,
) -> None:
    ids.append(node_id)
    names.append(label)
    parents.append(parent_id)
    colors.append(color)
    hover.append(hover_text)


def _build_tree_for_class(
    schema: dict,
    class_name: str,
    parent_id: str,
    ids: list,
    names: list,
    parents: list,
    colors: list,
    hover: list,
    color_map: dict[str, str],
    context_class: str,
    seen_classes: Optional[set] = None,
    depth: int = 0,
) -> None:
    """
    Recursively add schema slots (and their sub-classes) as sunburst nodes.
    Each slot becomes a node whose colour reflects its M/R/O status.
    If a slot's range is another schema class, that class's own slots are
    added as children, preserving the visual nesting of the original charts.
    """
    if seen_classes is None:
        seen_classes = set()
    if class_name in seen_classes or depth > 6:
        return
    seen_classes = seen_classes | {class_name}

    classes = schema.get("classes", {})

    # Direct and mixin-inherited slots
    direct_slots = get_all_class_slots(schema, class_name)
    for slot_name in direct_slots:
        mro = _slot_mro(schema, context_class if depth == 0 else class_name, slot_name)
        color = color_map.get(mro, "#dddddd")
        slot_id = f"{parent_id}|{slot_name}"
        slot_def = get_slot_details(schema, slot_name)
        range_type = slot_def.get("range", "")
        _add_node(ids, names, parents, colors, hover,
                  slot_id, slot_name.replace("_", " "), parent_id, color,
                  f"{slot_name} ({mro})")

        # If this slot points to a schema class, recurse into it
        if range_type and range_type in classes and not is_mixin(schema, range_type):
            _build_tree_for_class(
                schema, range_type, slot_id,
                ids, names, parents, colors, hover,
                color_map, context_class, seen_classes, depth + 1,
            )
            # Also expand any subclasses of the range class
            for sub in get_subclasses(schema, range_type):
                sub_id = f"{slot_id}|{sub}"
                sub_color = color_map.get(mro, "#dddddd")
                _add_node(ids, names, parents, colors, hover,
                          sub_id, sub.replace("_", " "), slot_id, sub_color,
                          f"{sub} (subclass of {range_type})")
                _build_tree_for_class(
                    schema, sub, sub_id,
                    ids, names, parents, colors, hover,
                    color_map, context_class, seen_classes | {range_type}, depth + 2,
                )

    # class-ranged slot_usage entries (gateway slots like realized_plan, had_input_entity)
    for su_name, synthetic in get_class_ranged_slot_usage(schema, class_name):
        if su_name in direct_slots:
            continue  # already handled above
        rng = synthetic.get("range", "")
        mro = _slot_mro(schema, class_name, su_name)
        color = color_map.get(mro, "#dddddd")
        su_id = f"{parent_id}|{su_name}"
        _add_node(ids, names, parents, colors, hover,
                  su_id, su_name.replace("_", " "), parent_id, color,
                  f"{su_name} ({mro})")
        if rng and rng in classes and not is_mixin(schema, rng):
            _build_tree_for_class(
                schema, rng, su_id,
                ids, names, parents, colors, hover,
                color_map, class_name, seen_classes, depth + 1,
            )
            for sub in get_subclasses(schema, rng):
                sub_id = f"{su_id}|{sub}"
                sub_color = color_map.get(mro, "#dddddd")
                _add_node(ids, names, parents, colors, hover,
                          sub_id, sub.replace("_", " "), su_id, sub_color,
                          f"{sub} (subclass of {rng})")
                _build_tree_for_class(
                    schema, sub, sub_id,
                    ids, names, parents, colors, hover,
                    color_map, class_name, seen_classes | {rng}, depth + 2,
                )


# ─────────────────────────────────────────────────────────────────────────────
# Chart generation
# ─────────────────────────────────────────────────────────────────────────────

def build_sunburst_chart(schema: dict, class_name: str) -> str:
    """Return standalone HTML for one sunburst chart."""
    key = class_name.lower()
    color_map = BASE_COLORS.get(key, BASE_COLORS["coremeta4cat"])

    ids:     list[str] = []
    names:   list[str] = []
    parents: list[str] = []
    colors:  list[str] = []
    hover:   list[str] = []

    # Root node
    root_color = color_map["M"]
    _add_node(ids, names, parents, colors, hover,
              class_name, class_name, "", root_color, f"Data class: {class_name}")

    _build_tree_for_class(
        schema, class_name, class_name,
        ids, names, parents, colors, hover,
        color_map, class_name,
    )

    fig = px.sunburst(ids=ids, names=names, parents=parents, hover_name=hover)
    fig.update_traces(marker=dict(colors=colors))
    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10), autosize=True)

    chart_html = to_html(
        fig,
        full_html=False,
        include_plotlyjs=False,
        config={"responsive": True},
    )

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8'>
  <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
  <style>
    html, body {{
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
    }}
    .chart-container {{
        width: 100%;
        height: 100vh;
    }}
  </style>
</head>
<body>
<div class="chart-container">
{chart_html}
</div>
</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main(schema_dir: str, output_dir: str) -> None:
    print(f"\nLoading CoreMeta4Cat modules from: {schema_dir}")
    schema = load_merged_schema(schema_dir)

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    main_classes = ["Synthesis", "Characterization", "Reaction", "Simulation"]
    print(f"Generating sunburst charts in: {output_dir}")
    for cls in main_classes:
        html = build_sunburst_chart(schema, cls)
        dest = out / f"metadata_{cls.lower()}_hierarchy.html"
        dest.write_text(html, encoding="utf-8")
        print(f"  OK {dest}")

    print(f"\nDone -- {len(main_classes)} charts written to '{output_dir}'.")


if __name__ == "__main__":
    schema_dir = str(_ROOT / "src" / "coremeta4cat" / "schema")
    output_dir = str(_ROOT / "docs" / "assets")
    main(schema_dir, output_dir)
