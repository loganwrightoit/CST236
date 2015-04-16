"""
Input
"""

import logging
from source.kingdom import Kingdom
from source.threat import Threat

logger = logging.getLogger(__name__)

class Input(object):
    """
    Input Class
    """
    def __init__(self):
        self.__stopped = False

    @property
    def stopped(self):
        return self.__stopped
    @stopped.setter
    def stopped(self, x):
        self.__stopped = x

    def process(self, command, kingdom = None):
        if command == "X":
            self.__stopped = True
        elif command == "?":
            return "Some options"
        elif command == "ENTer the Trees":
            if kingdom != None:
                kingdom.removeThreats()
                return "Killed all the threats"
            else:
                return "No kingdom to kill threats"
