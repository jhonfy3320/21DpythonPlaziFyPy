'''Para leer archivos CSV (Comma-Separated Values) en Python, puedes utilizar la biblioteca 
incorporadacsv . 
El formato CSV es ampliamente utilizado para almacenar datos tabulares, donde cada línea del 
archivo representa una fila y los valores de cada columna están separados por comas u otro delimitador.

A continuación, le mostraré un ejemplo detallado de cómo leer un archivo CSV en Python:

Supongamos que tenemos un archivo CSV llamado "datos.csv" con el siguiente contenido:'''

'''Nombre,Edad,Profesión
Juan,30,Ingeniero
María,25,Médico
Carlos,28,Abogado'''


#Vamos a escribir un programa en Python para leer este archivo y mostrar su contenido:

import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        return "El archivo no existe."
    except IOError:
        return "Error al leer el archivo."

# Nombre del archivo CSV que queremos leer
archivo = "datos.csv"

# Llamamos a la función para leer el archivo CSV
contenido = read_csv_file(archivo)

# Mostramos el contenido del archivo CSV
for row in contenido:
    print(row)
#Resultado de la ejecución del programa:

['Nombre', 'Edad', 'Profesión']
['Juan', '30', 'Ingeniero']
['María', '25', 'Médico']
['Carlos', '28', 'Abogado']

#Explicación del código:

'''
Importamos el módulo csv para trabajar con archivos CSV en Python.
Definimos una función llamada read_csv_fileque recibe el nombre del archivo CSV como parámetro.
Utilizamos un bloque try-exceptpara posibles excepciones, como la no existencia del archivo o errores de lectura.
Abrimos el archivo en modo de lectura utilizando el withenunciado.
Utilizamos csv.reader(file)para crear un objeto lector que nos permitirá leer el contenido del archivo CSV.
Convertimos el objeto lector en una lista de listas utilizando list(reader), donde cada lista representa una fila del archivo CSV.
Finalmente, retornamos la lista de listas que contiene el contenido del archivo CSV.
Es importante tener en cuenta que cada valor en el archivo CSV se trata como una cadena de caracteres en la lista resultante. 
Si necesita convertir los valores a otros tipos de datos (por ejemplo, convertir las edades a enteros), deberá realizar la conversión 
manualmente después de leer el archivo CSV. 
Además, asegúrese de que el archivo existe en la ruta especificada y de que el programa tiene permiso de lectura para el archivo. 
Si el archivo no existe o hay algún error al leerlo, el programa manejará las excepciones y mostrará un mensaje adecuado.'''