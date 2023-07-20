'''Las dictionary comprehensions, son una característica poderosa de Python que nos permite crear 
diccionarios de forma concisa y eficiente utilizando una sintaxis compacta. 
Son una forma elegante de transformar o filtrar elementos de una secuencia para crear un nuevo diccionario.
'''
## La sintaxis básica de una dictionary comprehension es la siguiente:

'''nuevo_diccionario = {clave_expresion: valor_expresion for elemento in secuencia if condicion}
clave_expresion es una expresión que define cómo se generarán las claves del nuevo diccionario.
valor_expresion es una expresión que define cómo se generarán los valores del nuevo diccionario.
elemento es una variable que representa cada elemento de la secuencia mientras se recorre.
secuencia es la secuencia de origen de la cual se obtendrán los elementos.
condicion es una condición opcional que filtra los elementos de la secuencia.
Aquí hay un ejemplo para uso de las dictionary comprehensions:'''

personas = [("Juan", 25), ("María", 30), ("Pedro", 20)]

# Crear un nuevo diccionario con el nombre como clave y la edad como valor, solo para personas mayores de 25 años
personas_mayores = {nombre: edad for nombre, edad in personas if edad > 25}
print(personas_mayores)  # Output: {'María': 30}

# Crear un nuevo diccionario con el nombre como clave y la longitud del nombre como valor para todas las personas

diccionario_longitudes = {nombre: len(nombre) for nombre, _ in personas}
print(diccionario_longitudes)  # Output: {'Juan': 4, 'María': 5, 'Pedro': 5}
'''
En el primer ejemplo, se crea un nuevo diccionario llamado personas_mayores que contiene solo a 
las personas mayores de 25 años del diccionario original. 
Las claves del nuevo diccionario son los nombres y los valores son las edades correspondientes. 
Esto se logra mediante la expresión nombre: 
edad en la dictionary comprehension, y se aplica la condición edad > 25.

En el segundo ejemplo, se crea un nuevo diccionario llamado diccionario_longitudes que contiene la 
longitud de cada nombre del diccionario original. 
Las claves del nuevo diccionario son los nombres y los valores son las longitudes de los nombres 
correspondientes. Esto se logra mediante la expresión nombre: len(nombre) en la dictionary comprehension.'''


'''Dictionary comprehension es una característica en Python que nos permite crear diccionarios 
de una manera concisa y legible en una sola línea de código. 
Es una forma compacta de definir un diccionario utilizando una expresión y un bucle for, 
lo que hace que el código sea más eficiente y fácil de entender.'''

#La sintaxis general de dictionary comprehension es la siguiente:

### nuevo_diccionario = {clave: valor for elemento in secuencia if condicion}

#Donde:

'''clave es la clave que se asigna a cada elemento en la secuencia y se agrega al nuevo diccionario.
valor es el valor que se asigna a cada clave en el nuevo diccionario.
elemento es cada elemento de la secuencia original.
secuencia es la colección de elementos sobre la cual se realiza el bucle.
condicion (opcional) es una expresión que determina si se agrega o no el elemento al nuevo diccionario.
Aquí tienes algunos ejemplos detallados de dictionary comprehension:
'''
'''Ejemplo 1: Crear un diccionario con el cuadrado de los primeros 5 números naturales como clave y el 
número original como valor:'''

cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(cuadrados_dict)
# Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''En este ejemplo, utilizamos dictionary comprehension para iterar sobre los números en el rango de 1 a 5 
(range(1, 6)) y creamos un diccionario donde cada número es una clave y su cuadrado es el valor 
correspondiente.'''

#Ejemplo 2: Crear un diccionario que contenga las letras de una palabra como clave y el índice de 
#cada letra como valor:

palabra = "python"
indices_dict = {letra: indice for indice, letra in enumerate(palabra)}
print(indices_dict)
# Salida: {'p': 0, 'y': 1, 't': 2, 'h': 3, 'o': 4, 'n': 5}
'''En este ejemplo, utilizamos dictionary comprehension para iterar sobre cada letra de la palabra 
"python" utilizando enumerate(), que nos proporciona tanto el índice como la letra de cada caracter en 
la palabra.'''

#Ejemplo 3: Filtrar un diccionario y crear un nuevo diccionario solo con las claves que cumplen con cierta condición:

numeros = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro"}
numeros_pares_dict = {clave: valor for clave, valor in numeros.items() if clave % 2 == 0}
print(numeros_pares_dict)
# Salida: {2: 'dos', 4: 'cuatro'}
'''En este ejemplo, utilizamos dictionary comprehension para iterar sobre los elementos del diccionario 
numeros utilizando items(), y filtramos solo las claves que son números pares (clave % 2 == 0) 
y creamos un nuevo diccionario con esas claves y sus respectivos valores.

Dictionary comprehension es una herramienta poderosa en Python que te permite crear y filtrar 
diccionarios de forma concisa y legible. 
Es útil cuando quieres crear diccionarios a partir de una secuencia o aplicar cierta lógica 
de filtrado sobre un diccionario existente.'''