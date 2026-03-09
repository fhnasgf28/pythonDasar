inventory = [
    {'name': 'Laptop', 'stock': 10, 'price': 1500},
    {'name': 'Mouse', 'stock': 50, 'price': 25},
    {'name': 'Keyboard', 'stock': 30, 'price': 45},
    {'name': 'Monitor', 'stock': 20, 'price': 200},
    {'name': 'Printer', 'stock': 5, 'price': 300},
]


# menampilkan berdasarkan daftar barang
def display_inventory(inventory):
    for item in inventory:
        print(f"Name: {item['name']}, Stock: {item['stock']}, Price: ${item['price']}")


display_inventory(inventory)

print("=========================================\n")


# sortir barang berdasarkan nama
def sort_by_name(inventory):
    return sorted(inventory, key=lambda x: x['name'])


sorted_inventory = sort_by_name(inventory)
display_inventory(sorted_inventory)
print("=============\n")


# sortir barang berdasarkan jumlah stock
def sort_by_stock(inventory):
    return sorted(inventory, key=lambda x: x['stock'])


sorted_inventory2 = sort_by_stock(inventory)
display_inventory(sorted_inventory2)
print('=================\n')


# sortir barang berdasarkan harga
def sort_by_price(inventory):
    return sorted(inventory, key=lambda x: x['price'], reverse=True)


sorted_inventory = sort_by_price(inventory)
display_inventory(sorted_inventory)
