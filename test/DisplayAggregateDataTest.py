import unittest
from DisplayAggregateData import DisplayAggregateData


class MossURLsTests(unittest.TestCase):
    def setUp(self):
        self.Display = DisplayAggregateData()

    def test_invalid_Address(self):
        self.Display.set_Address("")

    def tearDown(self):
        self.Display = None


def main():
    print("Start")


if __name__ == '__main__':
    unittest.main()