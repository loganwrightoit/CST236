from nose2.events import Plugin


class ReqTracer(Plugin):
    configSection = 'reqtracer'
    commandLineSwitch = ('T', 'reqtracer', 'Turn on requirements tracer')

    def startTestRun(self, event):

    def stopTestRun(self, event):
        """Output results to file"""
