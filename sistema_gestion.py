class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni

    @property
    def dni(self):
        return self._dni

class Empleado(Persona):
    def __init__(self, nombre, edad, dni, salario, cargo):
        super().__init__(nombre, edad, dni)
        self._salario = salario
        self.cargo = cargo

    def calcular_salario(self):
        if self.cargo == "senior":
            self._salario = self._salario * 2
            return print(f"El salario es de {self.salario}")
        elif self.cargo == "semi":
            self._salario = self.salario * 1.5
            return print(f"El salario es de {self.salario}")
        return print(f"El salario es de {self.salario}")

    @property
    def salario(self):
        return self._salario
    
class Gerente(Empleado):
    def __init__(self, nombre, edad, dni, salario, cargo, departamento):
        super().__init__(nombre, edad, dni, salario, cargo)
        self.departamento = departamento

class Departamento():
    def __init__(self, empleados: list):
        self._empleados = empleados

    def agregar_empleado(self, nuevo_empleado):
        self._empleados.append(nuevo_empleado)
        return print(f"Agregamos al empleado: {nuevo_empleado.nombre}.")

    def eliminar_empleados(self, eliminar_empleado):
        self._empleados.remove(eliminar_empleado)
        return print(f"Eliminamos al empleado: {eliminar_empleado}")
    
    def consultar_empleados(self):
        for i in self._empleados:
            print(f"Nombre: {i.nombre}, edad: {i.edad}, DNI: {i.dni}, salario: {i._salario} y cargo: {i.cargo}.")

    @property
    def empleados(self):
        return self._empleados
    
empleado1 = Empleado("Marcos Vizio",24,42254755,30000,"semi")
empleado2 = Empleado("Jose Ruiz",30,5587627,45000,"senior")
empleado3 = Empleado("Barbara Fernandez",28,14786522,35000,"junior")

departamento = Departamento([])

departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)
departamento.agregar_empleado(empleado3)

departamento.consultar_empleados()
    