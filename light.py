from color import *
from point import Point

class Light:
    def __init__(self, color : Color, position : Point):
        self.color = color
        self.position = position
    
def phong_lighting(ambient_coef : float, ambient_light : Color, object_color : Color):
    ambient_value = ambient_lighting(ambient_coef, ambient_light)
    others_value = Color(0, 0, 0)
    ## Outra parte da formula
    return ambient_value + others_value + object_color

def ambient_lighting(Ka : float, Ia : Color):
    return Ia * Ka