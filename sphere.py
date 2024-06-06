from ray import *
from vector import *
from point import *
from object import *

class Sphere(Object):
    def __init__(self, center : Point, radius : float, color : tuple):
        super().__init__()
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
                times = []
                if t1 > self.parameter_min:
                    times.append(t1)
                if t2 > self.parameter_min:
                    times.append(t2)
                if len(times) > 0:
                    return {"t" : min(times), "color" : self.get_color()}
            else:
                t = (-b)/(2 * a)
                if t > self.parameter_min:
                    return {"t" : t, "color" : self.get_color()}
        # Raio não intersecta a esfera
        return None
    
    def get_color(self):
        return self.color
    
    def get_points(self):
        return [self.center]

    def get_center(self):
        return self.center
    
    def transform(self, transformation_matrix : Matrix):
        self.center = transformation_matrix.dot_product(self.center)


##Classe "Sphere"
 ## - Propósito: Representa uma esfera em 3D.
 ## - Funções Comuns: Definição de centro e raio, cálculos de interseção com raios.
