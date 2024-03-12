"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from circle import Circle
import unittest
import math


class TestCircle(unittest.TestCase):
    def test_positive_radius(self):
        c = Circle(5)
        c2 = Circle(10)
        c3 = Circle(20)
        self.assertEqual(c.radius, 5)
        self.assertEqual(c2.radius, 10)
        self.assertEqual(c3.radius, 20)
        self.assertEqual(c.get_area(), math.pi * 5 ** 2)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            c = Circle(-5)

    def test_zero_radius(self):
        zero = Circle(0)
        self.assertEqual(zero.radius, 0)

