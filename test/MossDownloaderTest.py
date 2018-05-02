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
from uuid import uuid4
from Config import Config
from MossDownloader import *

class MossDownloaderTest (unittest.TestCase):

    #   Creates a MossDownloader object to be used in all tests
    def setUp(self):
        self.sessionId = str(uuid4())
        self.downloader = MossDownloader(self.sessionId)
        self.config = Config()

    def test_removeZipFile(self):
        file = open(self.sessionId + 'mossURLs.zip', 'w')
        file.close()
        self.downloader.removeAllTempFiles()
        self.assertFalse(os.path.exists('./' + self.sessionId + 'mossURLs.zip'))

    def test_removeArchiveDirectory(self):
        os.makedirs(self.sessionId + 'archive')
        self.downloader.removeAllTempFiles()
        self.assertFalse(os.path.isdir('./' + self.sessionId + 'archive'))

    def test_removeZipFileAndArchiveDirectory(self):
        file = open(self.sessionId + 'mossURLs.zip', 'w')
        file.close()
        os.makedirs(self.sessionId + 'archive')
        self.downloader.removeAllTempFiles()
        self.assertFalse(os.path.exists('./' + self.sessionId + 'mossURLs.zip') and (os.path.isdir('./' + self.sessionId + 'archive')))

    #def test_createZipFile(self):
    #def test_createArchiveDirectory(self):




    '''
    --------------------------------
            NEEDED TESTS:
    ---------------------------------
    - test_validURLDownloadSingleMatch:     Provide a valid URL and attempt to download the results HTMLs
    - test_invalidURLDownloadSingleMatch:   Provide an invalid URL and attempt to download the results HTMLs
    - test_validURLDownloadMultipleMatches: Provide valid URLs and attempt to download the results HTMLs
    - test_mixedURLDownloadMultipleMatches: Provide a mix of valid and invalid URLs and attempt to download the results HTMLs
    '''