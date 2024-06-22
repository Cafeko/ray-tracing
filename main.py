from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *
from material import *
from color import *
from environment import *
import time

def move_object(obj, vector):
    obj.move(vector)
    print(f"{time.time() - start_time:^7.4f} -- {obj.__class__.__name__} movido")

def scale_object(obj, vector):
    obj.scale(vector)
    print(f"{time.time() - start_time:^7.4f} -- {obj.__class__.__name__} escalado")

def rotate_object(obj, angle, axis):
    obj.rotate(angle, axis)
    print(f"{time.time() - start_time:^7.4f} -- {obj.__class__.__name__} rotacionado")

start_time = time.time()
print(f"{time.time() - start_time:^7.4f} -- Inicio")


# Cria objetos:
# Plano
material_plano = Material(Color(0, 255, 0))
p = Plane(Point(0, 0, -20), Vector(0, 0, 1), material_plano, False, False, 150)
# Mesh
material_mesh = Material(Color(255, 0, 0))
vertices = [Point(0, 0, 50), Point(40, 0, 0), Point(0, 25, 0), Point(0, -25, 0)]
triplas = [(0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)]
m = Mesh(vertices, triplas, 4, 4, material_mesh)
# Esfera
material_esfera = Material(Color(0, 0, 255))
s = Sphere(Point(-40 , 20, 50), 20, material_esfera)
objects_list = [p, m, s]

print(f"{time.time() - start_time:^7.4f} -- Objetos criados")


# Ambiente:
main_env = Environment(objects_list, Color(0, 0, 255))

print(f"{time.time() - start_time:^7.4f} -- Ambiente criados")


# Camera:
width = 600
heigth = 450
c = Camera(position=Point(100, 0, 0), target=Point(0, 0, 0), screen_distance=20,
           resolution_height=heigth, resolution_width=width)

print(f"{time.time() - start_time:^7.4f} -- Camera criada")


# Gerar imagem:
print(f"{time.time() - start_time:^7.4f} -- Raycast iniciado")
matrix = c.start_ray_cast(main_env)
print(f"{time.time() - start_time:^7.4f} -- Raycast finalizado")
generate_image(matrix, width, heigth, "Imagem")
print(f"{time.time() - start_time:^7.4f} -- Imagem 1 criada")


# Transformações:
move_object(s, Vector(0, -80, 0))
s.scale(2)
move_object(p, Vector(0, 0, 0))
rotate_object(p, 10, 0)
p.scale(15)
move_object(m, Vector(-2000, 0, 0))
scale_object(m, Vector(50, 50, 50))
rotate_object(m, 90, 2)

print(f"{time.time() - start_time:^7.4f} -- Transformações realizadas")


# Gerar imagem (pós transformação):
print(f"{time.time() - start_time:^7.4f} -- Raycast iniciado")
matrix = c.start_ray_cast(main_env)
print(f"{time.time() - start_time:^7.4f} -- Raycast finalizado")
generate_image(matrix, width, heigth, "Imagem2")
print(f"{time.time() - start_time:^7.4f} -- Imagem 2 criada")
print(f"{time.time() - start_time:^7.4f} -- Fim")



### Classe "Main"
## - Propósito: contém o ponto de entrada do programa, gerenciando a inicialização e execução do pipeline de renderização.
## - Funções Comuns: Configuração inicial, execução do loop principal do aplicativo.
