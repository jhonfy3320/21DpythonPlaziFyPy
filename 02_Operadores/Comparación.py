#Los operadores de comparación nos permiten comparar valores y nos devuelven True o False según el resultado de la comparación.

print(1 < 2) # True
print(2 > 1) # True
print(1 <= 2) # True
print(2 >= 1) # True
print(1 != 2) # True
'''Entre estos existen 2 operadores de igualdad los cuales son == y is. 
El primero realiza una comparación de valor y el segundo, además de comparar el valor, también verifica si ambos objetos son el 
mismo objeto en memoria.
'''
print(1 == "1") # True
print(1 is "1") # False
'''En el primer caso, 1 == "1" devuelve True ya que solo se está comparando el valor y no el tipo de dato. 
Sin embargo, en el segundo caso, 1 is "1" devuelve False ya que está comparando tanto el valor como el 
tipo de dato y, aunque ambos son iguales, uno es de tipo número y el otro de tipo string.'''


#Ejemplos: reaales 

'''Los operadores de comparación se utilizan en Python para comparar dos valores y obtener un resultado booleano (True o False) que indica si la 
comparación es verdadera o falsa. Aquí tienes una descripción de los operadores de comparación más comunes junto con ejemplos reales:
'''
#Igualdad (==): Este operador compara si dos valores son iguales y devuelve True si lo son, o False en caso contrario.

x = 5
y = 3
resultado = x == y
print(resultado)  # Salida: False

#Desigualdad (!=): Este operador compara si dos valores son diferentes y devuelve True si lo son, o False en caso contrario.

x = 5
y = 3
resultado = x != y
print(resultado)  # Salida: True
#Mayor que (>): Este operador compara si el valor de la izquierda es mayor que el valor de la derecha, 
# y devuelve True si es cierto, o False en caso contrario.

y = 3
resultado = x > y
print(resultado)  # Salida: True
#Menor que (<): Este operador compara si el valor de la izquierda es menor que el valor de la derecha, y devuelve True si es cierto, o False en caso contrario.

x = 5
y = 3
resultado = x < y

print(resultado)  # Salida: False
#Mayor o igual que (>=): Este operador compara si el valor de la izquierda es mayor o igual que el valor de la derecha, y
#devuelve True si es cierto, o False en caso contrario.

x = 5
y = 3
resultado = x >= y

print(resultado)  # Salida: True
'''Menor o igual que (<=): Este operador compara si el valor de la izquierda es menor o igual que el valor de la derecha, y 
devuelve True si es cierto, o False en caso contrario.e'''
x = 5
y = 3
resultado = x <= y
print(resultado)  # Salida: False
'''Estos son solo algunos ejemplos de los operadores de comparación en Python. 
Puedes utilizarlos para realizar comparaciones en expresiones condicionales, bucles y otros lugares donde necesites evaluar si una condición es verdadera o falsa.'''