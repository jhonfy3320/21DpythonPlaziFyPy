'''Los diccionarios son una estructura de datos que permiten almacenar una colección de pares 
clave-valor. 
Las claves son strings y se utilizan para acceder a los valores correspondientes. 
La sintaxis para crear un diccionario es la siguiente:'''

'''mi_diccionario = {
    'clave1': valor1,
    'clave2': valor2,
    'clave3': valor3
}'''

'''Por ejemplo, el siguiente código crea un diccionario llamado “curso” que tiene cinco pares clave-valor: 
“nombre”, “duración”, “clases”, “detalles” y “comentarios”:'''

curso = {
    'nombre': '30 días de Python',
    'duración': '20 horas',
    'clases': 100,
    'detalles': {
        'tecnologias': ['Python', 'Flask', 'Django'],
        'calificacion': 5,
    },
    'comentarios': ['¡Excelente curso!', 'Python es poderoso', 'Hola']
}
'''Para acceder a los valores de un diccionario, se utiliza la notación de corchetes y se especifica la clave. 
Por ejemplo, para acceder al nombre del curso anterior se utilizaría la siguiente sintaxis:
'''
print(curso['nombre']) 
# "30 días de Python"
'''Además de los valores, los diccionarios también pueden tener métodos, que son 
funciones asociadas a un diccionario. Por ejemplo, el siguiente código crea un diccionario 
“coche” con una clave “marca” y un método “encender”:'''

coche = {
    'marca': 'Toyota',
    'encender': lambda: print('El coche ha sido encendido')
}
'''Para llamar a un método de un diccionario, se utiliza la notación de corchetes y se 
especifica la clave. Por ejemplo:'''

coche['encender']() # "El coche ha sido encendido"
'''Python también tiene una característica llamada herencia, que permite crear nuevos diccionarios
a partir de diccionarios existentes y heredar sus pares clave-valor. 
Esto permite a los desarrolladores crear nuevos objetos a partir de objetos existentes 
y agregar o modificar sus pares clave-valor, pero esto lo verás mucho más adelante, 
por el momento no tienes de que preocuparte.'''

#Ejemplos 

'''Los diccionarios en Python son estructuras de datos que permiten almacenar pares de clave-valor. 
Cada valor está asociado a una clave única que se utiliza para acceder a ese valor. 
Aquí tienes algunos ejemplos claros de cómo usar diccionarios en Python:'''

#Crear un diccionario vacío:

mi_diccionario = {}

#Crear un diccionario con elementos:
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

#Acceder a un valor mediante su clave:
print(persona["nombre"])  # Salida: "Juan"
print(persona["edad"])    # Salida: 30

#Modificar el valor de una clave
persona["edad"] = 31
print(persona["edad"])  # Salida: 31

#Agregar un nuevo par clave-valor:

persona["ocupacion"] = "Ingeniero"
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniero'}

#Verificar si una clave está en el diccionario:
print("nombre" in persona)    # Salida: True
print("apellido" in persona)  # Salida: False

#Obtener todas las claves o valores del diccionario:
print(persona.keys())    # Salida: ['nombre', 'edad', 'ciudad', 'ocupacion']
print(persona.values())  # Salida: ['Juan', 31, 'Madrid', 'Ingeniero']

#Recorrer un diccionario usando un ciclo for:
for clave, valor in persona.items():
    print(clave, ":", valor)
# Salida:
# nombre : Juan
# edad : 31
# ciudad : Madrid
# ocupacion : Ingeniero

'''Estos son solo algunos ejemplos de cómo trabajar con diccionarios en Python. 
Los diccionarios son estructuras muy útiles para almacenar y acceder a datos 
utilizando claves significativas. 
Puedes usar para representar información estructurada y organizar tus datos de manera eficiente.'''