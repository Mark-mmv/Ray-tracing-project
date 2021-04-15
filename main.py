import sys, os
from vector import *
from frame import Frame
from color import Color
from point import Point
from objects import Sphere
from scene import Scene
from engine import RenderRT


def main():
    HEIGHT = 300
    WIDTH = 400

    camera = Vector(0.0, 0.0, -1.0)
    objects = [Sphere(Point(0.0, 0.0, 0.0), 0.5, Color.read_hex("#AAFF00"))]
    scene = Scene(camera, objects, HEIGHT, WIDTH)
    engine = RenderRT()
    image = engine.render(scene)
    image.convert_to_png('Sphere test1.png')


if __name__ == '__main__':
    main()
