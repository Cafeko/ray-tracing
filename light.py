from color import *
from point import Point
from vector import *
from material import *
from ray import Ray

class Light:
    def __init__(self, color : Color, position : Point):
        self.color = color
        self.position = position
    
def phong_lighting(ambient_light : Color, lights_list : list, object_material : Material, surface_normal : Vector, collision_point : Point, ray : Ray):
    ambient_value = ambient_lighting(object_material.ambient, ambient_light)
    others_value = sum_of_lights(lights_list, object_material, surface_normal, collision_point, ray)
    return ambient_value + others_value


def ambient_lighting(ambient_coef : float, ambient_light : Color):
    return ambient_light * ambient_coef


def sum_of_lights(lights_list : list, object_material : Material, surface_normal : Vector, collision_point : Point, ray : Ray):
    total_light = Color(0, 0, 0)
    for light in lights_list:
        surface_normal = surface_normal.normalize()
        to_light_vector = (light.position - collision_point).normalize()
        # Difusa:
        object_color_normaized = object_material.color.to_normalized_tuple()
        difuse_light = difuse_lighting(light.color, object_color_normaized, object_material.difusion, surface_normal, to_light_vector)
        # Especular:
        specular_reflection_vector = (2 * surface_normal * (surface_normal.dot_product(to_light_vector)) - to_light_vector).normalize()
        to_observer_vector = (ray.get_direction().invert()).normalize()
        specular_light = specular_lighting(light.color, object_material.specular, specular_reflection_vector, to_observer_vector, object_material.roughness)
        # Somatorio:
        total_light += difuse_light + specular_light
    return total_light


def difuse_lighting(light_intensity : Color, object_color_normalized : Color, difuse_coef : float, normal : Vector, light_vector):
    return light_intensity * object_color_normalized * difuse_coef * (normal.dot_product(light_vector))


def specular_lighting(light_intensity : Color, specular_coef : float, specular_reflection : Vector, observer_vector : Vector, object_roughness : float):
    return light_intensity * specular_coef * (max(specular_reflection.dot_product(observer_vector), 0) ** object_roughness)