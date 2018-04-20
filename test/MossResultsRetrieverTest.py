import unittest
from Config import Config
from MossResultsRetriever import MossResultsRetriever
from Result import Result

class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.validUrl = self.config.getMagicsquare()
        self.retriever = MossResultsRetriever()
        self.results = Result(1, "f1", "f2", "url", 40, 50, 60)

#
# isValidUrl()
#
    # Test a valid URL
    def test_validUrl(self):
        url = self.validUrl
        self.assertTrue(self.retriever.isValidUrl(url))

    # Test the same URL twice, which is considered a valid submission
    def test_validSameUrl(self):
        url = self.validUrl
        self.assertTrue(self.retriever.isValidUrl(url))
        self.assertTrue(self.retriever.isValidUrl(url))

    # Test an invalid String
    def test_invalidUrlString(self):
        url = "notURL"
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test an int
    def test_invalidUrlInt(self):
        url = 1
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test a double
    def test_invalidUrlDouble(self):
        url = 0.5
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test None
    def test_invalidUrlNone(self):
        url = None
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test empty list
    def test_invalidUrlListEmpty(self):
        url = []
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test a list with valid URLs as entries
    def test_invalidUrlListOfUrls(self):
        url = [self.validUrl, self.validUrl, self.validUrl]
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test an invalid URL like MOSSS
    def test_invalidUrlLikeMoss(self):
        url = "http://moss.stanford.edu/results/12121212121212/"
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test a URL that's two valid URLs appended together
    def test_invalidUrlTwoAppended(self):
        url = self.validUrl + self.validUrl
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test a valid URL that isn't MOSS
    def test_validUrlNotMoss(self):
        url = "https://google.com"
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test a valid URL with space
    def test_validUrlWithSpace(self):
        url = " " + self.validUrl + " "
        self.assertFalse(self.retriever.isValidUrl(url))

    # Test a valid URL with new line
    def test_validUrlWithNewLine(self):
        url = "\n" + self.validUrl + "\n"
        self.assertFalse(self.retriever.isValidUrl(url))

#
# isValidUrlList()
#
    # Test int
    def test_isValidUrlListInt(self):
        urls = 1
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, "argument " + str(urls) + " is not a valid list")

    # Test double
    def test_isValidUrlListDouble(self):
        urls = 0.5
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, "argument " + str(urls) + " is not a valid list")

    # Test empty string
    def test_isValidUrlListString(self):
        urls = " "
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, "argument " + str(urls) + " is not a valid list")

    # Test single, valid url string
    def test_isValidUrlListValidUrl(self):
        urls = self.validUrl
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, "argument " + str(urls) + " is not a valid list")

    # Test None
    def test_isValidUrlListNone(self):
        urls = None
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, "argument " + str(urls) + " is not a valid list")

    # Test empty list
    def test_isValidUrlListEmptyList(self):
        urls = []
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, "argument " + str(urls) + " is not a valid list")

    # Test list of ints
    def test_isValidUrlListIntList(self):
        urls = [1, 1, 1]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, 1)

    # Test list of doubles
    def test_isValidUrlListDoublesList(self):
        urls = [0.5, 0.5, 0.5]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, 0.5)

    # Test list of Nones
    def test_isValidUrlListNoneList(self):
        urls = [None, None, None]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, None)

    # Test list of lists
    def test_isValidUrlListOfLists(self):
        urls = [[], [], []]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, [])

    # Test mixed list
    def test_isValidUrlListMixed(self):
        urls = [" ", 1, None, 0.5]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, " ")

    # Test mixed list with valid url
    def test_isValidUrlListMixedWithValid(self):
        urls = [self.validUrl, " ", 1, None, 0.5]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertFalse(isValid)
        self.assertEqual(url, " ")

    # Test single valid
    def test_isValidUrlListSingleValid(self):
        urls = [self.validUrl]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertTrue(isValid)
        self.assertEqual(url, "success")

    # Test multiple valid
    def test_isValidUrlListMultipleValid(self):
        urls = [self.config.getMagicsquare(), self.config.getTwentyone(), self.config.getTwentyone()]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertTrue(isValid)
        self.assertEqual(url, "success")

    # Test multiple valid with duplicates
    def test_isValidUrlListMultipleValidDuplicates(self):
        urls = [self.config.getMagicsquare(), self.config.getTwentyone(), self.config.getTwentyone(),
                self.config.getMagicsquare(), self.config.getTwentyone(), self.config.getTwentyone()]
        isValid, url = self.retriever.isValidUrlList(urls)
        self.assertTrue(isValid)
        self.assertEqual(url, "success")

