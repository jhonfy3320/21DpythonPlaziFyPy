'''Las High Order Functions son funciones que cumplen al menos uno de los siguientes criterios:

Toman una o más funciones como argumentos.
Devuelven una función como resultado.
Estas funciones son fundamentales para la programación funcional y nos permiten trabajar con funciones 
de manera modular y flexible.'''

## En Python, algunas de las High Order Functions incorporadas más comunes son:

# map(función, secuencia): Aplica la función a cada elemento de la secuencia y devuelve un iterador con los resultados.
# filter(función, secuencia): Filtra los elementos de la secuencia según la función dada y devuelve un iterador con los elementos que cumplan la condición.
# reduce(función, secuencia): Aplica la función a los elementos de la secuencia de manera acumulativa, reduciéndolos a un solo valor.
# sorted(secuencia, key=función): Ordena la secuencia según la función de clave dada y devuelve una nueva lista con los elementos ordenados.
#Estas funciones de orden superior nos permiten escribir código más limpio y expresivo al evitar la necesidad de bucles explícitos y operaciones repetitivas.

'''Además, podemos crear nuestras propias High Order Functions en Python. 
Esto se logra utilizando la capacidad de Python para tratar las funciones como objetos de primera clase. 
Podemos pasar funciones como argumentos a otras funciones, devolver funciones desde funciones y almacenar funciones en variables.'''

## Aquí hay un ejemplo acerca del uso de las High Order Functions en Python:

def aplicar_operacion(func, a, b):
	return func(a, b)

def suma(a, b):
	return a + b

def resta(a, b):
	return a - b

resultado = aplicar_operacion(suma, 5, 3)
print(resultado)  # Output: 8

resultado = aplicar_operacion(resta, 10, 7)
print(resultado)  # Output: 3
'''En este ejemplo, tenemos una función aplicar_operacion que toma una función func y dos argumentos a y b. 
La función aplicar_operacion llama a func pasándole a y b como argumentos y devuelve el resultado.

Luego, definimos las funciones suma y resta que realizan operaciones de suma y resta, respectivamente.

Finalmente, llamamos a aplicar_operacion pasando las funciones suma y resta junto con los argumentos necesarios. 
Dependiendo de la función que se pase, se realiza la operación correspondiente y se obtiene el resultado.'''


# Ejemplos

'''Las funciones de orden superior son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultado. 
En Python, estas funciones posibles son gracias a que las funciones son tratadas como ciudadanos de primera clase, 
lo que significa que pueden ser tratadas como cualquier otro tipo de dato, como int, str, list, etc.'''

#Aquí tienes algunos ejemplos reales y explica detalladamente cómo funcionan las funciones de orden superior:

'''map(): La función map()toma una función y una secuencia (como una lista) como argumentos y aplica la función a cada elemento de la secuencia, 
devolviendo un iterable con los resultados.'''

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)

# Output: <map object at 0x7f99e0585c10>
print(cuadrados)

# Convertir el iterable a una lista
cuadrados_list = list(cuadrados)
# Output: [1, 4, 9, 16, 25]
print(cuadrados_list)
'''En este ejemplo, definimos la función cuadrado(x)que toma un número y retorna su cuadrado. 
Luego, usamos map()para aplicar la función cuadrado()a cada elemento de la lista numeros. 
El resultado es un iterable que podemos convertir a una lista para obtener [1, 4, 9, 16, 25].'''

## filter(): La función filter()toma una función y una secuencia como argumentos y devuelve un iterable con los elementos de la secuencia para los cuales la función retorna True.

def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5]
pares = filter(es_par, numeros)

# Output: <filter object at 0x7f99e0585f10>
print(pares)

# Convertir el iterable a una lista
pares_list = list(pares)
# Output: [2, 4]
print(pares_list)
'''En este ejemplo, definimos la función es_par(x)que retorna Truesi el número es par y Falsesi es impar. 
Usamos filter()para filtrar los números pares de la lista numeros, obteniendo [2, 4]'''

#reduce(): La función reduce()toma una función y una secuencia como argumentos y reduce la secuencia a un solo valor aplicando la función 
# acumulativamente a los elementos.


from functools import reduce

def suma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]
suma_total = reduce(suma, numeros)

# Output: 15
print(suma_total)
'''En este ejemplo, definimos la función suma(x, y)que devuelve la suma de dos números. 
Usamos reduce()para acumular la suma de todos los elementos de la lista numeros, obteniendo 15.'''

'''Las funciones de orden superior son herramientas poderosas en Python que nos permiten escribir código más limpio, modular y legible. 
Nos ayudan a evitar repeticiones de código y mejorar la eficiencia al trabajar con colecciones de datos y operaciones comunes. '''