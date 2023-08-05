 #Una implementación básica de un Queue (cola) en Python y lo ilustraremos con un ejemplo de llegada de mensajes de correo electrónico:

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise Exception("Queue is empty")

    def size(self):
        return len(self.items)
    
## Ahora, usemos esta cola para simular la llegada de mensajes de correo electrónico:

# Crear una cola para los mensajes de correo electrónico
email_queue = Queue()

# Simular la llegada de mensajes de correo electrónico
email_queue.enqueue("Mensaje 1")
email_queue.enqueue("Mensaje 2")
email_queue.enqueue("Mensaje 3")

# Verificar el tamaño de la cola
print("Número de mensajes en la cola:", email_queue.size())  # Output: Número de mensajes en la cola: 3

# Procesar los mensajes de correo electrónico en orden de llegada
while not email_queue.is_empty():
    message = email_queue.dequeue()
    print("Procesando:", message)

# Verificar si la cola está vacía después de procesar los mensajes
print("¿La cola está vacía?", email_queue.is_empty())  # Output: ¿La cola está vacía? True
'''
En este ejemplo, creamos una cola email_queue y simulamos la llegada de tres mensajes de correo electrónico mediante el método enqueue. 
Luego, procesamos los mensajes en orden de llegada utilizando el método dequeue. 
El resultado muestra cómo se procesan los mensajes en el orden correcto, manteniendo la propiedad FIFO (First In, First Out) de una cola. 
Finalmente, verificamos si la cola está vacía después de procesar todos los mensajes.'''

'''
Esta es solo una implementación básica de un Queue en Python. 
En aplicaciones reales, el Queue podría utilizarse para manejar la llegada y procesamiento de mensajes de correo electrónico, 
tareas encoladas en un servidor, procesamiento de datos en el orden de llegada y muchas otras situaciones donde 
se requiere mantener un orden específico en el procesamiento de elementos.'''