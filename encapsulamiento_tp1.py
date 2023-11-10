""" CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y
públicos para el saldo y titular. Definir métodos para depositar, retirar y
consultar el saldo de la cuenta.
 """

from datetime import date

class CuentaBancaria():
    def __init__(self, titular: str, saldo: int, cbu: str, transacciones: list):
        self.titular = titular
        self._saldo = saldo
        self.cbu = cbu
        self._transacciones = transacciones

    def depositar(self, monto_depositado:int):
        self._saldo = self._saldo + monto_depositado
        fecha_actual = date.today()
        transaccion = f"Monto depositado: {monto_depositado}, fecha: {fecha_actual}"
        self._transacciones.append(transaccion)
        return f"El saldo actual es de {self._saldo}"
    
    def retirar(self, monto_retirado:int):
        self._saldo = self._saldo - monto_retirado
        fecha_actual = date.today()
        transaccion = f"Monto retirado: {monto_retirado}, fecha: {fecha_actual}"
        self._transacciones.append(transaccion)
        return f"El saldo actual es de {self._saldo}"

    def mostrar_datos(self):
        return f"Titular: {self.titular}. Saldo: {self._saldo}. CBU: {self.cbu}. ULTIMAS TRANSACCIONES: {self._transacciones}."
    
cuenta = CuentaBancaria("Marcos Vizio", 15000, "0080156464555846", [])

print(cuenta.mostrar_datos())

print(cuenta.depositar(15000))

print(cuenta.mostrar_datos())

print(cuenta.retirar(30000))

print(cuenta.mostrar_datos())

""" Estudiante: Implementar la clase Estudiante con atributos como nombre,
edad y calificaciones. Utilizar el encapsulamiento para proteger los
datos que deban ser protegidos y proporcionar métodos públicos para
obtener dichos datos.
 """

class Estudiantes():
    def __init__(self, nombre: str, edad: int, calificaciones: tuple):
        self.nombre = nombre
        self.edad = edad
        self._calificaciones = calificaciones

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, edad: {self.edad} y calificaciones: {self.calificaciones}"
    
    @property
    def calificaciones(self):
        return self._calificaciones

estudiante = Estudiantes("Marcos Vizio", 24, (7,9,10))

print(estudiante.mostrar_datos())

""" Coche: Crear la clase Coche con atributos privados y/o públicos según
corresponda de velocidad y kilometraje. Definir métodos públicos para
acelerar y registrar el kilometraje de manera segura.
 """

class Coche():
    def __init__(self, velocidad, kilometraje, cant_nafta):
        self._velocidad = velocidad
        self.kilometraje = kilometraje
        self._cant_nafta = cant_nafta

    def acelerar(self, nueva_velocidad):
        self._velocidad = nueva_velocidad
        return f"La velocidad actual es de {self._velocidad}."
    
    def cargarNafta(self, nafta_cargada):
        self._cant_nafta = self._cant_nafta + nafta_cargada
        return f"La nafta actual es de: {self._cant_nafta}"
    
    def datosKilometraje(self):
        return f"El kilometraje actual es de: {self.kilometraje}"
    
coche = Coche(25,10000,50)

print(coche.cargarNafta(25))

print(coche.datosKilometraje())


