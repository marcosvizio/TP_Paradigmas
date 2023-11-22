""" Una clase es una plantilla que va a tener metodos y atributos """

""" Un objeto es una instancia de una clase va a tener atributos especificos """

""" Los atributos son las propiedades de un objeto """

""" Abstraccion, encapsulamiento, polimorfismo y herencia """

""" POO = Programacion orientada a objetos """

""" Es un = herencia y Tiene un = composicion """

""" El def __init__ o def atacar van a ser metodos """

class Humano:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni

    """ Getters y Setters  """
    """ Un getter va a ser un metodo para obtener un metodo privado """
    """ Con el property python va a entender que el codigo que este abajo va a ser una propiedad """
    @property
    def dni(self):
        return self._dni
    
    """ pascalCase, snake_case, CamelCase """
    """ Setter """
    def set_dni(self,newDni):
        if (newDni >= 1000000):
            return f"No se puede"
        self._dni = newDni
        return self.dni

    def mostrar_datos(self, numero):
        """ No usar print a la hora de retornar """
        return f"Nombre: {self.nombre}. Apellido: {self.apellido}. DNI: {self.dni}. Numero: {numero}"
    
""" ES UN : HERENCIA """
class Animal:
    pass

class Perro(Animal):
    pass

class Gato(Animal):
    pass

""" TIENE UN : COMPOSICION """

class Personaje:
    """ Composicion es instanciar una clase (objeto) dentro de una clase """
    
    pass

class Movimiento:
    pass

class Habilidad:
    pass

class Equipo:
    pass




humano1 = Humano("Marcos", "Vizio", 42148755)

humano2 = Humano("Agustina", "Monzon", 41623555)
