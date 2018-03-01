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
    def setUp (self):
        self.app = BackendServer.app.test_client()
        self.app.testing = True
    
    def testHTTPResponseSuccess (self):
        knownURLs = ['/', '/moss']

        for url in knownURLs:
            result = self.app.get(url)
            self.assertEqual (result.status_code, 200)



    def testHTTPResponseError (self):
        result = self.app.get ('/asdfqwnkd')

        # We assert 200 because we're handling the 404 internally. We will receive our generic error page with the information printed on it, however the status code will be 200.
        self.assertEqual(result.status_code, 200)

