import math


class Vector:
    """Elementary vector used in 3d graphics"""
    def __init__(self, x0=0.0, x1=0.0, x2=0.0):
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2

    def __str__(self):
        return '({}, {}, {})'.format(self.x0, self.x1, self.x2)

    def dot(self, other):
        """Dot product of two vectors"""
        return self.x0 * other.x0 + self.x1 * other.x1 + self.x2 * other.x2

    def norm(self):
        """Vector norm"""
        return math.sqrt(self.dot(self))
