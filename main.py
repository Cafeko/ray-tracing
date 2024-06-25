from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *
from material import *
from color import *
from environment import *
from light import *
import time

start_time = time.time()
print(f"{time.time() - start_time:^7.4f} -- Inicio")


# Cria objetos:
# Plano
material_plano = Material(Color(0, 255, 0))
p = Plane(Point(0, 0, -20), Vector(0, 0, 1), material_plano, False, True)
# Mesh
material_mesh = Material(Color(255, 0, 0))
vertices = [Point(0, 0, 50), Point(40, 0, 0), Point(0, 25, 0), Point(0, -25, 0)]
triplas = [(0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)]
m = Mesh(vertices, triplas, 4, 4, material_mesh)
# Esfera
material_esfera = Material(Color(0, 0, 200))
s = Sphere(Point(0 , 40, 50), 20, material_esfera)
objects_list = [p, s]

print(f"{time.time() - start_time:^7.4f} -- Objetos criados")


# Luzes:
light1 = Light(Color(255, 255, 255), Point(0, -40, 50))
lights_list = [light1]

print(f"{time.time() - start_time:^7.4f} -- Luzes criadas")


# Ambiente:
main_env = Environment(objects_list, Color(0, 0, 255), lights_list)

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
print(f"{time.time() - start_time:^7.4f} -- Imagem criada")

print(f"{time.time() - start_time:^7.4f} -- Fim")



### Classe "Main"
## - Propósito: contém o ponto de entrada do programa, gerenciando a inicialização e execução do pipeline de renderização.
## - Funções Comuns: Configuração inicial, execução do loop principal do aplicativo.
