## Getting Started for Local Development

FooBar uses [uv](https://docs.astral.sh/uv/){target=_blank} to manage the
development environment. First
[install uv](https://docs.astral.sh/uv/getting-started/installation/){target=_blank},
then clone the repository and sync the environment.

```bash
$ git clone https://github.com/foobar-author/foobar
$ cd foobar
$ uv sync              # creates .venv with the project + dev dependencies
$ uv run prek install  # install the git pre-commit hooks
```

`uv sync` installs the `dev` dependency group by default. Add the docs group
when working on documentation with `#!bash $ uv sync --group docs`.

Prefix commands with `#!bash $ uv run` to execute them inside the managed
environment (or activate it with `#!bash $ source .venv/bin/activate`).

## Continuous Integration

FooBar uses [prek](https://github.com/j178/prek){target=_blank} (a drop-in
replacement for pre-commit) and
[Tox](https://tox.wiki/en/latest/index.html){target=_blank} for continuous
integration (tests, linting, type checking, etc.).

### Linting and Type Checking (prek)

The hooks (Ruff, mypy, typos, complexipy, and more) are configured in
`.pre-commit-config.yaml`. Run them against all files with:

```bash
$ uv run prek run --all-files
```

### Tests (tox)

Tox environments run with uv via `tox-uv`. The entire CI workflow can be run
with `#!bash $ uv run tox`; this tests against multiple versions of Python and
can be slow.

Module-level unit tests are located in the `tests/` directory and its
structure is intended to match that of `foobar/`.
E.g. the tests for `foobar/x/y.py` are located in
`tests/x/y_test.py`; however, additional test files can be added
as needed. Tests should be narrowly focused and target a single aspect of the
code's functionality, tests should not test internal implementation details of
the code, and tests should not be dependent on the order in which they are run.

Code that is useful for building tests but is not a test itself belongs in the
`testing/` directory.

```bash
# Run all tests in a single environment
$ uv run tox -e py313
# Run a specific test
$ uv run tox -e py313 -- tests/x/y_test.py::test_z
# Or run pytest directly in the current environment
$ uv run pytest tests/x/y_test.py::test_z
```

## Docs

If code changes require an update to the documentation (e.g., for function
signature changes, new modules, etc.), the documentation can be built using
MkDocs.

```bash
# Manually (install the docs dependency group first)
$ uv sync --group docs
$ uv run mkdocs build --strict  # Build only to site/index.html
$ uv run mkdocs serve           # Serve locally

# With tox (will only build, does not serve)
$ uv run tox -e docs
```

Docstrings are automatically generated, but it is recommended to check the
generated docstrings to make sure details/links/etc. are correct.
