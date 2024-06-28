from object import *
from color import *
from light import *

class Environment:
    """
    Ambiente que contem os objetos.

    Atributos:
        objects ([Object]): Lista de objetos que estão no ambiente.
        lights ([Light]): Lista de luzes que estão no ambiente.
        color (Color): Cor do ambiente.
    """
    def __init__(self, objects : list, lights : list, color : Color = Color(0, 0, 0)):
        self.objects = self.set_objects(objects)
        self.color = color
        self.lights = self.set_lights(lights)

    def set_objects(self, objects_list : list):
        """ Adiciona objetos, de uma lista recebida, na lista de objetos do ambiente. """
        new_list = []
        for o in objects_list:
            if isinstance(o, Object):
                new_list.append(o)
        self.objects = new_list
        return self.objects
    
    def set_lights(self, lights_list : list):
        """ Adiciona luzes, de uma lista recebida, na lista de luzes do ambiente. """
        new_list = []
        for l in lights_list:
            if isinstance(l, Light):
                new_list.append(l)
        self.lights = new_list
        return self.lights
    
    def get_color(self):
        """ Retorna a cor da iluminação do ambiente. """
        return self.color
    
    def get_objects(self):
        """ Retorna lista de objetos do ambiente. """
        return self.objects
    
    def get_lights(self):
        """ Retorna lista de luzes do ambiente. """
        return self.lights
    
    def move_objects(self, movement_vector : Vector):
        """ Move todos os objetos do ambiente. """
        for o in self.objects:
            o.move(movement_vector)