""" Escribe un programa que solicite al usuario dos números y realice
la división de uno por el otro. Utiliza un bloque try y except para
manejar la excepción que ocurre si el segundo número es cero """

def division(dato):
    return dato["a"]/dato["b"]

dato={"a":5,"b":0}

try:
    print(division(dato))
except ZeroDivisionError as error:
    print("No se puede dividir por 0")

""" Crea una lista de números y, a continuación, intenta acceder a un
elemento en un índice especificado por el usuario. Utiliza un 
bloque try y except para manejar la excepción que se produce si
el índice está fuera de rango.
 """

numeros = [1,2,3,4,5]

try:
    indice_user=int(input("Ingrese el indice que desee acceder de la lista: "))
    print(numeros[indice_user])
except IndexError as error:
    print("No existe ese indice en la lista")


""" Solicita al usuario que ingrese una cadena que represente un
número. Utiliza un bloque try y except para manejar la excepción
que se produce si la cadena no se puede convertir a un número.
 """

try:
    letra_num = input("Ingresar un numero: ")
    num = int(letra_num)
    print(num)
except ValueError as error:
    print("La cadena ingresada no es un numero")

""" Escribe un programa que intente abrir un archivo que no existe y
utilice un bloque try y except para manejar la excepción de
"FileNotFoundError". """

try:
    with open("archivo3.txt", "r+") as archivo:
        archivo.write("Entraste al archivo 3")
        archivo.close()
except FileNotFoundError as error:
    print("El archivo no existe")

""" Crea un diccionario y luego intenta acceder a un valor utilizando
una clave que no está en el diccionario. Utiliza un bloque try y
except para manejar la excepción que se produce si la clave no
existe.
 """

diccionario1 = {"1": "hola","2": "como","3": "estas"}

try:
    valor=diccionario1[input("Ingrese a la key que desea ingresar: ")]
    print(valor)
except KeyError as error:
    print("La clave ingresada no existe")

""" Para cada caso anterior del manejo de excepciones (7.1.1, 7.1.2,
7.1.3, 7.1.4, 7.1.5) crear una excepción personalizada. """

class OneDivisionError(Exception):
    pass

def division2(dato):
    if dato["b"] == 1:
        raise OneDivisionError("No se puede dividir por 1.")
    return dato["a"]/dato["b"]

dato={"a":5,"b":1}

try:
    print(division2(dato))
except ZeroDivisionError as error:
    print("No se puede dividir por 0")
except OneDivisionError as error:
    print(error)

""" 7.1.2 ver 2 """

numeros = [1,2,3,4,5]

class OneIndexError(Exception):
    pass

try:
    indice_user=int(input("Ingrese el indice que desee acceder de la lista: "))
    if indice_user == 2:
        raise OneIndexError("No se puede ingresar al indice 1, esta bloqueado.")
    print(numeros[indice_user])
except IndexError as error:
    print("No existe ese indice en la lista")
except OneIndexError as error:
    print(error)

""" 7.1.3 ver 2 """

class FiveValueError(Exception):
    pass

try:
    letra_num = input("Ingresar un numero: ")
    num = int(letra_num)
    if num == 5:
        raise FiveValueError("No se permite que ingreses el numero valor: 5")
    print(num)
except ValueError as error:
    print("La cadena ingresada no es un numero")
except FiveValueError as error:
    print(error)

""" 7.1.4 ver 2 """

class ArchivoError(Exception):
    pass

def leer_archivo():
    try:
        with open("archivo3.txt", "r+") as archivo:
            archivo.write("Entraste al archivo 3")
            archivo.close()

    except FileNotFoundError as error:
        raise ArchivoError("El archivo no existe desde error personalizado") from error
    
try:
    leer_archivo()
except ArchivoError as error:
    print(error)

""" 7.1.5 ver 2 """

class ErrorInputPersonalizado(Exception):
    pass

diccionario1 = {"1": "hola","2": "como","3": "estas"}

try:
    valor = diccionario1[input("Ingrese a la key que desea ingresar: ")]
    if valor == "hola":
        raise ErrorInputPersonalizado("El valor 1 no se puede ingresar")
    print(valor)
except KeyError as error:
    print("La clave ingresada no existe")
except ErrorInputPersonalizado as error:
    print(error)

""" Escribe un programa que intente abrir un archivo, leer su
contenido y luego cerrarlo. Utiliza bloques try, except y finally
para asegurarte de que el archivo se cierre correctamente,
incluso si ocurre una excepción durante la lectura. """

archivo = None

try:
    with open("archivo2.txt", "r+") as archivo:
        archivo.read()
except FileNotFoundError as error:
    print(error)
finally:
    if archivo != None:
        archivo.close()

""" Crea un programa que solicite al usuario dos números y una
operación matemática (suma, resta, multiplicación, división) para
realizar. Utiliza bloques try, except y finally para manejar cualquier
excepción que pueda ocurrir durante la operación y asegurarte
de que los recursos se liberen correctamente. """


def operaciones(a,b, op):
    if op == "suma":
        return a+b
    if op == "resta":
        return a-b
    if op == "multiplicacion":
        return a*b
    if op == "division":
        return a/b
    
try:
    resultado = operaciones(int(input("Ingresar el numero A: ")), int(input("Ingresar el numero B: ")), input("Ingresar la operacion a realizar (suma, resta, multiplicacion o division): "))
    print(resultado)
except ValueError as error:
    print("Uno de los valores no es un numero")
except ZeroDivisionError as error:
    print("No se puede dividir sobre 0")

""" Escribe un programa que abra un archivo, lea su contenido y
escriba el mismo contenido en otro archivo. Utiliza bloques try,
except y finally para manejar cualquier excepción que pueda
ocurrir durante la lectura o escritura, y asegúrate de que ambos
archivos se cierren correctamente. """

archivo2 = None

try:
    with open("archivo2.txt", "r+") as archivo:
        contenido = archivo.read()
        with open("archivo.txt", "r+") as archivo2:
            archivo2.write(contenido)
            archivo2.read()
except FileNotFoundError as error:
    print(error)
finally:
    if archivo != None and archivo2 != None:
        archivo.close()
        archivo2.close()

