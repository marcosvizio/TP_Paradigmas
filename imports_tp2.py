""" Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación absoluta.
 """

from adm_contexto_tp2 import Perro

perro = Perro("Milo","Border Collie",3)

print(perro.mostrar_informacion())
