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
    # Test a valid URL
    def test_validUrl(self):
        url = self.validUrl
        self.assertTrue(self.retriever.getUrl(url))
        self.assertTrue(url in self.retriever.urls)

    # Test the same URL twice, which is considered a valid submission
    def test_validSameUrl(self):
        url = self.validUrl
        self.assertTrue(self.retriever.getUrl(url))
        self.assertTrue(self.retriever.getUrl(url))
        self.assertEqual(self.retriever.urls.count(url), 1)
        self.assertNotEqual(self.retriever.urls.count(url), 2)

    # Test an invalid String
    def test_invalidUrlString(self):
        url = "notURL"
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test an int
    def test_invalidUrlInt(self):
        url = 1
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test a double
    def test_invalidUrlDouble(self):
        url = 0.5
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test None
    def test_invalidUrlNone(self):
        url = None
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test empty list
    def test_invalidUrlListEmpty(self):
        url = []
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test a list with valid URLs as entries
    def test_invalidUrlListOfUrls(self):
        url = [self.validUrl, self.validUrl, self.validUrl]
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test an invalid URL like MOSSS
    def test_invalidUrlLikeMoss(self):
        url = "http://moss.stanford.edu/results/12121212121212/"
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test a URL that's two valid URLs appended together
    def test_invalidUrlTwoAppended(self):
        url = self.validUrl + self.validUrl
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test a valid URL that isn't MOSS
    def test_validUrlNotMoss(self):
        url = "https://google.com"
        self.assertFalse(self.retriever.getUrl(url))
        self.assertFalse(url in self.retriever.urls)

    # Test a duplicate valid URL is not appended to self.urls
    def test_duplicateUrls(self):
        url = self.validUrl
        self.retriever.getUrl(url)
        self.retriever.getUrl(url)
        self.assertTrue(url in self.retriever.urls)

#
# getFileUrls()
#
    def test_readUrlsValidFile(self):
        self.assertTrue(self.retriever.getFileUrls(self.config.getMossUrlsFile()))

    def test_readUrlsInvalidFile(self):
        self.assertFalse(self.retriever.getFileUrls("Invalid"))
        self.assertFalse(self.retriever.getFileUrls(1))

    def test_numberOfValidUrlsRead(self):
        self.retriever.getFileUrls(self.config.getMossUrlsFile())
        self.assertEqual(len(self.retriever.urls), 5)

    def test_resultObjects(self):
        self.retriever.getFileUrls(self.config.getMossUrlsFile())  # URLs file to parse
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

#
#
#
        

    def tearDown(self):
        self.retriever = None


if __name__ == '__main__':
    unittest.main()
