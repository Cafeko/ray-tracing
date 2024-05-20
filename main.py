from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *
from material import *

# Camera:
width = 400
heigth = 300
c = Camera(position=Point(1, 0, 0), target=Point(-20, 0, 0), screen_distance=100, screen_heigth=heigth, screen_width=width)

# Objetos:
p = Plane(Point(0, 0, -10), Vector(0, 0, 1), Material((0, 255, 0)))

# Matriz de cores:
matrix = c.start_ray_cast([p])

# Gerar imagem:
generate_image(matrix, width, heigth, "Imagem")

### Classe "Main"
 ## - Propósito: contém o ponto de entrada do programa, gerenciando a inicialização e execução do pipeline de renderização.
 ## - Funções Comuns: Configuração inicial, execução do loop principal do aplicativo.
