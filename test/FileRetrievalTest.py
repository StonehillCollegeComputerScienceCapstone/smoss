import unittest
from FileRetrieval import FileRetrieval
from Config import Config


class FileRetrievalTest(unittest.TestCase):
    def setUp(self):
        self.inputFile = FileRetrieval()
        self.config = Config()

    def test_validStringFile(self):
        self.assertTrue(self.inputFile.readFile(self.config.getMossUrlsFile()))

    def test_invalidStringFile(self):
        self.assertFalse(self.inputFile.readFile("Invalid"))
        self.assertFalse(self.inputFile.readFile(1))

    def test_correctNumberOfLinesRead(self):
        self.inputFile.readFile(self.config.getMossUrlsFile())
        self.assertEqual(len(self.inputFile.urlList), 5)

    def tearDown(self):
        self.inputFile = None

if __name__ == '__main__':
    unittest.main()
