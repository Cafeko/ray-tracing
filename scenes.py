from plane import *
from sphere import *
from mesh import *
from material import *
from color import *
from environment import *
from light import *
from camera import *
import mesh_shapes as shape

# -- Cores ------------------------------------------------------------------------------------------------- #

White = Color(255, 255, 255)
Black = Color(0, 0, 0)
Red = Color(255, 0, 0)
Green = Color(0, 255, 0)
Blue = Color (0, 0, 255)
Gold = Color(249, 166, 2)
YellowGround = Color(180, 180, 19)
Ceu = Color(29, 155, 255)

# ---------------------------------------------------------------------------------------------------------- #
# -- Exemplo ----------------------------------------------------------------------------------------------- #
# Background:
back_color = Black

# Materiais:
ambient_coef = 0.1
plane_difusion = 0.6
plane_specular = 0.1
plane_roughness = 2
spheres_difusion = 0.55
spheres_specular = 0.1
spheres_roughness = 2

p_material = Material(color=YellowGround, ambient=ambient_coef, difusion=plane_difusion, specular=plane_specular, roughness=plane_roughness)
s_material_1 = Material(color=Red, ambient=ambient_coef, difusion=spheres_difusion, specular=spheres_specular, roughness=spheres_roughness)
s_material_2 = Material(color=Green, ambient=ambient_coef, difusion=spheres_difusion, specular=spheres_specular, roughness=spheres_roughness)
s_material_3 = Material(color=Blue, ambient=ambient_coef, difusion=spheres_difusion, specular=spheres_specular, roughness=spheres_roughness)

# Objetos
plane = Plane(point=Point(0, 0, 0), normal=Vector(0, 0, 1), material=p_material) 
sphere1 = Sphere(center=Point(0, 0, 0), radius=50, material=s_material_1)
sphere2 = Sphere(center=Point(0, 0, 0), radius=50, material=s_material_2)
sphere3 = Sphere(center=Point(0, 0, 0), radius=50, material=s_material_3)
objects_list = [sphere1, sphere2, sphere3, plane]

# Transformações:
sphere1.move(Vector(75, 0, 0))
sphere2.move(Vector(120, 110, 50))
sphere3.move(Vector(120, -110, 50))

# Luz:
l = Light(color=White, position=Point(15, -120, 120))
lights_list = [l]

# Camera:
c = Camera(position=Point(-55, 0, 40), target=Point(0, 0, 40), screen_distance=50, fov_angle=70,
           resolution_height=450, resolution_width=600)

# Ambiente:
env = Environment(objects=objects_list, lights=lights_list, color=Black)

EXEMPLO = {"camera": c, "env" : env, "background" : back_color}

# ---------------------------------------------------------------------------------------------------------- #
# -- Casa -------------------------------------------------------------------------------------------------- #
# Background:
back_color = Ceu

# Materiais:
ambient_coef = 0.1
obj_difusion = 1
obj_difusion = 0.55
obj_specular = 0.1
obj_roughness = 2

cubo_material = Material(color=White, ambient=ambient_coef, difusion=obj_difusion, specular=obj_specular, roughness=obj_roughness)

# Objetos
v = shape.CUBE["vertices"]
t = shape.CUBE["triplas"]
cubo = Mesh(v, t, len(t), len(v), cubo_material)
objects_list = [cubo]

# Transformações:
cubo.move(Vector(40, 0, 39.5))
cubo.scale(Vector(50, 50, 50))
cubo.rotate(40, 2)
cubo.rotate(37, 1)

# Luz:
l = Light(color=White, position=Point(-100, 100, 175))
lights_list = [l]

# Camera:
c = Camera(position=Point(-50, 0, 40), target=Point(0, 0, 40), screen_distance=50, fov_angle=90,
           resolution_height=450, resolution_width=600)

# Ambiente:
env = Environment(objects=objects_list, lights=lights_list, color=Black)

CASA = {"camera": c, "env" : env, "background" : back_color}

# ---------------------------------------------------------------------------------------------------------- #
# -- Teste ------------------------------------------------------------------------------------------------- #
# Background:
back_color = Black

# Materiais:
ambient_coef = 0.04
obj_difusion = 5
obj_difusion = 0.55
obj_specular = 0.1
obj_roughness = 2

obj_material = Material(color=White, ambient=ambient_coef, difusion=obj_difusion, specular=obj_specular, roughness=obj_roughness)

# Objetos
obj = Sphere(center=Point(0, 0, 0), radius=50, material=obj_material)
objects_list = [obj]

# Transformações:
obj.move(Vector(80, 0, 40))


# Luz:
l = Light(color=White, position=Point(-100, 100, 175))
lights_list = [l]

# Camera:
c = Camera(position=Point(-55, 0, 40), target=Point(0, 0, 40), screen_distance=50, fov_angle=90,
           resolution_height=450, resolution_width=600)

# Ambiente:
env = Environment(objects=objects_list, lights=lights_list, color=Blue)

TESTE = {"camera": c, "env" : env, "background" : back_color}

# ---------------------------------------------------------------------------------------------------------- #