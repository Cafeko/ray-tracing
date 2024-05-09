from operations import Vector
import math

class Plane:
    """
    Representa um plano geometrico definido por um ponto e uma normal.

    Atributos:
        point (Vector): Um ponto no plano.
        normal (Vector): O vetor normal ao plano.
        material (Material): Material que define as propriedades de reflexao do plano.
    """

    def __init__(self, point, normal, material):
        """
        Inicializa uma instancia de Plane com um ponto, vetor normal e material.

        Args:
            point (Vector): Um ponto no plano.
            normal (Vector): O vetor normal ao plano, que deve ser normalizado.
            material (Material): O material do plano.
        """
        self.point = point
        self.normal = normal.normalize()
        self.material = material

    def __repr__(self):
        """
        Fornece uma representacao em string da instancia de Plane.
        
        Returns:
            str: Representacao textual do plano.
        """
        return f"Plane({repr(self.point)}, {repr(self.normal)})"

    def intersects(self, ray):
        """
        Calcula a intersecao do raio com o plano.

        Args:
            ray (Ray): O raio que pode ou nao intersectar o plano.

        Returns:
            float or None: O escalar t na equacao parametrica do raio, ou None se nao houver intersecao.
        """
        op = ray.origin - self.point
        a = Vector.dot(op, self.normal)
        b = Vector.dot(ray.direction, self.normal)
        if b < 0:
            return -a / b
        return None

    def surface_norm(self, point=None):
        """
        Retorna o vetor normal do plano.

        Args:
            point (Vector, optional): Um ponto no plano (nao utilizado neste caso, pois o normal eh constante).

        Returns:
            Vector: O vetor normal do plano.
        """
        return self.normal
    
    def get_material_reflection(self):
        """
        Retorna o coeficiente de reflexao do material do plano.

        Returns:
            float: Coeficiente de reflexao do material.
        """
        return self.material.reflects
    
    def get_base_color(self):
        """
        Retorna a cor base do material do plano.

        Returns:
            tuple: A cor base (R, G, B) do material.
        """
        return self.material.get_base_color()
