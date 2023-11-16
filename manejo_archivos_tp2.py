# A partir de aca empece a ayudarme con internet y chatGPT ya que no lo vimos todo en clase pero intente solucionarlo igual

""" Escribe un programa que abra un archivo de entrada, lea su contenido y
luego escriba ese contenido en un nuevo archivo de salida. Asegúrate
de cerrar ambos archivos al final. """

with open("archivo.txt", "r+") as archivo1:
    contenido1 = archivo1.read()
    archivo1.close()

with open("archivo2.txt", "r+") as archivo2:
    archivo2.write(contenido1)
    archivo2.seek(0)
    contenido2 = archivo2.read()
    print(contenido2)
    archivo2.close()

""" Escribe un programa que abra un archivo de texto, cuente cuántas
palabras contiene y muestre el resultado en la pantalla.
 """

with open("archivo.txt", "r+") as archivo3:
    contenido = archivo3.read()
    palabras = contenido.split() 
    total_palabras = len(palabras)
    print(total_palabras)
    archivo3.close()

""" Lee un archivo CSV que contiene registros de datos y realiza alguna
operación de procesamiento en los datos, cómo calcular promedios,
encontrar valores máximos o mínimos, o filtrar registros que cumplan
ciertas condiciones. """

import pandas as pd

data = pd.read_csv('ejemplo.csv')

promedio_notas = data['Notas'].mean()

print(promedio_notas)

""" Escribe un programa que tome varios archivos de texto y los concatena
en un solo archivo de salida. Asegúrate de cerrar todos los archivos
correctamente. """

with open("archivo.txt", "r") as archivo1:
    contenido1 = archivo1.read()
    archivo1.close()

with open("archivo2.txt", "r") as archivo2:
    contenido2 = archivo2.read()
    archivo2.close()

with open("archivo3.txt", "r+") as archivo3:
    archivo3.write(contenido1)
    archivo3.write(contenido2)
    archivo3.seek(0)
    archivo3.read()
    archivo3.close()

""" Lee un archivo CSV que contiene registros de datos y convertirlo en un
archivo JSON. """

data = pd.read_csv('ejemplo.csv')

data.to_json('ejemplo.json', orient='records', lines=True)

print("Conversión completada. Se ha creado el archivo ejemplo.json.")

