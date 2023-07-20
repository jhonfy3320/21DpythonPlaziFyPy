'''Los sets en Python no son estructuras indexadas, por lo que no se puede acceder a sus 
elementos mediante índices como se hace en las listas o tuplas. Sin embargo, 
es posible iterar sobre los elementos de un set utilizando un ciclo for-in.

Al iterar sobre un set, el ciclo for recorre automáticamente cada elemento del set 
en el orden en que fueron agregados.'''

#Aquí un ejemplo de como hacerlo 👇

my_set = {1, 2, 3, 4, 5}

# Iterar sobre los elementos del set
for element in my_set:
    print(element)

'''En este ejemplo, se declara un set llamado my_set con algunos elementos. 
Luego, se utiliza el ciclo for-in para iterar sobre los elementos del set y se imprime cada elemento en la consola.
'''

#Usando slice syntax

'''También se puede utilizar la slice syntax([1:]) para iterar sobre un set a partir de un índice específico. 
Esta técnica permite omitir los primeros elementos del set durante la iteración.

Aquí un ejemplo de cómo utilizar esta sintaxis para iterar en un set a partir del segundo elemento:
'''
my_set = {1, 2, 3, 4, 5}

# Iterar sobre los elementos del set a partir del segundo elemento
for item in my_set[1:]:
    print(item)

'''El set my_set contiene los elementos del 1 al 5. Al utilizar la sintaxis [1:], 
se indica que se desea iterar sobre los elementos a partir del segundo elemento (índice 1). 
Esto significa que se omitirá el primer elemento del set durante la iteración.
'''
#El resultado de este código será:

2
3
4
5

'''Cabe destacar que, a diferencia de las listas, los sets en Python no están indexados y no tienen un orden específico. 
Por lo tanto, al utilizar la slice syntax [1:] en un set, no se garantiza que se omitirán 
los primeros elementos en el mismo orden en que fueron agregados al set.'''


#contar la cantidad de marcas de carros diferentes:

def contar_marcas_carros(carros):
    marcas_diferentes = set()
    
    for carro in carros:
        marcas_diferentes.add(carro)
    
    cantidad_marcas = len(marcas_diferentes)
    
    return cantidad_marcas


carros = {"Toyota", "Honda", "Ford", "Toyota", "Chevrolet", "Honda", "Nissan"}

cantidad_marcas = contar_marcas_carros(carros)
print(cantidad_marcas)
# Salida: 5
'''En este ejemplo, tenemos un set llamado carros que contiene diferentes marcas de carros. 
Queremos contar la cantidad de marcas de carros diferentes.

La función contar_marcas_carros toma el set carros como parámetro. 
Creamos un set vacío llamado marcas_diferentes, que utilizaremos para almacenar las marcas de carros diferentes encontradas.

Luego, iteramos sobre cada elemento en el set carros utilizando un bucle for. 
Para cada elemento, lo agregamos al set marcas_diferentes utilizando el método add(). 
Como los sets no permiten elementos duplicados, solo se agregarán las marcas de carros que aún no han sido agregadas.

Después de recorrer todos los elementos, obtenemos la cantidad de marcas de carros diferentes contando la longitud 
del set marcas_diferentes utilizando la función len().

Finalmente, retornamos la cantidad de marcas de carros diferentes.

En este caso, el set carros contiene 7 elementos, pero solo hay 5 marcas de carros diferentes: 
Toyota, Honda, Ford, Chevrolet y Nissan. Por lo tanto, la función retorna 5 como resultado.'''