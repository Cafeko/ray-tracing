from object import *
from material import *
from point import *

class Mesh(Object):
    def __init__(self, vertices : list, triples : list, n_triangles: int, n_vertices : int, color: tuple):
        """
        Malha que é formada por um conjunto de triangulos que juntos formam um objeto 3D.

        Args:
        vertices ([Point]): Lista de pontos que representam os vertices dos triangulos.
        triples ((int, int, int)): Triplas que contem 3 inteiros que são os indices dos vertices de um triangulo.
        n_triangles (int): Número de triangulos na malha.
        n_vertices (int): Número de vertices na malha.
        color: (tupla): tupla com a cor da malha (r, g, b).

        Returns:
        Retorna a malha se for uma malha valida ou None se for uma malha invalida.
        """
        super().__init__()
        self.vertices : list = self.set_vertices(vertices)
        self.triples : list = self.set_triples(triples)
        self.n_triangles : int = n_triangles
        self.n_vertices : int = n_vertices
        if len(self.n_vertices) >= 3 and len(self.n_triangles) > 0 and \
            len(self.vertices) == self.n_vertices and len(self.triples) == self.n_triangles:
            self.color : tuple = color
            self.normals_triangles : list = self.create_triangles_normals_list()
            self.normals_vertices : list = self.create_vertices_normals_list()
        else:
            return None

    def set_vertices(self, vertices_list : list):
        """
        Define a lista de vertices.
        Se um elemento da na lista não for Point ele é removido da lista,
        e consequentimente a malha será invalida. 
        
        Args:
        vertices_list ([Point]): Lista de pontos que serão os vertices dos triangulos.

        Returns:
        [Point]: Lista de vertices que foi atribuida a malha.
        """
        vertices = [] 
        for v in vertices_list:
            if isinstance(v, Point):
                vertices.append(v)
        self.vertices = vertices
        return self.vertices
    
    def get_vertice(self, v_index):
        """
        Retorna um dos pontos da lista de vertices de acordo com o indice recebido.
        
        Args:
        v_index (int): Indice do vertice na lista de vertices.

        Returns:
        Retorna o Vertice com indice = v_index ou None se o indice for maior que o tamanho da lista ou menor que zero.
        """
        if v_index >= 0 and v_index < self.n_vertices:
            return self.vertices[v_index]
        else:
            return None

    def set_triples(self, triples_list : list):
        """
        Define a lista de triplas que representam os triangulos da malha.
        Se um elemento da lista não for uma tripla valida ele é removido da lista,
        e consequentimente a malha será invalida.
        
        Args:
        triples_list ([((int, int, int))]): Lista de triplas com 3 inteiros que são os indices dos vertices.

        Returns:
        [((int, int, int))]: Lista de triplas que foi atribuida a malha.
        """
        clean_triples_list = []
        for t in triples_list:
            if self.is_valid_triple(t):
                clean_triples_list.append(t)
        self.triples = clean_triples_list
        return triples_list
    
    @staticmethod
    def is_valid_triple(triple):
        """
        Determina se a tripla é valida para a malha.
        
        Args:
        triple ((int, int, int)): Tripla com 3 inteiros.

        Returns:
        Bool: retorna true se a tupla for valida e false se não for valida.
        """
        return isinstance(triple, tuple) and len(triple) == 3 and Mesh.get_vertice(triple[0]) != None and\
            Mesh.get_vertice(triple[1]) != None and Mesh.get_vertice(triple[2]) != None
    
    def get_color(self):
        """
        Retorna a cor da malha.

        Returns:
        Retorna a tupla com 3 elementos (r, g, b) que está associada a cor da malha.
        """
        return self.color

    def create_triangles_normals_list(self):
        """
        Cria a lista de vetores normais dos triangulos da malha.
        Para cada tripla, forma dois vetores com os vertices do triangulo,
        faz o produto cruzado entre esses vetores e normaliza o resultado (resultando em um vetor normal)
        e adiciona esse vetor normal em uma lista que será retornada.

        Returns:
        [Vector]: Lista de vetores normais dos triangulos.
        """
        normals_list = []
        for i in range(self.n_triangles):
            triple = self.triples[i]
            vec1 = self.get_vertice(triple[1]) - self.get_vertice(triple[0])
            vec2 = self.get_vertice(triple[2]) - self.get_vertice(triple[1])
            vec_normal = vec1.cross_product(vec2).normalize()
            normals_list.append(vec_normal)
        return normals_list
    
    def create_vertices_normals_list(self):
        """
        Cria a lista de vetores normais dos vertices da malha.
        Cria uma lista de vetores vazios para serem os vetores dos vertices,
        para cada tripla (triangulo), faz a soma de cada um dos vetores dos vertices com o vetor
        normal do triangulo e o resultado atualiza a lista de vetores de vertices,
        no fim os vetores dos vertices são normalizados e retornados.

        Returns:
        [Vector]: Lista de vetores normais dos vertices.
        """
        vertices_normals = [Vector()]*self.n_vertices
        for i in range(self.n_triangles):
            triple = self.triples[i]
            for index in triple:
                vertices_normals[index] +=  self.normals_triangles[i]
        for i in range(self.n_vertices):
            vertices_normals[i] = vertices_normals[i].normalize()
        return vertices_normals

    def intersects(self, ray):
        pass

### Classe "Mesh"
 ## - Propósito: Representa uma coleção de vértices, arestas e faces que define a forma de um objeto 3D.
  ##- Funções Comuns: Manipulação e renderização de malhas, transformações geométricas.