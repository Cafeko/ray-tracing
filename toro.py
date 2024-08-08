from material import Material
from mesh import *
from math_stuff import *

class Toro(Mesh):
    def __init__(self, ring_radius: float, tube_radius: float, ring_pieces: int, tube_pieces: int, material: Material):
        """
        Classe que cria um Mesh com o formato de um toroide a partir dos parametros especificados.

        Args:
        ring_radius (float): raio do toro, distancia entre o centro do toro e o centro do tubo do toro.
        tube_radius (float): raio do tubo do toro, distancia entre o centro do tubo e a extremidade dele.
        ring_pieces (int): indica a quantidade de circulos que vão formar o anel do toro.
        tube_pieces (int): indica a quantidade de pontos que vão formar o circulo.

        Returns:
        Retorna o mesh do toro se parametros forem validos ou retorna None se parametros forem invalidos.
        """
        self.ring_radius = ring_radius
        self.tube_radius = tube_radius
        self.ring_pieces = ring_pieces
        self.tube_pieces = tube_pieces
        v, t = self.create_toro_mesh()
        n_v = len(v)
        n_t = len(t)
        super().__init__(v, t, n_t, n_v, material)
    

    def create_toro_mesh(self):
        """
        Função que cria os vertices e as triplas que vão formar o mesh do toro.
        Primeiro calcula e guarda os pontos que formam o toro, depois pega os retangulos formados por esses pontos
        e os converte em dois triangulos e os armazena, retornando os pontos e os trianulos.

        Args:
        ring_pieces (int): indica a quantidade de circulos que vão formar o anel do toro.
        tube_pieces (int): indica a quantidade de pontos que vão formar o circulo.
        ring_radius (float): raio do toro, distancia entre o centro do toro e o centro do tubo do toro.
        tube_radius (float): raio do tubo do toro, distancia entre o centro do tubo e a extremidade dele.

        Returns:
        vertices_list ([Point]): lista de vertices do toro.
        triples_list ([(int, int, int)]): lista de triangulos que formam o mesh do toro.
        """
        vertices_list = []
        triples_list = []
        ring_angle = degree_to_rad(360.0) / self.ring_pieces # Angulo entre os circulos que formam o toro.
        tube_angle = degree_to_rad(360.0) / self.tube_pieces # Angulo entre os pontos dos circulos que formam o toro.
        
        # Gera vertices:
        for i in range(self.ring_pieces): # Percorre o anel.
            current_ring_angle = ring_angle * i
            for j in range(self.tube_pieces): # Percorre o circulo do tubo.
                current_tube_angle = tube_angle * j
                # Calcula e guarda pontos: 
                point = self.get_point_by_angles(current_tube_angle, current_ring_angle)
                vertices_list.append(point)
        
        # Gera triplas:
        for i in range(self.ring_pieces): # Percorre o anel.
            for j in range(self.tube_pieces): # Percorre o circulo do tubo.
                rectangle = self.get_rectangle(i, j)
                t1, t2 = self.rectangle_to_triangle(rectangle)
                triples_list.append(t1)
                triples_list.append(t2)

        return vertices_list, triples_list
    

    def get_point_by_angles(self, tube_angle: float, ring_angle: float):
        """
        Faz o calculo usando a equação parametrizada para encontrar um ponto no toro, de acordo
        com os angulos recebidos.

        Args:
        tube_angle (float): angulo no circulo, indica a posição do ponto dentro do tubo.
        ring_angle (float): angulo no anel, indica em que segmento do toro o ponto está.

        Returns:
        Ponto gerado com as cordenadas encontradas pelos calculos.
        """
        x = (self.ring_radius + self.tube_radius * cos(tube_angle)) * cos(ring_angle)
        y = (self.ring_radius + self.tube_radius * cos(tube_angle)) * sin(ring_angle)
        z = self.tube_radius * sin(tube_angle)
        return Point(x, y, z)
    

    def get_rectangle(self, i: int, j: int):
        """
        Retorna um retangulo de acordo com o circulo do anel e o ponto nele.

        Args:
        i (int): indica qual o circulo.
        j (int): indica qual o ponto do circulo.

        Returns:
        Quadrupla representando um retangulo.
        """
        # Circulo atual:
        current_circle = i * self.tube_pieces
        # Proximo circulo:
        if i == (self.ring_pieces - 1):
            next_circle = 0
        else:
            next_circle = current_circle + self.tube_pieces
        
        # Ponto atual:
        point = j
        # Proximo ponto:
        if j == (self.tube_pieces - 1):
            next_point = 0
        else:
            next_point = j + 1
        
        # Pontos que formam o retangulo:
        p0 = current_circle + point
        p1 = next_circle + point
        p2 = next_circle + next_point
        p3 = current_circle + next_point

        return (p0, p1, p2, p3)
    
    def rectangle_to_triangle(self, rect):
        """
        Transforma uma quadrupla que repesenta um retangulo em dois triangulos.

        Args:
        rect ((int, int, int, int)): quadrupla com os indices dos pontos que formam um retangulo.

        Returns:
        Dois triangulos gerados a partir do retangulo.
        """
        tri_1 = (rect[0], rect[1], rect[2])
        tri_2 = (rect[2], rect[3], rect[0])
        return tri_1, tri_2