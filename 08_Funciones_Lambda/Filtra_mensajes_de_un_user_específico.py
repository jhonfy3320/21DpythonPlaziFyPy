'''Para implementar la función filter_user_messages, podemos utilizar una comprensión de listas para filtrar los mensajes que coinciden 
con el nombre de usuario dado. 
Aquí tienes una posible implementación'''


def filter_user_messages(messages, user):
    filtered_messages = [message for message in messages if message.get('sender') == user]
    return filtered_messages

messages = [
    {"sender": "Juan", "content": "Hola"},
    {"sender": "María", "content": "¿Cómo estás?"},
    {"sender": "Juan", "content": "Todo bien, gracias"},
    {"sender": "Laura", "content": "Hola, soy Laura"}
]

user = "Juan"
result = filter_user_messages(messages, user)
print(result)
# Salida: [{'sender': 'Juan', 'content': 'Hola'}, {'sender': 'Juan', 'content': 'Todo bien, gracias'}]

## En esta implementación:

#Utilizamos una comprensión de listas para crear la lista filtered_messages. 
#Iteramos sobre cada uno messageen la lista messages.
#Para cada mensaje, utilizamos el método getde los diccionarios para obtener el valor asociado a la clave 'sender', que corresponde al remitente del mensaje.
#Comparamos el remitente con el nombre de usuario dado ( user) y si coinciden, incluimos el mensaje en la lista filtered_messages.
#Finalmente, retornamos la lista filtered_messages, que contiene solo los mensajes del usuario especificado.
#Ejemplo de uso:

'''En este ejemplo, utilizamos la función filter_user_messagespara filtrar los mensajes enviados por el usuario "Juan". 
Como resultado, obtenemos una lista con los mensajes enviados por dicho usuario. 
Si no hubiera mensajes del usuario especificado, la función devolvería una lista vacía [].'''