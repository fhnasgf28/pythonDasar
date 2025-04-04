class OrderLine:
    def __init__(self, product, qty, harga, diskon=0):
        self.product = product
        self.qty = qty
        self.harga = harga
        self.diskon = diskon

    def subtotal(self):
        total = self.qty * self.harga
        if self.diskon > 0:
            total -= total * (self.diskon / 100)
        return total

    def __str__(self):
        return f"{self.product} X {self.qty} : {self.subtotal()}"


class Order:
    def __init__(self):
        self.order_lines = []

    def tambah_order_line(self, order_line):
        self.order_lines.append(order_line)

    def total_order(self):
        return sum(line.subtotal() for line in self.order_lines)

    def tampilkan_order(self):
        print("=========Farhan Assegaf==========")
        for line in self.order_lines:
            print(line)
        print(f"Total Order: {self.total_order()}")

# contoh penggunaan
def main():
    order = Order()
    order.tambah_order_line(OrderLine("Laptop", 1, 1000000))
    order.tambah_order_line(OrderLine("Mouse", 2, 50000))
    order.tambah_order_line(OrderLine("Keyboard", 1, 30000))
    order.tampilkan_order()

if __name__ == "__main__":
    main()