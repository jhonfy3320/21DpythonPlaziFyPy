from Node import PatientNode

class PatientList:
    def __init__(self, max_beds):
        self.head = None
        self.max_beds = max_beds
        self.available_beds = max_beds

    def addPatient(self, name, age):
        if self.available_beds == 0:
            raise Exception("No hay camas disponibles")
        
        new_patient = PatientNode(name, age, self.max_beds - self.available_beds + 1)
        
        if not self.head:
            self.head = new_patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_patient
        
        self.available_beds -= 1

    def removePatient(self, name):
        if not self.head:
            raise Exception("Paciente no encontrado")
        
        if self.head.name == name:
            self.available_beds += 1
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.name == name:
                self.available_beds += 1
                current.next = current.next.next
                return
            current = current.next
        
        raise Exception("Paciente no encontrado")

    def getPatient(self, name):
        current = self.head
        while current:
            if current.name == name:
                return {
                    'name': current.name,
                    'age': current.age,
                    'bedNumber': current.bed_number
                }
            current = current.next
        
        raise Exception("Paciente no encontrado")

    def getPatientList(self):
        patient_list = []
        current = self.head
        while current:
            patient_list.append({
                'name': current.name,
                'age': current.age,
                'bedNumber': current.bed_number
            })
            current = current.next
        return patient_list

    def getAvailableBeds(self):
        return self.available_beds
# Creamos una lista de pacientes con 3 camas disponibles
patient_list = PatientList(3)

# Agregamos pacientes
patient_list.addPatient("Paciente 1", 20)
patient_list.addPatient("Paciente 2", 30)

# Obtenemos la lista de pacientes
print(patient_list.getPatientList())
# Output: [
#   {'name': 'Paciente 1', 'age': 20, 'bedNumber': 1},
#   {'name': 'Paciente 2', 'age': 30, 'bedNumber': 2}
# ]

# Obtenemos la información de un paciente en particular
print(patient_list.getPatient("Paciente 1"))
# Output: {'name': 'Paciente 1', 'age': 20, 'bedNumber': 1}

# Eliminamos un paciente
patient_list.removePatient("Paciente 1")

# Obtenemos la lista actualizada de pacientes
print(patient_list.getPatientList())
# Output: [
#   {'name': 'Paciente 2', 'age': 30, 'bedNumber': 2}
# ]

# Obtenemos el número de camas disponibles
print(patient_list.getAvailableBeds())
# Output: 2
