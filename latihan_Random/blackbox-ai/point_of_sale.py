class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name}: Rp {self.price:.2f}"


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self):
        #mengoverride method untuk menghitung harga setelah diskon
        discounted_price = self.price * (1 - self.discount / 100)
        return discounted_price

    def __str__(self):
        return f"{self.name} (Diskon {self.discount}%): Rp {self.get_price():.2f}"

def main():
    # membuat beberapa product
    product1 = Product("Product A", 10000)
    product2 = Product("Product B", 20000)
    discounted_product = DiscountedProduct("Product C", 30000, 10)

    # menampilkan Harga Product
    print("Daftar Product :")
    print(product1)
    print(product2)
    print(discounted_product)

    # menghitung total harga
    total_price = product1.get_price() + product2.get_price() + discounted_product.get_price()
    print(f"\nTotal Harga: Rp {total_price:.2f}")

if __name__ == "__main__":
    main()