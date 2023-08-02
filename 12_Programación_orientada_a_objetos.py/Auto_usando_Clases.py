## A continuación, te mostraré cómo implementar la clase Car con los métodos solicitados:

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.state = False

    def turnOn(self):
        self.state = True
        print("El auto está encendido.")

    def turnOff(self):
        self.state = False
        print("El auto está apagado.")

    def drive(self, kilometers):
        if self.state:
            self.mileage += kilometers
            print(f"Se han recorrido {kilometers} kilómetros. Kilometraje actual: {self.mileage} km.")
        else:
            raise Exception("El auto está apagado.")

# Crear un objeto de la clase Car
car1 = Car("Toyota", "Corolla", 2022, 10000)

# Encender el auto y conducir
car1.turnOn()
car1.drive(150)
car1.drive(50)

# Apagar el auto
car1.turnOff()

# Intentar conducir con el auto apagado
try:
    car1.drive(100)
except Exception as e:
    print(e)


'''
En este ejemplo, creamos la clase Car con los atributos brand, model, year, mileage y state. 
Luego, definimos los métodos turnOn, turnOff y drive para encender, apagar y conducir el auto respectivamente.

Al crear un objeto car1 de la clase Car, podemos usar los métodos para encender el auto, conducir una cierta cantidad de kilómetros 
y apagar el auto. Si intentamos conducir el auto cuando está apagado, se lanzará una excepción indicando que el auto está apagado.

Es importante manejar los errores con excepciones para asegurarnos de que el programa se comporte de manera adecuada 
y nos proporcione información sobre posibles problemas o situaciones inesperadas.'''