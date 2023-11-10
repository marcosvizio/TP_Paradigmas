""" Hacer un decorador para registrar las llamadas a una función, junto con
sus argumentos y resultados.
 """

def registro(func): 
    if func:
        def wrapper(*args,**kwargs):
            resultado = func(*args)
            wrapper.contador += 1
            print(f"Este es el contador de llamadas de la funcion: {wrapper.contador}")
            return print(f"Este es el resultado de la funcion: {resultado}")
        wrapper.contador = 0
        return wrapper


@registro
def funcionRandom(parametro:str):
    resultado = f"RESULTADO Y ESTE ES EL PARAMETRO: {parametro}"
    return resultado

funcionRandom("Hola")
funcionRandom("Wow")
funcionRandom("Chau")

""" Hacer un decorador para verificar que los argumentos de una función
sean del tipo correcto. """

def verificador_de_variables(func):
    if func:   
        def wrapper(*args, **kwargs):
            for i in args:
                if not isinstance(i,int):
                    return print(f"Por favor insertar numeros enteros.")
                resultado = func(*args, **kwargs)
                return print(f"Resultado: {resultado}.")
        return wrapper


@verificador_de_variables
def funcionPrueba(a, b):
    resultado = f"El parametro A: {a} y el parametro B: {b}"
    return resultado

funcionPrueba(5,4)

funcionPrueba("5",4)

""" Hacer un decorador para agrega un retardo antes de que se ejecute
una función """

import time

def retardador(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        time.sleep(2)
        return resultado
    return wrapper

@retardador
def funcionConRetardo():
    print("Comienzo de la función")
    return f"Se aplico la funcion con retardo."

print(funcionConRetardo())

""" Hacer un decorador para verificar las precondiciones antes de ejecutar
una función. """

def verificador_precondicion(condicion):
    def precondicionador(func):
        def wrapper(*args, **kwargs):
            if condicion(*args, **kwargs):
                resultado = func(*args,**kwargs)
                return resultado
            else:
                return ValueError("La precondicion no se cumple")
        return wrapper
    return precondicionador
    
def condicion(a,b):
    return a > b

@verificador_precondicion(condicion)
def multiplicacion(a, b):
    resultado = a * b
    return resultado

print(multiplicacion(21, 20))