'''
Para implementar el organizador de tareas utilizando Maps y Sets en Python, podemos utilizar un diccionario 
(Map) donde cada clave sea el nombre de la tarea (convertido a minúsculas) y el valor sea un conjunto 
(Set) que contenga las etiquetas asociadas a esa tarea. 

Aquí tienes la implementación de la clase TaskManager:'''

class TaskManager:
    def __init__(self):
        # Inicializamos el diccionario vacío para almacenar las tareas y etiquetas
        self.tasks = {}

    def addTask(self, task, tags):
        # Convertimos el nombre de la tarea a minúsculas
        task_lower = task.lower()

        # Si la tarea ya existe, agregamos las nuevas etiquetas al conjunto existente
        if task_lower in self.tasks:
            self.tasks[task_lower].update(tags)
        # Si la tarea no existe, creamos una nueva entrada en el diccionario con el conjunto de etiquetas
        else:
            self.tasks[task_lower] = set(tags)

    def printTasks(self):
        # Retornamos el diccionario con todas las tareas y etiquetas
        return self.tasks

# Ejemplo de uso
myTaskManager = TaskManager()
myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
myTaskManager.addTask("Sacar al perro", ["mascotas"])
myTaskManager.addTask("Hacer ejercicio", ["salud"])

print(myTaskManager.printTasks())
'''
En este ejemplo, hemos creado la clase TaskManager con los métodos addTask y printTasks. 
Al llamar al método addTask, agregamos las tareas con sus etiquetas al diccionario, y al llamar al método printTasks, 
imprimimos todas las tareas y sus etiquetas en el formato deseado.'''

## La salida del ejemplo será:

{
  'comprar leche': {'compras', 'urgente'}, 
  'sacar al perro': {'mascotas'}, 
  'hacer ejercicio': {'salud'}
}
'''
Observa cómo el nombre de la tarea "Comprar leche" se convirtió a minúsculas para asegurarnos de que las tareas sean insensibles a mayúsculas y minúsculas. T
ambién notarás que las etiquetas se almacenan en un conjunto (Set), lo que garantiza que no haya duplicados 
y que las etiquetas de cada tarea sean únicas.'''