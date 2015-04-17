from source.threat import Threat
import source.orc
import unittest

class ThreatTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = source.orc.OrcWhite()

    def test_distance(self):
        self.obj.distance = 5
        self.assertTrue(self.obj.distance == 5)

    def test_velocity(self):
        self.obj.velocity = 2
        self.assertTrue(self.obj.velocity == 2)

    def test_type(self):
        orc = source.orc.OrcWhite()
        self.assertEqual(self.obj.threatType, orc.threatType)

    def test_get_uuid(self):
        self.assertTrue(self.obj.uuid != None);

    def test_set_priority(self):
        self.assertNotEqual(self.obj.priority, 5)
        self.obj.priority = 5
        self.assertEqual(self.obj.priority, 5)
