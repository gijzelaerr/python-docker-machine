import unittest
import machine


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.machine = machine.Machine()

    def test_active(self):
        pass

    def test_config(self):
        self.machine.config()

    def test_config_invalid_machine(self):
        with self.assertRaises(RuntimeError):
            self.machine.config(machine="QPLNELJFEOWJFOPEWIDPOKLKJFDLSKJFNNPFONIEPFOIPOPNFIPOI")

    def test_create(self):
        pass

    def test_env(self):
        pass

    def test_inspect(self):
        pass

    def test_ip(self):
        pass

    def test_kill(self):
        pass

    def test_ls(self):
        pass

    def test_provision(self):
        pass

    def test_regenerate_certs(self):
        pass

    def test_restart(self):
        pass

    def test_rm(self):
        pass

    def test_ssh(self):
        pass

    def test_scp(self):
        pass

    def test_start(self):
        pass

    def test_status(self):
        pass

    def test_stop(self):
        pass

    def test_upgrade(self):
        pass

    def test_url(self):
        pass

    def test_version(self):
        self.machine.version()

    def test_help(self):
        pass
