import logging
from source.threat import Threat
import unittest

class ThreatTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Threat(2)
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test_distance(self):
        self.obj.distance = 5
        self.assertTrue(self.obj.distance == 5)

    def test_velocity(self):
        self.obj.velocity = 2
        self.assertTrue(self.obj.velocity == 2)

    def test_type(self):
        self.assertFalse(self.obj.threatType == 3)
        self.assertTrue(self.obj.threatType == 2)

    def test_get_uuid(self):
        self.assertTrue(self.obj.uuid != None);

    def test_set_priority(self):
        self.assertNotEqual(self.obj.priority, 5)
        self.obj.priority = 5
        self.assertEqual(self.obj.priority, 5)
