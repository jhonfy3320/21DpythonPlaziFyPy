#Intersecciones

'''Las intersecciones son una operación comúnmente utilizada en los sets para encontrar elementos que 
están presentes en dos o más sets al mismo tiempo. 
Puedes realizar la operación de intersección utilizando el método intersection() o el operador &.'''

#Aquí tienes un ejemplo de cómo encontrar la intersección entre dos sets:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Usando el método intersection()
intersection = set1.intersection(set2)
print(intersection)  # Output: {4, 5}

# Usando el operador &
intersection = set1 & set2
print(intersection)  # Output: {4, 5}

'''En este ejemplo, tenemos dos sets: set1 y set2. 
Queremos encontrar los elementos que están presentes en ambos sets. 
Utilizando el método intersection() o el operador &, obtenemos un nuevo set
llamado intersection que contiene la intersección de los dos sets originales.

El resultado de la impresión será {4, 5}, ya que esos son los elementos que se encuentran en ambos sets.

Es importante tener en cuenta que la operación de intersección devuelve un nuevo set que contiene 
los elementos comunes entre los sets originales. Si alguno de los sets no tiene elementos en común con los otros sets, 
la intersección resultante será un set vacío.

Además, puedes realizar la intersección entre más de dos sets al mismo tiempo. 
Solo necesitas agregar los sets adicionales dentro de la función intersection() o utilizar el operador & entre ellos.

Todo esto y más lo puedes aprender en el Curso de Python: Comprehensions, Funciones y Manejo de Errores'''

#Ejemplos 

'''Las intersecciones entre conjuntos (sets) en Python se refieren a los elementos que son comunes entre dos o más conjuntos. 
Es decir, la intersección de dos conjuntos es un nuevo conjunto que contiene únicamente los elementos que están presentes en ambos conjuntos.

Python proporciona el método intersection() y el operador & para realizar intersecciones entre conjuntos. 
Aquí tienes un ejemplo claro y detallado de cómo realizar una intersección entre dos conjuntos de marcas de carros:'''

marcas_carros_1 = {"Toyota", "Honda", "Ford", "Chevrolet"}
marcas_carros_2 = {"Honda", "Nissan", "Ford"}

interseccion = marcas_carros_1.intersection(marcas_carros_2)
print(interseccion)
# Salida: {'Honda', 'Ford'}
'''En este ejemplo, tenemos dos conjuntos de marcas de carros: 
marcas_carros_1 y marcas_carros_2. Queremos encontrar las marcas de carros que están presentes en ambos conjuntos.

Usamos el método intersection() en el conjunto marcas_carros_1 y pasamos el conjunto marcas_carros_2 como argumento. 
Esto nos devuelve un nuevo conjunto que contiene las marcas de carros que están presentes tanto en marcas_carros_1 como en marcas_carros_2.

Finalmente, imprimimos el resultado de la intersección, que en este caso es {'Honda', 'Ford'}.

También podemos realizar la intersección utilizando el operador & de la siguiente manera:'''

interseccion = marcas_carros_1 & marcas_carros_2
print(interseccion)
# Salida: {'Honda', 'Ford'}
'''El operador & entre dos conjuntos realiza la misma operación de intersección y devuelve un nuevo conjunto con los elementos comunes.

En ambos casos, obtenemos como resultado un conjunto que contiene las marcas de carros que se encuentran en ambos conjuntos.'''