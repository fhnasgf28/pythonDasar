import unittest

from project_pos_oop.main import PercentageDiscount, POSTransaction, Product, ShoppingCart


class TestProjectPOSOOP(unittest.TestCase):
    def test_cart_can_sum_same_product_quantity(self):
        product = Product("P001", "Kopi Susu", 18_000)
        cart = ShoppingCart()

        cart.add_product(product, 2)
        cart.add_product(product, 1)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].quantity, 3)
        self.assertEqual(cart.subtotal, 54_000)

    def test_transaction_calculates_total_discount_and_change(self):
        cart = ShoppingCart()
        cart.add_product(Product("P001", "Kopi Susu", 18_000), 2)
        transaction = POSTransaction(cart=cart, discount=PercentageDiscount(10))

        self.assertEqual(transaction.discount_amount, 3_600)
        self.assertEqual(transaction.total, 32_400)
        self.assertEqual(transaction.pay(50_000), 17_600)

    def test_transaction_rejects_insufficient_cash(self):
        cart = ShoppingCart()
        cart.add_product(Product("P001", "Kopi Susu", 18_000), 1)
        transaction = POSTransaction(cart=cart)

        with self.assertRaises(ValueError):
            transaction.pay(10_000)


if __name__ == "__main__":
    unittest.main()
