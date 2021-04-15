class Scene:
    """All elements needed for the render"""

    def __init__(self, camera, objects, lights, height, width):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.height = height
        self.width = width
