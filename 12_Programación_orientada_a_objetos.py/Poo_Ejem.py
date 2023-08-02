'''
La Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en la idea de organizar el código en torno a objetos que 
representan entidades del mundo real. 
En POO, los objetos son instancias de clases, que son modelos o plantillas para crear objetos con características y comportamientos específicos.'''

## Las características principales de la Programación Orientada a Objetos son:

#Clase: Una clase es una plantilla o modelo que define la estructura y el comportamiento de los objetos. 
#Define los atributos (propiedades) y los métodos (funciones) que tendrán los objetos creados a partir de ella.

#Objeto: Un objeto es una instancia concreta de una clase. 
#Es una entidad que tiene sus propias características y puede realizar acciones definidas por los métodos de su clase.

#Encapsulación: Es el concepto de ocultar la implementación interna de una clase y exponer solo los detalles necesarios para interactuar 
#con el objeto. Se utiliza para proteger los datos y evitar que sean accedidos o modificados directamente desde fuera de la clase.

#Abstracción: Permite modelar entidades del mundo real en forma de clases y objetos, simplificando y representando solo los aspectos 
#relevantes para el problema que se está resolviendo.

#Herencia: Es el mecanismo mediante el cual una clase puede heredar atributos y métodos de otra clase, reutilizando código y estableciendo 
#relaciones de jerarquía entre las clases.

#Polimorfismo: Permite que una clase se comporte de diferentes maneras según el contexto en el que se utiliza. 
# Una clase puede tener varios métodos con el mismo nombre pero con comportamientos distintos.

## Ejemplo:

'''
Supongamos que queremos modelar una entidad "Persona" en un programa. 
Podemos crear una clase llamada "Persona" que defina los atributos como nombre, edad y género, y los métodos para interactuar con la persona.'''

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

    def cumplir_anios(self):
        self.edad += 1

# Creamos objetos de la clase Persona
persona1 = Persona("Juan", 30, "Masculino")
persona2 = Persona("María", 25, "Femenino")

# Llamamos a los métodos de los objetos
persona1.saludar()  # Salida: Hola, mi nombre es Juan.
persona2.saludar()  # Salida: Hola, mi nombre es María.

print(persona1.edad)  # Salida: 30
persona1.cumplir_anios()
print(persona1.edad)  # Salida: 31

'''
En este ejemplo, creamos una clase "Persona" con los atributos "nombre", "edad" y "género", y dos métodos "saludar" y "cumplir_anios". 
Luego creamos dos objetos de la clase "Persona" (persona1 y persona2) y llamamos a sus métodos y accedemos a sus atributos.

La Programación Orientada a Objetos nos permite organizar nuestro código de manera más estructurada y modular, facilitando el mantenimiento y reutilización del código. 
Es especialmente útil cuando trabajamos con entidades complejas y necesitamos representar diferentes comportamientos y estados para cada una de ellas.'''