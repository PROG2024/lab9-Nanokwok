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

    def test_invoking(self):
        self.assertEqual(self.c1.count, 1)
        self.assertEqual(self.c1.count, 1)




