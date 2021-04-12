import sys, os
import unittest

sys.path.append(os.getcwd())
from main import *


class MainTests(unittest.TestCase):
    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main()