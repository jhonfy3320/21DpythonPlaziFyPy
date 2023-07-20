'''En Python, la característica de herencia no se aplica directamente a los diccionarios. 
La herencia se utiliza en la programación orientada a objetos para crear nuevas clases basadas en clases existentes, 
permitiendo a las nuevas clases heredar atributos y métodos de la clase base.

Sin embargo, en el contexto de diccionarios, es posible utilizar la función dict()para crear un nuevo diccionario a partir de un diccionario 
existente y luego agregar o modificar sus pares clave-valor. 
Aunque esto no está relacionado directamente con la herencia, te mostraré un ejemplo para aclarar cómo se puede lograr lo que estás buscando:
'''
# Diccionario existente
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Crear un nuevo diccionario basado en el diccionario existente
nueva_persona = dict(persona)

# Agregar o modificar pares clave-valor en el nuevo diccionario
nueva_persona["ocupacion"] = "Ingeniero"
nueva_persona["edad"] = 31

# Imprimir los dos diccionarios
print(persona)
print(nueva_persona)

'''En este ejemplo, se parte de un diccionario existente llamado persona. 
Luego, se utiliza la función dict()para crear un nuevo diccionario llamadonueva_persona basado en el diccionario existente. 
Ambos diccionarios comparten inicialmente los mismos pares clave-valor.

Luego, se agrega un nuevo par clave-valor "ocupacion": "Ingeniero"al diccionario nueva_personausando la notación de corchetes. 
Además, se modifica el valor de la clave "edad"en el diccionario nueva_personaasignándole un nuevo valor.

Al imprimir ambos diccionarios, se puede ver que el diccionario original personano se ha modificado, mientras que el diccionario 
nueva_personatiene los nuevos pares clave-valores agregados o modificados.

Aunque esto no es herencia en el sentido estricto, puede considerarlo como una forma de crear un nuevo diccionario basado en uno existente y 
personalizarlo agregando o modificando pares clave-valor según sus necesidades.'''