'''
Para resolver este desafío, primero definiremos la clase base Animal con las propiedades name, 
age, y specie, y el método getInfo que devuelve un diccionario con la información del animal.

Luego, crearemos la clase Mammal que hereda de Animal y tiene una propiedad adicional hasFur. 
Sobreescribiremos el método getInfo para incluir la información de hasFur.

Finalmente, crearemos la clase Dog que hereda de Mammal y tiene una propiedad adicional breed. S
obreescribiremos el método getInfo para incluir la información de breed, y definiremos el método bark que devuelva el string "woof!".

'''
## 

class Animal:
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie

    def getInfo(self):
        return {
            "name": self.name,
            "age": self.age,
            "specie": self.specie,
        }

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "mammal")
        self.hasFur = True

    def getInfo(self):
        info = super().getInfo()
        info["hasFur"] = self.hasFur
        return info

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Solo llamamos al constructor de la clase Mammal con dos argumentos
        self.breed = breed

    def getInfo(self):
        info = super().getInfo()
        info["specie"] = "dog"  # Sobreescribimos el valor de la propiedad 'specie' en la clase Dog
        info["breed"] = self.breed
        return info

    def bark(self):
        return "woof!"

# Ejemplo de uso
bird = Animal("pepe", 1, "bird")
print(bird.getInfo())

dog = Dog("Max", 3, "Labrador")
print(dog.getInfo())
print(dog.bark())

'''
En este ejemplo, creamos una instancia de Animal llamada bird y llamamos al método getInfo() para obtener la información del animal. 
uego, creamos una instancia de Dog llamada dog, 
llamamos al método getInfo() para obtener la información del perro y al método bark() para escuchar su ladrido.'''