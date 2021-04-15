from color import Color


class Material:
    """Properties of object"""
    def __init__(self, color=Color.read_hex("#000000"), ambient=0.1, diffuse=1.0, specular=1.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def color_at(self, position):
        return self.color