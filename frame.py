from color import Color
import PIL.Image


class Frame:
    """Frame for image in used 3d graphics"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, y=0, x=0, rgb=Color(0.0, 0.0, 0.0)):
        """Colored a pixel"""
        self.pixels[y][x] = rgb

    def convert_to_ppm(self, filename=str('Non_name_img.ppm')):
        def to_int8(color):
            return round(max(min(color * 255, 255), 0))

        with open(filename, 'w') as img_file:
            img_file.write('P3 {} {}\n255\n'.format(self.width, self.height))
            for row in self.pixels:
                for px in row:
                    img_file.write('{} {} {} '.format(to_int8(px.x0), to_int8(px.x1), to_int8(px.x2)))
                img_file.write('\n')

    def convert_to_png(self, filename=str('Non_name_img.png')):
        """The converter raw data to png format"""
        def to_int8(color):
            return int(max(min(color * 255, 255), 0))

        pixels_out = []
        for row in self.pixels:
            for px in row:
                pixels_out.append((to_int8(px.x0), to_int8(px.x1), to_int8(px.x2)))

        image_output = PIL.Image.new(mode='RGB', size=[self.width, self.height])
        image_output.putdata(pixels_out)
        image_output.save(filename)

