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
                x1 = (-b + sqrt(delta))/(2 * a)
                x2 = (-b - sqrt(delta))/(2 * a)
                p1 = a*x1*x1 + b*x1 + c
                p2 = a*x2*x2 + b*x2 + c
                return [ray.get_point_by_parameter(p1), ray.get_point_by_parameter(p2)]
            else:
                x = (-b)/(2 * a)
                p = a*x*x + b*x + c
                return ray.get_point_by_parameter(p)
        else:
            # Raio não intersecta a esfera
            return None
    
    def get_color(self):
        return self.color