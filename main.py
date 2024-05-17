from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *

# Camera:
c = Camera(position=Point(1, 0, 0), target=Point(-20, 0, 0), screen_distance=20, screen_heigth=200, screen_width=200)

# Objetos:
p = Plane(Point(0, 0, -1), Vector(0, 0, 1), Material((0, 255, 0)))
s = Sphere(Point(-35, 0, 0), 30, (255, 0, 0))

# Matriz de cores:
matrix = c.start_ray_cast([p, s])

# Gerar imagem:
generate_image(matrix, 200, 200, "Image")