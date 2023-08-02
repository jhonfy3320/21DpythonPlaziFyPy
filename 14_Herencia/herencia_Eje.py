'''
La herencia es uno de los conceptos fundamentales de la programación orientada a objetos 
(POO) que permite crear nuevas clases basadas en clases existentes. 
En Python, la herencia se logra al definir una nueva clase que hereda las características y 
comportamientos de una clase existente, que se conoce como clase base o superclase.'''

'''
Para crear una clase que herede de otra en Python, se coloca el nombre de la clase base entre paréntesis después del nombre de la nueva clase. 
La sintaxis es la siguiente:'''

#class NuevaClase(ClaseBase):
    # Definición de la nueva clase

'''
La nueva clase hereda automáticamente los atributos y métodos de la clase base, lo que permite reutilizar código y definir nuevas 
funcionalidades específicas para la nueva clase. Veamos un ejemplo real para entender mejor la herencia en Python:

Supongamos que estamos desarrollando una aplicación de gestión de empleados, y queremos crear dos tipos de empleados: 
empleados permanentes y empleados temporales. 
Ambos tipos de empleados comparten algunas características comunes, como el nombre y la edad, pero también tienen características 
específicas propias, como el salario y la duración del contrato.
'''

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase para empleados permanentes
class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Salario: ${self.salario}")

# Clase para empleados temporales
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, edad, duracion_contrato):
        super().__init__(nombre, edad)
        self.duracion_contrato = duracion_contrato

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Duración del contrato: {self.duracion_contrato} meses")

# Creamos objetos de las clases
empleado_permanente = EmpleadoPermanente("Juan", 35, 5000)
empleado_temporal = EmpleadoTemporal("María", 28, 6)

# Mostramos la información de cada empleado
empleado_permanente.mostrar_informacion()
empleado_temporal.mostrar_informacion()

'''
En este ejemplo, hemos definido la clase Empleado como la clase base que contiene las características comunes de todos los empleados, como el nombre y la edad. 
Luego, hemos creado dos clases, EmpleadoPermanente y EmpleadoTemporal, que heredan de la clase Empleado. 
Estas clases extienden la funcionalidad de la clase base al agregar características específicas, 
como el salario y la duración del contrato.'''

'''
Cuando creamos objetos de las clases EmpleadoPermanente y EmpleadoTemporal, podemos acceder tanto a los métodos y atributos heredados 
de la clase Empleado, como a los métodos y atributos específicos de cada clase. 
De esta manera, podemos reutilizar código y definir comportamientos específicos para cada tipo de empleado.

La herencia en Python nos permite crear una jerarquía de clases que refleja la relación entre los objetos en el mundo real y nos ayuda a 
escribir un código más claro, organizado y fácil de mantener. 
Es una poderosa herramienta de la programación orientada a objetos que nos permite crear estructuras complejas y extensibles 
en nuestros programas.'''