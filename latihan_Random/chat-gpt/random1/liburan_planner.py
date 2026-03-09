class LiburanPlanner:
    def __init__(self, target_biaya, tabungan_awal,tabungan_per_bulan, max_bulan):
        self.target_biaya = target_biaya
        self.tabungan_awal = tabungan_awal
        self.tabungan_per_bulan = tabungan_per_bulan
        self.total_tabungan = tabungan_awal
        self.max_bulan = max_bulan
        self.bulan_dibutuhkan = 0
    
    def hitung_tabungan(self):
        while self.total_tabungan < self.target_biaya and self.bulan_dibutuhkan < self.max_bulan:
            self.total_tabungan += self.tabungan_per_bulan
            self.bulan_dibutuhkan += 1
        
    def status(self):
        self.hitung_tabungan()
        if self.total_tabungan >= self.target_biaya:
            sisa_uang = self.total_tabungan - self.target_biaya
            return {
                "status": "Cukup",
                "bulan_dibutuhkan": self.bulan_dibutuhkan,
                "sisa_uang": sisa_uang
            }
        else:
            kekurangan = self.target_biaya - self.total_tabungan
            return {
                "status": "Tidak Cukup",
                "bulan_dibutuhkan": self.bulan_dibutuhkan,
                "kekurangan": kekurangan
            }
# Contoh penggunaan
if __name__ == "__main__":
    planner = LiburanPlanner(
        target_biaya=10000000,
        tabungan_awal=2000000,
        tabungan_per_bulan=1000000,
        max_bulan=12
    )
    
    hasil = planner.status()
    print(f"Status: {hasil['status']}")
    print(f"Bulan dibutuhkan: {hasil['bulan_dibutuhkan']}")
    
    if hasil['status'] == "Cukup":
        print(f"Sisa uang setelah liburan: {hasil['sisa_uang']}")
    else:
        print(f"Kekurangan untuk liburan: {hasil['kekurangan']}")
