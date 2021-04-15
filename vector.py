import math


class Vector:
    """Elementary vector used in 3d graphics"""
    def __init__(self, x0=0.0, x1=0.0, x2=0.0):
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2

    def __str__(self):
        return '({}, {}, {})'.format(self.x0, self.x1, self.x2)

    def __eq__(self, other):
        """Vectors comparison"""
        return self.x0 == other.x0 and self.x1 == other.x1 and self.x2 == other.x2

    def __add__(self, other):
        """Vectors addition"""
        return Vector(self.x0 + other.x0, self.x1 + other.x1, self.x2 + other.x2)

    def __sub__(self, other):
        """Vectors subtraction"""
        return Vector(self.x0 - other.x0, self.x1 - other.x1, self.x2 - other.x2)

    def __mul__(self, other):
        """Vector-scalar multiplication"""
        return Vector(self.x0 * other.x0, self.x1 * other.x1, self.x2 * other.x2)

    def __truediv__(self, other):
        """Vectors division"""
        try:
            return Vector(self.x0 / other.x0, self.x1 / other.x1, self.x2 / other.x2)
        except ZeroDivisionError:
            try:
                x0 = self.x0 / other.x0
            except:
                x0 = math.inf
            try:
                x1 = self.x1 / other.x1
            except:
                x1 = math.inf
            try:
                x2 = self.x2 / other.x2
            except:
                x2 = math.inf

            return Vector(x0, x1, x2)

    def multiply(self, other):
        """Vectors multiplication scalar"""
        assert not isinstance(other, Vector), 'operand < * > is not used in vector-scalar multiplication. ' \
                                              'You need apply method v.multiply(number) or vector*one_vector'
        return Vector(self.x0 * other, self.x1 * other, self.x2 * other)

    def divide(self, other):
        """Vectors multiplication scalar"""
        try:
            return Vector(self.x0 / other, self.x1 / other, self.x2 / other)
        except ZeroDivisionError:
            return Vector(math.inf, math.inf, math.inf)

    def dot(self, other):
        """Dot product of two vectors"""
        return self.x0 * other.x0 + self.x1 * other.x1 + self.x2 * other.x2

    def norm(self):
        """Vector norm"""
        return math.sqrt(self.dot(self))

    def normalize(self):
        """Vector normalize"""
        return self.divide(self.norm())


