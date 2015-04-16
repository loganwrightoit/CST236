import logging
from source.kingdom import Kingdom
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
