'''
En Python, una queue (cola) es una estructura de datos que sigue el principio FIFO (First In, First Out), 
lo que significa que el primer elemento que se inserta en la cola será el primero en ser retirado. 
Es similar a una fila de personas esperando para ser atendidas, donde la primera persona en llegar será la primera en ser atendida.

Para trabajar con colas en Python, podemos utilizar la clase deque del módulo collections, que proporciona una implementación eficiente de colas dobles (double-ended queues). 
La clase deque nos permite agregar y eliminar elementos tanto al frente como al final de la cola de forma eficiente.'''

## A continuación, veremos cómo utilizar colas en Python:

from collections import deque

# Crear una cola vacía
queue = deque()

# Agregar elementos a la cola (enqueue)
queue.append(10)
queue.append(20)
queue.append(30)

# Obtener el primer elemento de la cola (sin eliminarlo) (peek)
first_element = queue[0]
print(first_element)  # Output: 10

# Eliminar el primer elemento de la cola (dequeue)
removed_element = queue.popleft()
print(removed_element)  # Output: 10

# Verificar si la cola está vacía
if not queue:
    print("La cola está vacía")
else:
    print("La cola no está vacía")

# Vaciar la cola
queue.clear()
'''
En el ejemplo anterior, utilizamos la clase deque para crear una cola vacía. 
Luego, utilizamos el método append para agregar elementos a la cola y el método popleft para eliminar el primer elemento de la cola. 
Podemos acceder al primer elemento de la cola sin eliminarlo utilizando el índice 0 (queue[0]), 
pero es importante tener en cuenta que esto no es muy eficiente ya que el tiempo de acceso no es constante. 
Para verificar si la cola está vacía, simplemente comprobamos si está vacía utilizando un condicional (if not queue). 
Finalmente, utilizamos el método clear para vaciar completamente la cola.
'''
## Las colas son útiles en diversas situaciones, como:

'''
Gestión de tareas: 
Las colas pueden utilizarse para administrar tareas en una aplicación. 
Las tareas se agregan a la cola y se procesan en el orden en que fueron agregadas.

Procesamiento de colas de mensajes: 
Las colas son ampliamente utilizadas en sistemas de mensajería para encolar mensajes y procesarlos en el orden correcto.

Algoritmos: Algunos algoritmos, como el recorrido BFS (Breadth-First Search) en grafos, utilizan colas para explorar los vértices en el orden de distancia desde un punto de inicio.

En general, las colas son una herramienta valiosa para implementar procesos en el orden en que se agregan, lo que puede ser útil en una amplia variedad de escenarios en programación.'''