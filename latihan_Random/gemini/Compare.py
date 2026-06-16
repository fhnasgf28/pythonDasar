# Basic product comparison example

class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
    
    def __repr__(self):
        return f"Product({self.name}, ${self.price}, {self.rating}★)"

def compare_products(products):
    """Compare products and show differences"""
    print("Product Comparison:")
    print("-" * 50)
    
    for product in products:
        print(f"Name: {product.name}")
        print(f"Price: ${product.price}")
        print(f"Rating: {product.rating}★")
        print("-" * 50)
    
    # Find cheapest
    cheapest = min(products, key=lambda p: p.price)
    print(f"\nCheapest: {cheapest.name} (${cheapest.price})")
    
    # Find best rated
    best_rated = max(products, key=lambda p: p.rating)
    print(f"Best Rated: {best_rated.name} ({best_rated.rating}★)")

# Example usage
products = [
    Product("Laptop A", 999, 4.5),
    Product("Laptop B", 1199, 4.8),
    Product("Laptop C", 899, 4.2),
]

compare_products(products)
