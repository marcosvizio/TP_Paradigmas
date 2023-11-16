class Libro:
    def __init__(self, nombre, paginas, genero, autor):
        self.nombre = nombre
        self.paginas = paginas
        self.genero = Genero(genero)
        self.autor = Autor(autor)
    def infolibro(self):
        return f"Los datos del libro son {self.nombre}, {self.paginas}, {self.genero.tipo_genero}, {self.autor.nombre}"

class Autor():
    def __init__(self, nombre):
        self.nombre = nombre

class Genero():
    def __init__(self, tipo_genero):
        self.tipo_genero = tipo_genero

class Usuario(): 
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni

    def asignarDni(self, nuevo_dni):
        if nuevo_dni != "":
            self._dni = nuevo_dni
            return f"Tu nuevo dni es {nuevo_dni}"
        return "no se pudo asignar"

    @property
    def obtenerDni(self):
        return self._dni

    def leer(self):
        pass

class Estudiante(Usuario):
    def __init__(self, nombre, dni, edad, curso, materia):
        super().__init__(nombre,dni, edad)
        self.curso = curso
        self.materia = materia

    def leer(self):
        return f"El estudiante puede leer un libro de clase"

    def mostrar_info(self):

        return f"la info es {self.nombre}, {self._dni}, {self.edad}, {self.curso}, {self.materia}"

class Profesor(Usuario):
    def __init__(self, nombre, dni, edad, curso, materia):
        super().__init__(nombre,dni, edad)
        self.curso = curso
        self.materia = materia

    def leer(self):
        return f"El profesor puede leer las notas"

libro1 = Libro("pepe", 30, "comedia","Alguno")
estudiante1 = Estudiante("Maria", 35432123, 31, "5to", "POO")
profesor1 = Profesor("Juan", 35436432, 34, "5to", "POO")
print(estudiante1.leer())
print(profesor1.leer())
print(libro1.infolibro())
print(estudiante1.mostrar_info())