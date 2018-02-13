import unittest
from SortResults import SortResults

class MyTestCase(unittest.TestCase):

    def testValidInputFileLower(self):
        sr = SortResults()
        sr.fileName = "MOSSresults.csv"
        self.assertTrue(sr.isValidFilename())

    def testValidInputFileUpper(self):
        sr = SortResults()
        sr.fileName = "MOSSresults.CSV"
        self.assertTrue(sr.isValidFilename())

    def testValidInputFileXLS(self):
        sr = SortResults()
        sr.fileName = "MOSSresults.XLS"
        self.assertFalse(sr.isValidFilename())

    def testValidInputFileXLSX(self):
        sr = SortResults()
        sr.fileName = "MOSSresults.XLSX"
        self.assertFalse(sr.isValidFilename())

    if __name__ == '__main__':
        unittest.main()
