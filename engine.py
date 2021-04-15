from frame import Frame
from ray import Ray
from point import Point
from color import Color


class RenderRT:
    """Render 3d to 2d for using ray-tracing"""

    def render(self, scene):
        height = scene.height
        width = scene.width
        cam_ratio = float(width / height)
        x0 = -1.0
        x1 = 1.0
        x_step = (x1 - x0) / (width - 1)
        y0 = -1.0 / cam_ratio
        y1 = 1.0 / cam_ratio
        y_step = (y1 - y0) / (height - 1)

        camera = scene.camera
        image = Frame(height, width)

        for j in range(height):
            y = y0 + j * y_step
            for i in range(width):
                x = x0 + i * x_step
                ray = Ray(camera, Point(x, y) - camera)
                image.set_pixel(j, i, self.ray_trace(scene, ray))
        return image

    def ray_trace(self, scene, ray):
        distance_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return Color(100, 100, 100)
        hit_pos = ray.origin + ray.direction.multiply(distance_hit)
        color = self.color_add(obj_hit, hit_pos, scene)
        return color

    def find_nearest(self, ray, scene):
        distance_min = None
        obj_hit = None
        for obj in scene.objects:
            distance = obj.intersect(ray)
            if distance is not None and (obj_hit is None or distance < distance_min):
                distance_min = distance
                obj_hit = obj
        return (distance_min, obj_hit)

    def color_add(self, obj_hit, hit_pos, scene):
        return obj_hit.material