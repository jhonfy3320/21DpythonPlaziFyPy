def get_student_average(students):
    class_total = 0
    class_count = 0
    student_averages = []

    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades) / len(grades)
        rounded_average = round(average, 2)
        class_total += average
        class_count += 1
        student_averages.append({"name": name, "average": rounded_average})

    class_average = class_total / class_count
    rounded_class_average = round(class_average, 2)

    return {"class_average": rounded_class_average, "students": student_averages}

students = [
    {
        "name": "Pedro",
        "grades": [90, 87, 88, 90],
    },
    {
        "name": "Jose",
        "grades": [99, 71, 88, 96],
    },
    {
        "name": "Maria",
        "grades": [92, 81, 80, 96],
    },
]

result = get_student_average(students)
print(result)
# Salida:
# {
#   "class_average": 88.17,
#   "students": [
#     {
#       "name": "Pedro",
#       "average": 88.75
#     },
#     {
#       "name": "Jose",
#       "average": 88.5
#     },
#     {
#       "name": "Maria",
#       "average": 87.25
#     }
#   ]
# }


'''
En esta implementación, se utiliza un bucle for para iterar sobre cada estudiante 
en la lista students. Para cada estudiante, se obtiene su nombre y sus notas. 
Luego, se calcula el promedio dividiendo la suma de las notas entre la cantidad de notas.

A continuación, se redondea el promedio a dos decimales utilizando la función round(). 
Se agrega el promedio individual del estudiante a la lista student_averages en forma de diccionario con las propiedades "name" y "average".

Mientras se recorren los estudiantes, también se acumula la suma de los promedios de la clase en la variable class_total y se incrementa 
el contador de estudiantes class_count.

Después del bucle, se calcula el promedio general de la clase dividiendo la suma de los promedios de la clase entre la cantidad de estudiantes. 
Nuevamente, se redondea este promedio a dos decimales.

Finalmente, se retorna un nuevo diccionario con las propiedades "class_average" y "students", 
que contienen el promedio general de la clase y la lista de estudiantes con sus promedios individuales.

Puedes probar la función get_student_average con el ejemplo de entrada y salida que has proporcionado:'''