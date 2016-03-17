import pkg_resources
from .machine import Machine


try:
    __version__ = pkg_resources.require("python-docker-machine")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = "devel"
