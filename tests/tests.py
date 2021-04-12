import sys, os
import unittest

sys.path.append(os.getcwd())
from vector import *


class VectorsTest(unittest.TestCase):
    def setUp(self):
        self.vec1 = Vector(6.0, -2.0, 3.0)

    def test_norm(self):
        self.assertEqual(self.vec1.norm(), 7.0)

if __name__ == '__main__':
    unittest.main()