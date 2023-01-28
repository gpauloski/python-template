"""foobar package."""
# It is recommended to not write code in the __init__.py because it is easy
# to introduce import cycles and code becomes harder to search for.
from __future__ import annotations

import sys

if sys.version_info >= (3, 8):  # pragma: >=3.8 cover
    import importlib.metadata as importlib_metadata
else:  # pragma: <3.8 cover
    import importlib_metadata


__version__ = importlib_metadata.version('foobar')
