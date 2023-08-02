'''
El polimorfismo es un concepto fundamental en la programación orientada a objetos que permite a los objetos de diferentes 
clases ser tratados de manera uniforme a través de una interfaz común. 
En Python, el polimorfismo se logra mediante el uso de métodos y operadores que se comportan de manera diferente según el tipo 
de objeto que los esté utilizando.'''

'''
Un ejemplo real de polimorfismo en Python se puede observar en el uso de operadores como la suma ( +) y la multiplicación ( *). 
Estos operadores pueden utilizarse con diferentes tipos de datos, como números, cadenas y listas, 
y su comportamiento varía según el tipo de objeto con el que se están utilizando.
'''
# Veamos algunos ejemplos detallados:

## Sumas de numeros:

# Suma de dos números enteros
a = 5
b = 10
resultado = a + b
print(resultado)  # Output: 15

# Suma de dos números flotantes
x = 3.5
y = 2.2
resultado = x + y
print(resultado)  # Output: 5.7
'''
En este ejemplo, el operador de suma + se utiliza con dos números enteros y dos números flotantes. 
Python realiza la suma correctamente en ambos casos, sin importar el tipo de dato.
'''
## Concatenación de cadenas:

# Concatenación de dos cadenas
nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Output: "Juan Perez"
'''
En este ejemplo, el operador de suma + se utiliza para concatenar dos cadenas y crear una cadena más larga. 
Python entiende que, al utilizar el operador + con cadenas, la operación debe ser una concatenación en lugar de una suma matemática.'''

## Unión de listas:

# Unión de dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_union = lista1 + lista2
print(lista_union)  # Output: [1, 2, 3, 4, 5, 6]
#En este ejemplo, el operador de suma + se utiliza para unir dos listas y crear una nueva lista que contiene todos los elementos de ambas listas.

'''
En todos estos ejemplos, el operador +se comporta de manera diferente dependiendo del tipo de objeto con el que se esté utilizando.
Esto es un ejemplo de polimorfismo en Python, ya que el mismo operador se adapta automáticamente para trabajar con diferentes tipos de datos 
y producir resultados adecuados en cada caso.'''