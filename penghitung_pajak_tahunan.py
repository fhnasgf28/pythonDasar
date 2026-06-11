"""
Study Kasus: Penghitung Pajak Tahunan (PPh 21)
Deskripsi: Program untuk menghitung Pajak Penghasilan (PPh 21) tahunan
          berdasarkan gaji bulanan dengan perhitungan yang sesuai dengan
          peraturan pajak Indonesia.
"""

# ============================================================================
# KONSTANTA PERHITUNGAN PAJAK
# ============================================================================

# Biaya Jabatan / Pengurang Penghasilan Bruto
BIAYA_JABATAN_PERSEN = 0.05  # 5% dari gaji bruto, max Rp 6.000.000 per tahun
BIAYA_JABATAN_MAX = 6_000_000

# Penghasilan Tidak Kena Pajak (PTKP) per tahun 2024
PTKP = {
    "TK": 54_450_000,           # Tidak kawin
    "TK+1": 58_050_000,         # Tidak kawin + 1 anak
    "TK+2": 61_650_000,         # Tidak kawin + 2 anak
    "TK+3": 65_250_000,         # Tidak kawin + 3 anak
    "K": 58_050_000,            # Kawin
    "K+1": 61_650_000,          # Kawin + 1 anak
    "K+2": 65_250_000,          # Kawin + 2 anak
    "K+3": 68_850_000,          # Kawin + 3 anak
}

# Tarif Pajak Progresif (Tarif Pasal 17 UU PPh)
TARIF_PAJAK = [
    (60_000_000, 0.05),         # Sampai 60 juta: 5%
    (250_000_000, 0.15),        # 60 juta - 250 juta: 15%
    (500_000_000, 0.25),        # 250 juta - 500 juta: 25%
    (float('inf'), 0.30),       # Di atas 500 juta: 30%
]

# Iuran Jaminan Sosial
IURAN_JKK = 0.0024             # Jaminan Kecelakaan Kerja: 0.24% dari gaji
IURAN_JHT = 0.02               # Jaminan Hari Tua: 2% dari gaji
IURAN_JP = 0.01                # Jaminan Pensiun: 1% dari gaji
IURAN_JKPM = 0.003             # Jaminan Kematian: 0.3% dari gaji


# ============================================================================
# KELAS PENGHITUNG PAJAK
# ============================================================================

