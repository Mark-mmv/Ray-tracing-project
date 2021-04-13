import sys, os
import unittest
import math

sys.path.append(os.getcwd())
from vector import *


class VectorsTest(unittest.TestCase):
    """Vector class tests"""
    def setUp(self):
        self.vec1 = Vector(6.0, -2.0, 3.0)
        self.vec2 = Vector(-1.0, 2.0, 3.0)
        self.vec_one = Vector(1.0, 1.0, 1.0)
        self.vec_zero = Vector(0.0, 0.0, 0.0)

    def test_add(self):
        """Test of vectors addition"""
        self.assertEqual((self.vec1 + self.vec2).__str__(), Vector(5.0, 0.0, 6.0).__str__())
        self.assertEqual((self.vec1 + self.vec_one).__str__(), Vector(7.0, -1.0, 4.0).__str__())

    def test_subtract(self):
        """Test of vectors subtraction"""
        self.assertEqual((self.vec1 - self.vec2).__str__(), Vector(7.0, -4.0, 0.0).__str__())

    def test_multiply(self):
        """Test of vectors multiplication"""
        self.assertEqual((self.vec1 * self.vec2).__str__(), Vector(-6.0, -4.0, 9.0).__str__())
        self.assertEqual(self.vec1 * self.vec_zero, Vector(0.0, 0.0, 0.0))

    def test_divide(self):
        """Test of vectors multiplication"""
        self.assertEqual((self.vec1 / self.vec2).__str__(), Vector(-6.0, -1.0, 1.0).__str__())
        self.assertEqual((self.vec1 / self.vec_zero).__str__(), Vector(math.inf, math.inf, math.inf).__str__())

    def test_multiply_scalar(self):
        """Test of vector-scalar multiplication"""
        dot = self.vec1.multiply(2)
        self.assertEqual(getattr(dot, 'x0'), 12.0)

    def test_divide_scalar(self):
        """Test of vector-scalar division"""
        div = self.vec1.divide(2)
        self.assertEqual(getattr(div, 'x0'), 6 / 2)
        div = self.vec1.divide(0)
        self.assertEqual(getattr(div, 'x2'), math.inf)

    def test_dot(self):
        """Test of dot product vectors"""
        self.assertEqual(self.vec1.dot(self.vec2), -1.0)

    def test_norm(self):
        """Test of vector norm"""
        self.assertEqual(self.vec1.norm(), 7.0)

    def test_normalize(self):
        """Test of vector normalisation"""
        self.assertEqual(self.vec1.divide(self.vec1.norm()), Vector(6.0/7, -2.0/7, 3.0/7))
        vec = Vector(3.0, 4.0, 0.0)
        self.assertEqual(vec.divide(vec.norm()).__str__(), Vector(3 / 5, 4 / 5, 0 / 5).__str__())


if __name__ == '__main__':
    unittest.main()
