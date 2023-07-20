'''
La sintaxis básica en Python tiene algunos detalles como los 
siguientes

No es necesario poner punto y coma al final de las líneas.
Los bloques de código se definen mediante la indentación en lugar de corchetes o llaves. 
Esto significa que la indentación es muy importante en Python, ya que define la 
estructura del programa.
Las llaves o corchetes {} no se utilizan para delimitar bloques de código como en otros lenguajes. 
En su lugar, se utilizan la indentación y los dos puntos (😃 para indicar el comienzo de un bloque de código.

Por ejemplo, en el siguiente código, el bloque de código dentro de la 
estructura de control if está indentado con cuatro espacios:'''


#Python utiliza una sintaxis clara y legible que utiliza indentación en lugar de llaves para definir bloques de código. 
#Aquí tienes un ejemplo de estructuras de control básicas:
# Estructura if-else
x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")

# Bucle for
for i in range(5):
    print(i)  # Salida: 0, 1, 2, 3, 4

# Bucle while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1 en cada iteración

    '''Es importante tener en cuenta que la indentación es obligatoria en Python y que debe ser 
    consistente en todo el programa. Si se mezclan diferentes niveles de indentación, 
    el programa generará un error de sintaxis.
'''