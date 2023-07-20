'''Los ciclos son una herramienta esencial dentro de Python. 
Sirven para repetir un bloque de código varias veces, dependiendo de una condición específica. 
Los ciclos son fundamentales para la automatización de tareas y la eficiencia en el código.
Existen dos tipos de ciclos en Python: los ciclos “for” y los ciclos “while”. 
Ambos tienen una sintaxis similar, pero se utilizan en situaciones diferentes.
'''
# Ciclo For
#El ciclo “for” es utilizado para repetir un bloque de código un número específico de veces. Su sintaxis básica es la siguiente:

#for variable in secuencia:
  # código a ejecutar
#La variable se establece para recorrer los elementos en la secuencia especificada, y el código dentro del 
# ciclo se ejecutará para cada elemento de la secuencia. Por ejemplo, el siguiente ciclo “for” imprimirá los números del 1 al 10 en la consola:

for i in range(1, 11):
  print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
'''También se utiliza para recorrer las propiedades de un diccionario y de colecciones como una lista.
El uso de un ciclo “for in” es la siguiente:'''

user = {
  "name": "Pepito",
  "age": 20,
  "role": "Python developer"
}

for prop in user:
  print(user[prop])
# "Pepito"
# 20
# "Python developer"

'''En este ejemplo, se establece una variable “prop” que se utilizará para recorrer las propiedades del diccionario. 
El valor de cada propiedad se imprimirá en la consola.
Por otro lado, la sintaxis de un ciclo for para recorrer una lista es la siguiente:'''

technologies = ["py", "django", "webscraping"]

for element in technologies:
  print(element)
# "py"
# "django"
# "webscraping"

'''En este ejemplo, se establece una variable “element” que se utilizará para recorrer cada elemento en la lista. 
Cada valor se imprimirá en la consola.'''

# Ejemplos Reales 

'''El ciclo for en Python se utiliza para iterar sobre una secuencia de elementos o para ejecutar un bloque de código un número específico de veces. 
Aquí tienes una descripción detallada y ejemplos de cómo se utiliza el ciclo for:

La sintaxis general del ciclo for es la siguiente:
for elemento in secuencia:
    # Bloque de código a ejecutar
En cada iteración del ciclo, la variable elemento toma el valor de un elemento de la secuencia y se ejecuta el bloque de código correspondiente. Esto se repite hasta que se hayan recorrido todos los elementos de la secuencia.
'''
# Aquí tienes un ejemplo simple que muestra cómo iterar sobre una lista utilizando un ciclo for:
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
'''En este ejemplo, el ciclo for recorre la lista frutas y en cada iteración, la variable fruta toma el valor de un elemento de la lista. 
Luego, se imprime el valor de fruta. La salida será:'''

#manzana
#banana
#naranja

'''Además de iterar sobre listas, el ciclo for se puede utilizar con otras secuencias, como cadenas, tuplas y rangos. 
Aquí tienes ejemplos adicionales:'''

# Iterar sobre una cadena de texto
mensaje = "Hola, mundo!"
for letra in mensaje:
    print(letra)

# Iterar sobre una tupla
coordenadas = (3, 4, 5)
for coordenada in coordenadas:
    print(coordenada)

# Iterar utilizando un rango de números
for i in range(1, 200):
    print(i)
'''En resumen, el ciclo for es una estructura de control poderosa en Python que permite iterar sobre secuencias y ejecutar un bloque de código 
para cada elemento de la secuencia. 
Puedes utilizarlo para realizar diferentes tareas, como procesar elementos de una lista, recorrer caracteres de una cadena, 
trabajar con tuplas o iterar sobre rangos de números.'''