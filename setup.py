from setuptools import setup, find_packages

setup(
    name="mypkgdistr",
    packages=find_packages(),
    setup_requires=[
        "setuptools_scm",
        "setuptools_scm_git_archive",
    ],
    install_requires=["setuptools_scm"],
    use_scm_version={
        "version_scheme": "post-release",
    }
)
