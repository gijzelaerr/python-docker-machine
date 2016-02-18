=====================
python-docker-machine
=====================

Pythonic wrapper around docker-machine


installation
------------

::

    $ python setup.py install


or::

    $ pip install python-docker-machine



usage
-----

::

     import machine
     m = machine.Machine(path="/usr/local/bin/docker-machine")
     m.version()




requirements
------------

docker-machine on your system path

https://docs.docker.com/machine/install-machine/


running the test suite
----------------------

Make sure docker-machine is available on your system path.

test with nose::

    $  nosetests
    ......................
    ----------------------------------------------------------------------
    Ran 22 tests in 0.262s

or with tox::
