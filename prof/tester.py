import re
import subprocess as sp

class Test:

    def __init__(self, *, arguments, return_value, stdout_re, stderr_re):
        assert isinstance(arguments, list)
        self.arguments = arguments

        assert isinstance(return_value, int)
        self.return_value = return_value

        if isinstance(stdout_re, str):
            stdout_re = re.compile(stdout_re, flags=re.MULTILINE)
        assert isinstance(stdout_re, re.Pattern)
        self.stdout_re = stdout_re

        if isinstance(stderr_re, str):
            stderr_re = re.compile(stderr_re, flags=re.MULTILINE)
        assert isinstance(stderr_re, re.Pattern)
        self.stderr_re = stderr_re


    def check(self, *, rv, stdout, stderr):
        rv_check = rv == self.return_value
        stdout_check = self.stdout_re.match(stdout)
        stderr_check = self.stderr_re.match(stderr)
        return rv_check, stdout_check, stderr_re



class TestRunner:

    def __init__(self, executable):
        self.executable = executable

    def

    def run(self):
        pass
