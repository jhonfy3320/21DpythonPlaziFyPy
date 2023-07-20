'''Operadores lógicos en Python
También tenemos disponibles los operadores lógicos para realizar operaciones de comparación y evaluación.

AND (and): Este operador lógico evalúa si ambas expresiones son verdaderas. Si ambas expresiones son verdaderas, devuelve True, de lo contrario, devuelve False. Por ejemplo:'''
edad = 25
mayor_de_edad = edad >= 18

if edad >= 18 and mayor_de_edad:
    print("Eres mayor de edad")
else:
    print("Aún eres menor de edad")

#OR (or): Este operador lógico evalúa si al menos una de las expresiones es verdadera. Si al menos una de las expresiones es verdadera, devuelve True, de lo contrario, devuelve False. Por ejemplo:
edad = 25
tiene_identificacion = True

if edad >= 18 or tiene_identificacion:
    print("Puedes entrar al bar")
else:
    print("No tienes la edad o la identificación suficiente para entrar al bar")

#**NOT (not)**: Este operador lógico invierte el valor de la expresión. Si la expresión es verdadera, devuelve False, de lo contrario, devuelve True. Por ejemplo:
es_fin_de_semana = True

if not es_fin_de_semana:
    print("A trabajar")
else:
    print("A disfrutar del fin de semana")



#Ejemplos

'''Los operadores lógicos en Python se utilizan para combinar o negar expresiones 
lógicas y obtener un resultado booleano. 
Aquí tienes una descripción de los operadores lógicos más comunes junto con ejemplos:
'''
#Operador lógico "and": Devuelve True si ambas expresiones son verdaderas, y False en caso contrario.
x = 5
y = 3
z = 7
resultado = x > y and x < z
print(resultado)  # Salida: True

#Operador lógico "or": Devuelve True si al menos una de las expresiones es verdadera, y False si ambas son falsas.
x = 5
y = 3
z = 7
resultado = x > y or x > z
print(resultado)  # Salida: True

#Operador lógico "not": Niega el valor de una expresión. 
#Devuelve True si la expresión es falsa, y False si la expresión es verdadera.
x = 5
y = 3
resultado = not x > y
print(resultado)  # Salida: False
#Estos operadores lógicos se utilizan comúnmente en expresiones condicionales y bucles para evaluar múltiples condiciones y tomar decisiones basadas en el resultado booleano. Puedes combinarlos y utilizar paréntesis para crear expresiones lógicas más complejas según tus necesidades. 