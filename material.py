from color import Color


class Material:
    """Properties of object"""
    def __init__(self, color=Color.read_hex("#000000"), ambient=1.0, diffuse=1.0, specular=0.2, reflection=0.4):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self, position):
        return self.color

class TextureMaterial:
    """Properties of texture"""
    def __init__(self, color1=Color.read_hex("#AAAA00"), color2=Color.read_hex("#00AAAA"),
                 ambient=1.0, diffuse=1.0, specular=0.0, reflection=0.4):
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self, position):
        if int((position.x0 +5.0) * 3.0) % 2 == int(position.x2 * 3.0) % 2:
            return self.color1
        return self.color2