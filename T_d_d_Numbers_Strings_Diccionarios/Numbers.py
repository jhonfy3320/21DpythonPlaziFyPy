'''En Python, también existen distintos tipos de datos que podemos utilizar para almacenar 
información. Aquí te dejamos una lista de todos los que estarás usando en tu camino 
desarrollando con este lenguaje:

## Numbers
Los números son un tipo de dato que representa valores numéricos. 
En Python, podemos utilizar distintos tipos de datos para representar números, 
incluyendo enteros y números con decimales.

Podemos crear números utilizando la notación numérica, que incluye dígitos y puede incluir un 
punto decimal para representar números con decimales.'''

edad = 30
pi = 3.14
salario = 1500.50
#También podemos utilizar la notación científica para representar números muy grandes o muy pequeños.
numero_grande = 1e6 # 1 millón
numero_pequeno = 1e-6 # 0.000001

'''
Es importante mencionar que existe la opción de tipar las variables que representan números. 
Esto significa que podemos especificar qué tipo de dato esperamos que tenga una variable, 
lo que puede ser útil en situaciones donde queremos asegurarnos de que estamos trabajando 
con el tipo de dato correcto.

Por ejemplo, si queremos que una variable solo pueda contener números enteros, podemos tiparla 
utilizando el tipo de dato int. De esta forma, Python nos mostrará un error si intentamos asignar 
un número con decimales a esa variable.'''

edad: int = 30

'''
De igual forma, podemos tipar una variable para que solo pueda contener números con decimales utilizando el tipo de dato float'''
pi: float = 3.14
salario: float = 1500.50

'''En Python, hay varios tipos de números que puedes utilizar, como enteros 
(int), números de punto flotante 
(float) y números complejos 
(complex). Aquí tienes algunos ejemplos:'''

# Números enteros
x = 10
y = -5

# Números de punto flotante
pi = 3.14159
precio = 19.99

# Números complejos
z = 3 + 4j
