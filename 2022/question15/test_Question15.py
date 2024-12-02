import unittest

from Question15 import sum_ranges


class TestsForQuestion13(unittest.TestCase):

    def test_sum_two_ranges(self):
        self.assertEqual(sum_ranges([(1, 2), (2, 3)]), 3)
        self.assertEqual(sum_ranges([(1, 5), (5, 5)]), 5)
        self.assertEqual(sum_ranges([(-1, 5), (5, 5)]), 7)
        self.assertEqual(sum_ranges([(-1, 5), (0, 5)]), 7)
        self.assertEqual(sum_ranges([(-3, -2), (-2, -1)]), 3)
        self.assertEqual(sum_ranges([(-3, -2), (-2, -2)]), 2)
        self.assertEqual(sum_ranges([(-3, -2), (-2, 2)]), 6)

    def test_sum_two_ranges(self):
        self.assertEqual(sum_ranges([(1, 2), (2, 3), (4, 5)]), 5)
        self.assertEqual(sum_ranges([(1, 5), (5, 5), (5, 6)]), 6)
        self.assertEqual(sum_ranges([(-4, -2), (-1, 5), (5, 5)]), 10)
        self.assertEqual(sum_ranges([(-4, -3), (-1, 5), (0, 5)]), 9)
        self.assertEqual(sum_ranges([(-3, -3), (-3, -2), (-2, -1)]), 3)
        self.assertEqual(sum_ranges([(-100, -50), (-3, -2), (-2, -2)]), 53)
        self.assertEqual(sum_ranges([(-3, -2), (-2, -2), (-3, -2), (-2, 2)]), 6)
