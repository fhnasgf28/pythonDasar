"""
Study Kasus: Sistem Penjualan Kopi dengan Pendekatan OOP
Author: Student
Description: Program untuk mengelola penjualan kopi dengan fitur inventory, customer, dan transaksi
"""

from datetime import datetime
from typing import List, Dict


class Kopi:
    """Class untuk merepresentasikan produk kopi"""
    
    def __init__(self, kode: str, nama: str, harga: float, stok: int):
        """
        Inisialisasi produk kopi
        
        Args:
            kode: Kode unik kopi
            nama: Nama jenis kopi
            harga: Harga per cup
            stok: Jumlah stok tersedia
        """
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def kurangi_stok(self, jumlah: int) -> bool:
        """Mengurangi stok kopi"""
        if jumlah <= self.stok:
            self.stok -= jumlah
            return True
        return False
    
    def tambah_stok(self, jumlah: int):
        """Menambah stok kopi"""
        self.stok += jumlah
    
    def __str__(self) -> str:
        return f"{self.nama} (Rp {self.harga:,.0f}) - Stok: {self.stok}"


class Pelanggan:
    """Class untuk merepresentasikan pelanggan"""
    
    def __init__(self, id_pelanggan: str, nama: str, email: str = ""):
        """
        Inisialisasi pelanggan
        
        Args:
            id_pelanggan: ID unik pelanggan
            nama: Nama pelanggan
            email: Email pelanggan (optional)
        """
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email
        self.total_pembelian = 0
        self.riwayat_transaksi: List[Dict] = []
    
    def tambah_pembelian(self, jumlah: float):
        """Menambah total pembelian pelanggan"""
        self.total_pembelian += jumlah
    
    def tambah_transaksi(self, transaksi: Dict):
        """Mencatat transaksi ke riwayat"""
        self.riwayat_transaksi.append(transaksi)
    
    def get_diskon(self) -> float:
        """Mendapatkan persentase diskon berdasarkan total pembelian"""
        if self.total_pembelian >= 500000:
            return 0.15  # 15%
        elif self.total_pembelian >= 300000:
            return 0.10  # 10%
        elif self.total_pembelian >= 100000:
            return 0.05  # 5%
        return 0  # Tidak ada diskon
    
    def __str__(self) -> str:
        diskon = self.get_diskon() * 100
        return f"ID: {self.id_pelanggan} | {self.nama} | Total Belanja: Rp {self.total_pembelian:,.0f} | Diskon: {diskon}%"


class Transaksi:
    """Class untuk merepresentasikan transaksi penjualan"""
    
    def __init__(self, no_transaksi: str, pelanggan: Pelanggan):
        """
        Inisialisasi transaksi
        
        Args:
            no_transaksi: Nomor unik transaksi
            pelanggan: Object Pelanggan yang melakukan pembelian
        """
        self.no_transaksi = no_transaksi
        self.pelanggan = pelanggan
        self.tanggal = datetime.now()
        self.detail_pembelian: List[Dict] = []
        self.subtotal = 0
        self.diskon_amount = 0
        self.total_bayar = 0
    
    def tambah_item(self, kopi: Kopi, jumlah: int) -> bool:
        """
        Menambahkan item kopi ke transaksi
        
        Args:
            kopi: Object Kopi yang dibeli
            jumlah: Jumlah cup yang dibeli
            
        Returns:
            True jika berhasil, False jika stok tidak cukup
        """
        if kopi.kurangi_stok(jumlah):
            harga_total = kopi.harga * jumlah
            self.detail_pembelian.append({
                'kopi': kopi.nama,
                'kode': kopi.kode,
                'jumlah': jumlah,
                'harga_satuan': kopi.harga,
                'total': harga_total
            })
            self.subtotal += harga_total
            return True
        return False
    
    def hitung_total(self):
        """Menghitung total dengan diskon pelanggan"""
        diskon_persen = self.pelanggan.get_diskon()
        self.diskon_amount = self.subtotal * diskon_persen
        self.total_bayar = self.subtotal - self.diskon_amount
    
    def cetak_struk(self) -> str:
        """Mengembalikan string struk transaksi"""
        struk = "\n" + "="*50 + "\n"
        struk += "           STRUK PEMBELIAN KOPI\n"
        struk += "="*50 + "\n"
        struk += f"No Transaksi: {self.no_transaksi}\n"
        struk += f"Tanggal: {self.tanggal.strftime('%d-%m-%Y %H:%M:%S')}\n"
        struk += f"Pelanggan: {self.pelanggan.nama}\n"
        struk += "-"*50 + "\n"
        struk += f"{'Item':<20} {'Qty':<5} {'Harga':<10} {'Total':<10}\n"
        struk += "-"*50 + "\n"
        
        for item in self.detail_pembelian:
            struk += f"{item['kopi']:<20} {item['jumlah']:<5} Rp {item['harga_satuan']:>8,.0f} Rp {item['total']:>8,.0f}\n"
        
        struk += "-"*50 + "\n"
        struk += f"{'Subtotal:':<35} Rp {self.subtotal:>8,.0f}\n"
        
        if self.diskon_amount > 0:
            diskon_persen = self.pelanggan.get_diskon() * 100
            struk += f"{'Diskon ('+ str(int(diskon_persen)) +'%):':<35} -Rp {self.diskon_amount:>7,.0f}\n"
        
        struk += "-"*50 + "\n"
        struk += f"{'TOTAL BAYAR:':<35} Rp {self.total_bayar:>8,.0f}\n"
        struk += "="*50 + "\n"
        
        return struk


