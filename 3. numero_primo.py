'''
Reto # 3
¿ES UN NÚMERO PRIMO?
Fecha publicación enunciado: 17/01/22
Fecha publicación resolución: 24/01/22
Dificultad: MEDIA

Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

from math import sqrt

lista_numeros = []

for i in range(2, 100):
    rango = int(sqrt(i)) + 1
    condicion = True
    for j in range(2, rango):
        if i % j == 0:
            condicion = False
            break
        j += 1
    if condicion == True:
        lista_numeros.append(i)
    i += 1
print(f'{lista_numeros}')