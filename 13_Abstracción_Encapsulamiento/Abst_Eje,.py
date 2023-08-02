'''
Claro, en el texto anterior se mencionan los conceptos clave de la abstracción en Python: 
clases, objetos, métodos, herencia y sobreescritura de métodos. 
'''
# Ahora, vamos a ver ejemplos prácticos para cada uno de ellos:

## Clases y Objetos:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 25)

# Acceder a las propiedades y métodos del objeto
print(persona1.nombre)  # Salida: Juan
print(persona1.edad)    # Salida: 25
persona1.saludar()      # Salida: Hola, mi nombre es Juan y tengo 25 años.

'''En este ejemplo, creamos una clase Persona con dos propiedades (nombre y edad) y un método (saludar). 
Luego, creamos un objeto persona1 de la clase Persona y accedemos a sus propiedades y métodos utilizando la notación de punto.'''

## Herencia:

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau Miau")

# Crear objetos de las clases Perro y Gato
mi_perro = Perro("Max")
mi_gato = Gato("Luna")

# Llamar al método hacer_sonido de cada objeto
mi_perro.hacer_sonido()  # Salida: Guau Guau
mi_gato.hacer_sonido()   # Salida: Miau Miau

'''
En este ejemplo, creamos una clase Animal con un método hacer_sonido, que es abstracto (sin implementación). 
Luego, creamos dos clases Perro y Gato que heredan de Animal y sobre escriben el método hacer_sonido para representar 
sonidos diferentes para cada animal.'''

## Sobreescritura de Métodos:

class Figura:
    def area(self):
        return 0

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

# Crear objetos de las clases Cuadrado y Circulo
mi_cuadrado = Cuadrado(5)
mi_circulo = Circulo(3)

# Calcular el área de cada figura
print(mi_cuadrado.area())  # Salida: 25
print(mi_circulo.area())   # Salida: 28.26

'''
En este ejemplo, creamos una clase Figura con un método area, que es abstracto (retorna 0). 
Luego, creamos dos clases Cuadrado y Circulo que heredan de Figura y sobre escriben el método 
area para calcular el área de cada figura específica.

Estos ejemplos ilustran cómo la abstracción en Python nos permite representar objetos y sus características de manera simplificada, 
ocultando los detalles internos de su implementación y facilitando la reutilización de código. 
La abstracción es una técnica poderosa para organizar y simplificar el código en la programación orientada a objetos.'''