from latihan_Random.gemini.data_pelanggan import pelanggan
from models.product import Product
from models.customer import Customer
from sales.transaction import Transaction

# Setup awal
produk1 = Product(1, "Kopi", 15000)
produk2 = Product(2, "Teh", 10000)
pelanggan = Customer(101, "Andi")

# Transaksi
transaksi = Transaction(pelanggan)
transaksi.add_product(produk1, 2)
transaksi.add_product(produk2, 1)

print(f"{pelanggan.name} belanja total: Rp{transaksi.total()}")