#!/usr/bin/env/python

#
#   FILE:       FrontEndTestSuite.py
#   AUTHOR:     mmiddleton
#   DATE:       28 FEB 2018
#
#   DESCRIPTION:
#   This is the master file that will call all of the front-end web tests found in frontend/.
#

import unittest
from BackendServer import BackendServer
import test.frontend as frontEnd

class FrontEndTestSuite (unittest.TestCase):
    server = None
    testRunner = None
    testSuite = None

    def setUp (self):
        self.server = BackendServer ()
        self.testRunner = unittest.TextTestRunner ()
        self.CreateTestSuite ()
    
    def test_front_end_suite (self): 
        self.testRunner.run (self.testSuite)
        
    def CreateTestSuite (self):
        loader = unittest.TestLoader ()
        self.testSuite = unittest.TestSuite ()
        self.testSuite.addTests (unittest.TestLoader.loadTestsFromTestCase (loader, frontEnd.GoogleSearch))


if __name__ == "__main__":
    unittest.main ()