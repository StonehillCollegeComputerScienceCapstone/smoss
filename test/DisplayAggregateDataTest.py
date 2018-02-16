import unittest
import os
from DisplayAggregateData import DisplayAggregateData


class DisplayAggregateDataTest(unittest.TestCase):
    def setUp(self):
        self.Display = DisplayAggregateData()

    def test_Null_Address(self):
        self.assertFalse(self.Display.set_Address(None))

    def test_successful_post(self):
        self.assertTrue(self.Display.post())

    def test_form_HTML(self):
        self.assertTrue(self.Display.formHTML("test"))

    def test_print_to_file(self):
        file_name = "display_aggregate_data.txt"
        self.Display.formHTML("testing creation of file")
        self.assertTrue(self.Display.print_to_file(file_name))
        self.assertTrue(os.path.exists(file_name))

        # remove the generated file
        os.remove(file_name)

    def tearDown(self):
        self.Display = None


def main():
    print("Start")


if __name__ == '__main__':
    unittest.main()