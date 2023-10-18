from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="sdscripts",
    version="0.1.0",
    install_requires=_requires_from_file("requirements.txt"),
    packages=find_packages("."),
    package_dir={"": "."},
)
