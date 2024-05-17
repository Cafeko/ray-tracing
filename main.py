from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *

# camera
c = Camera(position=Point(1, 0, 0), target=Point(-20, 0, 0), screen_distance=20, screen_heigth=200, screen_width=200)

# plano
p = Plane(Point(0, 0, -1), Vector(0, 0, 1), Material((0, 255, 0)))

def gerar_imagem_longe_da_camera():
    # Esfera longe da câmera:
    s = Sphere(Point(-60, 0, 0), 30, (255, 0, 0))

    # Matriz de cores:
    matrix = c.start_ray_cast([p, s])

    # Gerar imagem:
    generate_image(matrix, 200, 200, "Imagem_longe_da_camera")

def gerar_imagem_perto_da_camera():
    # Esfera perto da câmera:
    s = Sphere(Point(-30, 0, 0), 30, (255, 0, 0))

    # Matriz de cores:
    matrix = c.start_ray_cast([p, s])

    # Gerar imagem:
    generate_image(matrix, 200, 200, "Imagem_perto_da_camera")

def gerar_imagem_esquerda_e_acima():
    # Esfera a esquerda e acima:
    s = Sphere(Point(-60, 90, 20), 30, (255, 0, 0))

    # Matriz de cores:
    matrix = c.start_ray_cast([p, s])

    # Gerar imagem:
    generate_image(matrix, 200, 200, "Imagem_esquerda_e_acima")

def gerar_imagem_direita_e_acima():
    # Esfera a direita e acima:
    s = Sphere(Point(-60, -90, 20), 30, (255, 0, 0))

    # Matriz de cores:
    matrix = c.start_ray_cast([p, s])

    # Gerar imagem:
    generate_image(matrix, 200, 200, "Imagem_direita_e_acima")

 
def gerar_imagem_dois_circulos():
    # Esfera a direita e acima:
    s1 = Sphere(Point(-60, -90, 20), 30, (255, 0, 0))
    s2 = Sphere(Point(-60, 90, 20), 30, (255, 0, 0))

    # Matriz de cores:
    matrix = c.start_ray_cast([p, s1, s2])

    # Gerar imagem:
    generate_image(matrix, 200, 200, "Imagem_dois_circulos")

gerar_imagem_longe_da_camera()
gerar_imagem_perto_da_camera()
gerar_imagem_esquerda_e_acima()
gerar_imagem_direita_e_acima()
gerar_imagem_dois_circulos()
