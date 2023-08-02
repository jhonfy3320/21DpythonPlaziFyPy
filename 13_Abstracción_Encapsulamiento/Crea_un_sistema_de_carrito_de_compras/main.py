from product import Product
from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def addToCart(self):
        pass

class Article(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def addToCart(self):
        return f"Agregando {self.quantity} unidades del artículo {self.name} al carrito"

class Service(Product):
    def addToCart(self):
        return f"Agregando el servicio {self.name} al carrito"

class Cart:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)
        print(product.addToCart())

    def deleteProduct(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Eliminando {product.name} del carrito")
        else:
            print(f"{product.name} no se encontró en el carrito")

    def calculateTotal(self):
        total = sum(product.price for product in self.products)
        return total

    def getProducts(self):
        return self.products

# Ejemplo de uso
book = Article("Libro", 100, 2)
course = Service("Curso", 120)

cart = Cart()
cart.addProduct(book)
cart.addProduct(course)
total = cart.calculateTotal()
print(f"Total: {total}")