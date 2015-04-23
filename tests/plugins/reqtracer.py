from nose2.events import Plugin
from tests.ReqTracer import *

class ReqTracer(Plugin):
    configSection = 'reqtracer'
    commandLineSwitch = ('T', 'reqtracer', 'Turn on requirements tracer')

    def stopTestRun(self, event):
        """Output results to file"""
        with open('reqtracer-output.txt', 'w') as f:
            for a in Requirements:
                f.write("ID: " + a + '\n')
                f.write("Requirement: " + Requirements[a].req_text)
                f.write("Functions: " + ", ".join(Requirements[a].func_name))
                f.write("\n\n")
