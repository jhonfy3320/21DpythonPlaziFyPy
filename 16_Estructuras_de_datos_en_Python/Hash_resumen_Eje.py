'''''
Las hash tables, también conocidas como tablas hash o diccionarios en Python, son estructuras de datos eficientes que nos permiten almacenar 
y recuperar datos utilizando una función hash. 
La función hash toma una clave y produce un valor numérico único que se utiliza para calcular el índice donde se almacenará el par clave-valor 
en un arreglo de tamaño fijo. Esto permite un acceso rápido a los valores, ya que no es necesario buscar a través de todos los elementos 
como en una lista o matriz, lo que resulta en una complejidad algorítmica constante O(1) para operaciones como inserción, búsqueda y eliminación.'''''

## En Python, podemos utilizar un simple diccionario como una hash table nativa. Por ejemplo:

# Crear una hash table utilizando un diccionario
hash_table = {}

# Insertar un par clave-valor en la hash table
hash_table["clave1"] = "valor1"
hash_table["clave2"] = "valor2"
hash_table["clave3"] = "valor3"

# Obtener un valor por clave
print(hash_table["clave2"])  # Output: "valor2"

# Eliminar un par clave-valor de la hash table
del hash_table["clave1"]

# Obtener todos los valores almacenados
all_values = list(hash_table.values())
print(all_values)  # Output: ["valor2", "valor3"]

'''
También podemos crear nuestra propia implementación de una hash table. 
Por ejemplo, utilizando la clase HashTable que se muestra en el código anterior:'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return

    def retrieve_all(self):
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_values.append(value)
        return all_values
'''
Con esta implementación, podemos crear una instancia de HashTable, 
insertar pares clave-valor, obtener valores por clave, eliminar pares y obtener todos los valores almacenados, similar a la hash table nativa.'''

my_table = HashTable(10)
my_table.insert("nombre", "Juan")
my_table.insert("edad", 25)

print(my_table.get("nombre"))  # Output: "Juan"

my_table.remove("edad")

all_values = my_table.retrieve_all()
print(all_values)  # Output: ["Juan"]
'''
En resumen, las hash tables son estructuras de datos eficientes y versátiles que permiten almacenar y recuperar datos de manera rápida. 
En Python, podemos utilizar el diccionario como una hash table nativa o implementar nuestra propia versión personalizada utilizando una función 
hash para calcular los índices donde se almacenarán los elementos.'''