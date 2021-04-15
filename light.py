from color import Color


class Light:
    """Light source"""

    def __init__(self, position, color=Color.read_hex("#FFFFFF")):
        self.position = position
        self.color = color
