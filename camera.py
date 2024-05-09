from operations import Vector

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
        self.scr_h : int = 1
        self.scr_w : int = 1
        self.set_screen_heigth(screen_heigth)
        self.set_screen_width(screen_width)
        # Vectors:
        self.vec_target : Vector = self.get_target_vector().normalize()
        self.vec_up : Vector = up_vector.normalize()
        self.vec_u : Vector = self.vec_target.cross_product(self.vec_up)
        self.vec_v : Vector = self.vec_target.cross_product(self.vec_v)
        self.vec_w : Vector = -self.vec_target
        # Ray
        self.ray : Vector = Vector()
        self.current_pixel = [0,0]
        self.put_ray_in_start_position()

    def get_target_vector(self):
        """
        Retorna o vetor que vai da posicão da câmera até a posição do target.
        
        Returns:
        Vector: vetor formado pela diferença entre o ponto do target e o ponto da posição da câmera.
        """
        result = self.target - self.position
        return Vector(result[0], result[1], result[2])

    def set_screen_heigth(self, heigth : int):
        """
        Define o valor da altura da tela.
        Se o valor recebido for menor ou igual a zero, a altura é definida como 1.

        Args:
        heigth (int): valor da altura da tela; deve ser maior que zero.
        """
        if heigth <= 0:
            self.scr_h = 1
        else:
            self.scr_h = heigth
    
    def set_screen_width(self, width : int):
        """
        Define o valor da largura da tela.
        Se o valor recebido for menor ou igual a zero, a largura é definida como 1.

        Args:
        width (int): valor da largura da tela; deve ser maior que zero.
        """
        if width <= 0:
            self.scr_h = 1
        else:
            self.scr_h = width

    def put_ray_in_start_position(self):
        """Posiciona o ray no centro do pixel que fica no topo esquerdo da tela (cordenada (0, 0))."""
        # Torna a direção do ray em um vetor (0, 0, 0) e as cordenadas do pixel atual em (0, 0).
        self.ray = Vector()
        self.current_pixel = [0,0]
        # Posiciona o ray no topo esquerdo da tela:
        self.ray = self.vec_target * self.scr_dist # ray vai para o centro da tela.
        self.ray = self.ray + (self.vec_v * -(self.scr_h/2)) # ray vai para o topo da tela.
        self.ray = self.ray + (self.vec_u * -(self.scr_w/2)) # ray vai para o topo esquerdo da tela.
        # Posiciona o ray no centro do pixel:
        pixel_size = 1/self.scr_h
        # posiciona o ray no centro do pixel (horizontalmente):
        if self.scr_h % 2 == 0:
            self.ray = self.ray + (self.vec_u * (pixel_size/2))
        # posiciona o ray no centro do pixel (verticalmente):
        if self.scr_w % 2 == 0:
            self.ray = self.ray + (self.vec_v * (pixel_size/2))
    
    def start_ray_cast():
        """
        
        Args:
        Returns:
        """
        pass