""" Dada una lista de números, utiliza map y una función lambda para crear
una nueva lista que contenga el doble de cada número.
 """

numeros = [1,2,3,4,5,6,7,8,9]

doble = lambda num: num*2

print(list(map(lambda num: num*2,numeros)))

    