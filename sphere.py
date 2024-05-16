from ray import *
from vector import *
from point import *
from object import *

class Sphere(Object):
    def __init__(self, center : Point, radius : float, color : tuple):
        self.center : Point = center
        self.radius : float = radius
        self.color : tuple = color

    def intersects(self, ray : Ray):
        ray_direction = ray.get_direction()
        oc : Vector = ray.get_origin() - self.center
        a = ray_direction.dot_product(ray_direction)
        b = 2.0 * oc.dot_product(ray_direction)
        c = oc.dot_product(oc) - self.radius * self.radius
        delta = b * b - 4 * a * c
        if delta >= 0:
            # Raio intersecta a esfera
            if delta > 0:
                t1 = (-b + sqrt(delta))/(2 * a)
                t2 = (-b - sqrt(delta))/(2 * a)
                points = []
                if t1 > 0:
                    points.append(ray.get_point_by_parameter(t1))
                if t2 > 0:
                    points.append(ray.get_point_by_parameter(t2))
                if len(points) > 1:
                    return points
                elif len(points) == 1:
                    return points[0]
                else:
                    return None
            else:
                t = (-b)/(2 * a)
                if t > 0:
                    return ray.get_point_by_parameter(t)
                else:
                    return None
        else:
            # Raio não intersecta a esfera
            return None
    
    def get_color(self):
        return self.color