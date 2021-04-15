from ray import Ray
from math import sqrt


class Sphere:
    """This is object sphere"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersect(self, ray):
        """Find a intersection with the sphere"""
        ray_origin_to_center = ray.origin - self.center
        b = ray.direction.dot(ray_origin_to_center)
        c = ray_origin_to_center.dot(ray_origin_to_center) - self.radius * self.radius
        discriminant = b * b - c
        if discriminant >= 0:
            distance_coefficient = -b - sqrt(discriminant)
            if distance_coefficient > 0:
                return distance_coefficient
        return None
