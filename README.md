# Python Package Template Repo

<!-- REPLACE THE FOLLOWING LINKS WITH YOUR USERNAME/PROJECT NAME -->
[![Tests](https://github.com/gpauloski/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
[![Style](https://github.com/gpauloski/python-template/actions/workflows/style.yml/badge.svg)](https://github.com/gpauloski/python-template/actions)
<!-- REPLACE READTHEDOCS LINK AND UNCOMMENT IF NEEDED
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
