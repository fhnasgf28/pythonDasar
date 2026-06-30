"""
belanja_ibu.py
Simulasi pembelanjaan barang "ibu-ibu" dengan pendekatan OOP.
- Product, Catalog, Cart, Customer, Shop
- Contoh pemakaian ada di blok __main__

Cara pakai:
$ python belanja_ibu.py

Author: GitHub Copilot (via assistant)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import datetime

@dataclass
class Product:
    sku: str
    name: str
    price: float
    stock: int

    def is_available(self, qty: int) -> bool:
        return self.stock >= qty

    def reduce_stock(self, qty: int) -> None:
        if qty > self.stock:
            raise ValueError(f"Stok tidak cukup untuk {self.name}")
        self.stock -= qty

    def increase_stock(self, qty: int) -> None:
        self.stock += qty

@dataclass
class Catalog:
    products: Dict[str, Product] = field(default_factory=dict)

    def add_product(self, product: Product) -> None:
        self.products[product.sku] = product

    def get(self, sku: str) -> Optional[Product]:
        return self.products.get(sku)

    def find_by_name(self, name: str) -> List[Product]:
        name = name.lower()
        return [p for p in self.products.values() if name in p.name.lower()]

    def list_products(self) -> List[Product]:
        return list(self.products.values())

@dataclass
class CartItem:
    product: Product
    quantity: int

    @property
    def subtotal(self) -> float:
        return round(self.product.price * self.quantity, 2)

@dataclass
class Cart:
    items: Dict[str, CartItem] = field(default_factory=dict)  # key=sku

    def add(self, product: Product, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("Kuantitas harus > 0")
        if not product.is_available(qty):
            raise ValueError(f"Stok tidak cukup untuk {product.name}")
        if product.sku in self.items:
            self.items[product.sku].quantity += qty
        else:
            self.items[product.sku] = CartItem(product=product, quantity=qty)

    def remove(self, sku: str, qty: int = 0) -> None:
        if sku not in self.items:
            raise KeyError("Produk tidak ada di keranjang")
        if qty <= 0 or qty >= self.items[sku].quantity:
            del self.items[sku]
        else:
            self.items[sku].quantity -= qty

    def total(self) -> float:
        return round(sum(item.subtotal for item in self.items.values()), 2)

    def clear(self) -> None:
        self.items.clear()

    def is_empty(self) -> bool:
        return len(self.items) == 0

@dataclass
class Customer:
    name: str
    balance: float = 0.0  # simpan uang tunai/virtual

    def pay(self, amount: float) -> bool:
        if amount <= 0:
            return False
        if self.balance >= amount:
            self.balance = round(self.balance - amount, 2)
            return True
        return False

class Shop:
    def __init__(self, catalog: Catalog, name: str = "Toko Ibu-Bu"):
        self.catalog = catalog
        self.name = name

    def apply_discount(self, cart: Cart) -> float:
        """
        Contoh kebijakan diskon sederhana:
        - Jika total >= 200_000 -> diskon 10%
        - Jika total >= 100_000 -> diskon 5%
        - Diskon untuk produk tertentu bisa ditambahkan
        """
        total = cart.total()
        discount = 0.0
        if total >= 200_000:
            discount = 0.10
        elif total >= 100_000:
            discount = 0.05
        return round(total * discount, 2)

    def checkout(self, cart: Cart, customer: Customer, payment_method: str = "cash") -> Dict:
        if cart.is_empty():
            raise ValueError("Keranjang kosong, tidak bisa checkout")

        # cek stock sebelum mengurangi
        for item in cart.items.values():
            if not item.product.is_available(item.quantity):
                raise ValueError(f"Stok tidak cukup untuk {item.product.name}")

        subtotal = cart.total()
        discount_amount = self.apply_discount(cart)
        total_due = round(subtotal - discount_amount, 2)

        # proses pembayaran (sederhana)
        payment_success = False
        if payment_method == "cash":
            payment_success = customer.pay(total_due)
        elif payment_method == "card":
            # simulasi: kartu selalu berhasil
            payment_success = True
        else:
            raise ValueError("Metode pembayaran tidak dikenal")

        if not payment_success:
            raise ValueError("Pembayaran gagal: saldo tidak cukup atau metode tidak valid")

        # kurangi stock
        for item in cart.items.values():
            item.product.reduce_stock(item.quantity)

        # buat receipt sederhana
        receipt = {
            "shop": self.name,
            "customer": customer.name,
            "date": datetime.datetime.now().isoformat(),
            "items": [
                {"sku": it.product.sku, "name": it.product.name, "qty": it.quantity, "unit_price": it.product.price, "subtotal": it.subtotal}
                for it in cart.items.values()
            ],
            "subtotal": subtotal,
            "discount": discount_amount,
            "total_due": total_due,
            "payment_method": payment_method,
        }

        cart.clear()
        return receipt

# Contoh pemakaian
if __name__ == "__main__":
    cat = Catalog()

    # Tambah produk yang sering dibeli ibu-ibu
    cat.add_product(Product(sku="BR001", name="Beras 5kg", price=65000.0, stock=30))
    cat.add_product(Product(sku="MG001", name="Minyak Goreng 2L", price=25000.0, stock=40))
    cat.add_product(Product(sku="TL001", name="Telur 1kg (±20 biji)", price=30000.0, stock=50))
    cat.add_product(Product(sku="GL001", name="Gula Pasir 1kg", price=15000.0, stock=45))
    cat.add_product(Product(sku="SS001", name="Susu UHT 1L", price=18000.0, stock=25))
    cat.add_product(Product(sku="SB001", name="Sabun Cuci", price=12000.0, stock=35))
    cat.add_product(Product(sku="DR001", name="Deterjen 1kg", price=20000.0, stock=25))
    cat.add_product(Product(sku="MI001", name="Mie Instan (1 pack)", price=3500.0, stock=200))

    # Buat customer
    ibu = Customer(name="Bu Ani", balance=250000.0)  # saldo tunai

    # Buat keranjang dan tambahkan barang
    cart = Cart()
    try:
        cart.add(cat.get("BR001"), 1)
        cart.add(cat.get("MG001"), 2)
        cart.add(cat.get("TL001"), 1)
        cart.add(cat.get("MI001"), 10)
    except Exception as e:
        print("Error menambahkan ke keranjang:", e)

    print("Isi keranjang:")
    for it in cart.items.values():
        print(f"- {it.product.name} x{it.quantity} = Rp {it.subtotal}")
    print("Subtotal:", cart.total())

    toko = Shop(cat, name="Warung Ibu-ibu")
    try:
        receipt = toko.checkout(cart, ibu, payment_method="cash")
        print("\nPembayaran berhasil. Struk:")
        print(f"Toko: {receipt['shop']}")
        print(f"Pembeli: {receipt['customer']}")
        print(f"Tanggal: {receipt['date']}")
        print("Items:")
        for it in receipt['items']:
            print(f"  - {it['name']} x{it['qty']} = Rp {it['subtotal']}")
        print(f"Subtotal: Rp {receipt['subtotal']}")
        print(f"Diskon: Rp {receipt['discount']}")
        print(f"Total bayar: Rp {receipt['total_due']}")
        print(f"Sisa saldo pembeli: Rp {ibu.balance}")
    except Exception as e:
        print("Checkout gagal:", e)
