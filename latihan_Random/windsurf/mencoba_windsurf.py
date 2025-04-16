def tambah_ke_list(daftar, element):
    """Fungsi untuk menambahkan element ke dalam list"""
    daftar.append(element)
    return daftar

def buat_list(n):
    """Fungsi untuk membuat list dengan n buah element"""
    daftar = []
    for i in range(n):
        daftar = tambah_ke_list(daftar, i)
    return daftar

if __name__ == "__main__":
    n = int(input("Masukkan jumlah element: "))
    hasil = buat_list(n)
    print(hasil)