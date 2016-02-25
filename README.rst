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

.. image:: https://readthedocs.org/projects/python-docker-machine/badge/?version=latest
   :target: http://python-docker-machine.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status

::

     import machine
     import docker
     m = machine.Machine(path="/usr/local/bin/docker-machine")
     client = docker.Client(**m.config(machine='default'))
     client.ping()



requirements
------------

docker-machine on your system path

https://docs.docker.com/machine/install-machine/


running the test suite
----------------------

Make sure docker-machine is available on your system path. Next you need to create a docker machine with the name
``python-docker-machine`` with the driver of your choice, for example the virtualbox driver::

   $ docker-machine create -d virtualbox python-docker-machine


Now you can run the tests with nose::

    $  nosetests
    ......................
    ----------------------------------------------------------------------
    Ran 22 tests in 0.262s

or with tox::

    $ tox

