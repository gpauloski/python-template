# Agent Instructions

Baseline guidance for AI coding agents working in this repository. Humans should
read the docs under `docs/contributing/`; this file is the concise, agent-facing
summary. `CLAUDE.md` imports this file so there is a single source of truth.

## Repository Layout

- `pypkg/` — the package source (flat layout, **no** `src/`). Avoid writing
  logic in `__init__.py`.
- `tests/` — pytest tests. Mirror the package layout; test files end in
  `_test.py` (e.g. `pypkg/x/y.py` → `tests/x/y_test.py`).
- `testing/` — shared helpers/fixtures for tests (not tests themselves).
- `docs/` — MkDocs sources. `docs/generate_api.py` auto-generates API pages, so
  do not hand-write `docs/api/`.
- `.github/workflows/` — CI (tests, prek, docs, publish).

`pypkg`, `pypkg-author`, and `gpauloski/python-template` are template
placeholders; in a real project they will be replaced with the actual names.

## Environment & Commands

This project uses [uv](https://docs.astral.sh/uv/). Create the environment and
activate it once, then invoke tools directly.

```bash
uv sync                       # install project + dev group
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

```bash
uv sync --group docs           # add docs dependencies
pytest                         # run tests
pytest tests/x/y_test.py::test_z   # run one test
prek run --all-files           # run all hooks (lint/format/type/spell)
mypy .                         # type check
tox                            # full matrix (py3.10-3.13, prek, docs)
tox -e py313                   # a single environment
uv build                       # build sdist + wheel
```

If the environment is not activated, prefix a command with `uv run` (e.g.
`uv run pytest`) to run it inside the managed environment.

Before finishing a change, ensure `prek run --all-files` and `pytest` both pass.

## Conventions

- **Every module** starts with `from __future__ import annotations` (enforced by
  Ruff isort). Fully type-annotate package code — mypy runs in **strict** mode.
- Formatting/linting is **Ruff with `ALL` rules enabled** (see `pyproject.toml`
  for the commented ignores). Style: single quotes, 79-char lines, Google-style
  docstrings. Do not fight the formatter.
- Spell checking is **typos**; complexity is gated by **complexipy**.
- Tests use `assert` and may omit docstrings/annotations (relaxed via per-file
  ignores). Put reusable test code in `testing/`, not `tests/`.
- Prefer pure functions; document all raised exceptions in docstrings. See
  `docs/contributing/style-guide.md` for the full style guide.

## Skills

Project skills live in `.claude/skills/`. Available skills: `check` (run the
full local gate), `release` (cut a release), `rename-template` (replace the
`pypkg` placeholders), and `add-docs-page` (scaffold a docs page). Skills are
optional helpers — the commands above are always the source of truth.
