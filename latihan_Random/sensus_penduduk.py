class Penduduk:
    def __init__(self, nama, umur, jenis_kelamin, pekerjaan, kota):
        self.nama = nama
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin
        self.pekerjaan = pekerjaan
        self.kota = kota
    
    def __str__(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Jenis Kelamin: {self.jenis_kelamin}, Pekerjaan: {self.pekerjaan}, Kota: {self.kota}"


class SensusPenduduk:
    def __init__(self):
        self.daftar_penduduk = []
    
    def tambah_penduduk(self, penduduk):
        self.daftar_penduduk.append(penduduk)
        print(f"Penduduk {penduduk.nama} telah ditambahkan.")
        print(f"Total penduduk saat ini: {len(self.daftar_penduduk)}")
        print(f"Daftar penduduk: {self.daftar_penduduk}")
    
    def tampilkan_penduduk(self):
        if not self.daftar_penduduk:
            print("Tidak ada penduduk yang terdaftar.")
        else:
            print("Daftar Penduduk:")
            for penduduk in self.daftar_penduduk:
                print(penduduk)
    
    def statistik(self):
        total = len(self.daftar_penduduk)
        if total == 0:
            print("Tidak ada penduduk yang terdaftar.")
            return
        
        total_umur = sum(penduduk.umur for penduduk in self.daftar_penduduk if penduduk.umur is not None)
        rata_rata_umur = total_umur / total if total_umur > 0 else 0
        print(f"Total penduduk: {total}")
        print(f"Rata-rata umur penduduk: {rata_rata_umur:.2f}")
        jumlah_laki = sum(1 for penduduk in self.daftar_penduduk if penduduk.jenis_kelamin == "Laki-laki")
        jumlah_wanita = total - jumlah_laki
        print(f"Jumlah Laki-laki: {jumlah_laki}")
        print(f"Jumlah Wanita: {jumlah_wanita}")

        print("\nStatistik:")
        print(f"Total penduduk      : {total}")
        print(f"Rata-rata umur      : {rata_rata_umur:.2f} tahun")
        print(f"Jumlah pria         : {jumlah_laki}")
        print(f"Jumlah wanita       : {jumlah_wanita}")

# Contoh penggunaan
if __name__ == "__main__":
    sensus = SensusPenduduk()
    
    # Menambahkan penduduk
    penduduk1 = Penduduk("John Doe", 30, "Laki-laki", "Programmer", "Jakarta")
    penduduk2 = Penduduk("Jane Smith", 25, "Perempuan", "Dokter", "Bandung")
    
    sensus.tambah_penduduk(penduduk1)
    sensus.tambah_penduduk(penduduk2)
    
    # Menampilkan daftar penduduk
    sensus.tampilkan_penduduk()
    
    # Menampilkan statistik
    sensus.statistik()