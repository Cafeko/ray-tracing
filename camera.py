from operations import Vector

class Camera:
    def __init__(self, position, target, screen_distance : float,
                 screen_heigth : int, screen_width  : int, up_vector : Vector =Vector(0,0,1)):
        self.position = position
        self.target = target
        self.vec_target : Vector = self.set_target_vector()
        self.scr_dist : float = screen_distance
        self.scr_h : int = self.set_screen_heigth(screen_heigth)
        self.scr_w : int = self.set_screen_width(screen_width)
        self.vec_up : Vector = up_vector.normalize()
        self.vec_u : Vector = self.vec_target.cross_product(self.vec_up)
        self.vec_v : Vector = self.vec_target.cross_product(self.vec_v)
        self.vec_w : Vector = -self.vec_target
        self.ray : Vector = Vector
        self.current_pixel = [0,0]
        self.put_ray_in_start_position()

    def set_target_vector(self):
        result = self.target - self.position
        return Vector(result[0], result[1], result[2])

    def set_screen_heigth(self, heigth):
        if heigth <= 0:
            self.scr_h = 1
        else:
            self.scr_h = heigth
    
    def set_screen_width(self, width):
        if width <= 0:
            self.scr_h = 1
        else:
            self.scr_h = width

    def put_ray_in_start_position(self):
        # Posiciona o ray no topo esquerdo da tela:
        self.ray = self.vec_target * self.scr_dist # ray vai para o centro da tela.
        self.ray = self.ray + (self.vec_v * -(self.scr_h/2)) # ray vai para o topo da tela.
        self.ray = self.ray + (self.vec_u * -(self.scr_w/2)) # ray vai para o topo esquerdo da tela.
        # Posiciona o ray no centro do pixel:
        pixel_size = 1/self.scr_h
        if self.scr_h % 2 == 0:
            self.ray = self.ray + (self.vec_u * (pixel_size/2)) # posiciona o ray no centro do pixel (horizontalmente).
        if self.scr_w % 2 == 0:
            self.ray = self.ray + (self.vec_v * (pixel_size/2)) # posiciona o ray no centro do pixel (verticalmente).
        self.current_pixel = [0,0]
    
    def start_ray_cast():
        pass
