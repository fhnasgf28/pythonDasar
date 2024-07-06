class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price: .2f} x {self.quantity}"


class Cart:
    def __init__(self, item):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to the cart.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} removed from the cart")
                return
        print(f"{item_name} not found in the cart")

    def view_cart(self):
        if not self.items:
            print("the cart is empty")
        else:
            for item in self.items:
                print(item)

    def total_price(self):
        total = sum(item.price * item.quantity for item in self.items)
        return total


class DiscountedItem(Item):
    def __init__(self, name, price, quantity, discount):
        super().__init__(name, price, quantity)
        self.discount = discount

    def price_after_discount(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return f"{self.name}: ${self.price_after_discount():.2f} x {self.quantity} (discount: {self.discount}%)"

def main():
    # Buat objek Cart
    cart = Cart()

    # Tambahkan item ke dalam keranjang
    item1 = Item("Apple", 0.5, 10)
    item2 = Item("Banana", 0.2, 5)
    item3 = DiscountedItem("Orange", 1.0, 3, 10)  # Diskon 10%

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    # Lihat isi keranjang
    print("\nItems in the cart:")
    cart.view_cart()

    # Hapus item dari keranjang
    cart.remove_item("Banana")

    # Lihat isi keranjang setelah penghapusan
    print("\nItems in the cart after removal:")
    cart.view_cart()

    # Hitung total harga
    total = cart.total_price()
    print(f"\nTotal price: ${total:.2f}")

if __name__ == "__main__":
    main()

