import unittest

from Question6 import find_marker

class TestsForQuestion6(unittest.TestCase):

    def test_marker(self):
        self.assertEqual(7, find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4))
        self.assertEqual(5, find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4))

    def test_message(self):
        self.assertEqual(19, find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14))
        self.assertEqual(23, find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14))
