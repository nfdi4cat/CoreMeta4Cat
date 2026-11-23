/*
 * Version selector for pull-request previews of the documentation.
 *
 * deploy_docs_preview.yaml publishes each PR's docs under
 *   <site>/pr-preview/pr-<number>/
 * Material looks for versions.json one folder above the site it is showing,
 * i.e. <site>/pr-preview/versions.json, finds nothing there and leaves the
 * version selector out. On a preview, this script draws Material's selector
 * from the real <site>/versions.json that mike maintains instead. Picking a
 * version leaves the preview for the published docs (the same page if that
 * version has it, otherwise the version's start page). The published docs
 * never list previews, so it is a one-way trip.
 *
 * On the published docs (any path without /pr-preview/pr-<number>/) this
 * script does nothing.
 */
(function () {
  "use strict";

  const match = window.location.pathname.match(/^(.*\/)pr-preview\/pr-(\d+)\//);
  if (!match) return;

  const siteRoot = new URL(match[1], window.location.origin);
  const previewRoot = new URL(`${match[1]}pr-preview/pr-${match[2]}/`, window.location.origin);
  const currentLabel = `PR #${match[2]} preview`;
  let versions = null;

  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  // Go to the same page in the chosen version if it exists there, else to
  // the version's start page (a page may be new in this PR).
  async function open(versionRoot) {
    const page = window.location.pathname.startsWith(previewRoot.pathname)
      ? window.location.pathname.slice(previewRoot.pathname.length)
      : "";
    const target = new URL(page + window.location.hash, versionRoot);
    try {
      const response = await fetch(target, { method: "HEAD" });
      window.location.href = response.ok ? target.href : versionRoot.href;
    } catch (e) {
      window.location.href = versionRoot.href;
    }
  }

  // Same markup as Material's own selector, so its styles and hover menu apply.
  function render() {
    const topic = document.querySelector(".md-header__topic");
    if (!versions || !versions.length || !topic || topic.querySelector(".md-version")) return;
    const box = el("div", "md-version");
    const current = el("button", "md-version__current", currentLabel);
    current.setAttribute("aria-label", "Select version");
    const list = el("ul", "md-version__list");
    versions
      .filter(v => !(v.properties && v.properties.hidden))
      .forEach(v => {
        const versionRoot = new URL(`${v.version}/`, siteRoot);
        const item = el("li", "md-version__item");
        const link = el("a", "md-version__link", v.title || v.version);
        link.href = versionRoot.href;
        // as on the published docs (mkdocs.yml: extra.version.alias)
        if (v.aliases && v.aliases.length) link.appendChild(el("span", "md-version__alias", v.aliases[0]));
        link.addEventListener("click", event => {
          event.preventDefault();
          open(versionRoot);
        });
        item.appendChild(link);
        list.appendChild(item);
      });
    box.append(current, list);
    topic.appendChild(box);
  }

  fetch(new URL("versions.json", siteRoot))
    .then(response => (response.ok ? response.json() : []))
    .then(data => {
      versions = Array.isArray(data) ? data : [];
      render();
    })
    .catch(() => { /* no published versions reachable: leave the header as it is */ });

  // Material swaps pages without a reload and may redraw the header.
  if (window.document$ && typeof window.document$.subscribe === "function") window.document$.subscribe(render);
  else document.addEventListener("DOMContentLoaded", render);
})();
