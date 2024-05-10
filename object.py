import abc

class Object(abc.ABC):
    def __init__():
        pass
    
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