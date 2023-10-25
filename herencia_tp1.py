""" Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir
atributos como nombre y edad. Las subclases deben heredar y definir
métodos y atributos relacionados con el comportamiento y
características de cada tipo de animal.
 """

class Animal():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
class Perro(Animal):
    def __init__(self, nombre, edad, raza, color_pelaje):
        super().__init__(nombre, edad)
        self.raza = raza
        self.color_pelaje = color_pelaje

    def ladrar(self):
        return print("Guau")
    
    def gruñir(self):
        return print("Grrr")
    
class Gato(Animal):
    def __init__(self, nombre, edad, genero, peso):
        super().__init__(nombre, edad)
        self.genero = genero
        self.peso = peso

    def ronrronear(self):
        return print("Prrr")
    
    def maullar(self):
        return print("Miau")
    
class Pajaro(Animal):
    def __init__(self, nombre, edad, especie, tamaño):
        super().__init__(nombre, edad)
        self.especie = especie
        self.tamaño = tamaño

    def volar(self):
        return print("Vuela")
    
    def cantar(self):
        return print("Pio pio")
    

perro = Perro("Milo", 5, "Border Collie", "Marron")

""" Empleado: Crear las clases Empleado, Gerente y Trabajador. Se debe
tener atributos como nombre, salario y departamento. Las subclases
deben heredar y definir los métodos y atributos necesarios para
representar cada tipo de empleado """

class Trabajador():
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

class Empleado(Trabajador):
    def __init__(self, nombre, salario, departamento, puesto, telefono):
        super().__init__(nombre, salario, departamento)
        self.puesto = puesto
        self.telefono = telefono

class Gerente(Empleado): 
    def __init__(self, nombre, salario, departamento, puesto, telefono, beneficios):
        super().__init__(nombre, salario, departamento, puesto, telefono)
        self.beneficios = beneficios

""" Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las
clases deben contener atributos como color y dimensiones. Las
subclases deben heredar y definir métodos y atributos para calcular el 
área y el perímetro de cada forma """

class Forma():
    def __init__(self, color:str, dimensiones:tuple):
        self.color = color
        self.dimensiones = dimensiones

class Circulo(Forma):
    pi = 3.14
    def __init__(self, color: str, dimensiones: tuple, radio):
        super().__init__(color, dimensiones)
        self.radio = radio

    def calcularArea(self):
        return self.pi * (self.radio * self.radio)
    
    def calcularPerimetro(self):
        return 2 * self.pi * self.radio

class Rectangulo(Forma):
    def __init__(self, color: str, dimensiones: tuple, base, altura):
        super().__init__(color, dimensiones)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura
    
    def calcularPerimetro(self):
        return 2*(self.base+self.altura)


        