class PenghitungPajakTahunan:
    """Class untuk menghitung pajak tahunan (PPh 21)"""
    
    def __init__(self, gaji_bulanan, status_perkawinan="TK", jumlah_anak=0):
        """
        Inisialisasi penghitung pajak
        
        Args:
            gaji_bulanan (float): Gaji bulanan dalam rupiah
            status_perkawinan (str): Status perkawinan ("TK" atau "K")
            jumlah_anak (int): Jumlah anak yang ditanggung
        """
        self.gaji_bulanan = gaji_bulanan
        self.status_perkawinan = status_perkawinan
        self.jumlah_anak = jumlah_anak
        self.gaji_tahunan = gaji_bulanan * 12
        
        # Tentukan kode PTKP
        self.kode_ptkp = self._tentukan_kode_ptkp()
        self.ptkp_nilai = PTKP.get(self.kode_ptkp, PTKP["TK"])
    
    def _tentukan_kode_ptkp(self):
        """Menentukan kode PTKP berdasarkan status perkawinan dan anak"""
        if self.status_perkawinan == "TK":
            if self.jumlah_anak == 0:
                return "TK"
            elif self.jumlah_anak == 1:
                return "TK+1"
            elif self.jumlah_anak == 2:
                return "TK+2"
            else:
                return "TK+3"
        else:  # Kawin
            if self.jumlah_anak == 0:
                return "K"
            elif self.jumlah_anak == 1:
                return "K+1"
            elif self.jumlah_anak == 2:
                return "K+2"
            else:
                return "K+3"
    
    def hitung_biaya_jabatan(self):
        """Menghitung biaya jabatan (pengurang penghasilan bruto)"""
        biaya = self.gaji_tahunan * BIAYA_JABATAN_PERSEN
        return min(biaya, BIAYA_JABATAN_MAX)
    
    def hitung_penghasilan_neto(self):
        """Menghitung penghasilan neto (bruto - biaya jabatan)"""
        biaya_jabatan = self.hitung_biaya_jabatan()
        return self.gaji_tahunan - biaya_jabatan
    
    def hitung_pkp(self):
        """Menghitung Penghasilan Kena Pajak (PKP)"""
        penghasilan_neto = self.hitung_penghasilan_neto()
        pkp = penghasilan_neto - self.ptkp_nilai
        return max(pkp, 0)  # PKP tidak bisa negatif
    
    def hitung_pajak_progressive(self, pkp):
        """
        Menghitung pajak dengan sistem progresif
        
        Args:
            pkp (float): Penghasilan Kena Pajak
            
        Returns:
            float: Total pajak yang harus dibayar
        """
        total_pajak = 0
        sisa_pkp = pkp
        
        for batas, tarif in TARIF_PAJAK:
            if sisa_pkp <= 0:
                break
            
            # Hitung pajak untuk bracket ini
            pajak_bracket = min(sisa_pkp, batas) * tarif
            total_pajak += pajak_bracket
            sisa_pkp -= batas
        
        return total_pajak
    
    def hitung_pph_21(self):
        """Menghitung PPh 21 tahunan"""
        pkp = self.hitung_pkp()
        return self.hitung_pajak_progressive(pkp)
    
    def hitung_iuran_jaminan_sosial(self):
        """Menghitung total iuran jaminan sosial karyawan"""
        iuran = {
            "JKK": self.gaji_tahunan * IURAN_JKK,
            "JHT": self.gaji_tahunan * IURAN_JHT,
            "JP": self.gaji_tahunan * IURAN_JP,
            "JKPM": self.gaji_tahunan * IURAN_JKPM,
        }
        iuran["Total"] = sum(iuran.values())
        return iuran
    
    def hitung_gaji_bersih(self):
        """Menghitung gaji bersih setelah pajak dan iuran sosial"""
        pph_21 = self.hitung_pph_21()
        iuran_sosial = self.hitung_iuran_jaminan_sosial()
        gaji_bersih = self.gaji_tahunan - pph_21 - iuran_sosial["Total"]
        return gaji_bersih
    
    def hitung_gaji_bersih_bulanan(self):
        """Menghitung gaji bersih per bulan"""
        return self.hitung_gaji_bersih() / 12
    
    def tampilkan_laporan_pajak(self):
        """Menampilkan laporan pajak lengkap"""
        biaya_jabatan = self.hitung_biaya_jabatan()
        penghasilan_neto = self.hitung_penghasilan_neto()
        pkp = self.hitung_pkp()
        pph_21 = self.hitung_pph_21()
        iuran_sosial = self.hitung_iuran_jaminan_sosial()
        gaji_bersih = self.hitung_gaji_bersih()
        gaji_bersih_bulanan = self.hitung_gaji_bersih_bulanan()
        
        print("\n" + "="*70)
        print("📊 LAPORAN PERHITUNGAN PAJAK TAHUNAN (PPh 21)")
        print("="*70)
        
        # Bagian 1: Data Karyawan
        print("\n📋 DATA KARYAWAN:")
        print("-"*70)
        print(f"Gaji Bulanan: Rp {self.gaji_bulanan:>18,.0f}")
        print(f"Gaji Tahunan: Rp {self.gaji_tahunan:>18,.0f}")
        print(f"Status Perkawinan: {self.status_perkawinan} | Jumlah Anak: {self.jumlah_anak}")
        print(f"Kode PTKP: {self.kode_ptkp} | Nilai PTKP: Rp {self.ptkp_nilai:>12,.0f}")
        
        # Bagian 2: Perhitungan Penghasilan Kena Pajak
        print("\n" + "-"*70)
        print("📈 PERHITUNGAN PENGHASILAN KENA PAJAK (PKP):")
        print("-"*70)
        print(f"Penghasilan Bruto: Rp {self.gaji_tahunan:>18,.0f}")
        print(f"Biaya Jabatan (5%, max 6juta): -{biaya_jabatan:>16,.0f}")
        print(f"{'─' * 70}")
        print(f"Penghasilan Neto: Rp {penghasilan_neto:>18,.0f}")
        print(f"PTKP ({self.kode_ptkp}): -{self.ptkp_nilai:>17,.0f}")
        print(f"{'─' * 70}")
        print(f"Penghasilan Kena Pajak (PKP): Rp {pkp:>13,.0f}")
        
        # Bagian 3: Perhitungan Pajak
        print("\n" + "-"*70)
        print("💰 PERHITUNGAN PAJAK (Tarif Progresif):")
        print("-"*70)
        
        # Tunjukkan perhitungan per bracket
        sisa_pkp = pkp
        untuk_ditampilkan = []
        
        for batas, tarif in TARIF_PAJAK:
            if sisa_pkp <= 0:
                break
            
            pajak_bracket = min(sisa_pkp, batas) * tarif
            dasar_pajak = min(sisa_pkp, batas)
            
            untuk_ditampilkan.append((dasar_pajak, tarif, pajak_bracket))
            sisa_pkp -= batas
        
        for dasar, tarif, pajak in untuk_ditampilkan:
            print(f"Rp {dasar:>10,.0f} × {tarif*100:>5.0f}% = Rp {pajak:>12,.0f}")
        
        print(f"{'─' * 70}")
        print(f"PPh 21 Tahunan: Rp {pph_21:>18,.0f}")
        
        # Bagian 4: Iuran Jaminan Sosial
        print("\n" + "-"*70)
        print("🛡️ IURAN JAMINAN SOSIAL KARYAWAN:")
        print("-"*70)
        print(f"JKK (0.24%): Rp {iuran_sosial['JKK']:>19,.0f}")
        print(f"JHT (2.00%): Rp {iuran_sosial['JHT']:>19,.0f}")
        print(f"JP (1.00%): Rp {iuran_sosial['JP']:>20,.0f}")
        print(f"JKPM (0.30%): Rp {iuran_sosial['JKPM']:>18,.0f}")
        print(f"{'─' * 70}")
        print(f"Total Iuran Sosial: Rp {iuran_sosial['Total']:>12,.0f}")
        
        # Bagian 5: Ringkasan Gaji Bersih
        print("\n" + "-"*70)
        print("💵 RINGKASAN GAJI BERSIH:")
        print("-"*70)
        print(f"Gaji Tahunan: Rp {self.gaji_tahunan:>18,.0f}")
        print(f"PPh 21: -{pph_21:>25,.0f}")
        print(f"Iuran Sosial: -{iuran_sosial['Total']:>24,.0f}")
        print(f"{'─' * 70}")
        print(f"Gaji Bersih Tahunan: Rp {gaji_bersih:>11,.0f}")
        print(f"Gaji Bersih Bulanan: Rp {gaji_bersih_bulanan:>11,.0f}")
        
        print("\n" + "="*70)
        
        # Return data untuk laporan
        return {
            "gaji_tahunan": self.gaji_tahunan,
            "biaya_jabatan": biaya_jabatan,
            "ptkp": self.ptkp_nilai,
            "pkp": pkp,
            "pph_21": pph_21,
            "iuran_sosial": iuran_sosial["Total"],
            "gaji_bersih_tahunan": gaji_bersih,
            "gaji_bersih_bulanan": gaji_bersih_bulanan,
        }


