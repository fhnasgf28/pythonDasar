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