#
# appendUrl()
#
    # Test a valid URL
    def test_appendValidUrl(self):
        url = self.validUrl
        self.retriever.appendUrl(url)
        self.assertTrue(url in self.retriever.urls)

    # Test the same URL twice, which is considered a valid submission
    def test_appendValidSameUrl(self):
        url = self.validUrl
        self.retriever.appendUrl(url)
        self.retriever.appendUrl(url)
        self.assertTrue(url in self.retriever.urls)
        self.assertEqual(self.retriever.urls.count(url), 1)
        self.assertNotEqual(self.retriever.urls.count(url), 2)

    # Test an invalid String
    def test_appendInvalidUrlString(self):
        url = "notURL"
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test an int
    def test_appendInvalidUrlInt(self):
        url = 1
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test a double
    def test_appendInvalidUrlDouble(self):
        url = 0.5
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test None
    def test_appendInvalidUrlNone(self):
        url = None
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test empty list
    def test_appendInvalidUrlEmptyList(self):
        url = []
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test a list with valid URLs as entries
    def test_appendInvalidUrlListOfUrls(self):
        url = [self.validUrl, self.validUrl, self.validUrl]
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test an invalid URL like MOSSS
    def test_appendInvalidUrlLikeMoss(self):
        url = "http://moss.stanford.edu/results/12121212121212/"
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test a URL that's two valid URLs appended together
    def test_appendInvalidUrlTwoAppended(self):
        url = self.validUrl + self.validUrl
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test a valid URL that isn't MOSS
    def test_appendValidUrlNotMoss(self):
        url = "https://google.com"
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test a valid URL with space
    def test_appendValidUrlWithSpace(self):
        url = " " + self.validUrl + " "
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

    # Test a valid URL with new line
    def test_appendValidUrlWithNewLine(self):
        url = "\n" + self.validUrl + "\n"
        self.retriever.appendUrl(url)
        self.assertFalse(url in self.retriever.urls)

#
# populateResults()
#
    #

#
# getDuplicateUrls()
#
    # Test int
    def test_getDuplicateUrlsInt(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(1)
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test double
    def test_getDuplicateUrlsDouble(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(0.5)
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test empty string
    def test_getDuplicateUrlsString(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(" ")
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test single, valid url string
    def test_getDuplicateUrlsValidUrl(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(self.validUrl)
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test None
    def test_getDuplicateUrlsNone(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(None)
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test empty list
    def test_getDuplicateUrlsEmptyList(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test list of ints
    def test_getDuplicateUrlsIntList(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([1, 1, 1])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test list of doubles
    def test_getDuplicateUrlsDoubleList(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([0.5, 0.5, 0.5])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test list of Nones
    def test_getDuplicateUrlsNoneList(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([None, None, None])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test list of lists
    def test_getDuplicateUrlsListOfLists(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([[], [], []])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test mixed list
    def test_getDuplicateUrlsMixedList(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([1, " ", 0.5, None])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test mixed list with valid url
    def test_getDuplicateUrlsMixedListWithValidUrl(self):
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls([self.validUrl, " ", 1])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [])

    # Test no duplicates
    def test_getDuplicateUrlsNoDuplicates(self):
        urls = [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone()]
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(urls)
        self.assertListEqual(duplicates, [])
        self.assertListEqual(nonDuplicates, [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone()])

    # Test one duplicate
    def test_getDuplicateUrlsOneDuplicate(self):
        urls = [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone(), self.config.getMagicsquare()]
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(urls)
        self.assertListEqual(duplicates, [self.config.getMagicsquare()])
        self.assertListEqual(nonDuplicates, [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone()])

    # Test all duplicates
    def test_getDuplicateUrlsAllDuplicate(self):
        urls = [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone(),
                self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone()]
        duplicates, nonDuplicates = self.retriever.getDuplicateUrls(urls)
        self.assertListEqual(duplicates, [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone()])
        self.assertListEqual(nonDuplicates, [self.config.getMagicsquare(), self.config.getPalindrome(), self.config.getTwentyone()])

#
# validateData()
#
    # Tests all the correct types for Result object
    def test_validData(self):
        self.retriever.results =[self.results, self.results]
        self.assertTrue(self.retriever.validateData())

    # Tests all the incorrect types for Result object
    def test_invalidData(self):
        self.results.fileOne = 1
        self.results.fileTwo = 2
        self.results.fileOnePercent = "52"
        self.results.fileTwoPercent = "58"
        self.results.url = 51
        self.retriever.results = [self.results, self.results]
        self.assertFalse(self.retriever.validateData())

    def tearDown(self):
        self.retriever = None
        self.results = None


if __name__ == '__main__':
    unittest.main()
