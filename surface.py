from mesh import *
from curve import *
from material import *

class Surface(Mesh):
    def __init__(self, material : Material, control_curves: list, surface_complexity: int = 2):
        self.control_curves = control_curves
        self.control_curve_complexity = self.control_curves[0].curve_complexity
        self.surface_complexity = surface_complexity
        points = self.generate_surface_points()
        triples = self.create_surface_triangles()
        super().__init__(points, triples, len(triples), len(points), material)
            
    def validate_curves(self, curves: list):
        """Verifica se as curvas de controle são validas para criar a superfice."""
        if len(curves) <= 1:
            return False
        for c in curves:
            if isinstance(c, Curve):
                return False
        curve_points_number = curves[0].curve_complexity
        for c in curves:
            if len(c.points) != curve_points_number:
                return False
        return True

    def calculate_bezier_surface(self, t : float):
        """Calcula os pontos que estão na superfice, de acordo com o t recebido."""
        control_points = []
        surface_points = []
        for i in range(self.control_curve_complexity):
            for c in self.control_curves:
                control_points.append(c.points[i])
            point_in_surface = Curve(control_points).calculate_bezier_curve(t) 
            surface_points.append(point_in_surface)
            control_points = []
        return surface_points
    
    def generate_surface_points(self):
        """Gera os pontos que formam a superfice."""
        piece = 1 / (self.surface_complexity - 1)
        surface_points = []
        for i in range(self.surface_complexity):
            t = i*piece
            points = self.calculate_bezier_surface(t)
            surface_points = surface_points + points
        return surface_points
    
    def create_surface_triangles(self):
        """Cria as triplas que vão representar os triangulos que formam a superfice"""
        triangles = []
        for points_line_index in range(self.surface_complexity - 1):
            for surface_curve_index in range(self.control_curve_complexity - 1):
                rect = self.form_rectangle(points_line_index, surface_curve_index)
                t1, t2, t3, t4 = self.rectangle_to_triangle(rect)
                triangles.append(t1)
                triangles.append(t2)
                triangles.append(t3)
                triangles.append(t4)
        return triangles
    
    def form_rectangle(self, line_index : int, curve_index : int):
        """Forma os retangulos entre 4 pontos que sera transformado em triangulos depois."""
        current_line = self.control_curve_complexity * line_index
        current_curve = curve_index
        next_line = self.control_curve_complexity + current_line
        next_curve = current_curve + 1
        p1 = current_line + current_curve
        p2 = next_line    + current_curve
        p3 = next_line    + next_curve
        p4 = current_line + next_curve
        return (p1, p2, p3, p4)

    def rectangle_to_triangle(self, rect):
        """Transforma uma quadrupla que repesenta um retangulo em 4 triangulos."""
        tri_1 = (rect[0], rect[1], rect[2])
        tri_2 = (rect[2], rect[3], rect[0])
        tri_3 = (rect[2], rect[1], rect[0])
        tri_4 = (rect[0], rect[3], rect[2])
        return tri_1, tri_2, tri_3, tri_4