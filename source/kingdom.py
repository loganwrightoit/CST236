"""
Kingdom
"""

from random import randint
from source.threat import Threat
import source.orc
import logging

logger = logging.getLogger(__name__)

class Kingdom(object):
    """
    Kingdom Class
    """

    __units = "imperial"

    def __init__(self):
        self.__breached = False
        self.__deployed = False
        self.__threats = []

    @property
    def breached(self):
        return self.__breached
    @breached.setter
    def breached(self, x):
        self.__breached = x

    @property
    def deployed(self):
        return self.__deployed
    @deployed.setter
    def deployed(self, x):
        self.__deployed = x

    @property
    def units(self):
        return self.__class__.__units
    @units.setter
    def units(self, x):
        self.__class__.__units = x

    def addThreat(self, threat):
        self.__threats.append(threat)

    def getThreats(self):
        return self.__threats

    def getThreat(self, threatType):
        result = []
        for a in self.__threats:
            if a.threatType == threatType:
                result.append(a)
        return result

    def removeThreat(self, uuid):
        for a in self.__threats:
            if a.uuid == uuid:
                self.__threats.remove(a)

    def removeThreats(self):
        self.__threats = []

    def getThreatByUUID(self, uuid):
        for a in self.__threats:
            if a.uuid == uuid:
                return a

    def generateThreats(self):
        self.__threats = []
        types = [ source.orc.OrcBlack(), source.orc.OrcWhite(), source.orc.OrcRed(), source.orc.OrcGreen(), source.orc.OrcBlue(), source.orc.OrcYellow(), source.orc.OrcOrange(), source.orc.OrcPink() ]
        numThreats = randint(2, 100)
        for a in range(0, numThreats):
            orcType = randint(0, 7)
            klass = types[randint(0, 7)].__class__
            self.__threats.append(klass())