class TokoKopi:
    """Class untuk merepresentasikan toko kopi (management system)"""
    
    def __init__(self, nama_toko: str):
        """
        Inisialisasi toko kopi
        
        Args:
            nama_toko: Nama toko kopi
        """
        self.nama_toko = nama_toko
        self.daftar_kopi: Dict[str, Kopi] = {}
        self.daftar_pelanggan: Dict[str, Pelanggan] = {}
        self.daftar_transaksi: List[Transaksi] = []
        self.no_transaksi_counter = 0
    
    def tambah_kopi(self, kopi: Kopi):
        """Menambahkan jenis kopi ke toko"""
        self.daftar_kopi[kopi.kode] = kopi
        print(f"✓ Kopi '{kopi.nama}' berhasil ditambahkan")
    
    def tambah_pelanggan(self, pelanggan: Pelanggan):
        """Menambahkan pelanggan baru"""
        self.daftar_pelanggan[pelanggan.id_pelanggan] = pelanggan
        print(f"✓ Pelanggan '{pelanggan.nama}' berhasil terdaftar")
    
    def ambil_pelanggan(self, id_pelanggan: str) -> Pelanggan:
        """Mengambil data pelanggan berdasarkan ID"""
        return self.daftar_pelanggan.get(id_pelanggan)
    
    def ambil_kopi(self, kode_kopi: str) -> Kopi:
        """Mengambil data kopi berdasarkan kode"""
        return self.daftar_kopi.get(kode_kopi)
    
    def buat_transaksi(self, id_pelanggan: str) -> Transaksi:
        """Membuat transaksi baru"""
        self.no_transaksi_counter += 1
        no_transaksi = f"TRX-{self.no_transaksi_counter:05d}"
        pelanggan = self.ambil_pelanggan(id_pelanggan)
        
        if pelanggan:
            transaksi = Transaksi(no_transaksi, pelanggan)
            return transaksi
        return None
    
    def selesaikan_transaksi(self, transaksi: Transaksi):
        """Menyelesaikan transaksi dan menyimpannya"""
        if transaksi and len(transaksi.detail_pembelian) > 0:
            transaksi.hitung_total()
            self.daftar_transaksi.append(transaksi)
            transaksi.pelanggan.tambah_pembelian(transaksi.total_bayar)
            transaksi.pelanggan.tambah_transaksi({
                'no_transaksi': transaksi.no_transaksi,
                'tanggal': transaksi.tanggal,
                'total': transaksi.total_bayar
            })
            print(transaksi.cetak_struk())
        else:
            print("✗ Transaksi tidak valid atau tidak ada item")
    
    def laporan_penjualan(self):
        """Menampilkan laporan penjualan"""
        total_penjualan = sum(t.total_bayar for t in self.daftar_transaksi)
        print("\n" + "="*50)
        print(f"LAPORAN PENJUALAN - {self.nama_toko}")
        print("="*50)
        print(f"Total Transaksi: {len(self.daftar_transaksi)}")
        print(f"Total Penjualan: Rp {total_penjualan:,.0f}")
        print("="*50 + "\n")
    
    def laporan_stok(self):
        """Menampilkan laporan stok kopi"""
        print("\n" + "="*50)
        print(f"LAPORAN STOK - {self.nama_toko}")
        print("="*50)
        for kopi in self.daftar_kopi.values():
            status = "✓ OK" if kopi.stok > 0 else "✗ HABIS"
            print(f"{kopi.nama:<20} | Stok: {kopi.stok:>3} | {status}")
        print("="*50 + "\n")
    
    def laporan_pelanggan_setia(self):
        """Menampilkan laporan pelanggan setia"""
        pelanggan_sorted = sorted(
            self.daftar_pelanggan.values(),
            key=lambda p: p.total_pembelian,
            reverse=True
        )
        print("\n" + "="*50)
        print("LAPORAN PELANGGAN SETIA")
        print("="*50)
        for i, pelanggan in enumerate(pelanggan_sorted, 1):
            print(f"{i}. {pelanggan}")
        print("="*50 + "\n")


