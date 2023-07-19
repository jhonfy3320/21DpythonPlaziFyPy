'''Los sets en son estructuras de datos que permiten almacenar valores únicos. 
Los sets en Python no permiten duplicados, lo que los hace ideales cuando se necesita mantener una colección de elementos únicos.

Crear un set en Python es sencillo, puedes hacerlo de la siguiente manera:'''

my_set = set()

#También es posible crear un set a partir de una lista existente:
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)

#Algunos de los métodos más utilizados en los sets de Python son:

'''add(value): este método agrega un valor único al set. Si se intenta agregar un valor que ya existe en el set, no ocurrirá ningún cambio.
remove(value): este método elimina un valor específico del set. Si el valor no existe, se generará un error.
discard(value): este método elimina un valor específico del set. Si el valor no existe, no se genera ningún error.
pop(): este método elimina y devuelve un elemento aleatorio del set.
clear(): este método vacía completamente el set.
len(): esta función devuelve la cantidad de elementos que existen en el set.'''

#Ejemplos de uso 👇

my_set = set()

# Agregar elementos al set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Imprimir el set
print(my_set)  # Output: {1, 2, 3}

# Verificar si un elemento existe en el set
print(2 in my_set)  # Output: True

# Eliminar un elemento del set
my_set.remove(2)

# Verificar si un elemento existe en el set después de ser eliminado
print(2 in my_set)  # Output: False

# Vaciar el set
my_set.clear()

# Verificar el tamaño del set después de ser vaciado
print(len(my_set))  # Output: 0

# Iterar sobre sets


#También es posible crear un set a partir de una lista existente:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_set = set(my_list)

#Algunos de los métodos más utilizados en los sets de Python son:

'''add(value): este método agrega un valor único al set. Si se intenta agregar un valor que ya existe en el set, no ocurrirá ningún cambio.
remove(value): este método elimina un valor específico del set. Si el valor no existe, se generará un error.
discard(value): este método elimina un valor específico del set. Si el valor no existe, no se genera ningún error.
pop(): este método elimina y devuelve un elemento aleatorio del set.
clear(): este método vacía completamente el set.
len(): esta función devuelve la cantidad de elementos que existen en el set.'''

#Ejemplos de uso 👇

my_set = set

# Agregar elemontos al set 
my_set.add(10, 11)
my_set.add(12, 13)
my_set.add(14, 15)

# Imprimir el set
print(my_set)  # Output: {1, 2, 3}

# Verificar si un elemento existe en el set
print(2 in my_set)  # Output: True

# Eliminar un elemento del set
my_set.remove(2)

# Verificar si un elemento existe en el set después de ser eliminado
print(2 in my_set)  # Output: False

# Vaciar el set
my_set.clear()

# Verificar el tamaño del set después de ser vaciado
print(len(my_set))  # Output: 0

my_set = set()

#También es posible crear un set a partir de una lista existente:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_set = set(my_list)

#Algunos de los métodos más utilizados en los sets de Python son:

'''add(value): este método agrega un valor único al set. Si se intenta agregar un valor que ya existe en el set, no ocurrirá ningún cambio.
remove(value): este método elimina un valor específico del set. Si el valor no existe, se generará un error.
discard(value): este método elimina un valor específico del set. Si el valor no existe, no se genera ningún error.
pop(): este método elimina y devuelve un elemento aleatorio del set.
clear(): este método vacía completamente el set.
len(): esta función devuelve la cantidad de elementos que existen en el set.'''

#Ejemplos de uso 👇

my_set = set

# Agregar elemontos al set 
my_set.add(10, 11)
my_set.add(12, 13)
my_set.add(14, 15)

# Imprimir el set
print(my_set)  # Output: {1, 2, 3}

# Verificar si un elemento existe en el set
print(2 in my_set)  # Output: True

# Eliminar un elemento del set
my_set.remove(2)

# Verificar si un elemento existe en el set después de ser eliminado
print(2 in my_set)  # Output: False

# Vaciar el set
my_set.clear()

# Verificar el tamaño del set después de ser vaciado
print(len(my_set))  # Output: 0

#Otros ejemplos 

'''Los sets (conjuntos) en Python son colecciones desordenadas y mutables de elementos únicos. 
A diferencia de las listas o tuplas, los sets no permiten elementos duplicados y no mantienen un orden específico. '''

#Aquí tienes algunos ejemplos claros de cómo usar sets en Python:

#Crear un set vacío:

mi_set = set()

#Crear un set con elementos:
frutas = {"manzana", "banana", "naranja"}
numeros = {1, 2, 3, 4, 5}

#Agregar elementos a un set:
frutas = {"manzana", "banana", "naranja"}
frutas.add("kiwi")

#Remover un elemento de un set:
frutas = {"manzana", "banana", "naranja"}
frutas.remove("banana")

#Verificar si un elemento está en un set:
frutas = {"manzana", "banana", "naranja"}
print("manzana" in frutas)  # Salida: True
print("kiwi" in frutas)  # Salida: False

#Obtener la longitud de un set:
frutas = {"manzana", "banana", "naranja"}
print(len(frutas))  # Salida: 3

#Recorrer un set utilizando un ciclo for:
frutas = {"manzana", "banana", "naranja"}
for fruta in frutas:
    print(fruta)
# Salida:
# manzana
# banana
# naranja