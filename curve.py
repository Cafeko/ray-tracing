import math_stuff as maths
from point import *

class Curve:
    def __init__(self, control_points: list, curve_complexity: int):
        self.control_points = control_points
        self.points = self.generate_curve_points(curve_complexity)

    def calculate_bezier_curve(self, t : float):
        """Calcula o ponto na curva, de acordo com o t recebido."""
        resultado = Point(0, 0, 0)
        n = len(self.control_points)-1
        for i in range(len(self.control_points)):
            B = self.calculate_bernstein_polynomial(i, n, t)
            point = self.control_points[i]
            resultado += point*B
        return resultado
    
    def calculate_bernstein_polynomial(self, i : int, n : int, t: float):
        """Calcula o polinomio de Bernstein de acordo com os parametros recebidos."""
        binomial_coef = maths.binomial_coefficient(n, i)
        return binomial_coef*((1-t)**(n-i))*(t**i)

    def generate_curve_points(self, curve_complexity : int):
        piece = 1 / curve_complexity
        points = []
        for i in range(curve_complexity+1):
            t = i*piece
            point = self.calculate_bezier_curve(t)
            points.append(point)
        return points