# ==================== DEMO PROGRAM ====================

def main():
    """Fungsi utama untuk demo program"""
    
    # Inisialisasi toko
    toko = TokoKopi("Kopi Nusantara")
    
    # Tambah jenis kopi
    print("📦 Menambahkan jenis kopi...\n")
    toko.tambah_kopi(Kopi("K001", "Arabika Premium", 35000, 50))
    toko.tambah_kopi(Kopi("K002", "Robusta Kuat", 25000, 75))
    toko.tambah_kopi(Kopi("K003", "Espresso", 30000, 40))
    toko.tambah_kopi(Kopi("K004", "Cappuccino", 40000, 30))
    
    # Tambah pelanggan
    print("\n👥 Mendaftarkan pelanggan...\n")
    toko.tambah_pelanggan(Pelanggan("P001", "Budi Santoso", "budi@email.com"))
    toko.tambah_pelanggan(Pelanggan("P002", "Siti Nurhaliza", "siti@email.com"))
    toko.tambah_pelanggan(Pelanggan("P003", "Ahmad Hidayat", "ahmad@email.com"))
    
    # Transaksi 1
    print("\n🛒 TRANSAKSI 1")
    print("-" * 50)
    transaksi1 = toko.buat_transaksi("P001")
    transaksi1.tambah_item(toko.ambil_kopi("K001"), 3)
    transaksi1.tambah_item(toko.ambil_kopi("K004"), 2)
    toko.selesaikan_transaksi(transaksi1)
    
    # Transaksi 2
    print("\n🛒 TRANSAKSI 2")
    print("-" * 50)
    transaksi2 = toko.buat_transaksi("P002")
    transaksi2.tambah_item(toko.ambil_kopi("K002"), 5)
    transaksi2.tambah_item(toko.ambil_kopi("K003"), 3)
    toko.selesaikan_transaksi(transaksi2)
    
    # Transaksi 3
    print("\n🛒 TRANSAKSI 3")
    print("-" * 50)
    transaksi3 = toko.buat_transaksi("P001")
    transaksi3.tambah_item(toko.ambil_kopi("K001"), 2)
    toko.selesaikan_transaksi(transaksi3)
    
    # Transaksi 4
    print("\n🛒 TRANSAKSI 4")
    print("-" * 50)
    transaksi4 = toko.buat_transaksi("P003")
    transaksi4.tambah_item(toko.ambil_kopi("K004"), 10)
    transaksi4.tambah_item(toko.ambil_kopi("K001"), 5)
    toko.selesaikan_transaksi(transaksi4)
    
    # Laporan
    toko.laporan_stok()
    toko.laporan_penjualan()
    toko.laporan_pelanggan_setia()


if __name__ == "__main__":
    main()
