import unittest
from Question3 import priority
from Question3 import find_common_items
from Question3 import find_badge


class TestsForQuestion3(unittest.TestCase):

    def test_priority(self):
        self.assertEqual(1, priority('a'))
        self.assertEqual(26, priority("z"))
        self.assertEqual(27, priority("A"))
        self.assertEqual(52, priority("Z"))

    def test_find_common_items(self):
        self.assertEqual({"a"}, find_common_items("aa"))
        self.assertEqual(set(), find_common_items("ab"))
        self.assertEqual({"p"}, find_common_items("vJrwpWtwJgWrhcsFMMfFFhFp"))

    def test_find_badge(self):
        self.assertEqual(set("A"), find_badge(["Ac", "PA", "bbbA"]))
