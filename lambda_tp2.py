""" Dada una lista de números, utiliza map y una función lambda para crear
una nueva lista que contenga el doble de cada número.
 """

numeros = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda num: num*2,numeros)))

""" Toma una lista de cadenas y utiliza map con una función lambda para
convertir todas las cadenas en mayúsculas """

cadenas = ["a","b","c","d","e"]

print(list(map(lambda cadena: cadena.upper(),cadenas)))

""" Dada una lista de cadenas, utiliza map y una función lambda para crear
una lista con la longitud de cada palabra. """

cadenas2 = ["hola", "como", "estas"]

print(list(map(lambda cadena: len(cadena), cadenas2)))

""" Toma una lista de números y utiliza map con una función lambda para
calcular la raíz cuadrada de cada número. """

import math

numeros2 = [4,9,16]

print(list(map(lambda num: math.sqrt(num),numeros2)))
