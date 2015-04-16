"""
Input
"""

import logging

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

    def process(self, command):
        if command == "X":
            self.__stopped = True
        elif command == "?":
            return "Some options"
