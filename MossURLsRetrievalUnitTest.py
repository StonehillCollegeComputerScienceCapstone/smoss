import unittest
from MossURLsRetrieval import MossURLsRetrieval

class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.MossURLsData = MossURLsRetrieval()

    def test_ValidURL(self):
        self.assertTrue(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))  # valid URL

    def test_InvalidURL(self):
        self.assertFalse(self.MossURLsData.getURL("notaURL"))  # this is not a valid URL
        self.assertFalse(self.MossURLsData.getURL(1)) #in case reading in a file can go wrong leading to this point
        self.assertFalse(self.MossURLsData.getURL("http://moss.stanford.edu/results/121212121212121212112/")) #in case invalid moss URL

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

def main():
    print("Start")

if __name__ == '__main__':
    unittest.main()