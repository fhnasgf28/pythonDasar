"""
Study Kasus: Sistem Pembelian Kopi
Deskripsi: Program untuk mengelola pembelian kopi dengan berbagai pilihan
          menu, ukuran, dan tambahan toppings.
"""

# ============================================================================
# DATA KOPI YANG TERSEDIA
# ============================================================================

MENU_KOPI = {
    "1": {"nama": "Espresso", "harga": 15000},
    "2": {"nama": "Americano", "harga": 18000},
    "3": {"nama": "Cappuccino", "harga": 22000},
    "4": {"nama": "Latte", "harga": 25000},
    "5": {"nama": "Macchiato", "harga": 20000},
    "6": {"nama": "Mocha", "harga": 28000},
}

UKURAN_KOPI = {
    "S": {"nama": "Small (250ml)", "tambahan": 0},
    "M": {"nama": "Medium (350ml)", "tambahan": 3000},
    "L": {"nama": "Large (500ml)", "tambahan": 5000},
}

TOPPINGS = {
    "1": {"nama": "Whipped Cream", "harga": 5000},
    "2": {"nama": "Chocolate Syrup", "harga": 3000},
    "3": {"nama": "Caramel", "harga": 3000},
    "4": {"nama": "Vanilla", "harga": 2000},
    "5": {"nama": "Extra Espresso Shot", "harga": 7000},
}

DISKON = {
    "member": 0.10,  # 10% diskon untuk member
    "student": 0.15,  # 15% diskon untuk pelajar
}


# ============================================================================
# KELAS PEMBELIAN KOPI
# ============================================================================

