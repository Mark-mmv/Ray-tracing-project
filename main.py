import sys, os
import settings
from scene import Scene
from engine import RenderRT


def rendering():
    engine = RenderRT()
    scene = Scene(settings.camera, settings.objects, settings.lights, settings.height, settings.width)
    image = engine.render(scene)
    image.convert_to_png('Spheres reflection.png')


if __name__ == '__main__':
    rendering()
