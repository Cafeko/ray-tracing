from color import *
from point import *
from vector import *
from material import *
from ray import *
from environment import Environment
from objray_interaction import *

def phong_lighting(env : Environment, object_material : Material, surface_normal : Vector,
                   collision_point : Point, ray : Ray, recursions_level : int):
    """
    Executa a equação de iluminação de Phong para determinar a cor em um ponto.
    
    Args:
    env (Environment): Ambiente que contem os objetos e as luzes.
    object_material (Material): Material do objeto atingido pelo raio, contem os coeficientes do material.
    surface_normal (Vector): Vetor normal da suprefice onde houve a colisão do raio com o objeto.
    collision_point (Point): Ponto onde houve a colisão do raio com o objeto.
    ray (Ray): raio que colidiu com o objeto.
    recursions_level (Int): define quantas recursões serão feitas para gerar o reflexo do objeto.
    """
    if recursions_level > 0:
        objects_list = env.get_objects()
        ambient_light = env.get_color()
        lights_list = env.get_lights()
        ambient_value = ambient_lighting(object_material.ambient, ambient_light)
        others_value = sum_of_lights(lights_list, object_material, surface_normal, collision_point, ray, objects_list)
        reflection_value = reflection_lighting(env, object_material, surface_normal, collision_point, ray, recursions_level)
        return (ambient_value + others_value) + reflection_value
    else:
        return Color(0, 0, 0)


def ambient_lighting(ambient_coef : float, ambient_light : Color):
    """
    Calcula a parte ambiental da equação de iluminação de Phong.
    
    Args:
    ambient_coef (float): coeficiente ambiente do objeto.
    ambient_light (Color): luz do ambiente.
    """
    return ambient_light * ambient_coef


def sum_of_lights(lights_list : list, object_material : Material, surface_normal : Vector,
                  collision_point : Point, ray : Ray, objects_list : list):
    """ Faz o somatorio das luzes geradas pelas fontes de luzes do ambiente no ponto. """
    total_light = Color(0, 0, 0)
    for light in lights_list:
        surface_normal = surface_normal.normalize()
        to_light_vector = (light.position - collision_point).normalize() # Vetor que aponta do ponto para a luz.
        # Sombra:
        to_light_ray = Ray(collision_point, to_light_vector)
        if verify_intersections(to_light_ray, objects_list) != {}:
            continue
        # Difusa:
        object_color_normaized = object_material.color.to_normalized_tuple()
        difuse_light = difuse_lighting(light.color, object_color_normaized, object_material.difusion, surface_normal, to_light_vector)
        # Especular:
        # Vetor de luz refletido
        specular_reflection_vector = reflect_vector(surface_normal, to_light_vector)
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


def reflection_lighting(env : Environment, object_material : Material, surface_normal : Vector,
                        collision_point : Point, ray : Ray, recursions_level : int):
    if object_material.reflection != 0:
        inverted_ray = (ray.get_direction().invert()).normalize()
        reflection_vector = reflect_vector(surface_normal, inverted_ray)
        reflect_ray = Ray(collision_point, reflection_vector)
        object_colission_info = get_reflected_object_info(env.get_objects(), reflect_ray)
        if object_colission_info != None:
            reflection_intercection_point = ray.get_point_by_parameter(object_colission_info["t"])
            reflection_obj_material = object_colission_info["material"]
            reflection_surface_normal = object_colission_info["normal"]
            reflection_color = phong_lighting(env, reflection_obj_material, reflection_surface_normal,
                                  reflection_intercection_point, reflect_ray, (recursions_level - 1))
            reflection_light = reflection_color * object_material.reflection
            return reflection_light
        else:
            return Color(0, 0, 0)
    else:
        return Color(0, 0, 0)


def transmission_lighting(env : Environment, object_material : Material, surface_normal : Vector,
                        collision_point : Point, ray : Ray, recursions_level : int):
    pass


def get_reflected_object_info(objects_list : list, ray : Ray):
    intercections = verify_intersections(ray, objects_list)
    closest = get_closest_object(intercections)
    if closest != None:
        return intercections[closest]
    else:
        return None


def reflect_vector(surface_normal : Vector, vector : Vector):
    surface_normal = surface_normal.normalize()
    vector = vector.normalize()
    return (2 * surface_normal * (surface_normal.dot_product(vector)) - vector).normalize()