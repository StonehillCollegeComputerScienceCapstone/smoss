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

#   removeAllTempFiles()
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

#   zipFile()
    def test_createZipFile(self):
        os.makedirs(self.downloader.sessionId + 'archive')
        self.downloader.zipFile()
        self.assertTrue(os.path.exists(self.downloader.sessionId + 'mossURLs.zip'))
        os.rmdir(self.downloader.sessionId + 'archive')
        os.remove(self.downloader.sessionId + 'mossURLs.zip')

#   getAssignmentIds()
    def test_getAssignmentIds(self):
        sessions = []
        urls = []
        for test in range(0, 5):
            session = str(uuid4())
            sessions.append(session)
            urls.append('http://moss.stanford.edu/results/' + str(session))
        assignmentIds = self.downloader.getAssignmentIds(urls)
        for test in range(0, 5):
            if (assignmentIds[test] != sessions[test]):
                self.assertTrue(False)
                return
        self.assertTrue(True)

    def test_invalidString(self):
        url = 'http://moss.stanford.edu/results/' + str(uuid4())
        self.assertFalse(self.downloader.getAssignmentIds(url))

    def test_invalidInteger(self):
        self.assertFalse(self.downloader.getAssignmentIds(2))

    def test_invalidDecimal(self):
        self.assertFalse(self.downloader.getAssignmentIds(12.2))

    def test_invalidItemsInList(self):
        self.assertFalse(self.downloader.getAssignmentIds(['http://moss.stanford.edu/results/123124', 213]))

#   downloadMatch()
    def test_invalidFirstArgumentType(self):
        self.assertFalse(self.downloader.downloadMatch(1, 'string'))

    def test_invalidSecondArgumentType(self):
        self.assertFalse(self.downloader.downloadMatch('string', 2))

    def test_invalidBothArgumentTypes(self):
        self.assertFalse(self.downloader.downloadMatch(13, 14))

    def test_invalidList(self):
        self.assertFalse(self.downloader.downloadMatch(['string'], ['string']))

    def test_invalidDecimal(self):
        self.assertFalse(self.downloader.downloadMatch(12.13, 13.14))

#   tryDownload()
    def test_downloadInvalidFirstArgumentType(self):
        self.assertFalse(self.downloader.tryDownload('string', 5))

    def test_downloadInvalidSecondArgumentType(self):
        self.assertFalse(self.downloader.tryDownload(5, 'string'))

    def test_downloadInvalidBothArgumentTypes(self):
        self.assertFalse(self.downloader.tryDownload(5, 5))

    def test_downloadInvalidDecimal(self):
        self.assertFalse(self.downloader.tryDownload(12.1, 13.1))

    def test_downloadInvalidList(self):
        self.assertFalse(self.downloader.tryDownload(['test'], ['test']))

#   downloadAllMatches()
    def test_downloadAllMatchesInvalidFirstArgumentType(self):
        self.assertFalse(self.downloader.downloadAllMatches('string', [5, 2]))

    def test_downloadAllMatchesInvalidSecondArgumentType(self):
        self.assertFalse(self.downloader.downloadAllMatches(['string', 'string'], 2))

    def test_downloadAllMatchesInvalidBothArgumentTypes(self):
        self.assertFalse(self.downloader.downloadAllMatches('string', 10))

    def test_downloadAllMatchesInvalidDecimal(self):
        self.assertFalse(self.downloader.downloadAllMatches(12.1, 13.1))

    def test_downloadAllMatchesInvalidList(self):
        self.assertFalse(self.downloader.downloadAllMatches(['test', 4], [5, 'test']))

#   downloadAllMatchesForAssignment()
    def test_downloadAllMatchesForAssignmentInvalidFirstArgumentType(self):
        self.assertFalse(self.downloader.downloadAllMatchesForAssignment('string', [5, 2]))

    def test_downloadAllMatchesForAssignmentInvalidSecondArgumentType(self):
        self.assertFalse(self.downloader.downloadAllMatchesForAssignment(['string', 'string'], 2))

    def test_downloadAllMatchesForAssignmentInvalidBothArgumentTypes(self):
        self.assertFalse(self.downloader.downloadAllMatchesForAssignment(10, 'test'))

    def test_downloadAllMatchesForAssignmentInvalidDecimal(self):
        self.assertFalse(self.downloader.downloadAllMatchesForAssignment(12.1, 13.1))

#   downloadSummaryPage()
    def test_invalidSummaryInput(self):
        self.assertFalse(self.downloader.downloadSummaryPage(3))
