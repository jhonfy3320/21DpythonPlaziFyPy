'''
Para implementar la clase "Usuario" con encapsulamiento en Python, utilizaremos propiedades (getters y setters) 
para acceder y modificar los atributos privados name y age. 
También crearemos los métodos públicos addFriend, sendMessage y showMessages para realizar las operaciones mencionadas.

Aquí está la implementación de la clase "Usuario":'''

class Usuario:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__friends = []
        self.__messages = []

# Getters y Setters para el nombre y edad
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # Método para agregar un amigo
    def addFriend(self, friend):
        self.__friends.append(friend)

    # Método para enviar un mensaje
    def sendMessage(self, message, friend):
        self.__messages.append(message)
        friend.receiveMessage(message)

    # Método para mostrar los mensajes
    def showMessages(self):
        return self.__messages

    # Método para recibir un mensaje
    def receiveMessage(self, message):
        self.__messages.append(message)

'''
En esta implementación, hemos definido atributos privados __name, __age, __friends y __messages. 
Utilizamos métodos getters y setters para acceder a los datos privados __name y __age, lo que nos permite proteger 
los datos y controlar su acceso desde fuera de la clase.

Los métodos addFriend, sendMessage, showMessages y receiveMessage nos permiten agregar amigos, enviar y recibir mensajes, 
y mostrar los mensajes del usuario actual. 
Nota que el método sendMessage también llama al método receiveMessage del amigo especificado para agregar el mensaje a su lista de mensajes.

Ahora podemos crear instancias de la clase "Usuario" y utilizar sus métodos y propiedades para interactuar con la red social:'''

user1 = Usuario("Alice", 25)
user2 = Usuario("Bob", 30)

user1.addFriend(user2)
user2.addFriend(user1)

user1.sendMessage("Hola Bob, ¿cómo estás?", user2)
user2.sendMessage("¡Hola Alice! Estoy bien, ¿y tú?", user1)

print(user1.showMessages())
print(user2.showMessages())

'''
Hemos creado dos usuarios (user1 y user2), los hemos agregado como amigos y hemos enviado mensajes entre ellos. 
La salida mostrará la lista de mensajes de cada usuario. 
Esto es un ejemplo de encapsulamiento en la clase "Usuario" para proteger sus datos privados.'''