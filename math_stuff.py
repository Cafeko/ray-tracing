#import numpy as np # Para teste

def factorial(n):
    if n == 0:
        return 1
    else:
        return  n * factorial(n-1)

def degree_to_rad(degree : float):
    return degree * 3.1415926535897932384626433 / 180

# Utilisa série de Taylor para obter um valor aproximado da função do seno.
def sin(rad : float, n : int = 12):
    seno = 0
    for i in range(n):
        termo = (-1)**i * (rad**(2*i + 1)) / factorial(2*i + 1)
        seno += termo
    return seno

# Utilisa série de Taylor para obter um valor aproximado da função do cosseno.
def cos(rad : float, n : int = 12):
    cosseno = 0
    for i in range(n):
        termo = (-1)**i * (rad**(2*i)) / factorial(2*i)
        cosseno += termo
    return cosseno

"""
grau = 87
print(np.sin(np.deg2rad(grau)))
print(sin(grau))
print()
print(np.cos(np.deg2rad(grau)))
print(cos(grau))
"""