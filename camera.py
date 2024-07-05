from vector import *
from point import *
from object import *
from ray import *
from environment import *
from lighting import *
from math import *
from objray_interaction import * 

class Camera:
    """
    Camera que faz o raycast.

    Atributos:
        position (Point): ponto em que a câmera está. 
        target (Point): ponto para o qual a câmera está olhando.
        screen_distance (float): distancia entre a câmera e a tela.
        fov_angle (float): angulo do campo de visão da camera.
        resolution_height (int): altura da tela.
        resolution_width (int): largura da tela.
        up_vector (Vector): vetor que aponta para cima.
    """
    def __init__(self, position : Point, target : Point, screen_distance : float, fov_angle: float,
                 resolution_height : int, resolution_width : int, up_vector : Vector =Vector(0,0,1)):
        # Posições:
        self.position : Point = position
        self.target : Point = target
        #Screen:
        self.scr_dist : float = screen_distance
        self.initial_scr_dist : float = self.scr_dist
        self.res_h : int = self.set_resolution_height(resolution_height)
        self.res_w : int = self.set_resolution_width(resolution_width)
        self.scr_size_x : float
        self.scr_size_y : float
        self.set_screen_size(fov_angle, self.scr_dist)
        # Vectors:
        self.vec_target : Vector = self.get_target_vector().normalize()
        self.vec_up : Vector = self.set_vector_up(up_vector)
        self.vec_u : Vector = self.vec_target.cross_product(self.vec_up).normalize()
        self.vec_v : Vector = self.vec_target.cross_product(self.vec_u).normalize()
        self.vec_w : Vector = -self.vec_target.normalize()
        self.vec_qx : Vector = self.scr_size_x/(self.res_w) * self.vec_u
        self.vec_qy : Vector = self.scr_size_y/(self.res_h) * self.vec_v
        # Ray
        self.ray : Ray = Ray(self.position, Vector())
        self.current_pixel = [0,0]

    def set_screen_size(self, fov_angle : float, screen_distance : float):
        """
        Define o tamanho da tela de acordo com a distancia e o FOV.
        Calcula a largura descobrindo o tamanho de metade da tela e depois multiplicando por dois.
        Calcula a altura a partir da escala da resolução da altura em relação a largura.
        
        Args:
        fov_angle (float): Angulo do campo de visão.
        screen_distance (float): distancia entre a tela e a camera.
        """
        # Angulo para radiano:
        half = fov_angle / 2.0
        rad = radians(half)
        # Calcula largura da tela:
        scr_half_x = screen_distance * tan(rad)
        self.scr_size_x = scr_half_x * 2
        # Calcula escala da altura em relação a largura:
        scale = self.res_h/self.res_w
        # Calcula altura da tela:
        self.scr_size_y = self.scr_size_x * scale

    def zoom(self, zoom_value : float):
        """ Da zoom na camera modificando a distancia entre a tela e a camera. """
        if self.scr_dist + zoom_value > 0:
            self.scr_dist += zoom_value


    def reset_zoom(self):
        """ Retorna a distancia da tela para seu valor inicial. """
        self.scr_dist = self.initial_scr_dist


    def get_target_vector(self):
        """
        Retorna o vetor que vai da posicão da câmera até a posição do target.
        
        Returns:
        Vector: vetor formado pela diferença entre o ponto do target e o ponto da posição da câmera.
        """
        return self.target - self.position


    def set_resolution_height(self, heigth : int):
        """
        Define o valor da altura da tela.
        Se o valor recebido for menor ou igual a zero, a altura é definida como 1.

        Args:
        heigth (int): valor da altura da tela; deve ser maior que zero.

        Returns:
        int: altura da tela.
        """
        if heigth <= 0:
            self.res_h = 1
        else:
            self.res_h = heigth
        return self.res_h
    

    def set_resolution_width(self, width : int):
        """
        Define o valor da largura da tela.
        Se o valor recebido for menor ou igual a zero, a largura é definida como 1.

        Args:
        width (int): valor da largura da tela; deve ser maior que zero.

        Returns:
        int: largura da tela.
        """
        if width <= 0:
            self.res_w = 1
        else:
            self.res_w = width
        return self.res_w


    def set_vector_up(self, vector : Vector):
        """
        Define o vector up da câmera, normalizando o vetor recebido como parametro.
        Se vetor for nulo, vetor up será Vector(0, 0, 1).

        Args:
        vector (Vector): vetor que será e passado para o vec_up.

        Returns:
        Vector: vetor que foi definido como vector up da câmera.
        """
        if vector != Vector(0, 0, 0):
            self.vec_up = vector.normalize()
        else:
            self.vec_up = Vector(0, 0, 1)
        return self.vec_up


    def put_ray_in_start_position(self):
        """Faz o ray apontar para o centro do pixel que fica no topo esquerdo da tela (cordenada (0, 0))."""
        # Muda a direção do ray para um vetor (0, 0, 0) e as cordenadas do pixel atual em (0, 0).
        self.ray.set_direction(Vector())
        self.current_pixel = [0,0]
        # Faz a direção do ray apontar para o topo esquerdo da tela:
        self.ray.change_direction((self.vec_w.invert() * self.scr_dist)) # ray aponta para o centro da tela.
        self.ray.change_direction((self.vec_v * -(self.scr_size_y/2))) # ray aponta para o topo da tela.
        self.ray.change_direction((self.vec_u * -(self.scr_size_x/2))) # ray aponta para o topo esquerdo da tela.
        # Posiciona o ray no centro do pixel:
        pixel_size_x = self.scr_size_x/self.res_w
        pixel_size_y = self.scr_size_y/self.res_h
        # Faz o ray apontar para o centro do pixel (horizontalmente):
        if self.res_w % 2 == 0:
            self.ray.change_direction((self.vec_u * (pixel_size_x/2)))
        # Faz o ray apontar para o centro do pixel (verticalmente):
        if self.res_h % 2 == 0:
            self.ray.change_direction((self.vec_v * (pixel_size_y/2)))
    

    def start_ray_cast(self, env : Environment):
        """
        Começa a fazer o processo de raycast, fazendo o raio passar por todos os pixels da tela e verificar se está
        atingindo algum objeto e dando a aquele pixel a cor do objeto atingido mais proximo.
        
        Args:
        objects (list): Lista de objetos que podem (ou não) colidir com o raio.

        Returns:
        matriz ([[(r, g, b)]]): Matriz com as cores dos pixels da tela.
        """
        screen_matrix = []
        self.put_ray_in_start_position()
        start_direction : Vector = self.ray.get_direction()
        for y in range(self.res_h):
            screen_matrix.append([])
            for x in range(self.res_w):
                self.ray.set_direction((start_direction + (x * self.vec_qx) + (y * self.vec_qy)))
                self.current_pixel = [x, y]
                intercections = verify_intersections(self.ray, env.get_objects())
                closest = get_closest_object(intercections)
                if closest != None:
                    intercection_point = self.ray.get_point_by_parameter(intercections[closest]["t"])
                    obj_material = intercections[closest]["material"]
                    surface_normal = intercections[closest]["normal"]
                    pixel_color = phong_lighting(env, obj_material, surface_normal, intercection_point, self.ray, 3)
                    pixel_color_tuple = pixel_color.to_tuple()
                    screen_matrix[y].append(pixel_color_tuple)
                else: 
                    screen_matrix[y].append(None)
        return screen_matrix


### Classe "Camera"
 ## - Propósito: Gerencia a perspectiva ou visão da cena 3D. Pode definir a posição, orientação e parâmetros de projeção da câmera.
## - Funções Comuns: Ajuste de posição e direção da câmera, configuração de projeção (perspectiva ou ortográfica).

