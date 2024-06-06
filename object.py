import abc
from vector import Vector
from matrix import Matrix

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
    def get_points(self):
        pass
    
    @abc.abstractmethod
    def get_center(self):
        pass
    
    @abc.abstractmethod
    def transform(self, transformation_matrix : Matrix):
        pass
    
    def move_object(self, movement_vector : Vector):
        move_matrix = Matrix.create_move_matrix(movement_vector)
        self.transform(move_matrix)
    

### Classe "Object"
 ## - Propósito: Uma classe genérica para representar objetos 3D na cena, possivelmente incluindo propriedades comuns a todos os objetos.
 ## - Funções Comuns: Armazenamento de atributos comuns a objetos 3D, como posição, rotação, escala.