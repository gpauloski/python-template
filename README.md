# Python Package Template Repo

<!-- REPLACE THE FOLLOWING LINKS WITH THE CORRECT ONES
- pre-commit.ci badge can be found on pre-commit.ci after you enable precommit for you repo.
- Alternatively, GitHub actions can be used to run pre-commit in CI by removing the '.disabled' from `.github/workflows/style.yml.disabled` and uncommenting the badge below.
- RTDs badge can be found on readthedocs.org after enabling RTD for your repo.
-->
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gpauloski/python-template/main.svg)](https://results.pre-commit.ci/latest/github/gpauloski/python-template/main)
[![Docs](https://github.com/gpauloski/python-template/actions/workflows/docs.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
[![Tests](https://github.com/gpauloski/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
<!--
[![Style](https://github.com/gpauloski/python-template/actions/workflows/style.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
[![Docs](https://readthedocs.org/projects/foobar/badge/?version=latest)](https://foobar.readthedocs.io/en/latest/?badge=latest)
-->

Python package template repo that provides:
- Package, examples, and testing layout.
- GitHub PR and Issue templates.
- Example docs with ReadTheDocs.
- CI framework with `pre-commit` and `tox`.
- GitHub actions for running `pre-commit` and `tox`.

To use the template to build your own package, start by fixing all instances of `foobar` in the template.
`foobar` is used to represent text that needs to be replaced by your package name, usernames of the maintainers, links, etc.
Many of the links, including those in the README, need to be updated as well.

This package setup is based on [Anthony Sottile's project setup](https://www.youtube.com/watch?v=q8DkatMZvUs&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY).

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
