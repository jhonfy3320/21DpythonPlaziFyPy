'''
Para implementar la clase ContactList como una hash table, utilizaremos un diccionario donde cada clave será el nombre del 
contacto y el valor será su número de teléfono. A continuación, te mostraré cómo puedes implementar cada uno de los métodos requeridos:'''

class ContactList:
    def __init__(self, size):
        self.size = size
        self.buckets = {}

    def hash(self, key):
        # La función hash toma el nombre del contacto y devuelve un índice calculado.
        # Utilizamos el operador módulo (%) para asegurar que el índice esté dentro del tamaño de la hash table.
        return hash(key) % self.size

    def insert(self, name, phone):
        # El método insert recibe el nombre y el número de teléfono de un contacto
        # y los agrega como una nueva entrada en la hash table.
        index = self.hash(name)
        self.buckets[index] = [name, phone]

    def get(self, name):
        # El método get recibe el nombre de un contacto y devuelve su número de teléfono.
        # Si el contacto no existe, retornará None.
        index = self.hash(name)
        contact_info = self.buckets.get(index)
        if contact_info and contact_info[0] == name:
            return contact_info[1]
        return None

    def retrieveAll(self):
        # El método retrieveAll devuelve una lista con todos los buckets utilizados en la hash table.
        # Cada bucket es una lista con el nombre y el número de teléfono del contacto.
        return [bucket for bucket in self.buckets.values() if bucket]

    def delete(self, name):
        # El método delete recibe el nombre de un contacto y lo elimina de la hash table.
        # Si el contacto no existe, retornará None.
        index = self.hash(name)
        contact_info = self.buckets.get(index)
        if contact_info and contact_info[0] == name:
            del self.buckets[index]
            return True
        return None

# Ejemplo de uso
contactList = ContactList(10)
contactList.insert("Mr michi", "123-456-7890")

print(contactList.retrieveAll())  # Output: [["Mr michi", "123-456-7890"]]

phone_number = contactList.get("Mr michi")
print(phone_number)  # Output: "123-456-7890"

result = contactList.delete("Mr michi")
print(result)  # Output: True

phone_number = contactList.get("Mr michi")
print(phone_number)  # Output: None
'''
En este ejemplo, hemos implementado la clase ContactList como una hash table utilizando un diccionario 
(self.buckets) para almacenar la información de los contactos. 
Cada contacto se agrega utilizando su nombre como clave y su número de teléfono como valor. 
Los métodos get, insert, retrieveAll y delete funcionan según lo requerido y manipulan los datos en la hash table.'''