# ============================================================================
# FUNGSI UTAMA
# ============================================================================

def main():
    """Fungsi utama program"""
    print("\n" + "="*70)
    print("🧮 KALKULATOR PAJAK TAHUNAN (PPh 21)")
    print("="*70)
    
    # Input data dari pengguna
    print("\n📝 MASUKKAN DATA ANDA:")
    print("-"*70)
    
    while True:
        try:
            gaji_bulanan = float(input("Gaji Bulanan (Rp): "))
            if gaji_bulanan <= 0:
                print("❌ Gaji harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka.")
    
    print("\nStatus Perkawinan:")
    print("1. TK (Tidak Kawin)")
    print("2. K (Kawin)")
    status_input = input("Pilih (1/2): ").strip()
    status = "TK" if status_input == "1" else "K"
    
    while True:
        try:
            jumlah_anak = int(input("\nJumlah Anak yang Ditanggung (0-3): "))
            if 0 <= jumlah_anak <= 3:
                break
            else:
                print("❌ Jumlah anak harus 0-3!")
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka.")
    
    # Buat objek penghitung pajak
    penghitung = PenghitungPajakTahunan(gaji_bulanan, status, jumlah_anak)
    
    # Tampilkan laporan
    data = penghitung.tampilkan_laporan_pajak()
    
    # Opsi untuk menampilkan laporan lain
    print("\n" + "-"*70)
    print("🔄 OPSI LAINNYA:")
    print("-"*70)
    print(f"Gaji Bruto Per Bulan: Rp {gaji_bulanan:>15,.0f}")
    print(f"Gaji Bersih Per Bulan: Rp {data['gaji_bersih_bulanan']:>13,.0f}")
    
    print("\nTerima kasih telah menggunakan kalkulator pajak kami! 😊")
    print("="*70 + "\n")


# ============================================================================
# CONTOH PENGGUNAAN DENGAN GAJI 7 JUTA
# ============================================================================

def contoh_gaji_7_juta():
    """Contoh perhitungan dengan gaji 7 juta per bulan"""
    print("\n" + "="*70)
    print("📊 CONTOH PERHITUNGAN GAJI 7 JUTA PER BULAN")
    print("="*70)
    
    # Scenario 1: TK (Tidak Kawin)
    print("\n" + "─"*70)
    print("Scenario 1: Tidak Kawin (TK)")
    print("─"*70)
    penghitung1 = PenghitungPajakTahunan(7_000_000, "TK", 0)
    penghitung1.tampilkan_laporan_pajak()
    
    # Scenario 2: Kawin + 2 Anak
    print("\n" + "─"*70)
    print("Scenario 2: Kawin + 2 Anak (K+2)")
    print("─"*70)
    penghitung2 = PenghitungPajakTahunan(7_000_000, "K", 2)
    penghitung2.tampilkan_laporan_pajak()


# ============================================================================
# JALANKAN PROGRAM
# ============================================================================

if __name__ == "__main__":
    # Tanyakan pengguna ingin mode apa
    print("\n" + "="*70)
    print("🎯 PILIH MODE:")
    print("="*70)
    print("1. Input Gaji Manual")
    print("2. Lihat Contoh Gaji 7 Juta")
    
    pilihan = input("\nPilih (1/2): ").strip()
    
    if pilihan == "2":
        contoh_gaji_7_juta()
    else:
        main()
