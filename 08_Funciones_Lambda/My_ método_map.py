'''Para implementar la función my_map, podemos utilizar un bucle forpara iterar sobre cada elemento 
de la lista y aplicar la función a cada elemento. 
Luego, agregamos el resultado de la función a una nueva lista que será el resultado final.

Aqui tienes la implementacion de la funcion my_map:'''

def my_map(list, func):
    result = []
    for element in list:
        result.append(func(element))
    return result

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
result = my_map(numeros, cuadrado)
# Output: [1, 4, 9, 16, 25]
print(result)

### En esta implementación:

#Creamos una lista vacía llamada resultque almacenará los resultados de aplicar la función a cada elemento.
#utilizamosforpara iterar sobre cada elemento de la lista list.
#En cada iteración, llamamos a la función funcpasándole el elemento actual como argumento, y agregamos el resultado de la función a la lista resultusando el método append().
#Finalmente, retornamos la lista resultque contiene los resultados de aplicar la función a cada elemento de la lista original.
#Ejemplo de uso:

'''En este ejemplo, definimos la función cuadrado(x)que toma un número y retorna su cuadrado. 
Luego, utilizamos nuestra función my_mappara aplicar la función cuadrado()a cada elemento de la lista numeros, obteniendo [1, 4, 9, 16, 25].'''