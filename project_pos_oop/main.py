from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Protocol


class RupiahFormatter:
    """Helper kecil untuk format angka menjadi Rupiah."""

    @staticmethod
    def format(amount: float) -> str:
        return f"Rp{amount:,.0f}".replace(",", ".")


@dataclass(frozen=True)
class Product:
    """Representasi produk yang dijual di POS."""

    code: str
    name: str
    price: float

    def __post_init__(self) -> None:
        if self.price <= 0:
            raise ValueError("Harga produk harus lebih dari 0")


@dataclass
class CartItem:
    """Satu baris item di keranjang belanja."""

    product: Product
    quantity: int = 1

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("Quantity harus lebih dari 0")

    @property
    def subtotal(self) -> float:
        return self.product.price * self.quantity


class Discount(Protocol):
    """Kontrak sederhana untuk semua tipe diskon."""

    def calculate(self, subtotal: float) -> float:
        ...


@dataclass(frozen=True)
class PercentageDiscount:
    """Diskon berdasarkan persentase, contoh 10%."""

    percentage: float

    def __post_init__(self) -> None:
        if not 0 <= self.percentage <= 100:
            raise ValueError("Persentase diskon harus di antara 0 sampai 100")

    def calculate(self, subtotal: float) -> float:
        return subtotal * (self.percentage / 100)


@dataclass
class ShoppingCart:
    """Keranjang belanja untuk menyimpan item POS."""

    items: List[CartItem] = field(default_factory=list)

    def add_product(self, product: Product, quantity: int = 1) -> None:
        for item in self.items:
            if item.product.code == product.code:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    @property
    def subtotal(self) -> float:
        return sum(item.subtotal for item in self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0


@dataclass
class POSTransaction:
    """Proses checkout POS: hitung diskon, total, bayar, dan struk."""

    cart: ShoppingCart
    discount: Discount | None = None

    @property
    def discount_amount(self) -> float:
        if self.discount is None:
            return 0
        return self.discount.calculate(self.cart.subtotal)

    @property
    def total(self) -> float:
        return self.cart.subtotal - self.discount_amount

    def pay(self, cash: float) -> float:
        if self.cart.is_empty():
            raise ValueError("Keranjang masih kosong")
        if cash < self.total:
            raise ValueError("Uang bayar tidak cukup")
        return cash - self.total

    def print_receipt(self, cash: float) -> str:
        change = self.pay(cash)
        lines = ["========= STRUK POS ========="]

        for item in self.cart.items:
            product_text = f"{item.product.name} x{item.quantity}"
            lines.append(f"{product_text:<18} {RupiahFormatter.format(item.subtotal):>10}")

        lines.extend(
            [
                "-----------------------------",
                f"{'Subtotal':<18} {RupiahFormatter.format(self.cart.subtotal):>10}",
                f"{'Diskon':<18} {RupiahFormatter.format(self.discount_amount):>10}",
                f"{'Total':<18} {RupiahFormatter.format(self.total):>10}",
                f"{'Bayar':<18} {RupiahFormatter.format(cash):>10}",
                f"{'Kembalian':<18} {RupiahFormatter.format(change):>10}",
                "=============================",
            ]
        )
        return "\n".join(lines)


def build_demo_transaction() -> POSTransaction:
    """Membuat data demo agar file bisa langsung dijalankan."""

    kopi_susu = Product("P001", "Kopi Susu", 18_000)
    roti_coklat = Product("P002", "Roti Coklat", 15_000)
    air_mineral = Product("P003", "Air Mineral", 5_000)

    cart = ShoppingCart()
    cart.add_product(kopi_susu, 2)
    cart.add_product(roti_coklat, 3)
    cart.add_product(air_mineral, 1)

    return POSTransaction(cart=cart, discount=PercentageDiscount(10))


if __name__ == "__main__":
    transaction = build_demo_transaction()
    print(transaction.print_receipt(cash=100_000))
