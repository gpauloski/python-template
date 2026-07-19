---
name: add-docs-page
description: Scaffold a new MkDocs documentation page and wire it into the navigation. Use when asked to "add a docs page", "add a guide", or "document" a feature in the site.
---

# Add a docs page

API reference pages are auto-generated from docstrings by
`docs/generate_api.py`; do not create those by hand. Use this for narrative
pages (guides, overviews, etc.).

1. Create the Markdown file under `docs/` (group guides under `docs/guides/`).
   Follow the tone/format of existing pages such as `docs/guides/example.md`.
2. Add the page to the `nav:` tree in `mkdocs.yml` under the appropriate
   section, e.g.:
   ```yaml
   - Guides:
       - guides/index.md
       - My Feature: guides/my-feature.md
   ```
3. Cross-reference symbols with mkdocstrings autorefs (e.g. `[pypkg.foo.bar][]`)
   where helpful.
4. Build with strict mode to catch broken links and nav issues:
   ```bash
   uv sync --group docs
   mkdocs serve                   # preview locally
   tox -e docs                    # strict build (must pass)
   ```
