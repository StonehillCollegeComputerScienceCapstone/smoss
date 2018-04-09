import unittest
from Config import Config
from MossResultsRetriever import MossResultsRetriever

class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.validUrl = self.config.getWarmup()
        self.retriever = MossResultsRetriever()

    def test_validUrl(self):
        self.assertTrue(self.retriever.getUrl(self.validUrl))  # valid URL

    def test_invalidUrl(self):
        self.assertFalse(self.retriever.getUrl("notURL"))  # this is not a valid URL
        self.assertFalse(self.retriever.getUrl(1))  # in case file reading goes wrong to this
        self.assertFalse(self.retriever.getUrl("http://moss.stanford.edu/results/12121212121212/"))  # 404 not found

    def test_validSameUrl(self):
        self.assertTrue(self.retriever.getUrl(self.validUrl))
        self.assertTrue(self.retriever.getUrl(self.validUrl))

    def test_readUrlsValidFile(self):
        self.assertTrue(self.retriever.getFileUrls("FileInput.txt"))

    def test_readUrlsInvalidFile(self):
        self.assertFalse(self.retriever.getFileUrls("Invalid"))
        self.assertFalse(self.retriever.getFileUrls(1))

    def test_numberOfValidUrlsRead(self):
        self.retriever.getFileUrls("FileInput.txt")
        self.assertEqual(len(self.retriever.urls), 2)

    def test_resultObjects(self):
        self.retriever.getFileUrls("FileInput.txt")  # URLs file to parse
        self.assertTrue(self.retriever.getResults())  # checking for errors in the parsing
        self.assertTrue(self.retriever.results)  # checks that it is not null
        

    def tearDown(self):
        self.retriever = None


if __name__ == '__main__':
    unittest.main()
