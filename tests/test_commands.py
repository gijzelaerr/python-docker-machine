import unittest
import os
import docker
from time import sleep

import machine

# machine name used for testing
TEST_MACHINE = os.environ.get("DOCKER_MACHINE", "python-docker-machine")

# invalid machine name
INVALID_MACHINE = TEST_MACHINE + "-invalid"

# temporary machine name
TEMPORARY_MACHINE = TEST_MACHINE + "-temporary"


class TestCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        error = "can't find machine '%s', please create before running test suite." % TEST_MACHINE
        cls.machine = machine.machine.Machine()
        exists = cls.machine.exists(machine=TEST_MACHINE)
        assert exists, error

    @classmethod
    def tearDownClass(cls):
        try:
            cls.machine.rm(machine=INVALID_MACHINE)
        except RuntimeError:
            pass
        try:
            cls.machine.rm(machine=TEMPORARY_MACHINE)
        except RuntimeError:
            pass
    
    def setUp(self):
        if not self.machine.status(machine=TEST_MACHINE):
            self.machine.start(machine=TEST_MACHINE)

    def test_active(self):
        self.machine.active()

    def test_config(self):
        config = self.machine.config(machine=TEST_MACHINE)
        client = docker.APIClient(**config)
        self.assertTrue(client.ping())


    def test_config_invalid_machine(self):
        with self.assertRaises(RuntimeError):
            self.machine.config(machine=INVALID_MACHINE)

    def test_env(self):
        self.machine.env(machine=TEST_MACHINE)

    def test_inspect(self):
        self.machine.inspect(machine=TEST_MACHINE)

    def test_ip(self):
        self.machine.ip(machine=TEST_MACHINE)

    def test_kill(self):
        self.machine.kill(machine=TEST_MACHINE)

    def test_ls(self):
        self.machine.ls()

    def test_provision(self):
        self.machine.provision(machine=TEST_MACHINE)

    def test_regenerate_certs(self):
        self.machine.regenerate_certs(machine=TEST_MACHINE)

    def test_restart(self):
        self.machine.restart(machine=TEST_MACHINE)

    def test_scp(self):
        # copy this file to the remote host
        source = os.path.realpath(__file__)
        destination = "%s:." % TEST_MACHINE
        self.machine.scp(source, destination)

    def test_ssh_echo(self):
        self.assertTrue(self.machine.exists(machine=TEST_MACHINE))
        self.assertEqual(self.machine.ssh(TEST_MACHINE, 'echo \"Hi\"'), ['Hi'])

    def test_start(self):
        self.machine.stop(machine=TEST_MACHINE)
        self.machine.start(machine=TEST_MACHINE)
        self.assertTrue(self.machine.status(machine=TEST_MACHINE))

    def test_status_when_up(self):
        self.assertTrue(self.machine.status(machine=TEST_MACHINE))

    def test_status_when_down(self):
        self.machine.stop(machine=TEST_MACHINE)
        self.assertFalse(self.machine.status(machine=TEST_MACHINE))

    def test_status_when_invalid_machine(self):
        with self.assertRaises(RuntimeError):
            self.machine.status(machine=INVALID_MACHINE)

    def test_stop(self):
        self.machine.stop(machine=TEST_MACHINE)
        self.assertFalse(self.machine.status(machine=TEST_MACHINE))

    def test_stop_when_stopped(self):
        self.machine.stop(machine=TEST_MACHINE)
        with self.assertRaises(RuntimeError):
            self.machine.stop(machine=TEST_MACHINE)

    def test_upgrade(self):
        self.machine.upgrade(machine=TEST_MACHINE)

    def test_url(self):
        self.machine.url(machine=TEST_MACHINE)

    def test_version(self):
        version = self.machine.version()

    def test_create_already_exists(self):
        self.assertTrue(self.machine.exists(machine=TEST_MACHINE))
        try:
            self.machine.create(TEST_MACHINE, blocking=True)
        except RuntimeError:
            pass # The test should raise this error
        try:
            self.machine.create(TEST_MACHINE, blocking=False)
        except RuntimeError:
            pass # The test should raise this error

    @unittest.skip("disabled since it takes ages")
    def test_create_non_blocking(self):
        self.assertFalse(self.machine.exists(machine=TEMPORARY_MACHINE))

        # Create a new machine with blocking=False, and wait...
        self.machine.create(TEMPORARY_MACHINE, blocking=False)

        max_time = 300 #Max waiting time opf 300 seconds
        for sec in range(max_time) :
            sleep(1)
            if self.machine.exists(machine=TEMPORARY_MACHINE):
                break
        self.assertTrue(self.machine.exists(machine=TEMPORARY_MACHINE))
        self.machine.stop(machine=TEMPORARY_MACHINE)
        self.machine.rm(machine=TEMPORARY_MACHINE)

    @unittest.skip("disabled since it takes ages")
    def test_create_blocking(self):
        self.assertFalse(self.machine.exists(machine=TEMPORARY_MACHINE))

        # Create a new machine with blocking=True, and wait...
        self.machine.create(TEMPORARY_MACHINE, blocking=True)
        self.assertTrue(self.machine.exists(machine=TEMPORARY_MACHINE))
        self.machine.stop(machine=TEMPORARY_MACHINE)
        self.machine.rm(machine=TEMPORARY_MACHINE)
