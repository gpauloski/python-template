# Python Package Template Repo

<!-- REPLACE THE FOLLOWING LINKS WITH THE CORRECT ONES
- pre-commit.ci badge can be found on pre-commit.ci after you enable precommit for you repo.
- RTDs badge can be found on readthedocs.org after enabling RTD for your repo.
-->
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gpauloski/python-template/main.svg)](https://results.pre-commit.ci/latest/github/gpauloski/python-template/main)
[![Tests](https://github.com/gpauloski/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
<!--
[![Docs](https://readthedocs.org/projects/foobar/badge/?version=latest)](https://foobar.readthedocs.io/en/latest/?badge=latest)
-->

Python package template repo that provides:
- Package, examples, and testing layout.
- GitHub PR and Issue templates.
- Example docs with ReadTheDocs.
- CI framework with `pre-commit` and `tox`.
- GitHub actions for running tests and publishing packages.

This package setup was based on [Anthony Sottile's project setup](https://www.youtube.com/watch?v=q8DkatMZvUs&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY) but deviates in some places (e.g., `pyproject.toml` and `ruff`).

## Setup Instructions

#. Click the "Use this template" button at the top right of this page.
#. Delete and directories you will not be using (commonly `docs/` if you do not want to use ReadTheDocs or `examples/` if you will not have example code).
#. Follow the instructions to create the new repo then clone your repo locally.
#. The template uses "foobar" to indicate things that need to be changed.
   Start by searching for all instances (`git grep foobar`) and changing them accordingly.
#. Configure pre-commit:
   - Go to [https://pre-commit.ci/](https://pre-commit.ci/) and enable pre-commit on your repo.
   - Update the pre-commit badge URL in this README with your new badge URL.
#. Configure ReadTheDocs (if relevant):
   - Go to [https://readthedocs.org/](https://readthedocs.org/) and import this repo as a new project.
   - Update the ReadTheDocs badge URL in this README with your new badge URL.
#. Configure PyPI releases (if relevant):
   - Create a new API token for [https://pypi.org/](https://pypi.org/).
   - Add the token as a GitHub actions secret (see the instructions [here](https://github.com/pypa/gh-action-pypi-publish)).
#. Delete this boilerplate stuff in the README.
#. Commit and push changes.

### GitHub Configuration

I recommend making a few other changes to the repo's setting on GitHub.
- In "General"
  - Select/deselect features you need/don't need.
  - Select "Automatically delete head branches
- In "Branches": enable branch protection on `main`.
  - Check "Require a pull request before merging"
  - Check "Require status checks to pass before merging"
    - Check "Require branches to be up to date before merging"
    - Set required checks (e.g., pre-commit.ci, tests, etc.)
  - Check "Do not allow bypassing the above settings"

## Installation

Install via pip:
```
$ pip install foobar
```

For local development:
```
$ tox --devenv venv -e py 310
$ pre-commit install
```
or
```
$ pip install -e .
```

## Additional README Sections

...
