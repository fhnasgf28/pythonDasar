class Product:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}"

product = Product(1, "Product A", 10000)
print(product)