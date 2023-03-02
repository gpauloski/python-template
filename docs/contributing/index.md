## Getting Started for Local Development

We recommend using [Tox](https://tox.wiki/en/latest/index.html){target=_blank}
to setup the development environment. This will create a new virtual
environment with all of the required packages installed
and FooBar installed in editable mode with the necessary extras options.

```bash
$ git clone https://github.com/foobar-author/foobar
$ cd foobar
$ tox --devenv venv -e py310
$ . venv/bin/activate
```

!!! warning

    Running Tox in a Conda environment is possible but it may conflict with
    Tox's ability to find the correct Python versions. E.g., if your
    Conda environment is Python 3.9, running `#!bash $ tox -e p38` may still use
    Python 3.9.

To install manually:
```bash
$ git clone https://github.com/foobar-author/foobar
$ cd foobar
$ python -m venv venv
$ . venv/bin/activate
$ pip install -e .[dev,docs]
```

## Continuous Integration

FooBar uses [pre-commit](https://pre-commit.com/){target=_blank} and
[Tox](https://tox.wiki/en/latest/index.html){target=_blank} for continuous integration
(test, linting, etc.).

### Linting and Type Checking (pre-commit)

To use pre-commit, install the hook and then run against files.

```bash
$ pre-commit install
$ pre-commit run --all-files
```

### Tests (tox)

The entire CI workflow can be run with `#!bash $ tox`.
This will test against multiple versions of Python and can be slow.

Module-level unit-test are located in the `tests/` directory and its
structure is intended to match that of `foobar/`.
E.g. the tests for `foobar/x/y.py` are located in
`tests/x/y_test.py`; however, additional test files can be added
as needed. Tests should be narrowly focused and target a single aspect of the
code's functionality, tests should not test internal implementation details of
the code, and tests should not be dependent on the order in which they are run.

Code that is useful for building tests but is not a test itself belongs in the
`testing/` directory.

```bash
# Run all tests in tests/
$ tox -e py39
# Run a specific test
$ tox -e py39 -- tests/x/y_test.py::test_z
```

## Docs

If code changes require an update to the documentation (e.g., for function
signature changes, new modules, etc.), the documentation can be built using
MKDocs.

```bash
# Manually
$ pip install -e .[docs]
$ mkdocs build --strict  # Build only to site/index.html
$ mkdocs serve           # Serve locally

# With tox (will only build, does not serve)
$ tox -e docs
```

Docstrings are automatically generated, but it is recommended to check the
generated docstrings to make sure details/links/etc. are correct.
