'''
Construyamos un Stack en Python usando una lista y veamos algunos ejemplos reales de cómo utilizarlo. 
Utilizaremos la implementación incorrecta que se mostró en la respuesta anterior.'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("El stack está vacío, no se puede hacer pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("El stack está vacío, no se puede hacer peek.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
## Ahora, veamos algunos ejemplos reales de cómo utilizar este Stack:

# Crear un Stack vacío
stack = Stack()

# Agregar elementos al Stack
stack.push(10)
stack.push(20)
stack.push(30)

# Obtener el elemento del top del Stack
print(stack.peek())  # Output: 30

# Eliminar elementos del Stack
stack.pop()
print(stack.peek())  # Output: 20

# Verificar si el Stack está vacío
print(stack.is_empty())  # Output: False

# Obtener el tamaño del Stack
print(stack.size())  # Output: 2

# Vaciar el Stack
stack.pop()
stack.pop()
print(stack.is_empty())  # Output: True

# Intentar hacer pop en un Stack vacío (lanzará una excepción IndexError)
# stack.pop()
'''
En estos ejemplos, hemos creado un Stack utilizando la clase Stacky hemos utilizado los métodos push(), 
pop(), peek(), size()e is_empty()para agregar, eliminar y obtener información de los elementos del Stack. 
Es importante asegurarse de manejar adecuadamente el caso cuando el Stack está vacío, como se muestra en el código, 
para evitar errores al hacer pop o peek en un Stack vacío.'''