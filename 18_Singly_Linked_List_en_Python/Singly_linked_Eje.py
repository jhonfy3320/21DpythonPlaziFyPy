'''
Una Singly Linked List, también conocida como lista simplemente enlazada, es una estructura de datos lineal en la que cada elemento se llama 
"nodo" y contiene dos partes: el dato que queremos almacenar y un puntero (referencia) que apunta al siguiente nodo en la lista. 
El último nodo de la lista apunta a None para indicar el final de la lista.

La ventaja principal de una Singly Linked List es que permite una inserción y eliminación eficiente de elementos en cualquier posición de la lista. 
Sin embargo, a diferencia de las listas nativas de Python, las Singly Linked Lists no ofrecen acceso aleatorio a los elementos 
(por índice), ya que para acceder a un elemento específico, debemos recorrer la lista desde el inicio hasta el nodo deseado.'''

# Para implementar una Singly Linked List en Python, primero necesitamos definir la estructura del nodo y luego la propia lista.

## Ejemplo detallado de Singly Linked List en Python:

# Definición de la clase Node para representar los nodos:

class Node:
    def __init__(self, data):
        self.data = data  # Almacena el dato del nodo
        self.next = None  # Puntero al siguiente nodo, inicialmente es None

# Definición de la clase SinglyLinkedList para crear y manipular la lista:

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Inicialmente la lista está vacía, por lo que el puntero a la cabeza es None

    def append(self, data):
        # Agregar un nuevo nodo al final de la lista
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_start(self, data):
        # Insertar un nuevo nodo al inicio de la lista
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        # Eliminar el primer nodo que contenga el dato dado
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        # Buscar un dato en la lista y devolver True si se encuentra, False si no
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        # Mostrar los elementos de la lista
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
##Ejemplo de uso:

# Crear una lista simplemente enlazada
sll = SinglyLinkedList()

# Agregar elementos a la lista
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)

# Mostrar los elementos de la lista
sll.display()  # Output: [10, 20, 30, 40]

# Insertar un elemento al inicio de la lista
sll.insert_at_start(5)
sll.display()  # Output: [5, 10, 20, 30, 40]

# Eliminar un elemento de la lista
sll.delete(20)
sll.display()  # Output: [5, 10, 30, 40]

# Buscar un elemento en la lista
print(sll.search(30))  # Output: True
print(sll.search(50))  # Output: False
'''
En este ejemplo, hemos implementado una Singly Linked List con sus operaciones básicas de agregar, insertar, eliminar y buscar elementos. 
Es importante notar que las operaciones de inserción y eliminación son eficientes, ya que no requieren desplazar 
todos los elementos como en una lista nativa de Python. 
Sin embargo, para acceder a un elemento en una posición específica, deberíamos recorrer la lista desde el principio, 
lo que puede ser menos eficiente que en una lista nativa. 
Por lo tanto, la elección de la estructura de datos depende de las necesidades y el uso específico en cada caso.'''