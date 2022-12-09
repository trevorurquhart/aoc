import unittest

from Question8 import transpose
from Question8 import reverse
from Question8 import can_view
from Question8 import is_visible
from Question8 import merge


class TestsForQuestion3(unittest.TestCase):

    def test_transpose(self):
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], transpose([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], transpose(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))

    def test_reverse(self):
        self.assertEqual([[3, 2, 1], [6, 5, 4], [9, 8, 7]], reverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_merge(self):
        self.assertEqual([[2, 4, 6], [8, 10, 12]],
                         merge([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], lambda x, y: x + y))

    def test_find_view(self):
        self.assertEqual([1, 3, 2, 1, 0], can_view([1, 5, 3, 2, 4]))

    def test_mark_visible(self):
        self.assertEqual([1, 1, 0, 1, 0], is_visible([1, 2, 2, 3, 1]))
