""" Sistema de Geometría 3D
Diseña un sistema de geometría tridimensional que trabaje con figuras en el
espacio 3D. Debes implementar las siguientes clases:
Punto3D: Una clase que representa un punto en el espacio 3D con
coordenadas x, y, y z.
Figura3D: Una clase abstracta que representa una figura tridimensional y
define métodos abstractos para calcular su volumen y área superficial.
Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos
para calcular el volumen y área superficial específicos de cada figura.
Crea instancias de estas clases y demuestra cómo calcular el volumen y área
superficial de diferentes figuras tridimensionales.
 """

from abc import ABC, abstractmethod

class Punto3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Figura3D(ABC):
    pi = 3.14
    def __init__(self, altura:int, radio:int, lados:tuple):
        self.altura = altura
        self.radio = radio
        self.lados = lados

    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass

class Cubo(Figura3D):
    def calcular_volumen(self):
        return self.lados[0]**3
    
    def calcular_area(self):
        return 6*self.lados[0]**2
    
class Esfera(Figura3D):
    def calcular_volumen(self):
        return 4/3*self.pi*(self.radio**3)

    def calcular_area(self):
        return 4*self.pi*(self.radio**2)
    
class Cilindro(Figura3D):
    def calcular_volumen(self):
        return self.pi*(self.radio**2)*self.altura
    
    def calcular_area(self):
        return 2*self.pi*(self.radio**2)+(2*self.pi*self.radio*self.altura)
    
cubo = Cubo(0,0,(5,0))

print(cubo.calcular_volumen())
print(cubo.calcular_area())

esfera = Esfera(0,6,())

print(esfera.calcular_volumen())
print(esfera.calcular_area())

cilindro = Cilindro(6,3,())

print(cilindro.calcular_volumen())
print(cilindro.calcular_area())
    