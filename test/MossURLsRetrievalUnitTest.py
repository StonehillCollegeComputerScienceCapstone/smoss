import unittest
from MossURLsRetrieval import MossURLsRetrieval


class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.MossURLsData = MossURLsRetrieval()

    def test_ValidURL(self):
        self.assertTrue(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))  # valid URL

    def test_InvalidURL(self):
        self.assertFalse(self.MossURLsData.getURL("notaURL"))  # this is not a valid URL
        self.assertFalse(self.MossURLsData.getURL(1)) #in case file reading goes wrong to this
        self.assertFalse(self.MossURLsData.getURL("http://moss.stanford.edu/results/12121212121212/"))

    def test_Invalid_sameURL(self):
        self.assertTrue(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))
        #trying to get the information from the same URL will fail
        self.assertFalse(self.MossURLsData.getURL("http://moss.stanford.edu/results/299782671/"))

    def tearDown(self):
        self.MossURLsData = None

def main():
    print("Start")


if __name__ == '__main__':
    unittest.main()