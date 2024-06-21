""" Init module."""

from importlib.metadata import PackageNotFoundError  # pragma: no cover
from importlib.metadata import version

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "gilda-opts"  # pylint: disable=C0103
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
