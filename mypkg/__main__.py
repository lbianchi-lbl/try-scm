import logging
from typing import List, Dict

from setuptools_scm import get_version
from . import __version__


_logger = logging("mypkg")


def get_versions(variants: List[Dict]):
    versions = {}
    try:
        key = get_version(**kwargs)
    except LookupError:
        _logger.exception("Version could not be determined using setuptools_scm")
    else:
        versions[key] = kwargs
    return versions


setuptools_scm_variants = get_versions(
    [
        dict(version_scheme="post-release"),
    ]
)

print(f"{__version__=}")
print(f"{setuptools_scm_variants=}")