class PembelianKopi:
    """Class untuk mengelola pembelian kopi"""
    
    def __init__(self, nama_pelanggan, adalah_member=False, adalah_pelajar=False):
        self.nama_pelanggan = nama_pelanggan
        self.adalah_member = adalah_member
        self.adalah_pelajar = adalah_pelajar
        self.pesanan = []
        self.total_harga = 0
    
    def tampilkan_menu_kopi(self):
        """Menampilkan menu kopi yang tersedia"""
        print("\n" + "="*50)
        print("📋 MENU KOPI TERSEDIA")
        print("="*50)
        for kode, kopi in MENU_KOPI.items():
            print(f"{kode}. {kopi['nama']:<20} Rp {kopi['harga']:>8,.0f}")
        print("="*50)
    
    def tampilkan_pilihan_ukuran(self):
        """Menampilkan pilihan ukuran kopi"""
        print("\n" + "="*50)
        print("📏 PILIHAN UKURAN")
        print("="*50)
        for kode, ukuran in UKURAN_KOPI.items():
            tambahan_text = f" (+Rp {ukuran['tambahan']:,.0f})" if ukuran['tambahan'] > 0 else " (Standar)"
            print(f"{kode}. {ukuran['nama']}{tambahan_text}")
        print("="*50)
    
    def tampilkan_pilihan_toppings(self):
        """Menampilkan pilihan toppings"""
        print("\n" + "="*50)
        print("🍫 PILIHAN TOPPINGS (Opsional)")
        print("="*50)
        for kode, topping in TOPPINGS.items():
            print(f"{kode}. {topping['nama']:<25} Rp {topping['harga']:>8,.0f}")
        print("0. Tidak ada topping")
        print("="*50)
    
    def pesan_kopi(self):
        """Proses pemesanan kopi"""
        self.tampilkan_menu_kopi()
        
        # Pilih jenis kopi
        kode_kopi = input("Pilih nomor kopi: ").strip()
        if kode_kopi not in MENU_KOPI:
            print("❌ Kopi tidak valid!")
            return False
        
        kopi = MENU_KOPI[kode_kopi]
        
        # Pilih ukuran
        self.tampilkan_pilihan_ukuran()
        kode_ukuran = input("Pilih ukuran (S/M/L): ").strip().upper()
        if kode_ukuran not in UKURAN_KOPI:
            print("❌ Ukuran tidak valid!")
            return False
        
        ukuran = UKURAN_KOPI[kode_ukuran]
        
        # Pilih toppings
        self.tampilkan_pilihan_toppings()
        toppings_dipilih = []
        harga_toppings = 0
        
        while True:
            kode_topping = input("Pilih topping (0 untuk selesai): ").strip()
            if kode_topping == "0":
                break
            if kode_topping not in TOPPINGS:
                print("❌ Topping tidak valid!")
                continue
            
            topping = TOPPINGS[kode_topping]
            toppings_dipilih.append(topping["nama"])
            harga_toppings += topping["harga"]
        
        # Hitung subtotal
        harga_kopi = kopi["harga"] + ukuran["tambahan"] + harga_toppings
        
        # Buat detail pesanan
        detail_pesanan = {
            "kopi": kopi["nama"],
            "ukuran": ukuran["nama"],
            "toppings": toppings_dipilih if toppings_dipilih else ["Tidak ada"],
            "harga_kopi": kopi["harga"],
            "harga_ukuran": ukuran["tambahan"],
            "harga_toppings": harga_toppings,
            "subtotal": harga_kopi
        }
        
        self.pesanan.append(detail_pesanan)
        self.total_harga += harga_kopi
        
        print(f"\n✅ {kopi['nama']} ({ukuran['nama']}) ditambahkan ke pesanan!")
        print(f"   Harga: Rp {harga_kopi:,.0f}")
        
        return True
    
    def tambah_pesanan_lagi(self):
        """Tanya apakah ingin pesan lagi"""
        jawab = input("\nIngin pesan lagi? (y/n): ").strip().lower()
        return jawab == 'y'
    
    def hitung_diskon(self):
        """Menghitung diskon berdasarkan kategori pelanggan"""
        diskon_persen = 0
        alasan_diskon = []
        
        if self.adalah_member:
            diskon_persen += DISKON["member"]
            alasan_diskon.append("Member")
        
        if self.adalah_pelajar:
            diskon_persen += DISKON["student"]
            alasan_diskon.append("Pelajar")
        
        return diskon_persen, alasan_diskon
    
    def tampilkan_struk(self):
        """Menampilkan struk pembelian"""
        print("\n" + "="*60)
        print("☕ STRUK PEMBELIAN KOPI ☕")
        print("="*60)
        
        print(f"Nama Pelanggan: {self.nama_pelanggan}")
        print(f"Status: ", end="")
        status = []
        if self.adalah_member:
            status.append("Member")
        if self.adalah_pelajar:
            status.append("Pelajar")
        print(", ".join(status) if status else "Reguler")
        
        print("\n" + "-"*60)
        print("DETAIL PESANAN:")
        print("-"*60)
        
        for i, pesanan in enumerate(self.pesanan, 1):
            print(f"\n{i}. {pesanan['kopi']} - {pesanan['ukuran']}")
            print(f"   Harga Kopi: Rp {pesanan['harga_kopi']:>10,.0f}")
            if pesanan['harga_ukuran'] > 0:
                print(f"   Tambahan Ukuran: Rp {pesanan['harga_ukuran']:>6,.0f}")
            
            if pesanan['harga_toppings'] > 0:
                print(f"   Toppings: {', '.join(pesanan['toppings'])}")
                print(f"   Harga Toppings: Rp {pesanan['harga_toppings']:>8,.0f}")
            
            print(f"   Subtotal: Rp {pesanan['subtotal']:>12,.0f}")
        
        print("\n" + "-"*60)
        print(f"Total Sebelum Diskon: Rp {self.total_harga:>12,.0f}")
        
        # Hitung dan tampilkan diskon
        diskon_persen, alasan_diskon = self.hitung_diskon()
        
        if diskon_persen > 0:
            jumlah_diskon = self.total_harga * diskon_persen
            total_bayar = self.total_harga - jumlah_diskon
            print(f"Diskon ({', '.join(alasan_diskon)}): -{diskon_persen*100:.0f}% (Rp {jumlah_diskon:>8,.0f})")
        else:
            total_bayar = self.total_harga
            print("Diskon: Tidak ada")
        
        print("-"*60)
        print(f"🎯 TOTAL BAYAR: Rp {total_bayar:>22,.0f}")
        print("="*60)
        
        return total_bayar
    
    def proses_pembayaran(self, jumlah_bayar):
        """Proses pembayaran"""
        while True:
            try:
                jumlah_dibayar = float(input(f"\nJumlah uang yang dibayarkan: Rp "))
                
                if jumlah_dibayar < jumlah_bayar:
                    kurang = jumlah_bayar - jumlah_dibayar
                    print(f"❌ Uang kurang! Kurangnya Rp {kurang:,.0f}")
                    continue
                
                kembalian = jumlah_dibayar - jumlah_bayar
                print(f"\n✅ Pembayaran berhasil!")
                print(f"Kembalian: Rp {kembalian:,.0f}")
                
                return True
            
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka.")


# ============================================================================
# FUNGSI UTAMA
# ============================================================================

def main():
    """Fungsi utama program"""
    print("\n" + "="*60)
    print("🎉 SELAMAT DATANG DI KEDAI KOPI KAMI 🎉")
    print("="*60)
    
    # Input data pelanggan
    nama_pelanggan = input("\nMasukkan nama Anda: ").strip()
    
    is_member = input("Apakah Anda member? (y/n): ").strip().lower() == 'y'
    is_pelajar = input("Apakah Anda pelajar/mahasiswa? (y/n): ").strip().lower() == 'y'
    
    # Buat objek pembelian
    pembelian = PembelianKopi(nama_pelanggan, is_member, is_pelajar)
    
    # Proses pemesanan
    while True:
        if not pembelian.pesan_kopi():
            continue
        
        if not pembelian.tambah_pesanan_lagi():
            break
    
    # Validasi ada pesanan
    if not pembelian.pesanan:
        print("\n❌ Tidak ada pesanan! Program dihentikan.")
        return
    
    # Tampilkan struk
    total_bayar = pembelian.tampilkan_struk()
    
    # Proses pembayaran
    pembelian.proses_pembayaran(total_bayar)
    
    print("\n" + "="*60)
    print("Terima kasih telah berbelanja di kedai kami! 😊")
    print("Nikmati kopi Anda! ☕")
    print("="*60 + "\n")


# ============================================================================
# JALANKAN PROGRAM
# ============================================================================

if __name__ == "__main__":
    main()
