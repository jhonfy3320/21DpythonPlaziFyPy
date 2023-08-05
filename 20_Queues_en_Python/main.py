from mail import Mail

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, from_email, to, body, subject):
        new_mail = Mail(from_email, to, body, subject)

        if self.is_empty():
            self.front = self.rear = new_mail
        else:
            self.rear.next = new_mail
            self.rear = new_mail

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        mail_to_dequeue = self.front
        self.front = self.front.next
        self.size -= 1

        return {
            'from': mail_to_dequeue.from_email,
            'to': mail_to_dequeue.to,
            'body': mail_to_dequeue.body,
            'subject': mail_to_dequeue.subject
        }

    def peek(self):
        if self.is_empty():
            return None

        return {
            'from': self.front.from_email,
            'to': self.front.to,
            'body': self.front.body,
            'subject': self.front.subject
        }

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

# Ejemplo de uso
emailQueue = Queue()

emailQueue.enqueue(
    'jane@ejemplo.com',
    'support@ejemplo.com',
    'No puedo iniciar sesión en mi cuenta',
    'Problema de inicio de sesión'
)

emailQueue.enqueue(
    'joe@ejemplo.com',
    'support@ejemplo.com',
    'Mi pedido no ha llegado todavía',
    'Estado del pedido'
)

email = emailQueue.dequeue()
print(email)

'''
En este ejemplo, hemos implementado una cola utilizando la clase Mail para representar cada correo electrónico. 
Los métodos de la clase Queue son enqueue, dequeue, peek, is_empty y size. 
Al encolar correos electrónicos, se agregan al final de la cola, y al desencolar, se obtiene y 
elimina el correo electrónico más antiguo de la cola.

Es importante mencionar que esta implementación utiliza una estructura de datos de cola (FIFO), lo que significa que los correos 
electrónicos se procesarán en el orden en que se agregaron a la cola. 
Esto asegura que los correos electrónicos más antiguos tengan prioridad en su procesamiento.'''