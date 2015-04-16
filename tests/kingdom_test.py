import logging
from source.kingdom import Kingdom
from source.threat import Threat
import unittest

class KingdomTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Kingdom()
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test_breach_perimeter(self):
        self.assertFalse(self.obj.breached)
        self.obj.breached = True
        self.assertTrue(self.obj.breached)

    def test_deploy_troops(self):
        self.assertFalse(self.obj.deployed)
        self.obj.deployed = True
        self.assertTrue(self.obj.deployed)

    def test_identify_orc_threats(self):
        threats = self.obj.getThreats()
        threats.append(Threat(2))
        threats.append(Threat(3))
        results = self.obj.getThreat(4)
        self.assertEqual(results, [])
        results = self.obj.getThreat(2)
        self.assertNotEqual(results, [])
        self.assertEqual(results[0].threatType, 2)

    def test_remove_threat_by_uuid(self):
        kingdom = Kingdom()
        threats = kingdom.getThreats()
        threats.append(Threat())
        threats.append(Threat())
        self.assertNotEqual(threats, [])
        uuid = threats[0].uuid;
        kingdom.removeThreat(uuid)
        threats = kingdom.getThreats()
        self.assertNotEqual(threats, [])
        new_uuid = threats[0].uuid
        self.assertNotEqual(uuid, new_uuid)

    def test_change_units(self):
        self.obj.units = "nautical"
        self.assertEqual(self.obj.units, "nautical")
        kingdom = Kingdom()
        kingdom.units = "metric"
        self.assertEqual(self.obj.units, "metric")

    def test_change_threat_priority(self):
        threats = self.obj.getThreats()
        threats.append(Threat(5))
        threats[0].priority = 2
        self.assertEqual(threats[0].priority, 2)
        threats[0].priority = 5
        self.assertEqual(threats[0].priority, 5)
