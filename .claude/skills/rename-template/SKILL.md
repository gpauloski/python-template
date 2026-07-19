---
name: rename-template
description: Replace the template placeholders (foobar, foobar-author, gpauloski/python-template) when starting a new project from this template. Use when asked to "rename the template", "set up a new project", or "replace foobar".
---

# Rename template placeholders

The template uses placeholders that must be replaced for a new project. Ask the
user for their values first if not provided:

- `foobar` — the Python package/import name (e.g. `mypkg`).
- `foobar-author` — the GitHub org/user or author handle.
- `gpauloski/python-template` — the new `owner/repo` slug.
- author name, email, and description for `pyproject.toml`.

Steps:

1. Find all occurrences so nothing is missed:
   ```bash
   git grep -n -e foobar -e foobar-author -e gpauloski/python-template
   ```
2. Rename the package directory:
   ```bash
   git mv foobar <package_name>
   ```
3. Replace the placeholders across the tree (review before running a bulk
   `sed`). Key files: `pyproject.toml`, `mkdocs.yml`, `README.md`,
   `.github/**`, `docs/**`, and the custom template
   `docs/templates/python/material/module.html.jinja`.
4. Update author, email, description, and URLs in `pyproject.toml`, and the
   `<CONTACT_EMAIL>` placeholder in `.github/CODE_OF_CONDUCT.md`.
5. Verify nothing was missed and the project still works:
   ```bash
   git grep -n foobar          # should return nothing meaningful
   uv sync && uv run pytest
   ```
