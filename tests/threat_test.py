import logging
from source.threat import Threat
import unittest

class ThreatTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Threat()
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test_distance(self):
        self.obj.__distance = 5
        self.assertTrue(self.obj.__distance == 5)

    def test_velocity(self):
        self.obj.__velocity = 2
        self.assertTrue(self.obj.__velocity == 2)
