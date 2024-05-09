from operations import Vector

class Camera:
    def __init__(self, position, target, screen_distance : float,
                 screen_heigth : int, screen_width  : int, up_vector : Vector =Vector(0,0,1)):
        self.position = position
        self.target = target
        self.vec_target : Vector = set_target_vector()
        self.scr_dist : float = screen_distance
        self.scr_h : int = screen_heigth
        self.scr_w : int = screen_width
        self.vec_up : Vector = up_vector.normalize()
        self.vec_u : Vector = self.vec_target.cross_product(self.vec_up)
        self.vec_v : Vector = self.vec_target.cross_product(self.vec_v)
        self.vec_w : Vector = -self.vec_target

        def set_target_vector(self):
            result = self.target - self.position
            return Vector(result[0], result[1], result[2])


