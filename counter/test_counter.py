"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.c1 = Counter()
        self.c2 = Counter()

    def test_add_one(self):
        self.assertEqual(self.c1.count, 1)
        self.assertEqual(self.c1.count, 1)
        self.assertEqual(self.c1.count, 1)

        self.c1.increment()
        self.assertEqual(self.c1.count, 2)

    def test_same_obj(self):
        self.assertIs(self.c1, self.c2)

    def test_shares_same_count(self):
        self.c2.increment()
        self.assertEqual(self.c1.count, 3)
