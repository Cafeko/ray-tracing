class Color:
    def __init__(self, red : int, green : int, blue : int):
        """
        Classe que contem os valores (R, G, B) de uma com e é capas de fazer operações entre cores.

        Args:
        R (Int): Valor vermelho da cor, de 0 a 255.
        G (Int): Valor verde da cor, de 0 a 255.
        B (Int): Valor azul da cor, de 0 a 255.
        """
        self.r = self.in_color_range(red)
        self.g = self.in_color_range(green)
        self.b = self.in_color_range(blue)

    def __add__(self, other):
        """ Soma os valores (R, G, B) de uma cor com outra e retorna o resultado. """
        # Red
        result_red   = self.r + other.r
        # Green
        result_green = self.g + other.g
        # Blue
        result_blue  = self.b + other.b
        return Color(result_red, result_green, result_blue)

    def __mul__(self, other):
        """ Multiplica os valores (R, G, B) de uma cor por um numero ou por uma tupla com 3 valores. """
        if isinstance(other, tuple):
            return self.mult_by_tuple(other)
        else:
            # Red
            result_red   = round(self.r * other)
            # Green
            result_green = round(self.g * other)
            # Blue
            result_blue  = round(self.b * other)
            return Color(result_red, result_green, result_blue)
    
    def mult_by_tuple(self, other):
        """ Faz a multiplicação por 3 valores em uma tupla, um para cada um das cores. """
        # Red
        result_red   = self.r * other[0]
        # Green
        result_green = self.g * other[1]
        # Blue
        result_blue  = self.b * other[2]
        return Color(result_red, result_green, result_blue)

    @staticmethod
    def in_color_range(value : int):
        """ Garante que o valor recebido está entre 0 e 255. """
        if value > 255:
            value = 255
        elif value < 0:
            value = 0
        return int(value)
    
    def to_tuple(self):
        """ Retorna os valores (R, G, B) da cor como uma tupla. """
        return (self.r, self.g, self.b)
    
    def to_normalized_tuple(self):
        """ Retorna os valores da cor normalizados em uma tupla. """
        red_normalized = self.r / 255
        green_normalized = self.g / 255
        blue_normalized = self.b / 255
        return (red_normalized, green_normalized, blue_normalized)