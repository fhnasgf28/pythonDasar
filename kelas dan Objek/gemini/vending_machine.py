class VendingMachine:
    def __init__(self, products):
        self.products = products

    def add_product(self, product_name, price, quantity):
        if product_name not in self.products:
            self.products[product_name] = {"price": price, "quantity": quantity}
            print(f"Product {product_name} added successfully")
        else:
            print(f"Product {product_name} already exists. Update quantity instead")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print(f"Product {product_name} removed successfully")
        else:
            print(f"Product {product_name} not found")

    def check_availability(self, product_name):
        if product_name in self.products:
            quantity = self.products[product_name]["quantity"]
            print(f"{product_name} is available. quantity: {quantity}")
        else:
            print(f"Product {product_name} not found.")

    def dispense_product(self, product_name):
        if product_name in self.products:
            quantity = self.products[product_name]["quantity"]
            if quantity > 0:
                quantity -= 1
                self.products[product_name]["quantity"] = quantity
                print(f"Dispensed {product_name}. Enjoy")
            else:
                print(f"sorry, {product_name} is out of stock")
        else:
            print(f"Product {product_name} not found")


# create a vending machine object
vending_machine = VendingMachine({
    'cola': {"price": 1000, 'quantity': 5},
    'chips': {"price": 2000, 'quantity': 4},
})

# check availability
vending_machine.check_availability("chip")

# check availability after dispensing
vending_machine.check_availability('cola')
