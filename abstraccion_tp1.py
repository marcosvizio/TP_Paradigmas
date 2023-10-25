"""  FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo
 y Triangulo y que contenga métodos y atributos relacionados con el
 cálculo del área y perímetro de una figura geométrica. Definan los
 métodos y atributos necesarios para calcular el área y el perímetro de
 cada tipo de figura utilizando los conceptos de abstracción. """

class FiguraGeometrica():
    def __init__(self, radio:int, altura:int, base:int, lado1: int, lado2: int, lado3: int):
        self.radio = radio
        self.altura = altura
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.pi = 3.14

class Circulo(FiguraGeometrica):
    def calcularArea(self):
        return self.pi * (self.radio * self.radio)
    
    def calcularPerimetro(self):
        return 2*self.pi*self.radio

circulo = Circulo(5,0,0,0,0,0)

print(circulo.calcularArea())
print(circulo.calcularPerimetro())

class Rectangulo(FiguraGeometrica):
    def calcularArea(self):
        return self.base * self.altura
    
    def calcularPerimetro(self):
        return 2*(self.altura+self.base)
    
rectangulo = Rectangulo(0,5,7,0,0,0)

print(rectangulo.calcularArea())
print(rectangulo.calcularPerimetro())

class Triangulo(FiguraGeometrica):
    def calcularArea(self):
        return (self.base*self.altura)/2
    
    def calcularPerimetro(self):
        return (self.lado1 + self.lado2 + self.lado3)
    
triangulo = Triangulo(0,5,6,3,6,9)
    
print(triangulo.calcularArea())

print(triangulo.calcularPerimetro())

""" Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir
atributos como titulo, autor y precio. La clase Libreria debe contener una
lista de objetos Libro y métodos para calcular el precio total de todos
los libros en la librería.
 """

class Libro():
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

libro1 = Libro("WOW Legends", "Marcos Vizio", 50)

libro2 = Libro("Ojo por ojo", "Agustina Monzon", 40)

libros = [libro1, libro2]

class Libreria(Libro):
    def __init__(self, libros=[]):
        self.libros = libros
        self.preciosTotal = 0

    def calcularPrecios(self):
        for i in self.libros:
            self.preciosTotal += i.precio
            print(self.preciosTotal)

libreria = Libreria(libros)

libreria.calcularPrecios()

""" Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y
Bicicleta. La clase Vehiculo debe tener propiedades como marca,
modelo y velocidad_maxima. Cada subclase debe definir sus métodos y
atributos específicos relacionados con el comportamiento de cada tipo
de vehículo. """

class Vehiculo():
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cant_nafta, patente):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cant_nafta = cant_nafta
        self.patente = patente

    def cargarNafta(self,cant_cargada):
        self.cant_nafta = self.cant_nafta + cant_cargada
        return print(f"La cantidad de nafta que queda es de {self.cant_nafta}")
    
    def verPatente(self):
        return print(f"La patente del coche es {self.patente}")
    
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cilindradas, peso_kg):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cilindradas = cilindradas
        self.peso_kg = peso_kg

    def verCilindradas(self):
        return print(f"Las cilindradas de la moto son: {self.cilindradas}")
    
    def calcularPesoTotal(self, peso_persona):
        pesoTotal = self.peso_kg + peso_persona
        return print(f"El peso total de la moto mas el conductor es {pesoTotal}")
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, color, numero_velocidades):
        super().__init__(marca, modelo, velocidad_maxima)
        self.color = color
        self.numero_velocidades = numero_velocidades

    def cambiarColor(self, color_nuevo):
        self.color = color_nuevo
        return print(f"Cambiaste el color de la bicicleta por {self.color}")
    
    def cambiarVelocidad(self):
        self.numero_velocidades = self.numero_velocidades + 1
        return print(f"Cambiaste la velocidad a {self.numero_velocidades}")

bicicleta = Bicicleta("GTO","RT345",100,"rojo",1) 

bicicleta.cambiarVelocidad()