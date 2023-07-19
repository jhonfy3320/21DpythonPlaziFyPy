'''Las tuplas son otro tipo de objeto que permiten almacenar una colección de valores, pero a diferencia de las listas, 
son inmutables, es decir, no se pueden modificar una vez que se han creado. La sintaxis para crear una tupla es la siguiente:'''

'''mi_tupla = (valor1, valor2, valor3)
Por ejemplo, el siguiente código crea una tupla llamada “puntos” que contiene tres valores: (1, 2), (3, 4) y (5, 6):
'''
puntos = ((1, 2), (3, 4), (5, 6))
'''Las tuplas también tienen un índice numérico que comienza en 0. Por lo tanto, el primer elemento de la tupla tiene el índice 0, 
el segundo tiene el índice 1, y así sucesivamente. 
Por ejemplo, para acceder al primer elemento de la tupla “puntos”, se utilizaría la sintaxis puntos[0].'''

puntos = ((1, 2), (3, 4), (5, 6))
puntos[0]
# (1, 2)
'''Como las tuplas son inmutables, no se pueden actualizar un valor específico en una tupla. 
Pero se puede crear una nueva tupla a partir de una existente, 
utilizando la sintaxis tupla = tupla[:indice] + (nuevo_valor,) + tupla[indice+1:].'''

puntos = ((1, 2), (3, 4), (5, 6))
nuevo_punto = (7, 8)
puntos = puntos[:1] + (nuevo_punto,) + puntos[2:]
print(puntos)
# ((1, 2), (7, 8), (5, 6))

# Métodos más usados en las tuplas

'''Aunque las tuplas son inmutables y no tienen métodos específicos como las listas, 
se pueden utilizar algunos métodos que aplican para cualquier objeto en Python.'''

#index(elemento): Retorna el índice de la primera ocurrencia del elemento en la tupla.
puntos = ((1, 2), (3, 4), (5, 6))
print(puntos.index((3, 4))) # 1

#count(elemento): Cuenta cuántas veces un elemento está en una tupla.
numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2)) # 3

#len(tupla): Retorna la cantidad de elementos de la tupla.
puntos = ((1, 2), (3, 4), (5, 6))
print(len(puntos)) # 3

#Ejemplos 

'''Las tuplas en Python son secuencias ordenadas e inmutables de elementos. 
Se utilizan para almacenar múltiples valores de diferentes tipos en una sola variable. 
Aquí tienes algunos ejemplos claros de cómo usar tuplas en Python:'''

#Crear una tupla vacía:
mi_tupla = ()

#Crear una tupla con elementos:
frutas = ("manzana", "banana", "naranja")
punto = (3, 4)
mixta = ("Hola", 42, True)

#Acceder a elementos de una tupla mediante índices:
frutas = ("manzana", "banana", "naranja")
print(frutas[0])  # Salida: "manzana"
print(frutas[2])  # Salida: "naranja"

#No se pueden modificar los elementos de una tupla (son inmutables):

punto = (3, 4)
punto[0] = 5  # Generará un error

#Obtener la longitud de una tupla:
frutas = ("manzana", "banana", "naranja")
print(len(frutas))  # Salida: 3

#Recorrer una tupla utilizando un ciclo for:
frutas = ("manzana", "banana", "naranja")
for fruta in frutas:
    print(fruta)
# Salida:
# manzana
# banana
# naranja

#Verificar si un elemento está en una tupla:
numeros = (1, 2, 3, 4, 5)
print(3 in numeros)  # Salida: True
print(6 in numeros)  # Salida: False