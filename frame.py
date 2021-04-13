from color import Color


class Frame:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, y=0, x=0, rgb=Color(0.0, 0.0, 0.0)):
        self.pixels[y][x] = rgb
