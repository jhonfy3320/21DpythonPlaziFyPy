'''Para implementar la función calculate_averageque maneje los casos especiales mencionados, podemos usar el manejo de excepciones 
con bloques tryy except.''' 

#Aqui tienes la implementacion:

def calculate_average(numbers):
    if not numbers:
        raise ValueError("La lista está vacía")

    total = 0
    count = 0

    for num in numbers:
        try:
            total += num
            count += 1
        except TypeError:
            raise TypeError("La lista contiene elementos no numéricos")

    return total / count

# Ejemplo de uso
try:
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print(f"El promedio es: {average}")
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
'''En esta implementación:

Comprobamos si la lista numbersestá vacía usando if not numbers. 
Si está vacía, lanzamos una excepción ValueErrorcon el mensaje "La lista está vacía" utilizando raise.

Inicializamos las variables totaly counta 0. Estas variables se utilizan para calcular el promedio de los números en la lista.

Utilizamos un bucle forpara iterar sobre cada elemento numen la lista numbers. Intentamos sumar el número a totaly aumentar el contador count. 
Si ocurre un error TypeError, significa que el elemento no es un número, 
por lo que lanzamos una excepción TypeErrorcon el mensaje "La lista contiene elementos no numéricos".

Finalmente, retornamos el promedio dividiendo totalentre count.

En el ejemplo de uso, la función calculate_averagese invoca con una lista de números válidos numbers = [10, 20, 30, 40, 50]. 
La función calcula el promedio correctamente y lo muestra en pantalla ( El promedio es: 30.0).

Si intentamos invocar la función con una lista vacía numbers = [], se generará una excepción ValueErrorcon el mensaje "La lista está vacía".

Si intentamos invocar la función con una lista que contiene elementos no numéricos numbers = [10, 20, '30', 40, 50], 
se generará una excepción TypeErrorcon el mensaje "La lista contiene elementos no numéricos".'''