import sys, os
from vector import *
from frame import Frame
from color import Color


def main():
    WIDTH = 3
    HEIGHT = 2
    img = Frame(WIDTH, HEIGHT)
    green = Color(x0=0, x1=1, x2=0)
    img.set_pixel(0, 0, green)



if __name__ == '__main__':
    main()



