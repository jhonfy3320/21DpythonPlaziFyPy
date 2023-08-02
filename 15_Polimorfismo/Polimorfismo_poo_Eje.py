'''
El polimorfismo es uno de los principios fundamentales de la programación orientada a objetos y se refiere a la capacidad 
de distintos objetos de responder de manera diferente a una misma llamada a un método o función. 
En Python, el polimorfismo se logra a través de la herencia y el uso de interfaces o clases abstractas.'''

#Vamos a ver un ejemplo de polimorfismo utilizando el concepto de "planetas" en un simulador espacial. 

'''
Supongamos que tenemos diferentes tipos de planetas, como planetas terrestres, planetas gaseosos y planetas enanos. 
Todos estos planetas tienen diferentes características y comportamientos, 
pero queremos poder tratarlos de manera genérica como "planetas".'''

'''
Primero, definiremos una clase base llamada "Planeta" que contendrá algunas propiedades comunes a todos los planetas, como el nombre y la masa, 
y un método para obtener información sobre el planeta:'''

class Planeta:
    def __init__(self, nombre, masa):
        self.nombre = nombre
        self.masa = masa

    def obtener_informacion(self):
        return f"Planeta: {self.nombre}, Masa: {self.masa} kg"
'''
Luego, definiremos las clases para los diferentes tipos de planetas que heredarán de la clase base "Planeta" y sobrescribirán 
el método obtener_informacion() para proporcionar información específica de cada tipo de planeta:'''

class PlanetaTerrestre(Planeta):
    def __init__(self, nombre, masa, tipo_superficie):
        super().__init__(nombre, masa)
        self.tipo_superficie = tipo_superficie

    def obtener_informacion(self):
        return f"Planeta Terrestre: {self.nombre}, Masa: {self.masa} kg, Tipo de Superficie: {self.tipo_superficie}"

class PlanetaGaseoso(Planeta):
    def __init__(self, nombre, masa, composicion):
        super().__init__(nombre, masa)
        self.composicion = composicion

    def obtener_informacion(self):
        return f"Planeta Gaseoso: {self.nombre}, Masa: {self.masa} kg, Composición: {self.composicion}"

class PlanetaEnano(Planeta):
    def __init__(self, nombre, masa, temperatura_superficie):
        super().__init__(nombre, masa)
        self.temperatura_superficie = temperatura_superficie

    def obtener_informacion(self):
        return f"Planeta Enano: {self.nombre}, Masa: {self.masa} kg, Temperatura Superficie: {self.temperatura_superficie} °C"
'''
Ahora podemos crear instancias de cada tipo de planeta y tratarlos de manera genérica como "planetas", 
ya que todos ellos comparten el método obtener_informacion():
'''
planeta_tierra = PlanetaTerrestre("Tierra", 5.97e24, "Rocoso")
planeta_jupiter = PlanetaGaseoso("Júpiter", 1.9e27, "Hidrógeno y Helio")
planeta_pluton = PlanetaEnano("Plutón", 1.3e22, -229)

lista_planetas = [planeta_tierra, planeta_jupiter, planeta_pluton]

for planeta in lista_planetas:
    print(planeta.obtener_informacion())
'''
Este es un ejemplo de polimorfismo en Python, donde cada tipo de planeta responde de manera diferente a la llamada del método 
obtener_informacion() aunque todos ellos compartan la misma interfaz definida en la clase base "Planeta". 
Gracias al polimorfismo, podemos tratar los diferentes tipos de planetas de manera genérica como "planetas" 
y trabajar con ellos de manera más sencilla y flexible en nuestro simulador espacial.'''