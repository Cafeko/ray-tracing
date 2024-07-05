from color import *

class Material:
    """
    Representa as propriedades fisicas de um material para renderizacao.

    Atributos:
        color (Color): Objeto da classe Color que contem as cores (R, G, B).
        ambient (float): Coeficiente ambiental, que afeta o quanto que o objeto é afetado pela luz do ambiente.
        difusion (float): Coeficiente do material que afeta a difusao da luz.
        specular (float): Coeficiente especular do material, que afeta o brilho especular.
        roughness (float): Define o quão rugosa é a superfice, afeta a especularidade.
        reflection (float): indice de refracao do material.
        transmission (float): Componente transmissiva do material, que afeta a transparencia.
        ior (Float): O índice de refração determina como a luz se comporta ao atravessar a interface entre dois materiais diferentes.
    """
    def __init__(self, color: Color = Color(), ambient=0.2, difusion=1.0, specular=0.5,
                 roughness=100.0, reflection=0, transmission=0, ior=1.0):
        self.color = color
        self.ambient = ambient
        self.difusion = difusion  
        self.specular = specular 
        self.reflection = reflection  
        self.transmission = transmission
        self.roughness = roughness
        self.ior = ior

