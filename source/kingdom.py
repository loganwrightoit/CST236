"""
Kingdom
"""

import logging

logger = logging.getLogger(__name__)

class Kingdom(object):
    """
    Kingdom Class
    """
    def __init__(self):
        self.__breached = False
        self.__deployed = False

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
