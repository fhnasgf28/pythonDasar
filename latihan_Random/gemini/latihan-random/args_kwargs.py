def jumlahkan(*args):
    """
    Fungsi untuk menjumlahkan semua argumen yang diberikan.
    
    Args:
        *args: Angka-angka yang akan dijumlahkan.
        
    Returns:
        int: Hasil penjumlahan dari semua argumen.
    """
    total = 0
    for angka in args:
        total += angka
    return total

print(jumlahkan(1, 2, 3, 4, 5))
print(jumlahkan(10, 20, 30))

def tampilkan_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

tampilkan_info(nama="John", umur=30, kota="Jakarta")

def format_pesan(pesan, *tambahan, **opsi):
    pesan_format = pesan.upper()
    if "penting" in opsi and opsi["penting"]:
        pesan_format += " (PENTING)" + " ".join(tambahan)
    return pesan_format
print(format_pesan("Ini adalah pesan", "tambahan1", "tambahan2", penting=True))
print(format_pesan("Ini adalah pesan", "tambahan1", "tambahan2"))