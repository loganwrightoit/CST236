import logging
from source.kingdom import Kingdom
from source.threat import Threat
import source.orc
from source.input import Input
import unittest

class InputTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Input()
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test_input_quit(self):
        self.obj.process("Y")
        self.assertFalse(self.obj.stopped)
        self.obj.process("X")
        self.assertTrue(self.obj.stopped)

    def test_input_options(self):
        result = self.obj.process("?")
        self.assertEqual(result, "Some options")

    def test_input_kill_all_threats(self):
        kingdom = Kingdom()
        kingdom.addThreat(source.orc.OrcWhite())
        kingdom.addThreat(source.orc.OrcGreen())
        threats = kingdom.getThreats()
        self.assertNotEqual(threats, [])
        self.obj.process("ENTer the Trees", kingdom)
        threats = kingdom.getThreats()
        self.assertEqual(threats, [])
