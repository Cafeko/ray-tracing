from operations import Vector
from ray import Ray

class Camera:
    def __init__(self, position, target, screen_distance : float,
                 screen_heigth : int, screen_width  : int, up_vector : Vector =Vector(0,0,1)):
        """
        Inicializa a câmera, a posicionando e definindo seus valores.

        Args:
        position (Point): ponto em que a câmera está. 
        target (Point): ponto para o qual a câmera está olhando.
        screen_distance (float): distancia entre a câmera e a tela.
        screen_heigth (int): altura da tela.
        screen_width (int): largura da tela.
        up_vector (Vector): vetor que aponta para cima.
        """
        # Posições:
        self.position = position
        self.target = target
        #Screen:
        self.scr_dist : float = screen_distance
        self.scr_h : int = self.set_screen_heigth(screen_heigth)
        self.scr_w : int = self.set_screen_width(screen_width)
        # Vectors:
        self.vec_target : Vector = self.get_target_vector().normalize()
        self.vec_up : Vector = self.set_vector_up(up_vector)
        self.vec_u : Vector = self.vec_target.cross_product(self.vec_up).normalize()
        self.vec_v : Vector = self.vec_target.cross_product(self.vec_u).normalize()
        self.vec_w : Vector = -self.vec_target.normalize()
        # Ray
        self.ray : Ray = Ray(Vector(self.position[0], self.position[1], self.position[2]), Vector())
        self.current_pixel = [0,0]

    def get_target_vector(self):
        """
        Retorna o vetor que vai da posicão da câmera até a posição do target.
        
        Returns:
        Vector: vetor formado pela diferença entre o ponto do target e o ponto da posição da câmera.
        """
        result = (self.target[0] - self.position[0], self.target[1] - self.position[1], self.target[2] - self.position[2])
        return Vector(result[0], result[1], result[2])

    def set_screen_heigth(self, heigth : int):
        """
        Define o valor da altura da tela.
        Se o valor recebido for menor ou igual a zero, a altura é definida como 1.

        Args:
        heigth (int): valor da altura da tela; deve ser maior que zero.

        Returns:
        int: altura da tela.
        """
        if heigth <= 0:
            self.scr_h = 1
        else:
            self.scr_h = heigth
        return self.scr_h
    
    def set_screen_width(self, width : int):
        """
        Define o valor da largura da tela.
        Se o valor recebido for menor ou igual a zero, a largura é definida como 1.

        Args:
        width (int): valor da largura da tela; deve ser maior que zero.

        Returns:
        int: largura da tela.
        """
        if width <= 0:
            self.scr_w = 1
        else:
            self.scr_w = width
        return self.scr_w

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
        self.ray.change_direction((self.vec_target * self.scr_dist)) # ray aponta para o centro da tela.
        self.ray.change_direction((self.vec_v * -(self.scr_h/2))) # ray aponta para o topo da tela.
        self.ray.change_direction((self.vec_u * -(self.scr_w/2))) # ray aponta para o topo esquerdo da tela.
        # Posiciona o ray no centro do pixel:
        pixel_size = 1/self.scr_h
        # Faz o ray apontar para o centro do pixel (horizontalmente):
        if self.scr_h % 2 == 0:
            self.ray.change_direction((self.vec_u * (pixel_size/2)))
        # Faz o ray apontar para o centro do pixel (verticalmente):
        if self.scr_w % 2 == 0:
            self.ray.change_direction((self.vec_v * (pixel_size/2)))
    
    def start_ray_cast(self):
        """
        
        Args:
        Returns:
        """
        self.put_ray_in_start_position()
        start_direction : Vector = self.ray.get_direction()


c = Camera((0, 0, 0), (4, 3, 0.5), 1, 100, 200)
c.start_ray_cast()
#print(c.vec_u)
#print(c.vec_v)
#print(c.vec_w)
#print(c.vec_target)
#print(c.ray)