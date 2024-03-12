"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

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

