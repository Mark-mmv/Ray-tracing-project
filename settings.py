from vector import *
from frame import Frame
from color import Color
from point import Point
from objects import Sphere
from light import Light
from material import Material, TextureMaterial


height = 600
width = 800
camera = Vector(0.0, 0.0, -1.0)
objects = [Sphere(Point(0.0, 10001.0, 0.0), 10000.0,
                  TextureMaterial(color1=Color.read_hex("#AAAA00"), color2=Color.read_hex("#334444"))),
           Sphere(Point(0.0, 0.0, 4.0), 1.0, Material(Color.read_hex("#88CCFF"))),
           Sphere(Point(2.0, -1.0, 3.0), 1.0, Material(Color.read_hex("#884466")))]
lights = [Light(Point(14, -15, -15), Color.read_hex("#FFFFFF"))]
