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



    if __name__ == '__main__':
        unittest.main()
