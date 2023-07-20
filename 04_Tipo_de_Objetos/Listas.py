'''Las listas son un tipo de objeto que permite almacenar una colección de valores. 
Estos valores pueden ser de cualquier tipo, como números, cadenas, objetos, incluso otras listas. 
Las listas son muy útiles para almacenar y manejar datos en una sola estructura.

La sintaxis para crear una lista en Python es la siguiente:

mi_lista = [valor1, valor2, valor3]
Por ejemplo, el siguiente código crea una lista llamada “colores” que contiene tres valores:
“rojo”, “azul” y “verde”:

colores = ["rojo", "azul", "verde"]
Las listas tienen un índice numérico que comienza en 0. 
Por lo tanto, el primer elemento de la lista tiene el índice 0, el segundo tiene el índice 1,
y así sucesivamente. Por ejemplo, para acceder al primer elemento de la lista “colores”, se 
utilizaría la sintaxis colores[0].'''

colores = ["rojo", "azul", "verde"]
colores[0]
# "rojo"
#Para actualizar un valor específico en una lista, se puede utilizar la sintaxis lista[indice] = nuevo_valor.

numeros = [1, 2, 3, 4, 5]
numeros[0] = -8
print(numeros) 
# [-8, 2, 3, 4, 5]

#Métodos más usados en las listas

#append(): Permite agregar un nuevo elemento al final de la lista.

colores.append("amarillo")
print(colores) # ["rojo", "azul", "verde", "amarillo"]

#pop(): Permite eliminar el último elemento de la lista.
colores.pop()
print(colores) # ["rojo", "azul", "verde"]

#count(elemento): Cuenta cuántas veces un elemento está en una lista.
numeros = [1, 2, 3, 2, 4, 2]
print(numeros.count(2)) # 3

#extend(lista): Permite extender una lista agregándole los elementos de otra lista.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1) # [1, 2, 3, 4, 5, 6]

#reverse(): Revierte el orden de los elementos de la lista.
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros) # [5, 4, 3, 2, 1]

#sort(): Ordena la lista de manera ascendente o descendente.
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()
print(numeros) # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numeros.sort(reverse=True)
print(numeros) # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Ejemplos

'''Las listas en Python son estructuras de datos que permiten almacenar múltiples elementos en una sola variable. 
Aquí tienes algunos ejemplos claros de cómo usar listas en Python:'''

#Crear una lista vacía:
mi_lista = []

#Crear una lista con elementos:
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mixta = [1, "hola", True, 3.14]

#Acceder a elementos de una lista mediante índices:
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])  # Salida: "manzana"
print(frutas[2])  # Salida: "naranja"

#Modificar elementos de una lista:
numeros = [1, 2, 3, 4, 5]
numeros[2] = 10
print(numeros)  # Salida: [1, 2, 10, 4, 5]

#Obtener la longitud de una lista:
frutas = ["manzana", "banana", "naranja"]
print(len(frutas))  # Salida: 3

#Agregar elementos a una lista:
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")
print(frutas)  # Salida: ["manzana", "banana", "naranja", "pera"]

#Recorrer una lista utilizando un ciclo for:
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)
# Salida:
# manzana
# banana
# naranja

#Verificar si un elemento está en una lista:
numeros = [1, 2, 3, 4, 5]
print(3 in numeros)  # Salida: True
print(6 in numeros)  # Salida: False

'''Estos son solo algunos ejemplos de cómo trabajar con listas en Python. 
Las listas son estructuras muy versátiles y se utilizan ampliamente en programación para almacenar y manipular conjuntos de elementos. '''