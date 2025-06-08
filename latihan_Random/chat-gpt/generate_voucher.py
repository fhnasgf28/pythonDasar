import random
import string

def generate_voucher_code(length=8):
    character = string.ascii_uppercase + string.digits
    return ''.join(random.choice(character) for _ in range(length))

def generate_multiple_voucher(count=10, length=8):
    return [generate_voucher_code(length) for _ in range(count)]

if __name__ == '__main__':
    jumlah = 20
    panjang = 10
    vouchers = generate_multiple_voucher(jumlah, panjang)

    print("Daftar Voucher:")
    for idx, v in enumerate(vouchers, 1):
        print(f"{idx}. {v}")