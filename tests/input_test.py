import logging
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
