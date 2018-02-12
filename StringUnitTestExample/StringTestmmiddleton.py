#!/usr/bin/python3
# noinspection PyPep8

import unittest

class MiddletonTestClass (unittest.TestCase):


    def test_equal (self):
        self.assertEqual (1, 1)

    def test_upper_equal (self):
        self.assertEqual ('test'.upper (), 'TEST')


if __name__ == '__main__':
    unittest.main()
