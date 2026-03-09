def send_package(recipient, address, weight, cost):
    # mencetak informasi pengiriman
    print('Mengirim kepada\t:', recipient)
    print('Alamat\t', address)
    print('Berat\t', weight, "Kg")
    print("Biaya: Rp", cost)

    # menentukan biaya pengiriman
    shipping_cost = calculate_shipping_cost(weight,cost)
    # mencetak biaya pengiriman
    print("Biaya pengiriman", shipping_cost)
    # mengirim paket
    send_to_shipping_company(recipient, address, weight, shipping_cost)

    print("Paket Berhasil dikirim")
def calculate_shipping_cost(weight, cost):
    # menentukan biaya pengiriman berdasarkan berat dan nilai barang
    if weight <= 1:
        return 10000
    elif weight <= 3:
        return 20000
    elif weight <= 5:
        return 30000
    else:
        return 40000 + (weight - 5) * 5000

def send_to_shipping_company(recipient, address, weight, cost):
    pass
# mencoba fungsi pengiriman pake
send_package("John Doe", "Jl. Sudirman", 2, 30000)