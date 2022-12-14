import unittest

from Question13 import right_order, RightOrder


class TestsForQuestion13(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(RightOrder.YES, right_order(1, 2))
        self.assertEqual(RightOrder.NO, right_order(2, 1))
        self.assertEqual(RightOrder.CONTINUE, right_order(1, 1))

    def test_simple_lists(self):
        self.assertEqual(RightOrder.NO, right_order([2, 2, 3], [2, 1, 2]))
        self.assertEqual(RightOrder.YES, right_order([1, 2, 1], [1, 2, 2]))
        self.assertEqual(RightOrder.YES, right_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))
        self.assertEqual(RightOrder.CONTINUE, right_order([], []))

    # self.assertEquals(RightOrder.NO, right_order(2, 1))
        # self.assertEquals(RightOrder.CONTINUE, right_order(1, 1))

    def test_unequal_lists(self):
        self.assertEqual(RightOrder.YES, right_order([], [3]))
        self.assertEqual(RightOrder.NO, right_order([7, 7, 7, 7], [7, 7, 7]))

    def test_integer_v_list(self):
        self.assertEqual(RightOrder.NO, right_order(4, [3]))
        self.assertEqual(RightOrder.NO, right_order([4], 3))

    def test_examples(self):
        self.assertEqual(RightOrder.YES, right_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))
        self.assertEqual(RightOrder.YES, right_order([[1], [2, 3, 4]], [[1], 4]))
        self.assertEqual(RightOrder.NO, right_order([9], [[8, 7, 6]]))
        self.assertEqual(RightOrder.YES, right_order([[4, 4], 4, 4], [[4, 4], 4, 4, 4]))
        self.assertEqual(RightOrder.NO, right_order([[[]]], [[]]))

    def test_one(self):
        self.assertEqual(RightOrder.YES, right_order([8, 8], [8, 8, 8]))
        self.assertEqual(RightOrder.CONTINUE, right_order([8, 8, 8], [8, 8, 8]))
        self.assertEqual(RightOrder.YES,
                     right_order([[8, [[7, 10, 10, 5], [8, 4, 9]], 3, 5], [[[3, 9, 4], 5, [7, 5, 5]], [[3, 2, 5], [10], [5, 5], 0, [8]]], [4, 2, [], [[7, 5, 6, 3, 0], [4, 4, 10, 7], 6, [8, 10, 9]]], [[4, [], 4], 10, 1]], [[[[8], [3, 10], [7, 6, 3, 7, 4], 1, 8]]]))
