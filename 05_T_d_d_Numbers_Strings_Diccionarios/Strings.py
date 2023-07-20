
'''Las cadenas de texto (strings) son un tipo de dato que representa una secuencia de caracteres. 
En Python, podemos crear strings utilizando comillas simples o comillas dobles.'''

nombre = "Platzi"
apellido = 'Academy'
# Al igual que los números, los strings pueden ser tipados para evitar errores a futuro.

mensaje: str = "Hola, ¿cómo estás?"
# Podemos concatenar dos strings utilizando el operador +:

print("Hola, " + nombre + " " + apellido + "!") 
# "Hola, Platzi Academy!"
# También podemos utilizar la notación f-strings para crear strings que incluyen variables y expresiones:

print(f"Hola, {nombre} {apellido}!") 
# "Hola, Platzi Academy!"
# Python proporciona una serie de métodos para manipular strings. Algunos de los métodos más comunes son:

'''len(): Devuelve la longitud de un string.
upper(): Devuelve el string en mayúsculas.
lower(): Devuelve el string en minúsculas.
split(): Devuelve una lista de strings separados por un carácter.
nombre = "Platzi"'''

print(len(nombre)) # 6
print(nombre.upper()) # PLATZI
print(nombre.lower()) # platzi
print(nombre.split('a')) # ['Pl', 'tzi']

'''Strings (Cadenas de caracteres):
Los Strings son secuencias de caracteres y se utilizan para representar texto en Python. 
Puedes definir cadenas utilizando comillas simples 
('') o comillas dobles (""). Aquí tienes algunos ejemplos:'''

mensaje = "Hola, ¿cómo estás?"
nombre = 'María'

# Concatenación de cadenas
saludo = "¡Hola, " + nombre + "! ¿Qué tal?"

# Acceso a caracteres individuales
primer_caracter = mensaje[0]  # Obtener el primer carácter de la cadena

# Longitud de una cadena
longitud = len(mensaje)  # Devuelve la cantidad de caracteres en la cadena
