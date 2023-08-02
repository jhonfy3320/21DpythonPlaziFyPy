## Resumiendo y proporcionando ejemplos reales de código para cada una de las estructuras de datos mencionadas:

#Listas:
#Descripción: Una lista es una secuencia ordenada y mutable de elementos.
#Ejemplo:

# Crear una lista
lista = [1, 2, 3, "Hola", True]

# Acceder a elementos de la lista
print(lista[0])  # Output: 1

# Modificar elementos de la lista
lista[1] = "Python"
print(lista)  # Output: [1, 'Python', 3, 'Hola', True]

#Tuplas:
#Descripción: Las tuplas son similares a las listas, pero son inmutables.
#Ejemplo:

# Crear una tupla
tupla = (1, 2, 3, "Hola", True)

# Acceder a elementos de la tupla
print(tupla[2])  # Output: 3

# Intentar modificar elementos de la tupla (esto generará un error)
tupla[1] = "Python"  # TypeError: 'tuple' object does not support item assignment

#Conjuntos:
#Descripción: Un conjunto es una colección no ordenada y mutable de elementos únicos.
#Ejemplo:

# Crear un conjunto
conjunto = {1, 2, 3, 4, 5}

# Agregar elementos al conjunto
conjunto.add(6)

# Intentar agregar un elemento duplicado (esto no tiene efecto)
conjunto.add(3)

# Eliminar un elemento del conjunto
conjunto.remove(4)

print(conjunto)  # Output: {1, 2, 3, 5, 6}

#Diccionarios:
#Descripción: Los diccionarios son estructuras de datos que almacenan pares clave-valor.
#Ejemplo:

# Crear un diccionario
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "México"}

# Acceder a valores mediante claves
print(diccionario["nombre"])  # Output: Juan

# Agregar un nuevo par clave-valor
diccionario["profesion"] = "Ingeniero"

# Modificar un valor existente
diccionario["edad"] = 30

# Eliminar un par clave-valor
del diccionario["ciudad"]

print(diccionario)  # Output: {'nombre': 'Juan', 'edad': 30, 'profesion': 'Ingeniero'}

#Pilas:
#Descripción: Una pila sigue la regla LIFO (Last In, First Out).
#Ejemplo:

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print(pila.pop())  # Output: 3
print(pila.pop())  # Output: 2

#Colas:
#Descripción: Una cola sigue la regla FIFO (First In, First Out).
#Ejemplo:

from collections import deque

cola = deque()
cola.append(1)
cola.append(2)
cola.append(3)

print(cola.popleft())  # Output: 1
print(cola.popleft())  # Output: 2

#Árboles:
#Descripción: Un árbol es una estructura de datos no lineal compuesta por nodos conectados mediante enlaces.
#Ejemplo:

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Crear un árbol binario
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

#Grafos:
#Descripción: Un grafo es una estructura de datos que consta de un conjunto de nodos y un conjunto de conexiones entre ellos.
#Ejemplo:

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.conexiones = {}

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.conexiones[nodo] = []

    def agregar_conexion(self, nodo1, nodo2):
        self.conexiones[nodo1].append(nodo2)
        self.conexiones[nodo2].append(nodo1)

grafo = Grafo()
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_conexion(1, 2)
'''
Estos son solo ejemplos básicos de cómo utilizar las diferentes estructuras de datos en Python. 
Cada estructura tiene muchas otras funcionalidades y métodos que se pueden explorar para adaptarse a diferentes escenarios y necesidades. 
La elección de la estructura de datos adecuada depende del problema que estés resolviendo y los requisitos de eficiencia 
y funcionalidad que necesites.'''