"""
Orc Threat
"""

from source.threat import Threat

class OrcBlack(Threat):
    """
    Black Orc Class
    """
    @property
    def threatType(self):
        return "BlackOrc"

class OrcWhite(Threat):
    """
    White Orc Class
    """
    @property
    def threatType(self):
        return "WhiteOrc"

class OrcRed(Threat):
    """
    Red Orc Class
    """
    @property
    def threatType(self):
        return "RedOrc"

class OrcGreen(Threat):
    """
    Green Orc Class
    """
    @property
    def threatType(self):
        return "GreenOrc"

class OrcBlue(Threat):
    """
    Blue Orc Class
    """
    @property
    def threatType(self):
        return "BlueOrc"

class OrcYellow(Threat):
    """
    Yellow Orc Class
    """
    @property
    def threatType(self):
        return "YellowOrc"

class OrcOrange(Threat):
    """
    Orange Orc Class
    """
    @property
    def threatType(self):
        return "OrangeOrc"

class OrcPink(Threat):
    """
    Pink Orc Class
    """
    @property
    def threatType(self):
        return "PinkOrc"
