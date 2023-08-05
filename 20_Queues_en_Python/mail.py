'''
Para implementar la cola de correos electrónicos (Queue), podemos usar la clase Mail proporcionada y diseñar los métodos de la 
clase Queue para manejar el encolamiento y desencolamiento de correos electrónicos en función de la antigüedad. 
A continuación, se muestra la implementación:'''

class Mail:
    def __init__(self, from_email, to, body, subject):
        self.from_email = from_email
        self.to = to
        self.body = body
        self.subject = subject
        self.next = None