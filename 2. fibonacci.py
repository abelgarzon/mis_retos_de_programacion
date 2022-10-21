'''
Reto  # 2
LA SUCESIÓN DE FIBONACCI
Fecha publicación enunciado: 10/01/22
Fecha publicación resolución: 17/01/22
Dificultad: DIFÍCIL

Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
'''

number_1 = 0
number_2 = 1

for i in range(0, 50):
    print(f'{number_1}')
    fibonacci = number_1 + number_2
    number_1 = number_2
    number_2 = fibonacci
    i += 1