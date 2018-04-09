import unittest
from Config import Config
from MossResultsRetriever import MossResultsRetriever
from Result import Result

class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.validUrl = self.config.getWarmup()
        self.retriever = MossResultsRetriever()

#
# getUrl()
#
    def test_validUrl(self):
        self.assertTrue(self.retriever.getUrl(self.validUrl))

    def test_invalidUrlString(self):
        self.assertFalse(self.retriever.getUrl("notURL"))

    def test_invalidUrlInt(self):
        self.assertFalse(self.retriever.getUrl(1))

    def test_invalidUrlDouble(self):
        self.assertFalse(self.retriever.getUrl(0.5))

    def test_invalidUrlLikeMoss(self):
        self.assertFalse(self.retriever.getUrl("http://moss.stanford.edu/results/12121212121212/"))

    def test_invalidUrlDouble(self):
        self.assertFalse(self.retriever.getUrl(self.validUrl + self.validUrl))

    def test_validSameUrl(self):
        self.assertTrue(self.retriever.getUrl(self.validUrl))
        self.assertTrue(self.retriever.getUrl(self.validUrl))

#
# getFileUrls()
#
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

#
# areDuplicateResults()
#
    def test_noDuplicateResults(self):
        r = Result(1, "f1", "f2", "url", 50, 50, 50)
        self.retriever.results.append(r)
        self.assertFalse(self.retriever.areDuplicateResults())
        self.retriever = MossResultsRetriever()

    def test_oneDuplicateResult(self):
        r = Result(1, "f1", "f2", "url", 50, 50, 50)
        self.retriever.results.append(r)
        self.retriever.results.append(r)
        self.assertTrue(self.retriever.areDuplicateResults())
        self.retriever = MossResultsRetriever()
        

    def tearDown(self):
        self.retriever = None


if __name__ == '__main__':
    unittest.main()
