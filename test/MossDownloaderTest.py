#!/usr/bin/env python3.6

#
#   FILE:   BackendServerTest.py
#   AUTHOR: mmiddleton
#   DATE:   19 FEB 2018
#
#   DESCRIPTION:
#   Unittest for BackendServer.py
#

import unittest
from Config import Config
from MossDownloader import *

class MossDownloaderTest (unittest.TestCase):
    #
    #   setUp():    Creates a MossDownloader object to be used in all tests
    #
    def setUp (self):
        self.downloader = MossDownloader ()
        self.config = Config ()
        

    '''
    --------------------------------
            NEEDED TESTS:
    ---------------------------------
    - test_validURLDownloadSingleMatch:     Provide a valid URL and attempt to download the results HTMLs
    - test_invalidURLDownloadSingleMatch:   Provide an invalid URL and attempt to download the results HTMLs
    - test_validURLDownloadMultipleMatches: Provide valid URLs and attempt to download the results HTMLs
    - test_mixedURLDownloadMultipleMatches: Provide a mix of valid and invalid URLs and attempt to download the results HTMLs
    '''