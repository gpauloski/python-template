## Getting Started for Local Development

pypkg uses [uv](https://docs.astral.sh/uv/){target=_blank} to manage the
development environment. First
[install uv](https://docs.astral.sh/uv/getting-started/installation/){target=_blank},
then clone the repository and sync the environment.

```bash
$ git clone https://github.com/pypkg-author/pypkg
$ cd pypkg
$ uv sync                    # creates .venv with the project + dev dependencies
$ source .venv/bin/activate  # Windows: .venv\Scripts\activate
$ prek install               # install the git pre-commit hooks
```

`uv sync` installs the `dev` dependency group by default. Add the docs group
when working on documentation with `#!bash $ uv sync --group docs`.

Activating the environment lets you invoke tools directly (`#!bash $ pytest`,
`#!bash $ tox`, ...). If you prefer not to activate it, prefix commands with
`#!bash $ uv run` instead.

## Continuous Integration

pypkg uses [prek](https://github.com/j178/prek){target=_blank} (a drop-in
replacement for pre-commit) and
[Tox](https://tox.wiki/en/latest/index.html){target=_blank} for continuous
integration (tests, linting, type checking, etc.).

### Linting and Type Checking (prek)

The hooks (Ruff, mypy, typos, complexipy, and more) are configured in
`.pre-commit-config.yaml`. Run them against all files with:

```bash
$ prek run --all-files
```

### Tests (tox)

Tox environments run with uv via `tox-uv`. The entire CI workflow can be run
with `#!bash $ tox`; this tests against multiple versions of Python and
can be slow.

Module-level unit tests are located in the `tests/` directory and its
structure is intended to match that of `pypkg/`.
E.g. the tests for `pypkg/x/y.py` are located in
`tests/x/y_test.py`; however, additional test files can be added
as needed. Tests should be narrowly focused and target a single aspect of the
code's functionality, tests should not test internal implementation details of
the code, and tests should not be dependent on the order in which they are run.

Code that is useful for building tests but is not a test itself belongs in the
`testing/` directory.

```bash
# Run all tests in a single environment
$ tox -e py313
# Run a specific test
$ tox -e py313 -- tests/x/y_test.py::test_z
# Or run pytest directly in the current environment
$ pytest tests/x/y_test.py::test_z
```

## Docs

If code changes require an update to the documentation (e.g., for function
signature changes, new modules, etc.), the documentation can be built using
MkDocs.

```bash
# Manually (install the docs dependency group first)
$ uv sync --group docs
$ mkdocs build --strict  # Build only to site/index.html
$ mkdocs serve           # Serve locally

# With tox (will only build, does not serve)
$ tox -e docs
```

Docstrings are automatically generated, but it is recommended to check the
generated docstrings to make sure details/links/etc. are correct.
