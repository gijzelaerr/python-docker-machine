from setuptools import setup, find_packages

__version__ = "0.2.2"

install_requires = [
    'docker-py',
]

setup(
    name="python-docker-machine",
    version=__version__,
    packages=find_packages(),
    install_requires=install_requires,
    package_data={
        '': ['*.rst'],
    },
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="Python wrapper around docker-machine",
    license="GPL2",
    keywords="docker machine docker-machine container",
    url="https://github.com/gijzelaerr/python-docker-machine",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
