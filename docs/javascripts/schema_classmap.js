/*
 * Interactive class map for the CoreMeta4Cat documentation.
 *
 * Renders into every
 *   <div class="cm4c-classmap" data-root="Simulation" data-src="../assets/schema_graph.json"
 *        data-site="../" data-elements="../elements/classes/"
 *        [data-sunburst="../assets/metadata_simulation_hierarchy.html"] [data-mode="overview"]>
 * The data-class pages are written by scripts/generate_schema_docs.py; the
 * data itself comes from scripts/schema_graph.py.
 *
 * Class map (default): one class is in focus at a time and drawn as a
 * UML-style box. Its origin or users are on the left, its fields in the
 * middle, the classes it points to on the right (each drawn once). A class
 * that comes in several types gets a type list to switch between them in place.
 * With data-sunburst set, a switch above the diagram swaps in the sunburst
 * chart produced by scripts/generate_charts.py.
 *
 * Overview (data-mode="overview"): a fixed, reduced view of one class in which
 * stand-in and generic classes are replaced by the specific CoreMeta4Cat
 * classes; the data classes link to their own pages.
 */
(function () {
  "use strict";

  const PRIMITIVE = {
    string: "text", str: "text", float: "number", double: "number", decimal: "number",
    integer: "whole number", date: "date", datetime: "date and time", boolean: "yes / no",
    uri: "link or identifier", uriorcurie: "link or identifier",
  };
  const REQUIREMENT = { M: "mandatory", R: "recommended", O: "optional" };
  const CARDINALITY = {
    M1: "mandatory, exactly one", "M*": "mandatory, one or more",
    R1: "recommended, at most one", "R*": "recommended, any number",
    O1: "optional, at most one", "O*": "optional, any number",
  };
  const SVG_NS = "http://www.w3.org/2000/svg";
  const FILTER_FROM = 10;   // show a filter box in type lists longer than this
  const GROUP_OPEN_MAX = 3; // used-by groups up to this size are listed directly
  const VIEW_KEY = "cm4c-diagram-view";
  let uid = 0;

  const multiplicity = f => `[${f.requirement === "M" ? 1 : 0}..${f.multivalued ? "*" : 1}]`;
  const cardinalityText = f => CARDINALITY[f.requirement + (f.multivalued ? "*" : "1")];
  const words = s => s.replace(/_/g, " ");
  const plural = (n, word) => `${n} ${n === 1 ? word : word + (/(s|x|ch|sh)$/.test(word) ? "es" : "s")}`;
  const humanName = s => s.replace(/([a-z])([A-Z])/g, "$1 $2").replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2");
  const joinOr = list => (list.length < 2 ? list.join("") : `${list.slice(0, -1).join(", ")} or ${list[list.length - 1]}`);

  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function activate(node, fn) {
    node.tabIndex = 0;
    node.setAttribute("role", "button");
    node.addEventListener("click", fn);
    node.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); fn(); } });
  }

  // A button with a caret that shows or hides `list`; redraws the connector lines afterwards.
  function disclosure(text, list) {
    const button = el("button", "cm4c-toggle");
    button.type = "button";
    button.setAttribute("aria-expanded", "false");
    button.append(el("span", null, text), el("span", "cm4c-caret", "▾"));
    list.hidden = true;
    button.addEventListener("click", e => {
      e.stopPropagation();
      list.hidden = !list.hidden;
      button.setAttribute("aria-expanded", String(!list.hidden));
      const stage = button.closest(".cm4c-stage");
      if (stage) requestAnimationFrame(() => drawLinks(stage));
    });
    return button;
  }

  const store = {
    get(key) { try { return window.localStorage.getItem(key); } catch (e) { return null; } },
    set(key, value) { try { window.localStorage.setItem(key, value); } catch (e) { /* private mode */ } },
  };

  const requests = {};
  function load(src) {
    if (!requests[src]) {
      requests[src] = fetch(src).then(r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      });
      requests[src].catch(() => { delete requests[src]; });
    }
    return requests[src];
  }

  /* ---------- pieces shared by both views ---------- */

  function context(host, stage, graph, paletteKey) {
    const CL = graph.classes;
    return {
      host, stage, graph, CL,
      elements: host.dataset.elements || "",
      palette: graph.colors[paletteKey] || { M: "#555", R: "#888", O: "#bbb" },
      label: n => humanName(CL[n] ? CL[n].label : n),
      fieldCount: n => (CL[n] ? CL[n].fields.length : 0),
      opens: t => !!t && (t.kind === "struct" || t.kind === "choice"),
      page: n => (graph.pages && graph.pages[n] ? (host.dataset.site || "") + graph.pages[n] : null),
    };
  }

  // Allowed values: a button that unfolds a wrapping list under the row.
  function enumControl(ctx, f) {
    const values = ctx.graph.enums[f.range] || [];
    const list = el("ul", "cm4c-enum");
    list.setAttribute("aria-label", `Allowed values of ${words(f.name)}`);
    values.forEach(v => list.appendChild(el("li", null, words(v))));
    return { control: disclosure(plural(values.length, "allowed value"), list), extra: list };
  }

  function valueCell(ctx, f, focus) {
    const w = el("div", "cm4c-value");
    let extra = null;
    const t = ctx.CL[f.range];
    const box = (txt, cls) => w.appendChild(el("span", "cm4c-vbox" + (cls ? " " + cls : ""), txt));
    const unitBox = () => box(f.unit || "unit", f.unit ? "cm4c-unit cm4c-set" : "cm4c-unit");
    const caption = txt => w.appendChild(el("span", "cm4c-cap", txt));
    if (f.targets) {
      w.appendChild(el("span", "cm4c-type cm4c-link", joinOr(f.targets.map(ctx.label)) + " →"));
    } else if (f.kind === "primitive") {
      if (f.unit) { box(PRIMITIVE[f.range] || f.range); unitBox(); }
      else w.appendChild(el("span", "cm4c-type", PRIMITIVE[f.range] || f.range));
    } else if (f.kind === "enum") {
      const e = enumControl(ctx, f);
      w.appendChild(e.control);
      extra = e.extra;
    } else if (t && t.kind === "quantity") {
      box("value"); unitBox(); caption(ctx.label(f.range).toLowerCase());
    } else if (t && t.kind === "range") {
      box("min"); w.appendChild(el("span", "cm4c-dash", "–")); box("max"); unitBox(); caption("range with one unit");
    } else if (t && t.kind === "term") {
      w.appendChild(el("span", "cm4c-type", "term: " + ctx.label(f.range).toLowerCase()));
    } else if (ctx.opens(t)) {
      const self = f.range === focus;
      w.appendChild(el("span", "cm4c-type" + (self ? "" : " cm4c-link"), ctx.label(f.range) + (self ? " (this class)" : " →")));
    } else {
      w.appendChild(el("span", "cm4c-type", ctx.label(f.range)));
    }
    return { cell: w, extra };
  }

  function fieldRow(ctx, f, focus) {
    const r = el("div", "cm4c-row");
    const dot = el("span", "cm4c-dot");
    dot.style.background = ctx.palette[f.requirement];
    dot.title = REQUIREMENT[f.requirement];
    const name = el("div", "cm4c-name");
    name.appendChild(el("span", null, words(f.name)));
    const card = el("span", "cm4c-card");
    card.appendChild(el("b", null, multiplicity(f)));
    card.appendChild(document.createTextNode(cardinalityText(f)));
    name.appendChild(card);
    const { cell, extra } = valueCell(ctx, f, focus);
    r.append(dot, name, cell);
    if (extra) r.appendChild(extra);
    if (f.description) r.title = f.description;
    return r;
  }

  function legend(ctx) {
    const box = el("div", "cm4c-legend");
    [["[1..1]", "mandatory, exactly one"], ["[1..*]", "mandatory, one or more"],
     ["[0..1]", "optional or recommended, at most one"], ["[0..*]", "optional or recommended, any number"]]
      .forEach(([m, t]) => { const d = el("div"); d.appendChild(el("b", null, m)); d.appendChild(document.createTextNode(t)); box.appendChild(d); });
    const dots = el("div", "cm4c-dots");
    ["M", "R", "O"].forEach(k => {
      const s = el("span");
      const d = el("span", "cm4c-dot");
      d.style.background = ctx.palette[k];
      s.append(d, document.createTextNode(REQUIREMENT[k]));
      dots.appendChild(s);
    });
    box.appendChild(dots);
    return box;
  }

  function focusHead(ctx, name, kind, description) {
    const head = el("div", "cm4c-head");
    head.appendChild(el("b", null, ctx.label(name)));
    if (kind) head.appendChild(el("small", null, kind));
    if (description) head.appendChild(el("p", null, description));
    if (ctx.elements) {
      const a = el("a", "cm4c-ref", "Schema reference");
      a.href = `${ctx.elements}${name}/`;
      head.appendChild(a);
    }
    return head;
  }

  function newMap() {
    const map = el("div", "cm4c-map");
    const svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("class", "cm4c-links");
    svg.setAttribute("aria-hidden", "true");
    map.appendChild(svg);
    return map;
  }

  // Rows carry data-targets="A B"; target boxes carry data-id="A".
  function highlight(stage, target, on) {
    stage.querySelectorAll(`.cm4c-row[data-targets~="${target}"]`).forEach(r => r.classList.toggle("cm4c-hl", on));
    stage.querySelectorAll(`.cm4c-links path[data-target="${target}"]`).forEach(p => p.classList.toggle("cm4c-hl", on));
    const b = stage.querySelector(`.cm4c-target[data-id="${target}"]`);
    if (b) b.classList.toggle("cm4c-hl", on);
  }

  function drawLinks(stage) {
    const svg = stage.querySelector(".cm4c-links");
    if (!svg || !svg.isConnected || stage.offsetParent === null || getComputedStyle(svg).display === "none") return;
    svg.innerHTML = "";
    const base = svg.getBoundingClientRect();
    const curve = (x1, y1, x2, y2, target) => {
      const p = document.createElementNS(SVG_NS, "path");
      const dx = Math.max(20, (x2 - x1) / 2);
      p.setAttribute("d", `M${x1},${y1} C${x1 + dx},${y1} ${x2 - dx},${y2} ${x2},${y2}`);
      if (target) p.dataset.target = target;
      svg.appendChild(p);
    };
    stage.querySelectorAll(".cm4c-row[data-targets]").forEach(r => {
      const a = r.getBoundingClientRect();
      r.dataset.targets.split(" ").forEach(id => {
        const tb = stage.querySelector(`.cm4c-target[data-id="${id}"]`);
        if (!tb) return;
        const b = tb.getBoundingClientRect();
        curve(a.right - base.left, a.top + 14 - base.top, b.left - base.left, b.top + 18 - base.top, id);
      });
    });
    const fb = stage.querySelector(".cm4c-focus");
    if (!fb) return;
    const f = fb.getBoundingClientRect();
    stage.querySelectorAll(".cm4c-user").forEach(u => {
      const a = u.getBoundingClientRect();
      // a group box: anchor at its heading, so the line stays put when the list unfolds
      const y = u.classList.contains("cm4c-group") ? a.top + 14 : a.top + a.height / 2;
      curve(a.right - base.left, y - base.top, f.left - base.left, f.top + 22 - base.top);
    });
  }

  function watchSize(stage) {
    if (!window.ResizeObserver) return;
    let frame = 0;
    new ResizeObserver(() => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => drawLinks(stage));
    }).observe(stage);
  }

  function wireHighlights(stage) {
    stage.querySelectorAll(".cm4c-row[data-targets]").forEach(r => {
      const ids = r.dataset.targets.split(" ");
      r.addEventListener("mouseenter", () => ids.forEach(id => highlight(stage, id, true)));
      r.addEventListener("mouseleave", () => ids.forEach(id => highlight(stage, id, false)));
    });
    stage.querySelectorAll(".cm4c-target[data-id]").forEach(b => {
      b.addEventListener("mouseenter", () => highlight(stage, b.dataset.id, true));
      b.addEventListener("mouseleave", () => highlight(stage, b.dataset.id, false));
    });
  }

  /* ---------- class map ---------- */

  function createClassMap(host, stage, graph) {
    const rootClass = host.dataset.root;
    const ctx = context(host, stage, graph, rootClass);
    const { CL, label } = ctx;
    const id = ++uid;

    // incoming references: class -> [{ from, field }]
    const usedBy = {};
    for (const [name, c] of Object.entries(CL)) {
      for (const f of c.fields) {
        if (f.kind === "class") (usedBy[f.range] ||= []).push({ from: name, field: f.name });
      }
    }

    // Focus and trail entries: { c: class shown, root: the class with several
    // types it was opened as (drives the type list), or null }.
    const state = { focus: null, trail: [], refocus: false };
    const current = () => state.focus || { c: rootClass, root: null };

    function nearestChoice(n) {
      for (let c = n, i = 0; c && CL[c] && i < 20; c = CL[c].is_a, i++) {
        if (CL[c].kind === "choice" && (c === n || CL[c].options.includes(n))) return c;
      }
      return null;
    }
    function depthBelow(o, root) {
      let d = 0;
      for (let c = o; c && c !== root && d < 20; c = CL[c] && CL[c].is_a) d++;
      return d;
    }

    // Going to a class already in the trail jumps back to it, so the trail never loops.
    function go(c, root) {
      const now = current();
      if (!CL[c] || c === now.c) return;
      const i = state.trail.findIndex(t => t.c === c);
      if (i >= 0) {
        state.focus = state.trail[i];
        state.trail = state.trail.slice(0, i);
      } else {
        state.trail.push(now);
        state.focus = { c, root: root !== undefined ? root : (c === rootClass ? null : nearestChoice(c)) };
      }
      render();
      if (host.getBoundingClientRect().top < 0) host.scrollIntoView({ block: "start" });
    }
    // Switching between the types of one class replaces the current step.
    function switchType(v) {
      const i = state.trail.findIndex(t => t.c === v);
      if (i >= 0) state.trail = state.trail.slice(0, i);
      state.focus = { c: v, root: current().root };
      state.refocus = true;
      render();
    }

    const crumbLabel = t => (t.root && t.c !== t.root ? `${label(t.root)}: ${label(t.c)}` : label(t.c));

    function kindText(n, root) {
      const c = CL[n];
      if (root && n !== root) return `one type of ${label(root).toLowerCase()} · ${plural(c.fields.length, "field")}`;
      if (n === rootClass && c.role) return `${humanName(c.role).toLowerCase()} · ${plural(c.fields.length, "field")}`;
      if (c.kind === "choice") {
        return `comes in ${c.options.length} types` + (c.fields.length ? ` · ${plural(c.fields.length, "shared field")}` : "");
      }
      if (c.kind === "struct") return plural(c.fields.length, "field");
      return "";
    }

    // The type list: a button showing the current type that unfolds a
    // wrapping, filterable list of all types (no native <select>, so long
    // names such as "High Performance Liquid Chromatography Mass
    // Spectrometry" are never cut off).
    function typePicker(root, focus) {
      const generic = `Generic ${label(root).toLowerCase()} (shared fields only)`;
      const v = el("div", "cm4c-variant");
      v.appendChild(el("span", "cm4c-variant-label", `Type of ${label(root).toLowerCase()}`));
      const button = el("button", "cm4c-picker");
      button.type = "button";
      button.setAttribute("aria-expanded", "false");
      button.setAttribute("aria-controls", `cm4c-types-${id}`);
      button.append(el("span", null, focus === root ? generic : label(focus)), el("span", "cm4c-caret", "▾"));
      const panel = el("div", "cm4c-picklist");
      panel.id = `cm4c-types-${id}`;
      panel.hidden = true;
      const options = [root, ...CL[root].options.filter(o => CL[o])];
      let filter = null;
      if (options.length > FILTER_FROM) {
        filter = el("input", "cm4c-filter");
        filter.type = "search";
        filter.placeholder = `Filter ${options.length - 1} types`;
        filter.setAttribute("aria-label", `Filter types of ${label(root).toLowerCase()}`);
        panel.appendChild(filter);
      }
      const list = el("div", "cm4c-picks");
      options.forEach(o => {
        const b = el("button", "cm4c-pick", o === root ? generic : label(o));
        b.type = "button";
        if (o !== root) b.style.paddingLeft = `${0.6 + Math.max(0, depthBelow(o, root) - 1)}em`;
        if (o !== root && !ctx.fieldCount(o)) b.appendChild(el("span", "cm4c-muted", " (no fields yet)"));
        if (o === focus) b.setAttribute("aria-current", "true");
        b.addEventListener("click", () => switchType(o));
        list.appendChild(b);
      });
      panel.appendChild(list);
      const open = on => {
        panel.hidden = !on;
        button.setAttribute("aria-expanded", String(on));
        if (on) (filter || list.querySelector("[aria-current]") || list.firstChild).focus();
      };
      button.addEventListener("click", () => open(panel.hidden));
      panel.addEventListener("keydown", e => { if (e.key === "Escape") { open(false); button.focus(); } });
      if (filter) {
        filter.addEventListener("input", () => {
          const q = filter.value.trim().toLowerCase();
          list.querySelectorAll(".cm4c-pick").forEach(b => { b.hidden = !!q && !b.textContent.toLowerCase().includes(q); });
        });
      }
      v.append(button, panel, el("small", null, `${CL[root].options.length} types. The fields below follow your choice.`));
      return v;
    }

    // One box per field that points at the focus: a single class is a plain
    // link box; several classes share one box with their names listed (or
    // folded away behind "N classes" when there are many).
    function userGroup(g) {
      const via = `via ${words(g.field)}` + (g.as ? ` (as ${label(g.as).toLowerCase()})` : "");
      if (g.classes.length === 1) {
        const b = el("div", "cm4c-box cm4c-user");
        activate(b, () => go(g.classes[0]));
        b.appendChild(document.createTextNode(label(g.classes[0])));
        b.appendChild(el("small", null, via));
        return b;
      }
      const b = el("div", "cm4c-box cm4c-user cm4c-group");
      b.appendChild(el("small", null, via));
      const list = el("div", "cm4c-members");
      g.classes.forEach(c => {
        const m = el("button", "cm4c-member", label(c));
        m.type = "button";
        m.addEventListener("click", () => go(c));
        list.appendChild(m);
      });
      if (g.classes.length > GROUP_OPEN_MAX) b.appendChild(disclosure(plural(g.classes.length, "class"), list));
      b.appendChild(list);
      return b;
    }

    function render() {
      const now = current();
      const focus = now.c;
      const c = CL[focus];
      const root = now.root;
      stage.innerHTML = "";

      // path
      const crumbs = el("nav", "cm4c-crumbs");
      crumbs.setAttribute("aria-label", "Class map path");
      [...state.trail, now].forEach((t, i, all) => {
        if (i) crumbs.appendChild(el("span", "cm4c-sep", "›"));
        if (i === all.length - 1) { crumbs.appendChild(el("b", null, crumbLabel(t))); return; }
        const b = el("button", null, crumbLabel(t));
        b.type = "button";
        b.addEventListener("click", () => {
          state.focus = state.trail[i];
          state.trail = state.trail.slice(0, i);
          render();
        });
        crumbs.appendChild(b);
      });
      stage.appendChild(crumbs);

      const map = newMap();

      // left: origin of a data class, or where the focused class is used
      const isRoot = focus === rootClass && !root;
      const L = el("div", "cm4c-col cm4c-left");
      if (isRoot) {
        const origins = (graph.origins && graph.origins[rootClass]) || [];
        if (origins.length) {
          L.appendChild(el("div", "cm4c-colhead", "Origin"));
          origins.forEach(o => {
            const href = ctx.page(o.class);
            const b = el(href ? "a" : "div", "cm4c-box cm4c-user" + (href ? "" : " cm4c-static"));
            if (href) b.href = href;
            b.appendChild(document.createTextNode(humanName(o.label)));
            b.appendChild(el("small", null, `via ${words(o.field)}` + (o.as ? ` (as ${label(o.as).toLowerCase()})` : "")));
            if (o.description) b.title = o.description;
            L.appendChild(b);
          });
        }
      } else {
        const groups = [];
        const byKey = new Map();
        const addUsers = (target, as) => (usedBy[target] || []).forEach(u => {
          if (u.from === focus) return;
          const key = `${u.field}|${as || ""}`;
          let g = byKey.get(key);
          if (!g) { g = { field: u.field, as, classes: [] }; byKey.set(key, g); groups.push(g); }
          if (!g.classes.includes(u.from)) g.classes.push(u.from);
        });
        if (root) addUsers(root, root !== focus ? root : null);
        addUsers(focus, null);
        if (groups.length) {
          L.appendChild(el("div", "cm4c-colhead", "Used by"));
          groups.forEach(g => L.appendChild(userGroup(g)));
        }
      }
      if (L.children.length) map.appendChild(L);
      else map.classList.add("cm4c-noleft");

      // centre: the focus box
      const M = el("div", "cm4c-col cm4c-center");
      M.appendChild(el("div", "cm4c-colhead", "Focus"));
      const box = el("div", "cm4c-box cm4c-focus");
      box.style.borderColor = ctx.palette.M;
      box.appendChild(focusHead(ctx, focus, kindText(focus, root), c.description));
      if (root) box.appendChild(typePicker(root, focus));

      const rows = el("div", "cm4c-rows");
      const addRow = f => {
        const r = fieldRow(ctx, f, focus);
        const t = CL[f.range];
        if (f.kind === "class" && ctx.opens(t) && f.range !== focus) {
          r.classList.add("cm4c-go");
          r.dataset.targets = f.range;
          activate(r, () => go(f.range, t.kind === "choice" ? f.range : null));
          r.setAttribute("aria-label", `${words(f.name)}: open ${label(f.range)}`);
        }
        rows.appendChild(r);
      };
      if (root && focus !== root && CL[root].fields.length) {
        const shared = new Set(CL[root].fields.map(f => f.name));
        const own = c.fields.filter(f => !shared.has(f.name));
        const common = c.fields.filter(f => shared.has(f.name));
        if (own.length) {
          rows.appendChild(el("div", "cm4c-sub", `Specific to ${label(focus).toLowerCase()}`));
          own.forEach(addRow);
        }
        if (common.length) {
          rows.appendChild(el("div", "cm4c-sub", `Shared by every ${label(root).toLowerCase()}`));
          common.forEach(addRow);
        }
      } else {
        c.fields.forEach(addRow);
      }
      if (!c.fields.length) rows.appendChild(el("p", "cm4c-muted cm4c-pad", "No fields defined yet."));
      box.appendChild(rows);
      M.append(box, legend(ctx));
      map.appendChild(M);

      // right: linked classes, each drawn once
      const R = el("div", "cm4c-col cm4c-right");
      R.appendChild(el("div", "cm4c-colhead", "Points to"));
      const targets = [...new Set(c.fields
        .filter(f => f.kind === "class" && f.range !== focus && ctx.opens(CL[f.range]))
        .map(f => f.range))];
      targets.forEach(tn => {
        const t = CL[tn];
        const b = el("div", "cm4c-box cm4c-target");
        activate(b, () => go(tn, t.kind === "choice" ? tn : null));
        b.dataset.id = tn;
        const h = el("div", "cm4c-head");
        h.appendChild(el("b", null, label(tn)));
        const k = kindText(tn, null);
        if (k) h.appendChild(el("small", null, k));
        b.appendChild(h);
        if (t.fields.length) {
          b.appendChild(el("p", "cm4c-muted cm4c-pad",
            t.fields.slice(0, 5).map(f => words(f.name)).join(", ") + (t.fields.length > 5 ? " …" : "")));
        }
        R.appendChild(b);
      });
      if (!targets.length) R.appendChild(el("p", "cm4c-muted", "Only plain values here. Nothing further to open."));
      map.appendChild(R);

      stage.appendChild(map);
      wireHighlights(stage);
      if (state.refocus) {
        state.refocus = false;
        const p = stage.querySelector(".cm4c-picker");
        if (p) p.focus();
      }
      requestAnimationFrame(() => drawLinks(stage));
    }

    watchSize(stage);
    render();
  }

  /* ---------- overview ---------- */

  function createOverview(host, stage, graph) {
    const name = host.dataset.root;
    const ov = graph.overviews[name];
    const ctx = context(host, stage, graph, name);
    const { CL, label } = ctx;
    stage.innerHTML = "";

    const map = newMap();
    map.classList.add("cm4c-noleft");

    const M = el("div", "cm4c-col cm4c-center");
    M.appendChild(el("div", "cm4c-colhead", "Entry point"));
    const box = el("div", "cm4c-box cm4c-focus");
    box.style.borderColor = ctx.palette.M;
    const kind = (ov.role ? `${humanName(ov.role).toLowerCase()} · ` : "") + plural(ov.fields.length, "CoreMeta4Cat field");
    box.appendChild(focusHead(ctx, name, kind, ov.description));
    const rows = el("div", "cm4c-rows");
    ov.fields.forEach(f => {
      const r = fieldRow(ctx, f.targets && f.targets.length ? f : { ...f, targets: undefined }, name);
      if (f.targets && f.targets.length) r.dataset.targets = f.targets.join(" ");
      rows.appendChild(r);
    });
    box.appendChild(rows);
    M.append(box, legend(ctx));
    map.appendChild(M);

    const R = el("div", "cm4c-col cm4c-right");
    R.appendChild(el("div", "cm4c-colhead", "Points to"));
    [...new Set(ov.fields.flatMap(f => f.targets || []))].forEach(tn => {
      const t = CL[tn];
      const href = ctx.page(tn);
      const b = el(href ? "a" : "div", "cm4c-box cm4c-target" + (href ? "" : " cm4c-static"));
      if (href) b.href = href;
      b.dataset.id = tn;
      const colour = graph.colors[tn];
      if (colour) b.style.borderLeft = `4px solid ${colour.M}`;
      const h = el("div", "cm4c-head");
      h.appendChild(el("b", null, label(tn)));
      if (t) {
        h.appendChild(el("small", null, (t.role ? `${humanName(t.role).toLowerCase()} · ` : "") + plural(t.fields.length, "field")));
      }
      b.appendChild(h);
      if (t && t.description) b.appendChild(el("p", "cm4c-muted cm4c-pad", t.description));
      if (href) b.appendChild(el("span", "cm4c-open", `Open the ${label(tn)} page →`));
      R.appendChild(b);
    });
    map.appendChild(R);

    stage.appendChild(map);
    wireHighlights(stage);
    watchSize(stage);
    requestAnimationFrame(() => drawLinks(stage));
  }

  /* ---------- class map / sunburst switch ---------- */

  // Adds "Class map | Sunburst chart" above the diagram. The chart page is
  // only loaded when first asked for; switching back keeps the class map as
  // it was. The choice is remembered for the next page.
  function addViewSwitch(host, stage) {
    const bar = el("div", "cm4c-views");
    bar.setAttribute("role", "group");
    bar.setAttribute("aria-label", "Diagram");
    const chart = el("div", "cm4c-chart");
    chart.hidden = true;
    const buttons = {};
    const show = view => {
      stage.hidden = view !== "map";
      chart.hidden = view !== "sunburst";
      Object.entries(buttons).forEach(([v, b]) => b.setAttribute("aria-pressed", String(v === view)));
      if (view === "sunburst" && !chart.firstChild) {
        const frame = el("iframe");
        frame.src = host.dataset.sunburst;
        frame.title = `Sunburst chart of the ${humanName(host.dataset.root)} fields`;
        chart.appendChild(frame);
      }
      if (view === "map") requestAnimationFrame(() => drawLinks(stage));
    };
    [["map", "Class map"], ["sunburst", "Sunburst chart"]].forEach(([view, text]) => {
      const b = el("button", null, text);
      b.type = "button";
      b.addEventListener("click", () => { show(view); store.set(VIEW_KEY, view); });
      buttons[view] = b;
      bar.appendChild(b);
    });
    host.insertBefore(bar, stage);
    host.appendChild(chart);
    show(store.get(VIEW_KEY) === "sunburst" ? "sunburst" : "map");
  }

  /* ---------- mounting ---------- */

  function mount(host) {
    if (host.dataset.cm4cMounted) return;
    host.dataset.cm4cMounted = "1";
    if (!host.dataset.src) return;
    const overview = host.dataset.mode === "overview";
    load(host.dataset.src)
      .then(graph => {
        const known = overview ? graph.overviews && graph.overviews[host.dataset.root] : graph.classes[host.dataset.root];
        if (!known) throw new Error(`unknown class ${host.dataset.root}`);
        host.innerHTML = "";
        const stage = el("div", "cm4c-stage");
        host.appendChild(stage);
        (overview ? createOverview : createClassMap)(host, stage, graph);
        if (!overview && host.dataset.sunburst) addViewSwitch(host, stage);
      })
      .catch(err => {
        host.textContent = `The class map could not be loaded (${err.message}).`;
      });
  }

  function init() { document.querySelectorAll(".cm4c-classmap").forEach(mount); }

  // Material for MkDocs swaps pages without a reload (navigation.instant) and
  // announces each new page on document$; fall back to a plain page load.
  if (window.document$ && typeof window.document$.subscribe === "function") window.document$.subscribe(init);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
