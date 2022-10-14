from setuptools import setup, find_packages


def _get_scm_version_config(
        time_format=r"%Y%m%d%H%M%S",
        local_sep: str = ".",
    ):
    def _verbatim_tag(v):
        return str(v.tag)

    def _distance_node_timestamp(v):
        if v.exact:
            return ""
        parts = [
            "{distance}",
            "{node}",
        ]
        if v.dirty:
            parts.append(f"d{{time:{time_format}}}")
        fmt = "+" + local_sep.join(parts)
        return v.format_with(fmt)

    return {
        "version_scheme": _verbatim_tag,
        "local_scheme": _distance_node_timestamp,
    }


setup(
    name="mypkgdistr",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    setup_requires=[
        "setuptools_scm>=7",
    ],
    use_scm_version=_get_scm_version_config,
)
