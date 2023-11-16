""" Escribe una función recursiva para encontrar y sumar todos los números
primos desde 1 hasta un número deseado. """

def num_primos(num, divisor = 2):
    if num % divisor == 0:
        return False
    else:
        return num_primos(num, divisor + 1)
    
def sum_primos(num):
    if num < 2:
        return 0
    elif num_primos(num):
        return num + sum_primos(num-1)
    else:
        return sum_primos(num-1)
    
print(sum_primos(11))

""" Escribe una función recursiva para calcular el MCD de dos números
enteros. """

def maxComDiv(a,b):
    if b == 0:
        return a
    else:
        return maxComDiv(b, a % b)
    
resultado = maxComDiv(48,18)

print(resultado)

"""  Escribe una función recursiva para invertir una cadena  """

def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[1:-1]) + cadena[0]

print(invertir_cadena("Hola"))


