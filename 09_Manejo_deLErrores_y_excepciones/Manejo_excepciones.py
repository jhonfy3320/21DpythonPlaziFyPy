'''Para implementar la función calculate_discounted_priceque cumpla con las condiciones y manejo de excepciones requeridas, 
podemos seguir los siguientes pasos:

Verificar que el precio y el descuento sean valores numéricos y positivos. 
Si no lo son, lanzaremos las excepciones ValueErrory TypeErrorsegún corresponda.

Calcular el precio con el descuento aplicado y devolver el resultado.

En caso de que preceda cualquier otro tipo de excepción no prevista, capturaremos la excepción y la relanzaremos como una excepción 
genérica del tipo Exception.

Aqui tienes la implementacion:'''

def calculate_discounted_price(price, discount):
    try:
        if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
            raise TypeError("El precio y el descuento deben ser números")

        if price < 0 or discount < 0:
            raise ValueError("El precio y el descuento deben ser valores positivos")

        discounted_price = price - (price * (discount / 100))
        return discounted_price

    except ValueError as ve:
        raise ve
    except TypeError as te:
        raise te
    except Exception as e:
        raise Exception("Ha ocurrido un error inesperado: " + str(e))

# Ejemplo de uso
try:
    price = 100
    discount = 20
    discounted_price = calculate_discounted_price(price, discount)
    print(f"El precio con descuento es: {discounted_price}")
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
except Exception as e:
    print(e)

    
'''En este ejemplo, la función calculate_discounted_pricetoma dos parámetros: pricey discount. 
Se realiza una verificación inicial para asegurarse de que ambos parámetros sean números válidos y positivos. 
Si se cumple alguna de las condiciones, se lanzan las excepciones ValueErroro TypeErrorsegún corresponda.

Si los parámetros son válidos, se procede a calcular el precio con el descuento aplicado y se devuelve el resultado. 
Si ocurre cualquier otro tipo de excepción no previsto, se captura y se relanza como una excepción genérica del tipo 
Exceptioncon un mensaje adecuado para obtener más detalles del error.

En el ejemplo de uso, se proporciona un precio de 100 y un descuento del 20%. 
La función calcula correctamente el precio con el descuento y lo muestra en pantalla ( El precio con descuento es: 80.0). 
Si se intenta pasar valores negativos o no numéricos como parámetros, la función lanzará las excepciones adecuadas con los mensajes 
correspondientes.'''