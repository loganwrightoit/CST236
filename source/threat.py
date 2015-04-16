"""
Threat
"""

class Threat(object):
    """
    Threat Class
    """

    __next_uuid = 0

    def __init__(self, threatType = 0):
        self.__distance = 10
        self.__velocity = 1
        self.__type = threatType
        self.__priority = 0
        self.__uuid = self.__class__.__next_uuid
        self.__class__.__next_uuid += 1
        
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

    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self, x):
        self.__priority = x

    @property
    def threatType(self):
        return self.__type

    @property
    def uuid(self):
        return self.__uuid
