from color import *
from point import Point
from vector import *
from material import *

class Light:
    def __init__(self, color : Color, position : Point):
        self.color = color
        self.position = position
    
def phong_lighting(ambient_light : Color, lights_list : list, object_material : Material, surface_normal : Vector, collision_point : Point):
    ambient_value = ambient_lighting(object_material.ambient, ambient_light)
    others_value = sum_of_lights(lights_list, object_material, surface_normal, collision_point)
    return ambient_value + others_value


def ambient_lighting(ambient_coef : float, ambient_light : Color):
    return ambient_light * ambient_coef


def sum_of_lights(lights_list : list, object_material : Material, surface_normal : Vector, collision_point : Point):
    total_light = Color(0, 0, 0)
    for light in lights_list:
        # Difusa:
        to_light_vector = (light.position - collision_point).normalize()
        difuse_light = difuse_lighting(light.color, object_material.color, object_material.difusion, surface_normal, to_light_vector)
        # Especular:
        specular_light = specular_lighting()
        # Somatorio:
        total_light += difuse_light + specular_light
    return total_light

def difuse_lighting(light_intensity : Color, object_color : Color, difuse_coef : float, normal : Vector, light_vector):
    return light_intensity * object_color * difuse_coef * (normal.dot_product(light_vector))


def specular_lighting():
    return Color(0, 0, 0)