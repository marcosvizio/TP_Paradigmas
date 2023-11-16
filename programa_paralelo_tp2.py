#Aca se me complico un poco ya que me costo entender el tema de programas paralelos, entiendo el uso pero lo que hay que hacer para usar no.

""" Crea dos hilos que ejecuten dos funciones diferentes simultáneamente
y muestran mensajes de salida """

import threading

palabras = ["Hola", "Chau", "Como", "Estas", "Wow"]

numeros = [1,2,3,4,5]

def hablar():
    for palabra in palabras:
        print(palabra)

def contar():
    for numero in numeros:
        print(numero)

hilo_1 = threading.Thread(target=hablar)
hilo_2 = threading.Thread(target=contar)

hilo_1.start()
hilo_2.start()

hilo_1.join()
hilo_2.join()

print("Ya terminaron los hilos")

"""  Implementa el problema del productor-consumidor utilizando hilos,
donde un hilo produce datos y otro hilo los consume desde una cola
compartida.
 """

import threading
import queue

cola_compartida = queue.Queue(maxsize=5) 

def productor():
    for i in range(10):
        dato = f"Dato-{i}"
        cola_compartida.put(dato)
        print(f"Productor produjo: {dato}")

def consumidor():
    while True:
        dato = cola_compartida.get()
        print(f"Consumidor consumió: {dato}")
        cola_compartida.task_done()

hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

hilo_productor.start()
hilo_consumidor.start()

hilo_productor.join()
hilo_consumidor.join()

#No entendi el punto disculpame asi que lo realice con ChatGPT para ayudarme a entender

""" Crea dos procesos utilizando la biblioteca multiprocessing y ejecuta
funciones diferentes en cada proceso. """

import multiprocessing
import time

def funcion_proceso1():
    for _ in range(5):
        print("Proceso 1 ejecutándose...")
        time.sleep(1)

def funcion_proceso2():
    for _ in range(5):
        print("Proceso 2 ejecutándose...")
        time.sleep(1)

if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=funcion_proceso1)
    proceso2 = multiprocessing.Process(target=funcion_proceso2)

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print("Ambos procesos han terminado.")

""" Utiliza un pool de procesos para realizar operaciones en paralelo en
una lista de datos. """

from multiprocessing import Pool


def operacion(elemento):
    return elemento * 2

if __name__ == "__main__":
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    num_procesos = 4

    with Pool(num_procesos) as pool:
        resultados = pool.map(operacion, datos)
        
    print("Datos originales:", datos)
    print("Resultados después de la operación:", resultados)
