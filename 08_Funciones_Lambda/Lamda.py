'''Las funciones lambda en Python son funciones anónimas que se pueden definir de manera 
concisa en una sola línea. A diferencia de las funciones regulares, 
las funciones lambda no requieren un nombre y se utilizan principalmente para realizar operaciones simples y rápidas.'''

## La sintaxis básica de una lambda es la siguiente:

'''lambda argumentos: expresion
argumentos son los parámetros de la función.
expresion es la operación que se realizará y se devolverá como resultado.
Las lambdas se utilizan comúnmente en combinación con otras funciones, como map(), filter() y reduce(), 
para realizar operaciones sobre secuencias de manera más concisa.
'''
#3 Aquí hay algunos ejemplos para ilustrar el uso de las lambdas:

# Ejemplo 1: Función lambda simple
suma = lambda a, b: a + b
resultado = suma(2, 3)
print(resultado)  # Output: 5

# Ejemplo 2: Uso de lambda con map()
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Output: [2, 4, 6, 8, 10]

# Ejemplo 3: Uso de lambda con filter()
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]

'''En el primer ejemplo, se define una función lambda llamada suma que toma dos argumentos a y b y devuelve su suma. 
Luego, se llama a la función lambda pasando los argumentos 2 y 3, y se almacena el resultado en la variable resultado.

En el segundo ejemplo, se utiliza una lambda junto con la función map() para duplicar cada elemento de la lista numeros. 
La función lambda multiplica cada elemento por 2, y map() aplica esta operación a cada elemento de la lista.

En el tercer ejemplo, se utiliza una lambda junto con la función filter() para filtrar los números pares de la lista numeros. 
La función lambda verifica si un número es divisible por 2 y devuelve True si lo es.

Las funciones lambda son útiles cuando se necesita definir rápidamente una función pequeña y sencilla sin tener que escribir una función 
completa. Se utilizan comúnmente en combinación con otras funciones para operar sobre secuencias de manera más eficiente y concisa.

Todo esto y más lo puedes aprender en el Curso de Python: Comprehensions, Funciones y Manejo de Errores'''


## Ejemplos 

'''Las funciones lambda, también conocidas como funciones anónimas, son funciones de una sola línea que pueden 
tener cualquier número de argumentos, pero solo pueden tener una expresión. 
Son muy útiles cuando necesita una función rápida y simple sin tener que definir una función completa con def.'''

## La sintaxis general de una función lambda en Python es la siguiente:

'''lambda argumentos: expresion
Dónde:'''

'''lambdaes la palabra clave que indica que estamos creando una función lambda.
argumentosson los parámetros de la función, separados por comas (pueden ser cero o más).
expresiones el cuerpo de la función que se ejecutará y devolverá el resultado.'''

# Aquí tienes algunos ejemplos para ilustrar el uso de funciones lambda en situaciones cotidianas:

## Ejemplo 1: Suma de dos números usando una función lambda

suma = lambda x, y: x + y
print(suma(2, 3))
# Salida: 5
#En este ejemplo, definimos una función lambda llamada sumaque toma dos argumentos xe yy devuelve la suma de ambos.

## Ejemplo 2: Elevar un número al cuadrado utilizando una función lambda

cuadrado = lambda x: x ** 2
print(cuadrado(4))
# Salida: 16
#En este ejemplo, definimos una función lambda llamada cuadradoque toma un argumento xy devuelve xelevado al cuadrado.

## Ejemplo 3: Filtrar una lista utilizando una función lambda

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
# Salida: [2, 4, 6, 8, 10]
#En este ejemplo, utilizamos la función filterjunto con una función lambda para filtrar los números pares de la lista numeros.

#Ejemplo 4: Ordenar una lista de tuplas utilizando una función lambda

personas = [
    ("Juan", 30),
    ("María", 25),
    ("Pedro", 35),
    ("Laura", 28)
]
personas_ordenadas = sorted(personas, key=lambda x: x[1])
print(personas_ordenadas)
# Salida: [('María', 25), ('Laura', 28), ('Juan', 30), ('Pedro', 35)]
'''En este ejemplo, utilizamos la función sortedpara ordenar la lista de tuplas personaspor la edad de cada persona, utilizando una 
función lambda para indicar que queremos ordenar por el segundo elemento de cada tupla ( x[1], que es la edad).

Las funciones lambda son útiles cuando necesitas crear funciones pequeñas y rápidas en línea sin tener que definir una función completa con def. 
Sin embargo, ten en cuenta que su uso excesivo puede dificultar la legibilidad del código, por lo que es importante utilizarlas con moderación 
y en situaciones adecuadas.'''