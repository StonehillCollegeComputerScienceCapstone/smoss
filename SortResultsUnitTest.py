import unittest
from SortResults import SortResults

class MyTestCase(unittest.TestCase):

    def setUpClass(self):
        self.sr = SortResults()

    def testValidInputFilecsv(self):
        self.fileName = "MOSSresults.csv"
        self.assertTrue(self.isValidFilename())

    def testValidInputFileCSV(self):
        self.fileName = "MOSSresults.CSV"
        self.assertTrue(self.isValidFilename())

    def testValidInputFileXLS(self):
        self.fileName = "MOSSresults.XLS"
        self.assertFalse(self.isValidFilename())

    def testValidInputFileXLS(self):
        self.fileName = "MOSSresults.XLSX"
        self.assertFalse(self.isValidFilename())

    def testEmptyFile(self):
        self.fileName = "MOSSresults.csv"
        self.assertFalse(self.isEmptyFile())

    def tearDownClass(cls):
        print("Tests complete")

    if __name__ == '__main__':
        unittest.main()
