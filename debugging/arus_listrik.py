# Program untuk Menghitung Arus Listrik pada Rumah
# Menggunakan Hukum Ohm: I = V / R
# Atau menggunakan Daya: I = P / V

class KalkulatorArusListrik:
    """Kelas untuk menghitung arus listrik pada rumah"""
    
    def __init__(self):
        self.perangkat = []
    
    def hitung_arus_dari_tegangan_dan_hambatan(self, tegangan, hambatan):
        """
        Hitung arus menggunakan Hukum Ohm: I = V / R
        Args:
            tegangan (float): Tegangan dalam Volt (V)
            hambatan (float): Hambatan dalam Ohm (Ω)
        Returns:
            float: Arus dalam Ampere (A)
        """
        if hambatan == 0:
            raise ValueError("Hambatan tidak boleh 0!")
        return tegangan / hambatan
    
    def hitung_arus_dari_daya_dan_tegangan(self, daya, tegangan):
        """
        Hitung arus menggunakan rumus daya: I = P / V
        Args:
            daya (float): Daya dalam Watt (W)
            tegangan (float): Tegangan dalam Volt (V)
        Returns:
            float: Arus dalam Ampere (A)
        """
        if tegangan == 0:
            raise ValueError("Tegangan tidak boleh 0!")
        return daya / tegangan
    
    def hitung_daya(self, tegangan, arus):
        """
        Hitung daya: P = V × I
        Args:
            tegangan (float): Tegangan dalam Volt (V)
            arus (float): Arus dalam Ampere (A)
        Returns:
            float: Daya dalam Watt (W)
        """
        return tegangan * arus
    
    def tambah_perangkat(self, nama, daya):
        """
        Tambahkan perangkat listrik ke daftar
        Args:
            nama (str): Nama perangkat
            daya (float): Daya perangkat dalam Watt (W)
        """
        self.perangkat.append({'nama': nama, 'daya': daya})
        print(f"✓ Perangkat '{nama}' ditambahkan (Daya: {daya}W)")
    
    def hitung_total_daya_rumah(self):
        """Hitung total daya semua perangkat dalam rumah"""
        total_daya = sum(p['daya'] for p in self.perangkat)
        return total_daya
    
    def hitung_arus_total_rumah(self, tegangan=220):
        """
        Hitung total arus rumah
        Args:
            tegangan (float): Tegangan rumah dalam Volt (default: 220V)
        Returns:
            float: Total arus dalam Ampere (A)
        """
        total_daya = self.hitung_total_daya_rumah()
        return self.hitung_arus_dari_daya_dan_tegangan(total_daya, tegangan)
    
    def tampilkan_laporan(self, tegangan=220):
        """Tampilkan laporan lengkap arus listrik rumah"""
        print("\n" + "="*50)
        print("LAPORAN ARUS LISTRIK RUMAH")
        print("="*50)
        
        if not self.perangkat:
            print("❌ Belum ada perangkat yang ditambahkan!")
            return
        
        print("\nDaftar Perangkat:")
        print("-" * 50)
        for i, p in enumerate(self.perangkat, 1):
            arus_perangkat = self.hitung_arus_dari_daya_dan_tegangan(p['daya'], tegangan)
            print(f"{i}. {p['nama']:<20} | Daya: {p['daya']:>6}W | Arus: {arus_perangkat:>6.2f}A")
        
        print("-" * 50)
        total_daya = self.hitung_total_daya_rumah()
        total_arus = self.hitung_arus_total_rumah(tegangan)
        
        print(f"\nTegangan Rumah: {tegangan}V")
        print(f"Total Daya: {total_daya}W ({total_daya/1000:.2f}kW)")
        print(f"Total Arus: {total_arus:.2f}A")
        print("="*50 + "\n")


# ============================================
# CONTOH PENGGUNAAN
# ============================================

if __name__ == "__main__":
    # Buat kalkulator
    kalkulator = KalkulatorArusListrik()
    
    # Tambahkan perangkat-perangkat rumah
    perangkat_rumah = [
        ("Lampu Ruang Tamu", 100),
        ("AC 1 PK", 1000),
        ("Kulkas", 500),
        ("TV", 150),
        ("Pemanas Air", 800),
        ("Mesin Cuci", 400),
        ("Laptop", 100),
        ("Charger HP", 25),
    ]
    
    for nama, daya in perangkat_rumah:
        kalkulator.tambah_perangkat(nama, daya)
    
    # Tampilkan laporan dengan tegangan 220V (standar Indonesia)
    kalkulator.tampilkan_laporan(tegangan=220)
    
    # Contoh perhitungan manual
    print("\n" + "="*50)
    print("CONTOH PERHITUNGAN MANUAL")
    print("="*50)
    
    # Contoh 1: Hitung arus dari Ohm's Law
    print("\n1. Menggunakan Hukum Ohm (I = V/R):")
    tegangan = 220  # Volt
    hambatan = 10   # Ohm
    arus = kalkulator.hitung_arus_dari_tegangan_dan_hambatan(tegangan, hambatan)
    print(f"   Tegangan: {tegangan}V, Hambatan: {hambatan}Ω")
    print(f"   Arus: {arus:.2f}A")
    
    # Contoh 2: Hitung arus dari Daya
    print("\n2. Menggunakan Rumus Daya (I = P/V):")
    daya = 2200  # Watt
    tegangan = 220  # Volt
    arus = kalkulator.hitung_arus_dari_daya_dan_tegangan(daya, tegangan)
    print(f"   Daya: {daya}W, Tegangan: {tegangan}V")
    print(f"   Arus: {arus:.2f}A")
    
    # Contoh 3: Hitung Daya
    print("\n3. Menghitung Daya (P = V × I):")
    tegangan = 220  # Volt
    arus = 5  # Ampere
    daya = kalkulator.hitung_daya(tegangan, arus)
    print(f"   Tegangan: {tegangan}V, Arus: {arus}A")
    print(f"   Daya: {daya}W ({daya/1000:.2f}kW)")
    
    print("\n" + "="*50)
