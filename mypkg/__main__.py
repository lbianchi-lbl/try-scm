from typing import List, Dict

from setuptools_scm import get_version
from . import __version__


def get_versions(variants: List[Dict]):
    return {
        get_version(**kwargs): kwargs
        for kwargs in variants
    }


setuptools_scm_variants = get_versions(
    [
        dict(version_scheme="post-release"),
    ]
)

print(f"{__version__=}")
print(f"{setuptools_scm_variants=}")
