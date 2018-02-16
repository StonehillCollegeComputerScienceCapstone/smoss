import unittest
from FileRetrieval import FileRetrieval


class FileRetrievalTest(unittest.TestCase):
    def setUp(self):
        self.input_file = FileRetrieval()

    def test_Valid_String_File(self):
        self.assertTrue(self.input_file.open_and_read_file("FileInput.txt"))

    def test_Invalid_String_File(self):
        self.assertFalse(self.input_file.open_and_read_file("Invalid"))
        self.assertFalse(self.input_file.open_and_read_file(1))

    def test_Correct_Number_of_Lines_Read(self):
        self.input_file.open_and_read_file("FileInput.txt")
        self.assertEqual(len(self.input_file.url_list), 11)

#    def test_File_Open_With_Popup(self): #this is a pop up to open a file if we need it for the future
#        self.assertTrue(self.input_file.pop_up_open_file()) #actually a file here
#        self.assertFalse(self.input_file.pop_up_open_file()) #cancel opening a file

    def tearDown(self):
        self.input_file = None


def main():
    print("Start")


if __name__ == '__main__':
    unittest.main()
