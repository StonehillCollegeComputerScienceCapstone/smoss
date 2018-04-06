import unittest
from FileRetrieval import FileRetrieval


class FileRetrievalTest(unittest.TestCase):
    def setUp(self):
        self.inputFile = FileRetrieval()

    def test_validStringFile(self):
        self.assertTrue(self.inputFile.readFile("FileInput.txt"))

    def test_invalidStringFile(self):
        self.assertFalse(self.inputFile.readFile("Invalid"))
        self.assertFalse(self.inputFile.readFile(1))

    def test_correctNumberOfLinesRead(self):
        self.inputFile.readFile("FileInput.txt")
        self.assertEqual(len(self.inputFile.urlList), 3)

    def tearDown(self):
        self.inputFile = None

if __name__ == '__main__':
    unittest.main()
