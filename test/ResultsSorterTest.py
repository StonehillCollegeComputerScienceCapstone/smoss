import unittest
from ResultsSorter import ResultsSorter

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sr = ResultsSorter()
        self.sr.inputFileName = "csv.csv"

    def test_ValidInputFileLower(self):
        self.assertTrue(self.sr.isValidFilename())

    def test_ValidInputFileJustExtension(self):
        self.sr.inputFileName = ".csv"
        self.assertFalse(self.sr.isValidFilename())

    def test_ValidInputFileUpper(self):
        self.sr.inputFileName = "csv.CSV"
        self.assertTrue(self.sr.isValidFilename())

    def test_ValidInputFileXLS(self):
        self.sr.inputFileName = "csv.XLS"
        self.assertFalse(self.sr.isValidFilename())

    def test_ValidInputFileXLSX(self):
        self.sr.inputFileName = "csv.XLSX"
        self.assertFalse(self.sr.isValidFilename())

    #def test_MainList(self):
     #   self.sr.createMainList()
      #  self.assertEqual(3, len(self.sr.MOSSresults))

    def test_MainListBadFile(self):
        self.assertTrue(self.sr.createMainList())

    def test_User1List(self):
        self.sr.createMainList()
        self.sr.user1.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.user1))

    def test_InvalidUser1List(self):
        self.sr.createMainList()
        self.sr.user1.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.user1))

    def test_User2List(self):
        self.sr.createMainList()
        self.sr.user2.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.user2))

    def test_InvalidUser2List(self):
        self.sr.createMainList()
        self.sr.user2.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.user2))

    def test_FileName1List(self):
        self.sr.createMainList()
        self.sr.fileName1.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.fileName1))

    def test_InvalidFileName1List(self):
        self.sr.createMainList()
        self.sr.fileName1.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.fileName1))

    def test_FileName2List(self):
        self.sr.createMainList()
        self.sr.fileName2.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.fileName2))

    def test_InvalidFileName2List(self):
        self.sr.createMainList()
        self.sr.fileName2.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.fileName2))

    def test_Match1List(self):
        self.sr.createMainList()
        self.sr.match1.append("testString")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match1))

    def test_InvalidMatch1List(self):
        self.sr.createMainList()
        self.sr.match1.append("3")
        self.assertTrue(self.sr.isValidMatchedList(self.sr.match1))

    def test_InvalidMatch1DoubleList(self):
        self.sr.createMainList()
        self.sr.match1.append("3.0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match1))

    def test_InvalidZeroMatch1List(self):
        self.sr.createMainList()
        self.sr.match1.append("0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match1))

    def test_Match2List(self):
        self.sr.createMainList()
        self.sr.match2.append("testString")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match2))

    def test_InvalidMatch2List(self):
        self.sr.createMainList()
        self.sr.match2.append("3")
        self.assertTrue(self.sr.isValidMatchedList(self.sr.match2))

    def test_InvalidMatch2DoubleList(self):
        self.sr.createMainList()
        self.sr.match2.append("3.0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match2))

    def test_InvalidZeroMatch2List(self):
        self.sr.createMainList()
        self.sr.match2.append("0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.match2))

    def test_InvalidLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("testString")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.linesMatched))

    def test_InvalidFloatLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("3.0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.linesMatched))

    def test_InvalidZeroLinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("0")
        self.assertFalse(self.sr.isValidMatchedList(self.sr.linesMatched))

    def test_LinesMatchedList(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("3")
        self.assertTrue(self.sr.isValidMatchedList(self.sr.linesMatched))

    def test_URLList(self):
        self.sr.createMainList()
        self.sr.URL.append("testString")
        self.assertTrue(self.sr.isValidStringList(self.sr.URL))

    def test_InvalidURLList(self):
        self.sr.createMainList()
        self.sr.URL.append("3")
        self.assertFalse(self.sr.isValidStringList(self.sr.URL))

    def test_ValidLength(self):
        self.sr.createMainList()
        self.assertTrue(self.sr.isValidLength())

    def test_InvalidValidLength(self):
        self.sr.createMainList()
        self.sr.match2.append("testString")
        self.assertFalse(self.sr.isValidLength())

    def test_ValidateDatainvalidlength(self):
        self.sr.createMainList()
        self.sr.linesMatched.append("22")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidlength(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidFilename1(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("3")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidFilename1(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidFilename2(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("3")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidFilename2(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidMatch1(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("test")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidMatch1(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidMatch2(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("test")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidMatch2(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidURL(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("3")
        self.sr.linesMatched.append("22")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidURL(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidLinesMatched(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("test")
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataValidLinesMatched(self):
        self.sr.createMainList()
        self.sr.user1.append("User1")
        self.sr.user2.append("User2")
        self.sr.fileName1.append("test.java")
        self.sr.fileName2.append("hello.java")
        self.sr.match1.append("22")
        self.sr.match2.append("22")
        self.sr.URL.append("test.html")
        self.sr.linesMatched.append("22")
        self.assertTrue(self.sr.validateData())

    def test_ValidateDataInvalidInputFile(self):
        self.sr.createMainList()
        self.sr.inputFileName = "csv.XLS"
        self.assertFalse(self.sr.validateData())

    def test_ValidateDataInvalidInputFileCSV(self):
        self.sr.createMainList()
        self.sr.inputFileName = "csv.csv"
        self.assertTrue(self.sr.validateData())


    def tearDown(self):
        self.sr = None

if __name__ == '__main__':
    unittest.main()
