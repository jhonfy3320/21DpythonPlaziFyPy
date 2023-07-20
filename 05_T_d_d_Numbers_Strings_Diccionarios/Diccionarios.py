'''Diccionarios
Los diccionarios son estructuras de datos que nos permiten almacenar un conjunto de pares clave-valor.
Estos pares son conocidos como elementos del diccionario.

Para crear un diccionario, debemos utilizar las llaves {} y especificar los elementos del diccionario 
mediante la sintaxis clave: valor. Los valores de los elementos pueden ser de cualquier tipo de dato, 
incluyendo otros diccionarios.
'''
#Ejemplo:

persona = {
  "nombre": "Fulanita",
  "platziRank": 9567,
	"cursoFavorito": {
		"nombre": "Básico de Python",
		"clases": 30,
		"duracion": "2 horas"
	}
}
#Para acceder a los elementos de un diccionario, podemos utilizar la clave como índice.

#Ejemplo:

print(persona["nombre"]) # "Fulanita"
print(persona["cursoFavorito"]["nombre"]) # "Básico de Python"
print(persona["platziRank"]) # 9567
'''Booleanos
Booleanos
Los valores booleanos (boolean) son un tipo de dato que representa un valor verdadero o falso. En Python, podemos utilizar la palabra clave True para representar el valor verdadero y False para representar el valor falso.
'''
curso_completado = True
lectura_completada = False
'''No pasa nada si no recuerdas el tipo de dato con el que estás trabajando, dentro de Python existe la 
función type() la cual te dirá el tipo de dato con el que estás trabajando'''

type("#PlatziChallenge") 
# <class 'str'>
type(30) 
# <class 'int'>
type({}) 
# <class 'dict'>

type([]) # <class 'list'>

'''Los diccionarios son útiles cuando necesitas almacenar y acceder a datos de manera eficiente 
utilizando claves. Puedes realizar diversas operaciones con diccionarios, como agregar elementos, 
eliminar elementos, actualizar valores, entre otros.'''

# Creación de un diccionario
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceso a valores mediante claves
print(persona["nombre"])  # Salida: Juan
print(persona["edad"])  # Salida: 25

# Modificación de valores
persona["edad"] = 26

# Agregar un nuevo par clave-valor
persona["profesion"] = "Ingeniero"

# Eliminar un par clave-valor
del persona["ciudad"]
