from setuptools import setup, find_packages

setup(
    name="mypkgdistr",
    packages=find_packages(),
    setup_requires=[
        "setuptools_scm>=7",
    ],
    use_scm_version={
        "version_scheme": lambda v: str(v.tag),
        "local_scheme": "node-and-timestamp",
    }
)
