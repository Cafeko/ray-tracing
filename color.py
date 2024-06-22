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
        result_red = self.in_color_range(result_red)
        # Green
        result_green = self.g + other.g
        result_green =  self.in_color_range(result_green)
        # Blue
        result_blue  = self.b + other.b
        result_blue = self.in_color_range(result_blue)

        return Color(result_red, result_green, result_blue)

    def __mul__(self, other):
        """ Multiplica os valores (R, G, B) de uma cor por um numero. """
        # Red
        result_red   = self.r * other
        result_red = self.in_color_range(result_red)
        # Green
        result_green = self.g * other
        result_green =  self.in_color_range(result_green)
        # Blue
        result_blue  = self.b * other
        result_blue = self.in_color_range(result_blue)

        return Color(result_red, result_green, result_blue)
    
    @staticmethod
    def in_color_range(value : int):
        """ Garante que o valor recebido está entre 0 e 255. """
        if value > 255:
            value = 255
        elif value < 0:
            value = 0
        return value    
    
    def to_tuple(self):
        """ Retorna os valores (R, G, B) da cor como uma tupla. """
        return (self.r, self.g, self.b)