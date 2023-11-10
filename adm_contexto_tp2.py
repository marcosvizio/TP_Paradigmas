""" Hacer un administrador de contexto para notificar eventos al entrar y al
salir de un bloque de código. """

with open("archivo.txt", "r+") as archivo:
    archivo.write("Entraste a un bloque de codigo. ")
    a = archivo.read()
    print(a)

    class Perro:
        def __init__(self, nombre, raza, edad):
            self.nombre = nombre
            self.raza = raza
            self.edad = edad

        def mostrar_informacion(self):
            return f"Nombre: {self.nombre}, raza: {self.raza} y edad: {self.edad}. "

        def ladrar(self):
            return f"Guau!"
        
    perro = Perro("Milo", "Border Collie", 3)

    archivo.write(perro.mostrar_informacion())
    archivo.write("Saliste de un bloque de codigo. ")
    archivo.seek(0)
    a = archivo.read() 
    print(a)
    archivo.close()
    
""" Crea un administrador de contexto que permita cambiar el directorio de
trabajo al entrar en un bloque y volver al directorio original al salir. """

class FileManager:
    def __init__(self, filename="archivo.txt", mode="r+"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, type, value, traceback):
        self.file.close()

directorio_actual = "archivo2.txt"

with FileManager(directorio_actual) as archivo:
    archivo.write("Cambiamos de directorio e ingresamos al archivo2.txt")
    archivo.seek(0)
    a=archivo.read()
    print(a)