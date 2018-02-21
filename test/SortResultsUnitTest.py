import unittest
from SortResults import SortResults

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sr = SortResults();
        self.sr.inputFileName = "MOSSinput.csv"

    def testValidInputFileLower(self):
        self.assertTrue(self.sr.isValidFilename())

    def testValidInputFileJustExtension(self):
        self.sr.inputFileName = ".csv"
        self.assertFalse(self.sr.isValidFilename())

    def testValidInputFileUpper(self):
        self.sr.inputFileName = "MOSSresults.CSV"
        self.assertTrue(self.sr.isValidFilename())

    def testValidInputFileXLS(self):
        self.sr.inputFileName = "MOSSresults.XLS"
        self.assertFalse(self.sr.isValidFilename())

    def testValidInputFileXLSX(self):
        self.sr.inputFileName = "MOSSresults.XLSX"
        self.assertFalse(self.sr.isValidFilename())

    #def testMainList(self):
     #   self.sr.createMainList()
      #  self.assertEqual(3, len(self.sr.MOSSresults))

    def testMainListBadFile(self):
        self.assertTrue(self.sr.createMainList())

    def testUser1List(self):
        self.sr.createMainList()
        self.sr.user1.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.user1))

    def testInvalidUser1List(self):
        self.sr.createMainList()
        self.sr.user1.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.user1))

    def testUser2List(self):
        self.sr.createMainList()
        self.sr.user2.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.user2))

    def testInvalidUser2List(self):
        self.sr.createMainList()
        self.sr.user2.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.user2))

    def testFileName1List(self):
        self.sr.createMainList()
        self.sr.fileName1.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.fileName1))

    def testInvalidFileName1List(self):
        self.sr.createMainList()
        self.sr.fileName1.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.fileName1))

    def testFileName2List(self):
        self.sr.createMainList()
        self.sr.fileName2.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.fileName2))

    def testInvalidFileName2List(self):
        self.sr.createMainList()
        self.sr.fileName2.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.fileName2))

    def testMatch1List(self):
        self.sr.createMainList()
        self.sr.match1.append("testString")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match1))

    def testInvalidMatch1List(self):
        self.sr.createMainList()
        self.sr.match1.append("3")
        self.assertTrue(self.sr.isValidMatchedList(self.sr.match1))

    def testInvalidMatch1List(self):
        self.sr.createMainList()
        self.sr.match1.append("3.0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match1))

    def testInvalidZeroMatch1List(self):
        self.sr.createMainList()
        self.sr.match1.append("0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match1))

    def testMatch2List(self):
        self.sr.createMainList()
        self.sr.match2.append("testString")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match2))

    def testInvalidMatch2List(self):
        self.sr.createMainList()
        self.sr.match2.append("3")
        self.assertTrue(self.sr.isValidMatchedList(self.sr.match2))

    def testInvalidMatch2List(self):
        self.sr.createMainList()
        self.sr.match2.append("3.0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match2))

    def testInvalidZeroMatch2List(self):
        self.sr.createMainList()
        self.sr.match2.append("0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match2))

    def testInvalidLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("testString")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.linesMatched))

    def testInvalidFloatLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("3.0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.linesMatched))

    def testInvalidZeroLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.linesMatched))

    def testLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("3")
        self.assertTrue(self.sr.isValidMatchedList(self.sr.linesMatched))

    def testURLList(self):
        self.sr.createMainList()
        self.sr.URL.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.URL))

    def testInvalidURLList(self):
        self.sr.createMainList()
        self.sr.URL.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.URL))

   # def testValidLength(self):
    #    self.sr.createMainList()
     #   self.assertTrue(self.sr.isValidLength())

    #def testInvalidValidLength(self):
     #   self.sr.createMainList()
      #  self.sr.user2.append("testString")
       # self.assertFalse(self.sr.isValidLength())




    def tearDown(self):
        self.sr = None

    if __name__ == '__main__':
        unittest.main()
