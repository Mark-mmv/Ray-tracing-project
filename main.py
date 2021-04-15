import sys, os
from vector import *
from frame import Frame
from color import Color
from point import Point
from objects import Sphere
from scene import Scene
from engine import RenderRT
from light import Light
from material import Material


class Viewer:
    def __init__(self):
        self.width, self.height = [1200, 900]
        self.resolution = [self.width, self.height]

    def rendering(self):
        camera = Vector(0.0, 0.0, -1.0)
        objects = [Sphere(Point(0.0, 0.0, 0.0), 0.5, Material(Color.read_hex("#88CCFF"), ambient=1.0, diffuse=1.0, specular=0.5))]
        lights = [Light(Point(8, -15, -10), Color.read_hex("#FFFFFF"))]
        scene = Scene(camera, objects, lights, self.height, self.width)
        engine = RenderRT()
        image = engine.render(scene)
        image.convert_to_png('Sphere test1.png')


if __name__ == '__main__':
    app = Viewer()
    app.rendering()
