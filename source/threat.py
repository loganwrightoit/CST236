"""
Threat
"""

class Threat(object):
    """
    Threat Class
    """

    def __init__(self):
        self.__distance = 10
        self.__velocity = 1
        
    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, x):
        self.__distance = x

    @property
    def velocity(self):
        return self.__velocity
    @velocity.setter
    def velocity(self, x):
        self.__velocity = x
