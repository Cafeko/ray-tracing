from PIL import Image

# Create ppm:
width = input("Largura: ")
heigth = input("Altura: ")
image_file = open("Imagem.ppm", "w")
image_file.write("P3\n")
image_file.write(width + " " + heigth + "\n")
image_file.write("255\n")
for y in range(int(heigth)):
    for x in range(int(width)):
        r = (y * 255) // int(heigth)
        c = "255"
        image_file.write(str(r) + " " + c + " " + c)
        image_file.write("\n")
image_file.close()
# Convert ppm to jpg:
image_path = ".\Imagem"
image = Image.open(image_path + ".ppm")
image.save(image_path + ".jpg")


import numpy as np

class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def intersect(self, ray_origin, ray_direction):
        oc = ray_origin - self.center
        a = np.dot(ray_direction, ray_direction)
        b = 2.0 * np.dot(oc, ray_direction)
        c = np.dot(oc, oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            # Raio intersecta a esfera
            return True
        else:
            # Raio não intersecta a esfera
            return False

def ray_color(ray_origin, ray_direction, objects):
    for obj in objects:
        if obj.intersect(ray_origin, ray_direction):
            # Se houver interseção, o ponto está na sombra
            return np.array([0.0, 0.0, 0.0])  # Cor preta
    # Se não houver interseção, o ponto está iluminado
    unit_direction = ray_direction / np.linalg.norm(ray_direction)
    t = 0.5 * (unit_direction[1] + 1.0)
    return (1.0 - t) * np.array([1.0, 1.0, 1.0]) + t * np.array([0.5, 0.7, 1.0])

# Exemplo de uso
ray_origin = np.array([0, 0, 0])
ray_direction = np.array([0, 0, -1])
sphere1 = Sphere(np.array([0, 0, -3]), 1, np.array([1, 0, 0]))  # Esfera vermelha
sphere2 = Sphere(np.array([0, -1001, -3]), 1000, np.array([0, 0, 1]))  # Chão azul

objects = [sphere1, sphere2]

print(ray_color(ray_origin, ray_direction, objects))  # Saída: [0.5 0.7 1. ]

#- classe Sphere representa uma esfera com centro, raio e cor.
#- O método intersect na classe Sphere verifica se um raio dado (definido por sua origem e direção) intersecta a esfera.
#- A função ray_color calcula a cor de um ponto na cena, verificando se o raio da câmera até esse ponto intersecta alguma esfera. Se o raio intersectar alguma esfera, o ponto está na sombra, então a cor retornada é preta. Se não houver interseção, o ponto está iluminado e sua cor é calculada com base em uma iluminação ambiente simples.
#- O exemplo final mostra como usar essas classes e funções para calcular a cor de um ponto na cena.
