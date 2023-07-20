'''Por otro lado, el ciclo while se utiliza para repetir un bloque de código mientras se cumpla una determinada condición. 
Su sintaxis básica es la siguiente:

while #condición:
  # código a ejecutar
La condición se evalúa antes de ejecutar el código dentro del ciclo y si la condición es verdadera, el código se ejecutará de nuevo. 
Por ejemplo, si quisiéramos hacer una implementación del ejemplo anterior con los números del 1 al 10, quedaría de la siguiente manera:
'''
i = 1
while i <= 10:
  print(i)
  i += 1
'''En Python no existe una estructura de ciclo do-while como en otros lenguajes de programación, pero se puede lograr un comportamiento 
similar utilizando un ciclo while junto con una condición inicial que siempre se cumpla.

Por ejemplo, para imprimir los números del 1 al 10 utilizando un ciclo while con un comportamiento similar a un do-while, 
se puede hacer lo siguiente en Python:
'''
i = 1
while True:
    print(i)
    i += 1
    if i > 100:
        break
'''En este caso, la condición inicial es True, por lo que el ciclo se ejecutará al menos una vez. En cada iteración, 
se imprime el valor de la variable i y se incrementa en 1. Después de cada incremento, se evalúa la condición de que i sea mayor que 10. 
Si esto es cierto, se utiliza la instrucción break para salir del ciclo.

Este código imprimirá los números del 1 al 10 en la consola de Python.'''


#Ejemplos Wile

'''El ciclo while en Python se utiliza para repetir un bloque de código mientras se cumpla una condición. 
A diferencia del ciclo for, que se utiliza cuando se conoce de antemano la cantidad de iteraciones, el ciclo while se ejecuta mientras 
una condición sea verdadera. Aquí tienes una descripción detallada y ejemplos de cómo se utiliza el ciclo while:

La sintaxis general del ciclo while es la siguiente:'''

#while condicion:
    # Bloque de código a ejecutar
#El bloque de código se ejecutará siempre que la condición sea evaluada como verdadera. Después de cada ejecución del bloque, la condición se volverá a evaluar. Si la condición sigue siendo verdadera, el ciclo continuará ejecutándose; de lo contrario, el ciclo terminará y el programa continuará con la siguiente instrucción después del bloque while.

#Aquí tienes un ejemplo simple que muestra cómo utilizar un ciclo while para contar hasta un número determinado:

contador = 0

while contador < 100:
    print(contador)
    contador += 1
'''En este ejemplo, el ciclo while se ejecutará mientras el valor de contador sea menor que 100. 
En cada iteración, se imprime el valor actual de contador y luego se incrementa en 1. La salida será:'''


0
1
2
3
4
'''Ten en cuenta que es importante asegurarse de que la condición de salida se vuelva falsa en algún momento para evitar bucles infinitos. 
Es posible que necesites actualizar la condición dentro del bloque de código para asegurarte de que en algún momento se cumpla.'''

#Aquí tienes otro ejemplo que utiliza un ciclo while para sumar números ingresados por el usuario hasta que se ingrese un número negativo:

total = 0

while True:
    numero = int(input("Ingrese un número (ingrese un número negativo para salir): "))
    
    if numero < 0:
        break
    
    total += numero

print("La suma total es:", total)

'''En este ejemplo, el ciclo while se ejecuta indefinidamente (while True) hasta que se ingrese un número negativo. 
En cada iteración, se solicita al usuario que ingrese un número. 
Si se ingresa un número negativo, se utiliza la instrucción break para salir del ciclo. 
De lo contrario, el número se suma al total. Al final, se muestra la suma total de los números ingresados.

Recuerda que es importante asegurarte de que la condición en el ciclo while eventualmente se vuelva falsa para evitar bucles infinitos.'''