from image import *
from camera import *
from plane import *
from sphere import *
from mesh import *
from material import *
from color import *
from environment import *
from light import *
import scenes as scene
import time

start_time = time.time()
print(f"{time.time() - start_time:^7.4f} -- Inicio")


# Cena:
cena = scene.EXEMPLO
c = cena["camera"]
env = cena["env"]

print(f"{time.time() - start_time:^7.4f} -- Cena Carregada")


# Gerar imagem:
width = c.res_w
heigth = c.res_h

print(f"{time.time() - start_time:^7.4f} -- Raycast iniciado")

matrix = c.start_ray_cast(env)

print(f"{time.time() - start_time:^7.4f} -- Raycast finalizado")

generate_image(matrix, width, heigth, "Imagem")
print(f"{time.time() - start_time:^7.4f} -- Imagem criada")


print(f"{time.time() - start_time:^7.4f} -- Fim")



### Classe "Main"
## - Propósito: contém o ponto de entrada do programa, gerenciando a inicialização e execução do pipeline de renderização.
## - Funções Comuns: Configuração inicial, execução do loop principal do aplicativo.
