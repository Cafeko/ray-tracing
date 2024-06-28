from color import *
from point import Point
from vector import *
from material import *
from ray import Ray

class Light:
    """
    Fonte de luz que ilumina objetos em um ambiente.

    Atributos:
        color (Color): Intencidade da luz para as cores (R,G,B).
        position (Point): Ponto em que a fonte de luz está.
    """
    def __init__(self, color : Color, position : Point):
        self.color = color
        self.position = position
    
def phong_lighting(ambient_light : Color, lights_list : list, object_material : Material, surface_normal : Vector, collision_point : Point, ray : Ray):
    """
    Executa a equação de iluminação de Phong para determinar a cor em um ponto.
    
    Args:
    ambient_light (Color): Luz do ambiente.
    lights_list ([Light]): Lista de luzes que estão no ambiente.
    object_material (Material): Material do objeto atingido pelo raio, contem os coeficientes do material.
    surface_normal (Vector): Vetor normal da suprefice onde houve a colisão do raio com o objeto.
    collision_point (Point): Ponto onde houve a colisão do raio com o objeto.
    ray (Ray): raio que colidiu com o objeto.
    """
    ambient_value = ambient_lighting(object_material.ambient, ambient_light)
    others_value = sum_of_lights(lights_list, object_material, surface_normal, collision_point, ray)
    return ambient_value + others_value


def ambient_lighting(ambient_coef : float, ambient_light : Color):
    """
    Calcula a parte ambiental da equação de iluminação de Phong.
    
    Args:
    ambient_coef (float): coeficiente ambiente do objeto.
    ambient_light (Color): luz do ambiente.
    """
    return ambient_light * ambient_coef


def sum_of_lights(lights_list : list, object_material : Material, surface_normal : Vector, collision_point : Point, ray : Ray):
    """ Faz o somatorio das luzes geradas pelas fontes de luzes do ambiente no ponto. """
    total_light = Color(0, 0, 0)
    for light in lights_list:
        surface_normal = surface_normal.normalize()
        to_light_vector = (light.position - collision_point).normalize() # Vetor que aponta do ponto para a luz.
        # Difusa:
        object_color_normaized = object_material.color.to_normalized_tuple()
        difuse_light = difuse_lighting(light.color, object_color_normaized, object_material.difusion, surface_normal, to_light_vector)
        # Especular:
        # Vetor de luz refletido
        specular_reflection_vector = (2 * surface_normal * (surface_normal.dot_product(to_light_vector)) - to_light_vector).normalize()
        # Vetor que aponta do ponto até a camera
        to_observer_vector = (ray.get_direction().invert()).normalize()
        specular_light = specular_lighting(light.color, object_material.specular, specular_reflection_vector, to_observer_vector, object_material.roughness)
        # Somatorio:
        total_light += difuse_light + specular_light
    return total_light


def difuse_lighting(light_intensity : Color, object_color_normalized : Color, difuse_coef : float, normal : Vector, light_vector : Vector):
    """
    Calcula a parte difusa da equação de iluminação de Phong.
    
    Args:
    light_intensity (Color): Intencidade da luz gerada pela fonte de luz para as cores (R,G,B)
    object_color_normalized (Color): Cor do objeto normalizada, entre 0 e 1.
    difuse_coef (float): coeficiente de difusão do objeto.
    normal (Vector): vetor normal da superfice no ponto de colisão.
    light_vector (Vector): Vetor que aponta do ponto de colisão até a luz.
    """
    return light_intensity * object_color_normalized * difuse_coef * normal.dot_product(light_vector)


def specular_lighting(light_intensity : Color, specular_coef : float, specular_reflection : Vector, observer_vector : Vector, object_roughness : float):
    """
    Calcula a parte especular da equação de iluminação de Phong.
    
    Args:
    light_intensity (Color): Intencidade da luz gerada pela fonte de luz para as cores (R,G,B)
    specular_coef (float): coeficiente especular do objeto.
    specular_reflection (Vector): Vetor da luz refletido.
    observer_vector (Vector): Vetor que aponta do ponto de colisão até a camera.
    object_roughness (float): coeficiente de rugosidade do objeto.
    """
    return light_intensity * specular_coef * (max(specular_reflection.dot_product(observer_vector), 0) ** object_roughness)