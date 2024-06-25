from color import *

class Material:
    """
    Representa as propriedades fisicas de um material para renderizacao.

    Atributos:
        color (Color): Objeto da classe Color que contem as cores (R, G, B).
        ambient (float): Coeficiente ambiental, que afeta o quanto que o objeto é afetado pela luz do ambiente.
        difusion (float): Coeficiente do material que afeta a difusao da luz.
        specular (float): Coeficiente especular do material, que afeta o brilho especular.
        material_type (str): Tipo do material (por exemplo, "DIFFUSE").
        reflection (float): indice de refracao do material.
        transmission (float): Componente transmissiva do material, que afeta a transparencia.
    """

    def __init__(self, color: Color, ambient=0.2, difusion=1, specular=0.5, reflection=1.5, transmission=0.5, roughness=1):
        self.color = color
        self.ambient = ambient
        self.difusion = difusion  
        self.specular = specular 
        self.reflection = reflection  
        self.transmission = transmission
        self.roughness = roughness