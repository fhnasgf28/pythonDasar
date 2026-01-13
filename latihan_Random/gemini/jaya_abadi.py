def hitunng_product_loop(daftar_angka):
    if not daftar_angka:
        return 1
    
    product = 1 
    for angka in daftar_angka:
        product *= angka
    return product

# contoh penggunaan 
angka1 = [1,2,3,4,5,6,7,8]
print(f"daftar angka: {angka1}")
print(f"Product (hasil kali) menggunakan loop {hitunng_product_loop(angka1)}")

def hitung_product_dari_input_pengguna():
    input_str = input("masukkan angka-angka (pisahkan dengan spasi, misal 10,5,)")
    str_angka = input_str.split()
    angka_valid = []
    for s in str_angka:
        try:
            angka_valid.append(float(s))
        except ValueError:
            print(f"Peringatan: '{s}'")
    
    if not angka_valid:
        print("Tidak ada angka valid yang dimasukkan. Product dianggap 1")
        return 1 
    
    product_akhir = hitunng_product_loop(angka_valid)