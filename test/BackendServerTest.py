#!/usr/bin/python

#
#   FILE:   BackendServerTest.py
#   AUTHOR: mmiddleton
#   DATE:   19 FEB 2018
#
#   DESCRIPTION:
#   Unittest for BackendServer.py
#

import unittest
from flask import *
from BackendServer import *

class BackendServerTest (unittest.TestCase):
    def testHTTPResponse400OK(self):
        self.app = app.test_client()
        self.app.testing = True
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/moss')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)