'''El manejo de excepciones, también conocido como manejo de errores, es una técnica en programación que nos permite controlar 
y gestionar situaciones excepcionales que pueden ocurrir durante la ejecución de un programa. 
Una excepción es un evento que interrumpe el flujo normal de ejecución y puede ser causado por diferentes factores, 
como errores de sintaxis, errores en tiempo de ejecución, problemas de lógica, entre otros.

En Python, el manejo de excepciones se realiza mediante bloques try, except, elsey finally. 
La estructura general es la siguiente:'''

#try:
    # Código que puede generar una excepción
#except TipoDeExcepcion:
    # Código que se ejecuta si ocurre una excepción del tipo especificado
#except OtroTipoDeExcepcion:
    # Código que se ejecuta si ocurre otra excepción del tipo especificado
#else:
    # Código que se ejecuta si no ocurre ninguna excepción
#finally:
    # Código que se ejecuta siempre, independientemente de si ocurre o no una excepción

#El bloque trycontiene el código que se evaluará para detectar posibles excepciones.
#Los bloques exceptespecifican los tipos de excepciones que se capturarán. 
#Si ocurre alguna excepción del tipo especificado, el código dentro del bloque exceptse ejecutará.
#El bloque elsese ejecuta si no ocurre ninguna excepción en el bloque try.
#El bloque finallyse ejecuta siempre, independientemente de si ocurrió una excepción o no. 
#Se utiliza para realizar tareas de limpieza o liberar recursos que deben ejecutarse sin importar si ocurrió una excepción o no.

#Ejemplo:

try:
    x = int(input("Ingresa un número: "))
    resultado = 10 / x
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")
else:
    print("La operación se realizó correctamente.")
finally:
    print("Fin del manejo de excepciones.")

    
'''En este ejemplo, el bloque tryintenta obtener un número del usuario, luego realiza una división y muestra el resultado. 
Pueden ocurrir dos tipos de excepciones: 
ValueErrorsi el usuario ingresa algo que no es un número y ZeroDivisionErrorsi el usuario ingresa cero como divisor.

Si ocurre una excepción, el programa salta al bloque exceptcorrespondiente y muestra un mensaje de error adecuado. 
Si no ocurre ninguna excepción, el programa ejecuta el bloque else. 
Finalmente, el bloquefinally se ejecuta siempre, independientemente de si ocurrió o no una excepción, 
para indicar el final del manejo de excepciones y realizar cualquier acción de limpieza necesaria.

El manejo de excepciones es una técnica poderosa que nos permite mejorar la robustez de nuestros programas y proporcionar un comportamiento 
más controlado y amigable al usuario en situaciones excepcionales. 
Nos ayuda a evitar que el programa se detenga bruscamente y nos permita tomar acciones adecuadas en caso de errores o situaciones imprevistas.'''