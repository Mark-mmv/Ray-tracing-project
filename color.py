from vector import Vector


class Color(Vector):
    """Implement color of pixel as a 3d-vector"""
    @classmethod
    def read_hex(cls, hexcolor="#000000"):
        x0 = int(hexcolor[1:3], 16) / 255.0
        x1 = int(hexcolor[3:5], 16) / 255.0
        x2 = int(hexcolor[5:7], 16) / 255.0
        return cls(x0, x1, x2)

