import logging
from testfixtures import LogCapture
from source.kingdom import Kingdom
from source.threat import Threat
import source.orc
import unittest

class KingdomTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Kingdom()
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
        self.logger.level = logging.DEBUG
        self.logCapture = LogCapture()

    def tearDown(self):
        self.logCapture.uninstall()

    def test_logger(self):
        self.logger.info('a message')
        self.logger.error('an error')
        klass = __name__ + '.' + self.__class__.__name__
        self.logCapture.check(
            (klass, 'INFO', 'a message'),
            (klass, 'ERROR', 'an error'),
            )

    def test_breach_perimeter(self):
        self.assertFalse(self.obj.breached)
        self.obj.breached = True
        self.assertTrue(self.obj.breached)

    def test_deploy_troops(self):
        self.assertFalse(self.obj.deployed)
        self.obj.deployed = True
        self.assertTrue(self.obj.deployed)

    def test_add_threat(self):
        threats = self.obj.getThreats()
        self.assertEqual(threats, [])
        self.obj.addThreat(source.orc.OrcRed())
        threats = self.obj.getThreats()
        self.assertNotEqual(threats, [])

    def test_identify_orc_threats(self):
        threats = self.obj.getThreats()
        threats.append(source.orc.OrcWhite())
        threats.append(source.orc.OrcBlack())
        results = self.obj.getThreat(source.orc.OrcYellow().threatType)
        self.assertEqual(results, [])
        results = self.obj.getThreat(source.orc.OrcWhite().threatType)
        self.assertNotEqual(results, [])
        self.assertEqual(results[0].threatType, source.orc.OrcWhite().threatType)

    def test_remove_threat_by_uuid(self):
        kingdom = Kingdom()
        threats = kingdom.getThreats()
        threats.append(source.orc.OrcWhite())
        threats.append(source.orc.OrcBlue())
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
        threats.append(source.orc.OrcWhite())
        threats[0].priority = 2
        self.assertEqual(threats[0].priority, 2)
        threats[0].priority = 5
        self.assertEqual(threats[0].priority, 5)

    def test_find_threat_by_uuid(self):
        threats = self.obj.getThreats()
        threat = source.orc.OrcBlack()
        uuid = threat.uuid
        threats.append(source.orc.OrcWhite())
        threats.append(threat)
        threats.append(source.orc.OrcPink())
        newThreat = self.obj.getThreatByUUID(uuid)
        self.assertEqual(newThreat.uuid, uuid)

    def test_kill_all_threats(self):
        self.obj.addThreat(source.orc.OrcWhite())
        self.obj.addThreat(source.orc.OrcRed())
        threats = self.obj.getThreats()
        self.assertNotEqual(threats, [])
        self.obj.removeThreats()
        threats = self.obj.getThreats()
        self.assertEqual(threats, [])

    def test_random_orc_generation(self):
        self.assertEqual(self.obj.getThreats(), [])
        self.obj.generateThreats()
        threats = self.obj.getThreats()
        self.assertNotEqual(threats, [])
