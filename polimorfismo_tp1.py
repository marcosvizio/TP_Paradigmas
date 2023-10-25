""" FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de
abstracción y crear un método muestre información específica de la
figura utilizando polimorfismo. Luego, crear una lista de figuras
geométricas de diferentes tipos y utilizar el polimorfismo para imprimir
su información.
 """

class FiguraGeometrica():
    def __init__(self, radio:int, altura:int, base:int):
        self.radio = radio
        self.altura = altura
        self.base = base
        self.pi = 3.14

    def informacionFigura(self):
        return print(f"Base: {self.base}, Altura: {self.altura} y Radio: {self.radio}")


class Rectangulo(FiguraGeometrica):
    def informacionFigura(self):
        return super().informacionFigura()
    
class Circulo(FiguraGeometrica):
    def informacionFigura(self):
        return super().informacionFigura()
    
rectangulo = Rectangulo(0,5,8)

circulo = Circulo(6,0,0)

rectangulo.informacionFigura()

circulo.informacionFigura()

""" Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar
polimorfismo para realizar el sonido característico del animal. Luego,
crear una lista de animales de diferentes tipos y utilizar el polimorfismo
para hacer que emiten sus sonidos """

class Animal():
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido

    def hacer_sonido(self):
        return print(f"{self.sonido}")
    
class Perro(Animal):
    def hacer_sonido(self):
        return super().hacer_sonido()
    
class Gato(Animal):
    def hacer_sonido(self):
        return super().hacer_sonido()
    
class Pollito(Animal):
    def hacer_sonido(self):
        return super().hacer_sonido()
    
perro = Perro("Milo", 3, "Guau")

gato = Gato("Min", 5, "Miau")

pollito = Pollito("Little", 8, "Pio pio")

perro.hacer_sonido()
gato.hacer_sonido()
pollito.hacer_sonido()

""" Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar
polimorfismo para calcular el salario de acuerdo con las reglas
específicas de cada tipo de empleado. Luego, crear una lista de
empleados de diferentes tipos y utilizar el polimorfismo para calcular
sus salarios. """

class Trabajador():
    def __init__(self, nombre, salario, experiencia):
        self.nombre = nombre
        self._salario = salario
        self.experiencia = experiencia

    def calcular_salario(self):
        if self.experiencia == "senior":
            self._salario = self._salario * 2
            return print(f"Tu sueldo es de: {self._salario}")
        elif self.experiencia == "semi":
            self._salario = self._salario * 1.5
            return print(f"Tu sueldo es de: {self._salario}")
        return print(f"Tu sueldo es de: {self._salario}")

class Empleado(Trabajador):
    def calcular_salario(self):
        return super().calcular_salario()
    
empleado1 = Empleado("Marcos Vizio", 15000, "junior")

empleado1.calcular_salario()

empleado2 = Empleado("Agustina Monzon", 20000, "semi")

empleado2.calcular_salario()