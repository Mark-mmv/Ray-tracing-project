import sys, os
from vector import *
from frame import Frame
from color import Color


def main():
    HEIGHT = 300
    WIDTH = 400
    img = Frame(HEIGHT, WIDTH)

    for row in range(HEIGHT):
        for i in range(WIDTH):
            px = Color(x0=(1+i)*0.005, x1=(1+i)*0.01, x2=(1+i)*0.003)
            img.set_pixel(row, i, px)

    img.convert_to_png('Test_img_1.png')


if __name__ == '__main__':
    main()



