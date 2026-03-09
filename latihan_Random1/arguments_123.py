def jumlahkan_semuanya(*args):
    total = 0
    for angka in args:
        total += angka
    return total

print(jumlahkan_semuanya(3,4,5,6,7,3,))

def buat_profil_user(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

buat_profil_user(nama="farhanassegaf", role="Developer Odoo", lokasi="Jakarta")