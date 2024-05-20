from object import *
from material import *
from point import *

class Mesh(Object):
    def __init__(self, vertices : list, triples : list, n_triangles: int, n_vertices : int, color_normalized : tuple):
        super().__init__()
        self.vertices : list = self.set_vertices(vertices)
        self.triples : list = self.set_triples(triples)
        self.n_triangles : int = n_triangles
        self.n_vertices : int = n_vertices
        if len(self.n_vertices) >= 3 and len(self.n_triangles) > 0 and \
            len(self.vertices) == self.n_vertices and len(self.triples) == self.n_triangles:
            self.color_normalized : tuple = color_normalized
            self.normals_triangles : list = self.create_triangles_normals_list()
            self.normals_vertices : list = self.create_vertices_normals_list()
        else:
            return None

    def set_vertices(self, vertices_list : list):
        vertices = [] 
        for v in vertices_list:
            if isinstance(v, Point):
                vertices.append(v)
        self.vertices = vertices
        return self.vertices
    
    def get_vertice(self, v_index):
        if v_index >= 0 and v_index < self.n_vertices:
            return self.vertices[v_index]
        else:
            return None

    def set_triples(self, triples_list : list):
        clean_triples_list = []
        for t in triples_list:
            if self.is_valid_triple(t):
                clean_triples_list.append(t)
        self.triples = clean_triples_list
        return triples_list
    
    @staticmethod
    def is_valid_triple(triple):
        return isinstance(triple, tuple) and len(triple) == 3 and Mesh.get_vertice(triple[0]) != None and\
            Mesh.get_vertice(triple[1]) != None and Mesh.get_vertice(triple[2]) != None
    
    def get_color(self):
        r = self.color_normalized[0] * 255
        g = self.color_normalized[1] * 255
        b = self.color_normalized[2] * 255
        color = (r, g, b)
        return color

    def create_triangles_normals_list(self):
        normals_list = []
        for i in range(self.n_triangles):
            triple = self.triples[i]
            vec1 = self.get_vertice(triple[1]) - self.get_vertice(triple[0])
            vec2 = self.get_vertice(triple[2]) - self.get_vertice(triple[1])
            vec_normal = vec1.cross_product(vec2).normalize()
            normals_list.append(vec_normal)
        return normals_list
    
    def create_vertices_normals_list(self):
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