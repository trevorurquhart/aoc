import unittest
import re

from Question5 import find_move
from Question5 import parse_crates


class TestsForQuestion3(unittest.TestCase):

    def test_priority(self):
        self.assertEqual([1, 3, 2], find_move("move 1 from 3 to 2"))
        self.assertEqual([13, 7, 8], find_move("move 13 from 7 to 8"))

    def test_crates(self):
        self.assertEqual([[], ["G"], [], [], ["P"], [], [], ["M"]], parse_crates("    [G]         [P]         [M]"))
