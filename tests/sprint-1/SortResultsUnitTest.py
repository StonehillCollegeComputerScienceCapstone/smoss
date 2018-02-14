import unittest
from SortResults import SortResults

class MyTestCase(unittest.TestCase):

    def testValidInputFileLower(self):
        sr = SortResults()
        sr.inputFileName = "MOSSresults.csv"
        self.assertTrue(sr.isValidFilename())

    def testValidInputFileJustExtension(self):
        sr = SortResults()
        sr.inputFileName = ".csv"
        self.assertFalse(sr.isValidFilename())

    def testValidInputFileUpper(self):
        sr = SortResults()
        sr.inputFileName = "MOSSresults.CSV"
        self.assertTrue(sr.isValidFilename())

    def testValidInputFileXLS(self):
        sr = SortResults()
        sr.inputFileName = "MOSSresults.XLS"
        self.assertFalse(sr.isValidFilename())

    def testValidInputFileXLSX(self):
        sr = SortResults()
        sr.inputFileName = "MOSSresults.XLSX"
        self.assertFalse(sr.isValidFilename())

    def testMainList(self):
        sr = SortResults()
        sr.inputFileName = "MOSSinput.csv"
        sr.createMainList()
        self.assertEqual(3, len(sr.MOSSresults))

    def testMainListBadFile(self):
        sr = SortResults()
        sr.inputFileName = "MOSSinput.csv"
        self.assertTrue(sr.createMainList())

    def testUser1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.user1.append("testString")
        self.assertTrue(sr.isValidStringList(sr.user1))

    def testInvalidUser1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.user1.append("3")
        self.assertFalse(sr.isValidStringList(sr.user1))

    def testUser2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.user2.append("testString")
        self.assertTrue(sr.isValidStringList(sr.user2))

    def testInvalidUser2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.user2.append("3")
        self.assertFalse(sr.isValidStringList(sr.user2))

    def testFileName1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.fileName1.append("testString")
        self.assertTrue(sr.isValidStringList(sr.fileName1))

    def testInvalidFileName1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.fileName1.append("3")
        self.assertFalse(sr.isValidStringList(sr.fileName1))

    def testFileName2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.fileName2.append("testString")
        self.assertTrue(sr.isValidStringList(sr.fileName2))

    def testInvalidFileName2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.fileName2.append("3")
        self.assertFalse(sr.isValidStringList(sr.fileName2))

    def testMatch1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.match1.append("testString")
        self.assertFalse(sr.isValidMatchedList(sr.match1))

    def testInvalidMatch1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.match1.append("3")
        self.assertTrue(sr.isValidMatchedList(sr.match1))

    def testInvalidMatch1List(self):
        sr = SortResults()
        sr.createMainList()
        sr.match1.append("3.0")
        self.assertFalse(sr.isValidMatchedList(sr.match1))

    def testMatch2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.match2.append("testString")
        self.assertFalse(sr.isValidMatchedList(sr.match2))

    def testInvalidMatch2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.match2.append("3")
        self.assertTrue(sr.isValidMatchedList(sr.match2))

    def testInvalidMatch2List(self):
        sr = SortResults()
        sr.createMainList()
        sr.match2.append("3.0")
        self.assertFalse(sr.isValidMatchedList(sr.match2))

    def testInvalidLinesMatchedList(self):
        sr = SortResults()
        sr.createMainList()
        sr.linesMatched.append("testString")
        self.assertFalse(sr.isValidMatchedList(sr.linesMatched))

    def testInvalidFloatLinesMatchedList(self):
        sr = SortResults()
        sr.createMainList()
        sr.linesMatched.append("3.0")
        self.assertFalse(sr.isValidMatchedList(sr.linesMatched))

    def testLinesMatchedList(self):
        sr = SortResults()
        sr.createMainList()
        sr.linesMatched.append("3")
        self.assertTrue(sr.isValidMatchedList(sr.linesMatched))

    def testURLList(self):
        sr = SortResults()
        sr.createMainList()
        sr.URL.append("testString")
        self.assertTrue(sr.isValidStringList(sr.URL))

    def testInvalidURLList(self):
        sr = SortResults()
        sr.createMainList()
        sr.URL.append("3")
        self.assertFalse(sr.isValidStringList(sr.URL))

    def testInvalidURLList(self):
        sr = SortResults()
        sr.createMainList()
        sr.URL.append("3")
        self.assertFalse(sr.isValidStringList(sr.URL))

    def testValidLength(self):
        sr = SortResults()
        sr.createMainList()
        self.assertTrue(sr.isValidLength())

    def testInvalidValidLength(self):
        sr = SortResults()
        sr.createMainList()
        sr.user2.append("testString")
        self.assertFalse(sr.isValidLength())




    if __name__ == '__main__':
        unittest.main()
