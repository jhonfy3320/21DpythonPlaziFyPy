'''
La encapsulación es uno de los principios fundamentales de la programación orientada a objetos que nos permite proteger los datos 
y comportamientos internos de un objeto, evitando que sean accesibles y modificables desde fuera de la clase. 
En Python, la encapsulación se logra mediante el uso de convenciones de nomenclatura y el uso de métodos getters y setters.

Para ejemplificar la encapsulación con carros, consideremos una clase Car que represente un automóvil y tenga atributos como la marca, 
el modelo, el año y la velocidad. 
Aplicaremos la encapsulación para proteger los atributos y controlar su acceso.'''

class Car:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = 0

    # Getter para obtener la marca del carro
    def get_brand(self):
        return self._brand

    # Setter para modificar la marca del carro
    def set_brand(self, brand):
        self._brand = brand

    # Getter para obtener el modelo del carro
    def get_model(self):
        return self._model

    # Setter para modificar el modelo del carro
    def set_model(self, model):
        self._model = model

    # Getter para obtener el año del carro
    def get_year(self):
        return self._year

    # Setter para modificar el año del carro
    def set_year(self, year):
        self._year = year

    # Método para acelerar el carro
    def accelerate(self, speed):
        self._speed += speed

    # Método para frenar el carro
    def brake(self, speed):
        self._speed -= speed

    # Getter para obtener la velocidad del carro
    def get_speed(self):
        return self._speed


'''
En este ejemplo, hemos utilizado convenciones de nomenclatura para indicar que los atributos 
_brand, _model, _year y _speed son privados y no deberían ser accedidos directamente desde fuera de la clase.

Hemos creado métodos getters y setters para acceder y modificar los atributos privados. 
Los getters nos permiten obtener el valor de los atributos de forma controlada y los setters nos permiten modificar los valores de los 
atributos aplicando alguna lógica adicional si es necesario.'''

## Veamos cómo podemos utilizar la clase Car con la encapsulación:

car = Car("Toyota", "Corolla", 2022)

print(car.get_brand())  # Output: Toyota
print(car.get_model())  # Output: Corolla
print(car.get_year())   # Output: 2022

car.accelerate(50)
print(car.get_speed())  # Output: 50

car.brake(20)
print(car.get_speed())  # Output: 30

# Modificamos la marca utilizando el setter
car.set_brand("Honda")
print(car.get_brand())  # Output: Honda

'''
En este ejemplo, hemos utilizado los métodos getters y setters para acceder y modificar los atributos del carro de forma controlada, 
protegiendo así los detalles internos de la clase Car. Esto es un ejemplo de encapsulación en Python.'''