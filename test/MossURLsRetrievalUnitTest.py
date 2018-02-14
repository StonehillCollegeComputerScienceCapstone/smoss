import unittest
from MossURLsRetrieval import MossURLsRetrieval

class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.MossURLsData = MossURLsRetrieval()

    def test_ValidURL(self):
        self.assertTrue(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))  # valid URL

    def test_InvalidURL(self):
        self.assertFalse(self.MossURLsData.getURL("notaURL"))  # this is not a valid URL

    def test_Invalid_sameURL(self):
        self.assertTrue(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))

        #trying to get the information from the same URL will fail
        self.assertFalse(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))

    def test_validHTML(self):
        self.assertTrue(self.MossURLsData.parseHTML("http://moss.stanford.edu/results/299782671/"))

    def test_invalidHTML(self):
        self.assertFalse(self.MossURLsData.parseHTML("")) #NEED SOME SORT OF BAD HTML

    def tearDown(self):
        self.MossURLsData = None