""" Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación absoluta.
 """

from herencia_tp1 import Perro

perro = Perro("Milo",4,"Border Collie", "Rubio")

print(perro.ladrar())

""" Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación relativa """

from .abstraccion_tp1 import Rectangulo

rectangulo = Rectangulo(0,5,8,0,0,0)

""" Crear dos módulos en el mismo directorio. Desde un módulo, importar
el otro sin usar from """

import abstraccion_tp1

coche = abstraccion_tp1.Coche("Nissan", "Skyline GT 34", 250, 50, "Xr4TX")

""" Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación absoluta y
generar un error de importación circular. """

from ejemplo_import import importCircular

importCircular()

""" Crear dos módulos en el mismo directorio. Desde un módulo, importar
el otro sin usar from y utilizando alias. """

import polimorfismo_tp1 as poli

trabajador = poli.Trabajador("Marcos",2500,"semi")

""" Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación absoluta y
utilizar un alias """

from .encapsulamiento_tp1 import Estudiantes as Estu

estudiante = Estu("Marcos", 18, (10,8,9))

""" Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación relativa y
utilizar un alias """

from encapsulamiento_tp1 import CuentaBancaria as Cuenta

cuenta = Cuenta("Marcos",50000,"15a15D1SD112",[])


