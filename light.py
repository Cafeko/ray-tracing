from color import *
from point import *

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