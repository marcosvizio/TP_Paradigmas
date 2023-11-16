""" Escribe una función que sume los dígitos de un número pares de un
número entero. Si el número es impar, restarle 3 y sumarlo. Si el número
da negativo, sumar 1. """

def sumar_digitos(num):
    if (num % 2 == 0):
        cadena_num = str(num)
        suma=0
        for digitoStr in cadena_num:
            digito = int(digitoStr)
            suma += digito
        return print(suma)
    elif (num % 2 != 0):
        numIm = num + 3
        sumar_digitos(numIm)
    else:
        numNeg = num + 1
        sumar_digitos(numNeg)

sumar_digitos(55)

