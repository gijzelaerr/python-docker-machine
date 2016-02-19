from setuptools import setup, find_packages

from machine.version import __version__

setup(
    name="python-docker-machine",
    version=__version__,
    packages=find_packages(),
    package_data={
        '': ['*.rst'],
    },
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="Python wrapper around docker-machine",
    license="GPL2",
    keywords="docker machine docker-machine container",
    url="https://github.com/gijzelaerr/python-docker-machine",
)