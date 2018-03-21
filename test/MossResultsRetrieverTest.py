import unittest
from Config import Config
from MossResultsRetriever import MossResultsRetriever

class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.validUrl = self.config.getWarmup()
        self.MossURLsData = MossResultsRetriever()

    def test_validUrl(self):
        self.assertTrue(self.MossURLsData.getUrl(self.validUrl))  # valid URL

    def test_invalidUrl(self):
        self.assertFalse(self.MossURLsData.getUrl("notURL"))  # this is not a valid URL
        self.assertFalse(self.MossURLsData.getUrl(1))  # in case file reading goes wrong to this
        self.assertFalse(self.MossURLsData.getUrl("http://moss.stanford.edu/results/12121212121212/"))  # 404 not found

#    def test_invalidSameUrl(self): #user accidentally entered the same URL. Test should not break the code.
#        self.assertTrue(self.MossURLsData.getUrl(self.validUrl))
        # trying to get the information from the same URL will fail
#        self.assertFalse(self.MossURLsData.getUrl(self.validUrl))

    def test_readUrlsValidFile(self):
        self.assertTrue(self.MossURLsData.get_file_urls("FileInput.txt"))

    def test_readUrlsInvalidFile(self):
        self.assertFalse(self.MossURLsData.get_file_urls("Invalid"))
        self.assertFalse(self.MossURLsData.get_file_urls(1))

    def test_numberOfValidUrlsRead(self):
        self.MossURLsData.get_file_urls("FileInput.txt")
        self.assertEqual(len(self.MossURLsData.urls), 2)

    def test_resultObjects(self):
        self.MossURLsData.get_file_urls("FileInput.txt")  # URLs file to parse
        self.assertTrue(self.MossURLsData.get_results())  # checking for errors in the parsing
        self.assertTrue(self.MossURLsData.results)  # checks that it is not null

    def tearDown(self):
        self.MossURLsData = None


def main():
    print("Start")


if __name__ == '__main__':
    unittest.main()
