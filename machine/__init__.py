
import os
from subprocess import Popen, PIPE
import re

from .version import __version__

LS_FIELDS = ["Name", "Active", "ActiveHost", "ActiveSwarm", "DriverName", "State", "URL", "Swarm", "Error",
             "DockerVersion", "ResponseTime"]


def which(program):

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


class Machine:
    def __init__(self, path="docker-machine"):
        """
        :param path: path to docker-machine binary
        """
        where = which(path)
        if not where:
            raise RuntimeError("Cant find docker-machine binary (%s)" % path)
        self.path = where

    def _run(self, cmd, raise_error=True):
        """

        :param cmd: a list of the docker-machine command with the arguments to run
        ;param raise_error: raise an exception on non 0 return code
        :return:  stdout, stderr, error_code
        """
        cmd = [self.path] + cmd
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        error_code = p.returncode
        if raise_error and error_code:
            raise RuntimeError("cmd returned error %s: %s" % (error_code, stderr.decode('utf-8').strip()))
        return stdout.decode('utf-8'), stderr.decode('utf-8'), error_code

    def _match(self, cmd, regexp):
        """
        Run cmd and match regular expression regexp on it, return results
        """
        stdout, stderr, errorcode = self._run(cmd)
        cleaned = stdout.strip()
        match = re.match(regexp, cleaned)
        if not match:
            raise RuntimeError("can't parse output (\"%s\")" % (cleaned))
        return match

    def version(self):
        cmd = ["version"]
        regexp = "docker-machine version (.+), build (.+)"
        match = self._match(cmd, regexp)
        return match.group(1)

    def config(self, machine="default"):
        """
        Returns the docker configuration for the given machine

        :param machine: The machine name
        returns: tlscacert, tlscert, tlskey, host
        """
        cmd = ["config", machine]
        regexp = """--tlsverify\n--tlscacert="(.+)"\n--tlscert="(.+)"\n--tlskey="(.+)"\n-H=(.+)"""
        match = self._match(cmd, regexp)
        return match.group(1, 2, 3)

    def ls(self):
        """
        List machines
        """
        seperator = "\t"
        fields = seperator.join(["{{.%s}}" % i for i in LS_FIELDS])
        cmd = ["ls", "-f", fields]
        stdout, stderr, errorcode = self._run(cmd)
        machines = []
        for line in stdout.split("\n"):
            machine = {LS_FIELDS[index]: value for index, value in enumerate(line.split(seperator))}
            machines.append(machine)
        return machines




