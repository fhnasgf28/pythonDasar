products = [
    {"name": "Buku", "price": 60000},
    {"name": "Pensil", "price": 40000},
    {"name": "Tas", "price": 100000},
    {"name": "Komputer", "price": 6000000},
]

total_price = 0
for product in products:
    quantity = int(input(f"Masukan jumlah {product['name']:}"))
    item_price = product['price'] * quantity
    total_price += item_price

    print(f"{product['name']} x {quantity} = {item_price}")