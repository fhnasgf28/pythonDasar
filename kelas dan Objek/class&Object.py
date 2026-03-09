class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
    
    def tampilkan_info(self):
        print(f"namanya {self.nama}")
        print(f"nimnya {self.nim}")
        print(f"ipknya {self.ipk}")

    def hitung_ipk(self):
        # implementasi untuk menghitung ipk
        pass

mahasiswa1 = Mahasiswa("Farhan", "1910631170019", 3.8)
mahasiswa2 = Mahasiswa("Muhammad Farhan", "1910631170019", 3.5)

mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()