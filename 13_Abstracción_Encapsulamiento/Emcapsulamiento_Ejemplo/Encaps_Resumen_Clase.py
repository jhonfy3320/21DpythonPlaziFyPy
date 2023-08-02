
'''
La encapsulación es uno de los cuatro principios fundamentales de la programación orientada a objetos (POO), junto con la abstracción, herencia y polimorfismo. 
Consiste en ocultar los detalles internos de un objeto y permitir el acceso controlado a sus atributos y métodos. 
En Python, la encapsulación se logra utilizando convenciones de nomenclatura y, en el caso de las propiedades, 
mediante el uso de decoradores como @property.'''

## Convenciones de nomenclatura: 
'''En Python, se utilizan convenciones de nomenclatura para indicar el nivel de accesibilidad de los atributos y métodos de una clase. 
La convención más común es utilizar un guion bajo (_) al comienzo de un nombre de atributo o método para indicar que es un atributo 
o métodos, se considera una buena práctica no hacerlo.
'''
## Ejemplo de atributo privado:

class MiClase:
    def __init__(self):
        self._atributo_privado = 10

## Decorador @property: 
# El decorador @propertyse utiliza para crear un método getter para acceder a un atributo privado como si fuera una propiedad pública. 
# El método getter se denomina como la propiedad que se desea acceder y se define utilizando el decorador @property.

## Ejemplo:

class MiClase:
    def __init__(self):
        self._atributo_privado = 10

    @property
    def atributo_publico(self):
        return self._atributo_privado

'''
En este ejemplo, el atributo _atributo_privadoes un atributo privado, pero se puede acceder a él desde fuera de la clase utilizando el método 
getter atributo_publico.

Setter utilizando el decorador @atributo_publico.setter: 
También se puede utilizar el decorador @atributo_publico.setterpara crear un método setter que permita modificar un atributo privado a través 
de una sintaxis similar a la estimación de una propiedad. 
El método setter se denomina como la propiedad que se desea modificar y se define utilizando el decorador @atributo_publico.setter.'''

## Ejemplo:

class MiClase:
    def __init__(self):
        self._atributo_privado = 10

    @property
    def atributo_publico(self):
        return self._atributo_privado

    @atributo_publico.setter
    def atributo_publico(self, nuevo_valor):
        self._atributo_privado = nuevo_valor
'''
En este ejemplo, el método setteratributo_publico permite modificar el atributo _atributo_privadoutilizando una sintaxis similar 
a la solicitada de una propiedad.'''

'''
Métodos y atributos privados: 
Además de utilizar la convención de nomenclatura con el guion bajo (_), se puede hacer uso de métodos y atributos privados 
en Python utilizando dos guiones bajos ( ) . 
Aunque técnicamente no hay restricciones de acceso, se considera una convención que los métodos y atributos que comienzan con dos guiones bajos 
( ) sean tratados como privados y no sean accedidos directamente desde fuera de la clase.'''

## Ejemplo:

class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def __metodo_privado(self):
        pass
'''
En este ejemplo, el atributo __atributo_privado y el método __metodo_privado son privados, pero Python los renombra internamente 
utilizando el nombre de la clase que los contiene para evitar conflictos con clases derivadas. 
Por ejemplo, el atributo __atributo_privado se renombraría a _MiClase__atributo_privado internamente.'''

'''
En resumen, la encapsulación en Python permite proteger los detalles internos de una clase y controlar el acceso a sus atributos y métodos. 
Utilizando convenciones de nomenclatura y decoradores como @property, 
podemos definir atributos y métodos privados y proporcionar una interfaz controlada para interactuar con los objetos de una clase.'''