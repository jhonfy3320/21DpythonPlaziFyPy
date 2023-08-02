'''
Para implementar una hash table en el dataset "penguins" puedes utilizar un diccionario en Python para almacenar la información de cada 
pinguino utilizando una clave única, como podría ser su nombre, por ejemplo. 
Cada clave estará asociada a un diccionario que contendrá los atributos del pinguino, como su especie, longitud del pico, longitud de la aleta, 
etc.

A continuación, te mostraré un ejemplo de cómo podrías implementar una hash table utilizando el dataset "penguins" y cómo agregar algunos 
pinguinos al diccionario:'''

# Ejemplo de implementación de una hash table con el dataset penguins
# Utilizaremos el nombre de cada pinguino como clave y un diccionario con sus atributos como valor.

# Dataset penguins (algunos registros de ejemplo)
penguins_data = [
    {"species": "Adelie", "bill_length_mm": 39.1, "bill_depth_mm": 18.7, "flipper_length_mm": 181.0},
    {"species": "Gentoo", "bill_length_mm": 39.5, "bill_depth_mm": 17.4, "flipper_length_mm": 186.0},
    {"species": "Chinstrap", "bill_length_mm": 40.9, "bill_depth_mm": 17.9, "flipper_length_mm": 186.0},
]

# Crear la hash table para almacenar los pinguinos
pinguinos_dict = {}

# Agregar los pinguinos al diccionario utilizando su nombre como clave
for pinguino in penguins_data:
    nombre = pinguino["species"]
    pinguinos_dict[nombre] = pinguino

# Obtener información de un pinguino específico por su nombre
nombre_pinguino = "Adelie"
if nombre_pinguino in pinguinos_dict:
    pinguino_info = pinguinos_dict[nombre_pinguino]
    print(f"Información del pinguino {nombre_pinguino}:")
    print(pinguino_info)
else:
    print(f"No se encontró información del pinguino {nombre_pinguino}.")

# Agregar un nuevo pinguino al diccionario
nuevo_pinguino = {
    "species": "Emperor",
    "bill_length_mm": 45.0,
    "bill_depth_mm": 20.0,
    "flipper_length_mm": 210.0,
}
pinguinos_dict[nuevo_pinguino["species"]] = nuevo_pinguino

# Obtener la lista de nombres de todos los pinguinos en el diccionario
nombres_pinguinos = list(pinguinos_dict.keys())
print("Nombres de los pinguinos en el diccionario:", nombres_pinguinos)

# Obtener la cantidad total de pinguinos en el diccionario
cantidad_pinguinos = len(pinguinos_dict)
print("Cantidad total de pinguinos en el diccionario:", cantidad_pinguinos)
'''
En este ejemplo, hemos creado una hash table utilizando un diccionario llamado pinguinos_dict. 
Cada pinguino del dataset se almacena como un valor en el diccionario, utilizando su especie como clave única. 
Luego, podemos obtener la información de un pinguino específico por su nombre utilizando la clave en el diccionario.

Recuerda que este es solo un ejemplo básico de implementación de una hash table en el dataset "penguins". 
En aplicaciones más complejas, es posible que necesites ajustar la estructura de datos y la forma en que accedes a los elementos 
según tus necesidades específicas.'''




