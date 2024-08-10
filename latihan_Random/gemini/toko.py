products = [
    {"name": "Buku", "price": 60000},
    {"name": "Pensil", "price": 40000},
    {"name": "Tas", "price": 100000},
    {"name": "Komputer", "price": 6000000},
]

discount_rate = 0.1
total_price = 0
for product in products:
    quantity = int(input(f"Masukan jumlah {product['name']:}"))
    item_price = product['price'] * quantity
    discount_amount = item_price * discount_rate
    discounted_price = item_price - discount_amount
    total_price += item_price

    print(f"{product['name']} x {quantity} = {item_price}")
    if discount_amount > 0:
        print(f"discon: {discount_amount}")
        print(f"harga discount: {discounted_price}")