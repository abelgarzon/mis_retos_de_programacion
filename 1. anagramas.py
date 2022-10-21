'''
Reto # 1
¿ES UN ANAGRAMA?
Fecha publicación enunciado: 03/01/22
Fecha publicación resolución: 10/01/22
Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.
'''

# solicigo ingreso de la primera palabra
word_1 = str(input('ingresa la primera palabra: '))

# solicito ingreso de la segunda palabra
word_2 = str(input('ingresa la segunda palabra: '))

# paso primera palabra a minusculas
word_1_lower = word_1.lower()

# paso segunda palabra a minusculas
word_2_lower = word_2.lower()

# inicializo condition en falso
condition = False

if word_1_lower != word_2_lower and len(word_1) == len(word_2): # si las palabras son diferentes y de la misma longuitud
    word_1_lower_order = ''.join(sorted(word_1_lower))          # las organizo alfabeticamente
    word_2_lower_order = ''.join(sorted(word_2_lower))
    if word_1_lower_order == word_2_lower_order:                # si las palabras organizadas son iguales
        condition = True                                        # paso condition a True
print(f'{condition}')                                           # finalmente imprimo condition