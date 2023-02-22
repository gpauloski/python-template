# Contributing

## Getting Started for Local Development

This package uses [pre-commit](https://pre-commit.com/) and [Tox](https://tox.wiki/en/latest/index.html) for code checking and testing.

```bash
$ git clone https://github.com/foobar-user/foobar.git
$ cd foobar
$ tox --devenv venv -e py39
$ . venv/bin/activate
```

Note that running Tox in a Conda environment will conflict with Tox's ability to find the correct Python versions.

Pre-commit and Tox are used for continuous integration (locally and on GitHub).

To use pre-commit, install the hook and then run against files.
Note that sometimes pre-commit needs to be run multiple times to fix all the issues.

```bash
$ pre-commit install
$ pre-commit run --all-files
```

The Python code and docstring format mostly follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), but the pre-commit config is the authoritative source for code format compliance.

The entire CI workflow can be run with `#!bash $ tox`.
This will test against multiple versions of Python and can be slow.

Module-level unit-test are located in the `tests/` directory and its structure is intended to match that of `foobar/`.
E.g. the tests for `foobar/foo.py` are located in `tests/foo_test.py`.

```bash
# Run all tests in tests/
$ tox -e py38
# Run a specific test
$ tox -e py38 -- tests/foo_test.py::test_bar_sum
```

## Docs

If code changes require an update to the documentation (e.g., for function
signature changes, new modules, etc.), the documentation can be built using
MKDocs.

```bash
# Manually
$ pip install -e .[docs]
$ mkdocs build --strict  # Build only to site/index.html
$ mkdocs server          # Serve locally

# With tox
$ tox -e docs
```

Docstrings are automatically generated, but it is recommended to check the
generated docstrings to make sure details/links/etc. are correct.

## Issues

We use GitHub issues to report problems, request and track changes, and discuss future ideas.

If you open an issue for a specific problem, please follow the template guides.

## Pull Requests

We use the standard GitHub contribution cycle.

1. Fork the repository and clone to your local machine
2. Create local changes
    - Changes should conform to the style and testing guidelines, referenced above.
    - Commit messages should start with a sentence describing the changes followed by a blank line then a detailed description of what changed and why.
3. Push commits to your fork
    - Please squash commits fixing mistakes to keep the git history clean.
      For example, if commit "b" follows commit "a" and only fixes a small typo from "a", please squash "a" and "b" into a single, correct commit.
4. Open a pull request in this repository
    - The pull request should include a description of the motivation for the PR and included changes.
      A PR template is provided to guide this process.
