'''Para crear el planificador de tareas utilizando closures, vamos a definir la función createTaskPlannerque devolverá una serie de métodos 
internos para administrar las tareas. 
Utilizaremos los cierres para mantener la información de las tareas y los métodos asociados con ellas.
'''
# Aquí está la implementación del planificador de tareas:

def createTaskPlanner():
    tasks = []

    def addTask(task):
        task['completed'] = False
        tasks.append(task)

    def removeTask(value):
        if isinstance(value, int):
            tasks[:] = [task for task in tasks if task['id'] != value]
        elif isinstance(value, str):
            tasks[:] = [task for task in tasks if task['name'] != value]

    def getTasks():
        return tasks

    def getPendingTasks():
        return [task for task in tasks if not task['completed']]

    def getCompletedTasks():
        return [task for task in tasks if task['completed']]

    def markTaskAsCompleted(value):
        if isinstance(value, int):
            for task in tasks:
                if task['id'] == value:
                    task['completed'] = True
                    break
        elif isinstance(value, str):
            for task in tasks:
                if task['name'] == value:
                    task['completed'] = True
                    break

    def getSortedTasksByPriority():
        return sorted(tasks, key=lambda task: task['priority'])

    def filterTasksByTag(tag):
        return [task for task in tasks if tag in task['tags']]

    def updateTask(taskId, updates):
        for task in tasks:
            if task['id'] == taskId:
                task.update(updates)
                break

    return {
        'addTask': addTask,
        'removeTask': removeTask,
        'getTasks': getTasks,
        'getPendingTasks': getPendingTasks,
        'getCompletedTasks': getCompletedTasks,
        'markTaskAsCompleted': markTaskAsCompleted,
        'getSortedTasksByPriority': getSortedTasksByPriority,
        'filterTasksByTag': filterTasksByTag,
        'updateTask': updateTask
    }

# Ejemplo de uso:
planner = createTaskPlanner()

planner['addTask']({'id': 1, 'name': 'Task 1', 'priority': 2, 'tags': ['work']})
planner['addTask']({'id': 2, 'name': 'Task 2', 'priority': 3, 'tags': ['personal']})
planner['addTask']({'id': 3, 'name': 'Task 3', 'priority': 1, 'tags': ['work', 'urgent']})

print(planner['getTasks']())  # Mostrar todas las tareas
print(planner['getPendingTasks']())  # Mostrar tareas pendientes
print(planner['getCompletedTasks']())  # Mostrar tareas completadas

planner['markTaskAsCompleted'](1)  # Marcar tarea 1 como completada

print(planner['getPendingTasks']())  # Mostrar tareas pendientes después de marcar una como completada

planner['removeTask'](2)  # Eliminar tarea 2

print(planner['getTasks']())  # Mostrar todas las tareas después de eliminar una
print(planner['getSortedTasksByPriority']())  # Mostrar tareas ordenadas por prioridad

planner['updateTask'](3, {'priority': 2})  # Actualizar prioridad de tarea 3

print(planner['getTasks']())  # Mostrar todas las tareas después de actualizar una


'''En esta implementación, utilizamos un diccionario que contiene cierres para cada uno de los métodos requeridos. 
Cada método tiene acceso a la lista de tareas tasksy puede operar en ella para realizar las acciones correspondientes.

Al crear una instancia del planificador con createTaskPlanner(), obtenemos un diccionario que contiene todos los métodos para administrar las tareas. 
Podemos agregar tareas, eliminar tareas, obtener tareas pendientes y completadas, marcar tareas como completadas, 
obtener tareas ordenadas por prioridad, filtrar tareas por etiqueta y actualizar propiedades de una tarea.

El ejemplo de uso muestra cómo usar los diferentes métodos del planificador de tareas. 
Puedes agregar más tareas, probar diferentes combinaciones de acciones y utilizar las funciones según tus necesidades.'''