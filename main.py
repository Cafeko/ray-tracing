from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *
from material import *
import time

def move_object(obj, vector):
    obj.move(vector)
    print(f"{time.time() - start_time:^7.4f} -- {obj.__class__.__name__} movido")

start_time = time.time()
print(f"{time.time() - start_time:^7.4f} -- Inicio")

# Camera:
width = 600
heigth = 450
c = Camera(position=Point(60, 0, 0), target=Point(0, 0, 0), screen_distance=100, screen_heigth=heigth, screen_width=width)

print(f"{time.time() - start_time:^7.4f} -- Camera criada")


# Cria objetos:
p = Plane(Point(0, 0, -10), Vector(0, 0, 1), Material((0, 255, 0)), False)
vertices = [Point(0, 0, 50), Point(40, 0, 0), Point(0, 25, 0), Point(0, -25, 0)]
triplas = [(0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)]
m = Mesh(vertices, triplas, 4, 4, (255, 0, 0))
s = Sphere(Point(-40 , 40, 50), 35, (0, 0, 255))
objects_list = [p, m, s]

print(f"{time.time() - start_time:^7.4f} -- Objetos criados")


# Gerar imagem:
print(f"{time.time() - start_time:^7.4f} -- Raycast iniciado")
matrix = c.start_ray_cast(objects_list)
print(f"{time.time() - start_time:^7.4f} -- Raycast finalizado")
generate_image(matrix, width, heigth, "Imagem")
print(f"{time.time() - start_time:^7.4f} -- Imagem 1 criada")

# Transformações:
move_object(s, Vector(0, -80, 0))
p.move(Vector(0, 0, 0))
m.move(Vector(-1000, 0, 0))
m.scale(Vector(50, 50, 50))
m.rotate(90, 2)
p.rotate(0, 0)

print(f"{time.time() - start_time:^7.4f} -- Transformações realizadas")


# Gerar imagem (pós transformação):
print(f"{time.time() - start_time:^7.4f} -- Raycast iniciado")
matrix = c.start_ray_cast(objects_list)
print(f"{time.time() - start_time:^7.4f} -- Raycast finalizado")
generate_image(matrix, width, heigth, "Imagem2")
print(f"{time.time() - start_time:^7.4f} -- Imagem 2 criada")
print(f"{time.time() - start_time:^7.4f} -- Fim")



### Classe "Main"
## - Propósito: contém o ponto de entrada do programa, gerenciando a inicialização e execução do pipeline de renderização.
## - Funções Comuns: Configuração inicial, execução do loop principal do aplicativo.
