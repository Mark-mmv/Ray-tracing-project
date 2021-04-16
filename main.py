import sys, os
import settings
from scene import Scene
from engine import RenderRT


def rendering():
    engine = RenderRT()
    mod = settings
    scene = Scene(mod.camera, mod.objects, mod.lights, mod.height, mod.width)
    image = engine.render(scene)
    image.convert_to_png('Spheres reflection.png')


if __name__ == '__main__':
    rendering()
