'''El manejo de errores en Python es una parte fundamental de la programación para garantizar que nuestros programas sean 
robustos y puedan manejar situaciones inesperadas. 
Python proporciona diversas herramientas y técnicas para manejar y controlar errores.

En Python, los errores se conocen como excepciones y se producen cuando ocurre una situación inesperada durante la ejecución de un programa. 
Algunos ejemplos comunes de excepciones son TypeError, NameError, ValueError, entre otros.

A continuación, se presenta una descripción detallada sobre el manejo de errores en Python:

Bloques try-except: El bloque try-except se utiliza para capturar y manejar excepciones. 
El código sospechoso de causar una excepción se coloca dentro del bloque try, y si se produce alguna excepción, se ejecuta el bloque except 
correspondiente.'''

#A continuación, se presenta una descripción detallada sobre el manejo de errores en Python:

'''Bloques try-except: El bloque try-except se utiliza para capturar y manejar excepciones. 
El código sospechoso de causar una excepción se coloca dentro del bloque try, y si se produce alguna excepción, 
se ejecuta el bloque except correspondiente.'''

'''try:
    # Código sospechoso
except ExceptionType:
    # Manejar la excepción
El bloque except puede manejar excepciones específicas o genéricas. Por ejemplo:

try:
    # Código sospechoso
except ValueError:
    # Manejar la excepción ValueError
except:
    # Manejar cualquier otra excepción
Bloque finally: El bloque finally se utiliza para ejecutar código que debe ejecutarse sin importar si se produjo una excepción o no. Este bloque se coloca después del bloque try-except.
try:
    # Código sospechoso
except ExceptionType:
    # Manejar la excepción
finally:
    # Código que se ejecuta siempre
Cláusula raise: La cláusula raise se utiliza para generar manualmente una excepción en Python. Esto nos permite lanzar una excepción específica cuando ocurre una condición no deseada.
if condition:
    raise ExceptionType("Mensaje de error")
Por ejemplo, para generar una excepción TypeError, se puede utilizar la siguiente línea de código:

raise TypeError("Se esperaba un tipo de dato diferente")
Bloques try-except-else: También se puede utilizar un bloque else junto con try-except para especificar un código que se ejecutará si no se produce ninguna excepción.
try:
    # Código sospechoso
except ExceptionType:
    # Manejar la excepción
else:
    # Código que se ejecuta si no hay excepciones
Manejo de excepciones específicas: Además de capturar excepciones genéricas, también es posible manejar excepciones específicas y personalizadas. Esto permite un manejo más granular y adaptado a situaciones particulares.
try:
    # Código sospechoso
except ValueError as ve:
    # Manejar excepción ValueError
except TypeError as te:
    # Manejar excepción TypeError'''

'''Estas son algunas de las técnicas más comunes para manejar excepciones en Python. 
Sin embargo, hay muchas más opciones y posibilidades para adaptarse a diferentes escenarios.

El manejo de errores adecuado es crucial para garantizar la robustez y confiabilidad de nuestros programas. 
Al anticipar y manejar las excepciones de manera adecuada, podemos evitar fallas inesperadas y proporcionar mensajes de error 
claros y útiles para los usuarios y desarrolladores.'''


# Ejemplos reales 

'''El manejo de errores, también conocido como manejo de excepciones, es una técnica en programación que nos permite anticiparnos 
y tratar situaciones inesperadas o errores que pueden ocurrir durante la ejecución del programa. 
Al manejar los errores de manera adecuada, podemos evitar que el programa se detenga bruscamente y proporcionar un 
comportamiento más controlado y amigable para el usuario.'''

#En Python, el manejo de errores se realiza utilizando bloques try, except, elsey finally. 
#El bloque tryes donde se coloca el código que se quiere evaluar en busca de errores. 
#El bloque exceptes donde se manejan los errores específicos que pueden ocurrir. 
#El bloque elsese ejecuta si no ocurre ningún error en el bloque try. 
#El bloque finallyse ejecuta siempre, independientemente de si ocurrió un error o no.

#Aquí tienes un ejemplo real y una explicación detallada de cómo manejar errores en Python:

def dividir_numeros(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    except TypeError:
        print("Error: Asegúrate de ingresar números válidos.")
    else:
        print(f"El resultado de la división es: {resultado}")
    finally:
        print("Fin del manejo de errores.")

# Ejemplo de uso
dividir_numeros(10, 2)
dividir_numeros(10, 0)
dividir_numeros(10, "2")
#En este ejemplo, tenemos una función dividir_numeros(a, b)que toma dos argumentos y realiza una división entre ellos. 
#Sin embargo, pueden ocurrir algunos errores en este proceso:

'''ZeroDivisionError: Si el segundo argumento bes igual a cero, ocurrirá una división entre cero, lo cual es inválido y generará un error 
ZeroDivisionError.
TypeError: Si alguno de los argumentos ao bno es un número, ocurrirá un error TypeErroral intentar realizar la operación de división.
Para manejar estos errores, utilizamos bloques tryy except. En el bloque try, realizamos la división y almacenamos el resultado 
en la variable resultado. 
Si ocurre algún error, el programa salta al bloque exceptcorrespondiente y muestra un mensaje de error adecuado. 
Si no ocurre ningún error, el programa continúa el bloque else, donde se muestra el resultado de la división. 
Finalmente, el bloque finallyse ejecuta siempre, independientemente de si ocurrió un error o no, para indicar el final del manejo de errores.'''

#En el ejemplo de uso, la función se invoca tres veces:

#dividir_numeros(10, 2):   #No ocurre ningún error y muestra el resultado de la división ( El resultado de la división es: 5.0)
#dividir_numeros(10, 0):   #Ocurre un error ZeroDivisionErrory muestra el mensaje de error correspondiente ( Error: No es posible dividir entre cero.).
#dividir_numeros(10, "2"): #Ocurre un error TypeErrory muestra el mensaje de error correspondiente ( Error: Asegúrate de ingresar números válidos.).

#El manejo de errores es una técnica poderosa que nos permite anticiparnos a posibles problemas en nuestro código y tomar acciones 
# adecuadas en caso de que se escondan errores. 
# Nos ayuda a mejorar la robustez y confiabilidad de nuestros programas, evitando fallas inesperadas y necesitando una mejor experiencia 
# de usuario.