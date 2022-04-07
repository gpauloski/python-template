"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
-- Path setup --------------------------------------------------------------
If extensions (or modules to document with autodoc) are in another directory,
add these directories to sys.path here. If the directory is relative to the
documentation root, use os.path.abspath to make it absolute, like shown here.
"""
from __future__ import annotations

from typing import Any

import foobar  # noqa: F401


def linkcode_resolve(domain: str, info: dict[str, Any]) -> str | None:
    """Add GitHub source links."""
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return f'https://github.com/foobar-author/foobar/blob/main/{filename}.py'


def skip(
    app: Any,
    what: Any,
    name: str,
    obj: Any,
    would_skip: bool,
    options: Any,
) -> bool:
    """Prevent docs skipping __init__ docstrings."""
    if name == '__init__':
        return False
    return would_skip


def setup(app: Any) -> None:
    """Setup sphinx docs."""
    app.connect('autodoc-skip-member', skip)


# -- Project information -----------------------------------------------------

project = 'foobar'
copyright = '20XX, foobar author'
author = 'foobar author'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

todo_include_todos = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.linkcode',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
