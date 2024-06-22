from object import *
from color import *

class Environment:
    def __init__(self, objects : list, color : Color):
        """
        Ambiente que contem os objetos.

        Args:
        objects ([Object]): Lista de objetos que estão no ambiente.
        color (Color): Cor do ambiente.
        """
        self.objects = self.set_objects(objects)
        self.color = color

    def set_objects(self, objects_list : list):
        new_list = []
        for o in objects_list:
            if isinstance(o, Object):
                new_list.append(o)
        self.objects = new_list
        return self.objects
    
    def get_color(self):
        return self.color
    
    def get_objects(self):
        return self.objects