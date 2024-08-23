import math_stuff as maths
from point import *

class Curve:
    def __init__(self, control_points: list, curve_complexity: int = 2):
        self.control_points = control_points
        self.curve_complexity = curve_complexity
        self.points = self.generate_curve_points()

    def calculate_bezier_curve(self, t : float):
        """Calcula o ponto na curva, de acordo com o t recebido."""
        curve_point = Point(0, 0, 0)
        n = len(self.control_points)-1
        for i in range(len(self.control_points)):
            B = self.calculate_bernstein_polynomial(n, i, t)
            point = self.control_points[i]
            curve_point += point*B
        return curve_point
    
    def calculate_bernstein_polynomial(self, n : int, i : int, t: float):
        """Calcula o polinomio de Bernstein de acordo com os parametros recebidos."""
        binomial_coef = maths.binomial_coefficient(n, i)
        return binomial_coef*((1-t)**(n-i))*(t**i)

    def generate_curve_points(self,):
        piece = 1 / self.curve_complexity-1
        points = []
        for i in range(self.curve_complexity):
            t = i*piece
            point = self.calculate_bezier_curve(t)
            points.append(point)
        return points