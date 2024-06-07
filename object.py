import abc
from vector import Vector
from point import Point
from matrix import Matrix
import math_stuff

class Object(abc.ABC):
    def __init__(self):
        self.parameter_min = 0.0
    
    @abc.abstractmethod
    def intersects(self, ray):
        """
        Calcula a intersecao do raio com o plano.

        Args:
            ray (Ray): O raio que pode ou nao intersectar o objeto.
        """
        pass

    @abc.abstractmethod
    def get_color(self):
        """Retorna a cor do objeto."""
        pass
    
    @abc.abstractmethod
    def get_center(self):
        pass
    
    @abc.abstractmethod
    def move(self, movement_vector : Vector):
        pass

    @abc.abstractmethod
    def rotate(self, degree : float, axis : int):
        pass

### Classe "Object"
 ## - Propósito: Uma classe genérica para representar objetos 3D na cena, possivelmente incluindo propriedades comuns a todos os objetos.
 ## - Funções Comuns: Armazenamento de atributos comuns a objetos 3D, como posição, rotação, escala.