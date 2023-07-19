'''La estructura de control “if” en Python sirve para tomar decisiones en función de si una determinada 
condición es verdadera o falsa. 
El código dentro de un bloque “if” sólo se ejecutará si la condición es verdadera, mientras que el código en un bloque “else” sólo se ejecutará si la condición es falsa.

La sintaxis básica de una estructura “if” es la siguiente:
'''

'''if condicion:
  # código a ejecutar si la condición es verdadera
else:
  # código a ejecutar si la condición es falsa'''

edad = 25
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
'''En este ejemplo, se establece una variable “edad” con un valor de 25. 
Luego, se utiliza una estructura “if” para comprobar si la edad es mayor o igual a 18. 
Si es verdadero, se imprimirá “Eres mayor de edad” en la consola, de lo contrario, se imprimirá 
“Eres menor de edad”.'''

#También es posible utilizar varias condiciones en una estructura “if” utilizando la palabra clave “elif”. 
#Por ejemplo:

calificacion = 75

if calificacion >= 90:
  print("Obtuviste una A")
elif calificacion >= 80:
  print("Obtuviste una B")
elif calificacion >= 70:
  print("Obtuviste una C")
else:
  print("Obtuviste una calificación insuficiente")

'''En este ejemplo, se establece una variable “calificacion” con un valor de 75. 
Luego, se utiliza una estructura “if-elif” para determinar en qué rango de calificación se encuentra. 
Si la calificación es mayor o igual a 90, se imprimirá “Obtuviste una A”, si es mayor o igual a 80, 
se imprimirá “Obtuviste una B”, y así sucesivamente.

Todo esto y más lo puedes aprender en el Curso de Fundamentos de Python'''

# Ejemplos reales con estructuras 

'''Los condicionales en Python permiten ejecutar diferentes bloques de código dependiendo de si se cumple o no una condición. 
Los condicionales se definen mediante la estructura if-elif-else. 
quí tienes una explicación detallada y un ejemplo de cómo se usarían los condicionales en un cajero automático de un banco:

En un cajero automático, uno de los requisitos típicos es verificar si un usuario tiene suficiente saldo para realizar una transacción de retiro. 
A continuación, te muestro un ejemplo simplificado:
'''

saldo_disponible = 1000
monto_retiro = 500

if monto_retiro <= saldo_disponible:
    print("Retiro exitoso. Retire su dinero.")
    saldo_disponible -= monto_retiro
else:
    print("Fondos insuficientes. No se puede completar el retiro.")

  
'''En este ejemplo, se tienen dos variables: saldo_disponible representa el saldo actual en la cuenta del usuario, y monto_retiro 
es el monto que el usuario desea retirar.

El condicional if verifica si el monto_retiro es menor o igual que el saldo_disponible. 
Si se cumple esta condición, se imprime "Retiro exitoso. Retire su dinero." y se actualiza el saldo_disponible restando el monto_retiro. 
En caso contrario, si el monto_retiro es mayor que el saldo_disponible, se imprime "Fondos insuficientes. No se puede completar el retiro."

Este es un ejemplo sencillo que muestra cómo se utiliza un condicional para realizar una verificación y tomar decisiones en función 
de una condición. 
En un cajero automático real, habría más lógica y verificaciones adicionales, 
pero este ejemplo proporciona una idea básica de cómo se aplicaría un condicional en ese contexto.'''