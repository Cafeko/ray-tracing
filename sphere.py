from ray import *
from vector import *
from point import *
from object import *

class Sphere(Object):
    def __init__(self, center : Point, radius : float, color : tuple):
        self.center : Point = center
        self.radius : float = radius
        self.color : tuple = color

    def intersects(self, ray_origin : Vector, ray_direction : Vector):
        oc = ray_origin - self.center
        a = ray_direction.dot_product(ray_direction)
        b = 2.0 * oc.dot_product(ray_direction)
        c = oc.dot_product(oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            # Raio intersecta a esfera
            return True
        else:
            # Raio não intersecta a esfera
            return False
    
    def get_color(self):
        pass

def ray_color(ray_origin, ray_direction, objects):
    for obj in objects:
        if obj.intersect(ray_origin, ray_direction):
            # Se houver interseção, o ponto está na sombra
            return Vector(0.0, 0.0, 0.0)  # Cor preta
    # Se não houver interseção, o ponto está iluminado
    unit_direction = ray_direction / ray_direction.magnitude()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Vector(1.0, 1.0, 1.0) + t * Vector(0.5, 0.7, 1.0)

# Exemplo de uso
ray_origin = Vector(0, 0, 0)
ray_direction = Vector(0, 0, -1)
sphere1 = Sphere(Vector(0, 0, -3), 1, Vector(1, 0, 0))  # Esfera vermelha
sphere2 = Sphere(Vector(0, -1001, -3), 1000, Vector(0, 0, 1))  # Chão azul

objects = [sphere1, sphere2]

print(ray_color(ray_origin, ray_direction, objects))  # Saída: [0.5 0.7 1. ]