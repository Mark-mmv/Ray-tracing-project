class Scene:
    """All elements needed for the render"""

    def __init__(self, camera, objects, height, width):
        self.camera = camera
        self.objects = objects
        self.height = height
        self.width = width
