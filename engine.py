from frame import Frame
from ray import Ray
from point import Point
from color import Color


class RenderRT:
    """Render 3d to 2d for using ray-tracing"""

    def render(self, scene):
        height = scene.height
        width = scene.width
        self.max_depth = 3
        self.min_distance = 0.001
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

    def ray_trace(self, scene, ray, depth=0):
        color = Color.read_hex("#444422")
        distance_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.direction.multiply(distance_hit)
        hit_normal = obj_hit.normal(hit_pos)
        color = self.color_add(obj_hit, hit_pos, hit_normal, scene)
        if depth < self.max_depth:
            new_ray_pos = hit_pos + hit_normal.multiply(self.min_distance)
            new_ray_dir = ray.direction - hit_normal.multiply(2 * ray.direction.dot(hit_normal))
            new_ray = Ray(new_ray_pos, new_ray_dir)
            color += self.ray_trace(scene, new_ray, depth+1).multiply(obj_hit.material.reflection)
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

    def color_add(self, obj_hit, hit_pos, hit_normal, scene):
        material = obj_hit.material
        obj_color = material.color_at(hit_pos)
        to_cam = scene.camera - hit_pos
        color = Color.read_hex("#000000").multiply(material.ambient)
        specular_k = 50

        for light in scene.lights:
            ray_light = Ray(hit_pos, light.position - hit_pos)

            # Diffuse illumination Lambert
            color += (obj_color.multiply(material.diffuse * max(hit_normal.dot(ray_light.direction), 0)))

            # Specular illumination Blinn-Phong
            half_vector = (ray_light.direction + to_cam).normalize()
            color += (light.color.multiply(material.specular * max(hit_normal.dot(half_vector), 0) ** specular_k))

        return color