class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
    
    def remove_item(self, menu_item):
        self.items.remove(menu_item)
    
    def calculate_total(self):
        return sum(item.price for item in self.items)
    
    def display_order(self):
        if not self.items:
            print("Order is empty")
            return
        print("Your order:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")

class Restaurant:
    def __init__(self):
        self.menu = []
    
    def add_menu_item(self, menu_item):
        self.menu.append(menu_item)
    
    def display_menu(self):
        print("Menu:")
        for item in self.menu:
            print(item)

def main():
    restaurant = Restaurant()

    # add some menu items
    restaurant.add_menu_item(MenuItem("Burger", 5.99))
    restaurant.add_menu_item(MenuItem("Pizza", 8.99))
    restaurant.add_menu_item(MenuItem("Salad", 4.99))
    restaurant.add_menu_item(MenuItem("Soda", 1.99))
    restaurant.add_menu_item(MenuItem("Fries", 2.49))
    restaurant.add_menu_item(MenuItem("Ice Cream", 3.49))

    # display the menu
    restaurant.display_menu()

    # create an order
    order = Order()

    # simulate adding items to the order
    order.add_item(restaurant.menu[0])  # Burger
    order.add_item(restaurant.menu[1])  # Pizza
    order.add_item(restaurant.menu[3])  # Soda
    order.add_item(restaurant.menu[4])  # Fries
    order.add_item(restaurant.menu[5])  # Ice Cream
    order.add_item(restaurant.menu[2])  # Salad
    order.add_item(restaurant.menu[0])  # Burger
    order.add_item(restaurant.menu[1])  # Pizza
    order.add_item(restaurant.menu[3])  # Soda
    order.add_item(restaurant.menu[4])  # Fries
    order.add_item(restaurant.menu[5])  # Ice Cream
    order.add_item(restaurant.menu[2])  # Salad
    order.add_item(restaurant.menu[0])  # Burger
    order.add_item(restaurant.menu[1])  # Pizza
    order.add_item(restaurant.menu[3])  # Soda 

    # display the order
    order.display_order()

    # simulate removing an item
    order.remove_item(restaurant.menu[2])  # Salad
    print("\nAfter removing Salad:")
    order.display_order()

    # display updated order
    order.display_order()


if __name__ == "__main__":
    main()