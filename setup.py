from setuptools import setup, find_packages

from machine.version import __version__

setup(
    name="python-docker-machine",
    version=__version__,
    packages=find_packages(),
    scripts=[],
    install_requires=['six'],

    package_data={
        '': ['*.txt', '*.rst'],
    },

    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="Python wrapper around docker-machine",
    license="GPL2",
    keywords="docker machine docker-machine container",
    url="https://github.com/gijzelaerr/python-docker-machine",
)