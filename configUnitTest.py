import unittest
from config import config

#------Methods being Tested----------
#testURLValidity


class MyTestCase(unittest.TestCase):

    def setUp(self):
        configTest = config()

    def test_testURLValidity(self):
        self.assertTrue(configTest.testURLValidity())