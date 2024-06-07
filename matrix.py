from vector import Vector
from point import Point
import math_stuff as ms

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
        """ Utilisa eliminação de Gauss-Jordan para calcular a inversa da matriz e retornar o resultado. """
        if self.n_linhas == self.n_colunas:
            # Cria copia para não substituir os valores originais.
            n = self.n_colunas
            matriz = self.copy_values()

            # Concatena a matriz com a matriz identidade.
            matriz_identidade = self.create_identity_matrix(n).copy_values()
            matriz_concat = []
            for i in range(n):
                matriz_concat.append(matriz[i] + matriz_identidade[i])
            
            # Repete os passos a seguir para todas as colunas da matriz. 
            for coluna in range(n):
                # Encontra o indice da linha do maior valor da coluna atual.
                maior_index = 0
                maior = 0
                for i in range(coluna, n):
                    valor = matriz_concat[i][coluna]
                    if maior < abs(valor):
                        maior = valor
                        maior_index = i
                # Troca de lugar a linha com o mesmo indice da coluna atual e a linha com o maior valor da coluna.
                matriz_concat[coluna], matriz_concat[maior_index] = matriz_concat[maior_index], matriz_concat[coluna]

                # Transforma linha para que elemento da diagonal vire um.
                escalar = matriz_concat[coluna][coluna]
                matriz_concat[coluna] = [elemento / escalar for elemento in matriz_concat[coluna]]

                # Para todas as linhas diferentes da coluna atual, vai tornar os elementos da coluna que não estão na diagonal
                # principal iguais a 0, faz isso multiplicando os valores da linha que tem o mesmo indice da coluna atual 
                # pelos valores dos elementos das outras linhas, que estão na mesma coluna, e depois subtraindo nessas linhas.
                for linha in range(n):
                    if linha != coluna:
                        escalar = matriz_concat[linha][coluna]
                        matriz_concat[linha] = [elemento - (escalar * matriz_concat[coluna][i])
                                                for i, elemento in enumerate(matriz_concat[linha])]
            
            # Retira a matriz invertida da matriz concatenada.
            matriz_invertida = []
            for i in range(n):
                matriz_invertida.append(matriz_concat[i][n:])
            return Matrix(matriz_invertida)
        else:
            return None

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
    def create_identity_matrix(size):
        ident = []
        for i in range(size):
            ident.append([])
            for j in range(size):
                if i == j:
                    ident[i].append(1)
                else:
                    ident[i].append(0)
        return Matrix(ident)

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
            angle = ms.degree_to_rad(degree)
            if axis == 0:
                m = [[1, 0            ,  0            , 0],
                     [0, ms.cos(angle), -ms.sin(angle), 0],
                     [0, ms.sin(angle),  ms.cos(angle), 0],
                     [0, 0            ,  0            , 1]]
            elif axis == 1:
                m = [[ ms.cos(angle), 0, ms.sin(angle), 0],
                     [ 0            , 1, 0            , 0],
                     [-ms.sin(angle), 0, ms.cos(angle), 0],
                     [ 0            , 0, 0            , 1]]
            elif axis == 2:
                m = [[ms.cos(angle), -ms.sin(angle), 0, 0],
                     [ms.sin(angle),  ms.cos(angle), 0, 0],
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
m = [[24, 28, 34],
     [47, 54, 65],
     [78, 89, 107]]

M = Matrix(m)
print(M.inverse().values)
"""

