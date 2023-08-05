'''
Los Maps en Python son estructuras de datos que permiten almacenar pares clave-valor y acceder a ellos de manera eficiente. 
Las claves en un mapa pueden ser de cualquier tipo de dato inmutable, como enteros, cadenas, tuplas y objetos personalizados.'''

# Los métodos más utilizados en los Mapas son los siguientes:

'''
map[key] = value: Agrega un par clave-valor al Map.

value = map.get(key): Devuelve el valor asociado a una clave determinada. Si la clave no existe, devuelve None.

key in map: Verifica si una clave determinada existe en el Mapa. Devuelve True si la clave existe y False en caso contrario.

del map[key]: Elimina una clave y su valor asociado del Mapa.

map.clear(): Vacía completamente el Mapa.

len(map): Devuelve la cantidad de pares clave-valor que existen en el Map.'''

## Ejemplos de uso de Mapas en Python:

# Crear un Map vacío
mapa = {}

# Agregar pares clave-valor al Map
mapa["nombre"] = "Juan"
mapa["edad"] = 30
mapa[1] = "primer elemento"

# Obtener el valor asociado a una clave
print(mapa.get("nombre"))  # Output: "Juan"

# Verificar si una clave existe en el Map
print("edad" in mapa)  # Output: True

# Eliminar una clave del Map
del mapa["edad"]

# Verificar si una clave existe en el Map después de ser eliminada
print("edad" in mapa)  # Output: False

# Vaciar el Map
mapa.clear()

# Verificar el tamaño del Map después de ser vaciado
print(len(mapa))  # Output: 0
'''
En este ejemplo, hemos creado un Map llamado map y hemos utilizado algunos de los métodos mencionados anteriormente. 
Hemos agregado pares clave-valor, recuperado valores por clave, verificado si una clave existe, eliminado una clave 
y su valor, y verificado el tamaño del Map después de vaciarlo.

Los Maps son muy útiles cuando necesitamos realizar búsquedas rápidas de valores asociados a una clave determinada y ofrecen una forma 
eficiente de organizar y acceder a los datos en nuestras aplicaciones.'''