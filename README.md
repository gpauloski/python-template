# Python Package Template Repo

[![docs](https://github.com/gpauloski/python-template/actions/workflows/docs.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
[![tests](https://github.com/gpauloski/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
[![prek](https://github.com/gpauloski/python-template/actions/workflows/prek.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)

An opinionated, modern Python package template that provides:

- A flat package layout with `examples/` and `testing/` helpers.
- [uv](https://docs.astral.sh/uv/) for dependency management and environments.
- Strict linting/formatting ([Ruff](https://docs.astral.sh/ruff/)), type
  checking ([mypy](https://mypy.readthedocs.io/) strict), and spell checking
  ([typos](https://github.com/crate-ci/typos)).
- [prek](https://github.com/j178/prek) (a fast pre-commit replacement) and
  [tox](https://tox.wiki/) for local and CI checks.
- GitHub Actions for tests, docs, and publishing (PyPI Trusted Publishing).
- Docs with [MkDocs](https://www.mkdocs.org/) + Material and GitHub Pages.
- PR/issue templates and agent instructions (`AGENTS.md`/`CLAUDE.md`).

The original layout was inspired by
[Anthony Sottile's project setup](https://www.youtube.com/watch?v=q8DkatMZvUs&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY),
but this template has since diverged significantly.

## Creating a New Project

You can either start from this template or scaffold from scratch with uv.

**Option A — Use this template (recommended).**

1. Click **"Use this template"** at the top right of the repo.
2. Clone your new repo locally.
3. Delete directories you will not use (e.g. `docs/` if you do not want MkDocs,
   or `examples/`).
4. The template uses `foobar` as a placeholder. Find and replace every instance:
   ```bash
   git grep -l foobar   # review the matches
   ```
   Rename the `foobar/` package directory and update `foobar`, `foobar-author`,
   and `gpauloski/python-template` throughout (`pyproject.toml`, `mkdocs.yml`,
   docs, workflows, etc.).
5. Update author, description, and URLs in `pyproject.toml`.
6. Configure the repository (see [Repository Setup](#repository-setup)).

**Option B — Start fresh with uv.**

Run `uv init --lib <name>` to scaffold a new library, then copy the tooling
config from this template (`pyproject.toml` tool sections, `.pre-commit-config.yaml`,
`tox.ini`, `.github/`, and the agent files). Note that `uv init --lib` uses a
`src/` layout; this template uses a flat layout, so move the package up a level
if you want to match it.

## Development

This project uses [uv](https://docs.astral.sh/uv/). Install it first
(see the [uv install docs](https://docs.astral.sh/uv/getting-started/installation/)):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then set up the environment and git hooks:

```bash
uv sync                 # create .venv and install the project + dev tools
uv run prek install     # install the git pre-commit hooks
```

Common tasks (`uv run` executes inside the managed environment):

```bash
uv run pytest                     # run the tests
uv run prek run --all-files       # run all lint/format/type/spell checks
uv run mypy .                     # type check
uv run tox                        # full matrix: py3.10-3.13, prek, docs
uv run tox -e py313               # a single environment
uv run mkdocs serve               # preview docs locally (needs the docs group)
```

Install the docs dependency group when working on documentation:

```bash
uv sync --group docs
```

## Installation

Install the released package via pip:

```bash
pip install foobar
```

## Repository Setup

After creating your repository from the template, configure GitHub:

- **General:** enable "Automatically delete head branches" and prefer
  "Squash merging".
- **Branches:** add a branch protection (or ruleset) for `main` requiring a PR
  and passing status checks (`tests`, `prek`, `check-docs`).
- **Pages:** deploy from the `gh-pages` branch (created by the docs workflow).
- **PyPI:** configure [Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
  pointing at the `publish` workflow (no API token required).

See `docs/contributing/repository-setup.md` for the full checklist, including
recommended issue labels that align with the release-notes categories, and
`docs/contributing/releases.md` for how to cut a release.
