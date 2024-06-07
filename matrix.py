from vector import Vector
from point import Point
import math_stuff
import numpy as np

class Matrix:
    def __init__(self, matrix_values : list):
        self.values = matrix_values
        self.n_linhas= len(self.values)
        self.n_colunas= len(self.values[0])

    def __str__(self):
        values_string = ""
        for l in range(self.n_linhas):
            values_string += "["
            for c  in range(self.n_colunas):
                if c == 0:
                    values_string += f"{self.values[l][c]}"
                else:
                    values_string += f", {self.values[l][c]}"
            values_string += "]\n"
        return values_string
    
    def set_value(self, line : int, column : int, value : float):
        self.values[line-1][column-1] = value

    def copy_values(self):
        copy = []
        for l in range(self.n_linhas):
            copy.append([])
            for c in range(self.n_colunas):
                copy[l].append(self.values[l][c])
        return copy

    def inverse(self):
        return Matrix(np.linalg.inv(self.values))

    def dot_product(self, other):
        if isinstance(other, (Vector)):
            other_matrix = self.to_matrix(other)
            result = self.dot_product_matrix(self, other_matrix)
            if result != None:
                result = self.matrix_to(result, Vector)
            return result
        elif isinstance(other, (Point)):
            other_matrix = self.to_matrix(other)
            result = self.dot_product_matrix(self, other_matrix)
            if result != None:
                result = self.matrix_to(result, Point)
            return result
        elif isinstance(other, Matrix):
            other_matrix = other
            result = self.dot_product_matrix(self, other_matrix)
            return result
        else:
            return None
    
    @staticmethod
    def dot_product_matrix(matrix1, matrix2):
        if matrix2.n_linhas== matrix1.n_colunas:
            result = []
            for l in range(matrix1.n_linhas):
                result.append([])
                for c in range(matrix2.n_colunas):
                    position_value = 0
                    for i in range(matrix2.n_linhas):
                        position_value += matrix1.values[l][i] * matrix2.values[i][c]
                    result[l].append(position_value)
            return Matrix(result)
        else:
            return None

    @staticmethod
    def to_matrix(thing):
        if isinstance(thing, (Vector, Point)):
            values = [[thing.x], [thing.y], [thing.z], [1]]
            return Matrix(values)
        else:
            return None

    @staticmethod
    def matrix_to(matrix, to_type):
        return to_type(matrix.values[0][0], matrix.values[1][0], matrix.values[2][0])

    @staticmethod
    def create_defaut_matrix():
        m = [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        return m

    @staticmethod
    def create_move_matrix(move_direction : Vector):
        m = [[1, 0, 0, move_direction.x],
             [0, 1, 0, move_direction.y],
             [0, 0, 1, move_direction.z],
             [0, 0, 0, 1               ]]
        return Matrix(m)

    @staticmethod
    def create_rotation_matrix(degree : float, axis : int = 0):
        if axis == 0 or axis == 1 or axis == 2:
            angle = math_stuff.degree_to_rad(degree)
            if axis == 0:
                m = [[1, 0            ,  0            , 0],
                     [0, np.cos(angle), -np.sin(angle), 0],
                     [0, np.sin(angle),  np.cos(angle), 0],
                     [0, 0            ,  0            , 1]]
            elif axis == 1:
                m = [[ np.cos(angle), 0, np.sin(angle), 0],
                     [ 0            , 1, 0            , 0],
                     [-np.sin(angle), 0, np.cos(angle), 0],
                     [ 0            , 0, 0            , 1]]
            elif axis == 2:
                m = [[np.cos(angle), -np.sin(angle), 0, 0],
                     [np.sin(angle),  np.cos(angle), 0, 0],
                     [0            ,  0            , 1, 0],
                     [0            ,  0            , 0, 1]]
            return Matrix(m)
        else:
            return Matrix.create_defaut_matrix()

    """
    @abc.abstractmethod
    def create_scale_matrix():
    pass
    """

# Teste:
'''
m1 = [[2, 0, 0, 0],
      [0, 2, 0, 0],
      [0, 0, 2, 0],
      [0, 0, 0, 1]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]


M1 = Matrix(m1)
M2 = Matrix(m2)

print(str(M1.dot_product(Point(1, 2, 2))))


m1 = [[2, 1],
      [1, 2]]

m2 = [[1, 2],
      [3, 4]]

M1 = Matrix(m1)
M2 = Matrix(m2)

print(str(M1.dot_product(M2)))
print(str(M2.dot_product(M1)))
'''

"""
m = [[ 1,  0,  0,  3],
     [ 0,  1,  0,  4],
     [ 0,  0,  1, -5],
     [ 0,  0,  0,  1]]

M = Matrix(m)
print(M.inverse().values)
"""