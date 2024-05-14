from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *

# Camera:
c = Camera(Point(1, 0, 0), Point(-20, 0, 0), 20, 200, 200)

# Objetos:
p = Plane(Point(0, 0, -1), Vector(0, 0, 1), Material((0, 255, 0)))
s = Sphere(Point(-40, 0, 0), 30, (255, 0, 0))

# Matriz de cores:
matrix = c.start_ray_cast([p, s])

# Gerar imagem:
generate_image(matrix, 200, 200, "Image")