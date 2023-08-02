'''La lectura de archivos de texto en Python es una operación común y sencilla. 
Puedes utilizar el método open()para abrir un archivo en modo de lectura ( 'r') 
y luego utilizar diferentes métodos para leer su contenido. '''

#Aquí tienes un ejemplo detallado y real de cómo leer un archivo de texto .txt:

#Supongamos que tenemos un archivo de texto llamado "datos.txt" con el siguiente contenido:

'''Nombre: Juan
Edad: 30
Profesión: Ingeniero'''

#Vamos a escribir un programa en Python para leer este archivo y mostrar su contenido:

def read_txt_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "El archivo no existe."
    except IOError:
        return "Error al leer el archivo."

# Nombre del archivo que queremos leer
archivo = "datos.txt"

# Llamamos a la función para leer el archivo
contenido = read_txt_file(archivo)

# Mostramos el contenido del archivo
print(contenido)

#Resultado de la ejecución del programa:

'''
Nombre: Juan
Edad: 30
Profesión: Ingeniero'''

#Explicación del código:
'''
Definimos una función llamada read_txt_fileque recibe el nombre del archivo como parámetro.
Utilizamos un bloque try-exceptpara posibles excepciones, como la no existencia del archivo o errores de lectura.
Abrimos el archivo en modo de lectura utilizando elwith enunciado, lo cual garantiza que el archivo se cerrará automáticamente después de su uso.
Leemos el contenido del archivo utilizando el método read()y lo almacenamos en la variable content.
Finalmente, retornamos el contenido del archivo.
Es importante asegurarse de que el archivo existe en la ruta especificada y de que el programa tiene permiso de lectura para el archivo. 
Si el archivo no existe o hay algún error al leerlo, el programa manejará las excepciones y mostrará un mensaje adecuado.'''