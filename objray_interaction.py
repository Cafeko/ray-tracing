from ray import *

def verify_intersections(ray : Ray, objects : list):
    """
    Verifica se o raio colide com os objetos de uma lista de objetos.

    Args:
    ray (Ray): Raio o qual a colisão será verificada.
    objects (list): Lista de objetos que podem (ou não) colidir com o raio.

    Returns:
    dict: Dicionario que contem como chave os objetos que colidiram com o raio e como valores as informações da colisão.
    """
    intersection_info = None
    intersections_dict = {}
    for obj in objects:
        intersection_info = obj.intersects(ray)
        if intersection_info != None:
            intersections_dict[obj] = intersection_info
    return intersections_dict
    

def get_closest_object(intercetion_dict : dict):
    """
    Determina quais dos objetos está mais proximo do ponto de origem, a partir do parametro t
    que determina que ponto do raio bateu no objeto, o que tiver o menor t é o mais proximo.
    
    Args:
    intercetion_dict (dict): Dicionario que contem os objetos e as informações de colisão.

    Returns:
    Objeto mais proximo (com o menor t).
    """
    if len(intercetion_dict.keys()) > 0:
        closest_obj = None
        distance = None
        for k in intercetion_dict.keys():
            if closest_obj == None:
                closest_obj = k
                distance = intercetion_dict[k]["t"]
            else:
                if distance > intercetion_dict[k]["t"]:
                    closest_obj = k
                    distance = intercetion_dict[k]["t"]
        return closest_obj
    else:
        return None