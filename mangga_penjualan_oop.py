"""
Studi Kasus: Sistem Pembelian dan Penjualan Mangga dengan Pendekatan OOP
Author: Student & Antigravity AI
Description: Program untuk mengelola transaksi pembelian (restock dari supplier) dan penjualan (ke pelanggan) buah mangga dengan model OOP.
"""

from datetime import datetime
from typing import List, Dict


class Mangga:
    """Class untuk merepresentasikan produk mangga"""
    
    def __init__(self, kode: str, jenis: str, harga_beli: float, harga_jual: float, stok: int = 0):
        """
        Inisialisasi produk mangga
        
        Args:
            kode: Kode unik mangga (misal: M001)
            jenis: Jenis mangga (misal: Harum Manis)
            harga_beli: Harga beli per kg dari supplier (modal)
            harga_jual: Harga jual per kg ke pelanggan
            stok: Jumlah stok awal dalam kg
        """
        self.kode = kode
        self.jenis = jenis
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual
        self.stok = stok
    
    def kurangi_stok(self, jumlah: int) -> bool:
        """Mengurangi stok mangga ketika ada penjualan"""
        if jumlah <= self.stok:
            self.stok -= jumlah
            return True
        return False
    
    def tambah_stok(self, jumlah: int):
        """Menambah stok mangga ketika ada pembelian dari supplier"""
        self.stok += jumlah
    
    def __str__(self) -> str:
        return f"[{self.kode}] Mangga {self.jenis} - Stok: {self.stok} kg | Harga Beli: Rp {self.harga_beli:,.0f}/kg | Harga Jual: Rp {self.harga_jual:,.0f}/kg"


class Supplier:
    """Class untuk merepresentasikan supplier mangga"""
    
    def __init__(self, id_supplier: str, nama: str, telepon: str = ""):
        self.id_supplier = id_supplier
        self.nama = nama
        self.telepon = telepon
        
    def __str__(self) -> str:
        return f"Supplier ID: {self.id_supplier} | {self.nama} ({self.telepon})"


class Pelanggan:
    """Class untuk merepresentasikan pelanggan"""
    
    def __init__(self, id_pelanggan: str, nama: str, telepon: str = ""):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.telepon = telepon
        self.total_belanja = 0
        
    def tambah_belanja(self, jumlah: float):
        """Mencatat total nominal belanja untuk kalkulasi diskon loyalitas"""
        self.total_belanja += jumlah
        
    def get_diskon_persen(self) -> float:
        """Mendapatkan diskon berdasarkan loyalitas total belanja"""
        if self.total_belanja >= 500000:
            return 0.10  # 10% diskon
        elif self.total_belanja >= 200000:
            return 0.05  # 5% diskon
        return 0.0
        
    def __str__(self) -> str:
        diskon = self.get_diskon_persen() * 100
        return f"Pelanggan ID: {self.id_pelanggan} | {self.nama} | Total Belanja: Rp {self.total_belanja:,.0f} (Diskon Member: {diskon}%)"


class TransaksiPembelian:
    """Class untuk merepresentasikan transaksi pembelian/restok mangga dari Supplier"""
    
    def __init__(self, no_transaksi: str, supplier: Supplier):
        self.no_transaksi = no_transaksi
        self.supplier = supplier
        self.tanggal = datetime.now()
        self.detail_barang: List[Dict] = []
        self.total_pengeluaran = 0
        
    def tambah_barang(self, mangga: Mangga, jumlah: int):
        """Menambahkan mangga yang dibeli dari supplier dan memperbarui stok"""
        mangga.tambah_stok(jumlah)
        total_harga = mangga.harga_beli * jumlah
        self.detail_barang.append({
            'mangga': mangga,
            'jumlah': jumlah,
            'harga_beli': mangga.harga_beli,
            'subtotal': total_harga
        })
        self.total_pengeluaran += total_harga
        
    def cetak_faktur(self) -> str:
        """Mencetak faktur pembelian dari supplier"""
        faktur = "\n" + "="*55 + "\n"
        faktur += "          FAKTUR RESTOK MANGGA (PEMBELIAN)\n"
        faktur += "="*55 + "\n"
        faktur += f"No Transaksi : {self.no_transaksi}\n"
        faktur += f"Tanggal      : {self.tanggal.strftime('%d-%m-%Y %H:%M:%S')}\n"
        faktur += f"Supplier     : {self.supplier.nama}\n"
        faktur += "-"*55 + "\n"
        faktur += f"{'Jenis Mangga':<20} {'Qty (kg)':<10} {'Harga Beli':<12} {'Subtotal':<10}\n"
        faktur += "-"*55 + "\n"
        for item in self.detail_barang:
            m = item['mangga']
            faktur += f"{m.jenis:<20} {item['jumlah']:<10} Rp {item['harga_beli']:>8,.0f} Rp {item['subtotal']:>8,.0f}\n"
        faktur += "-"*55 + "\n"
        faktur += f"{'TOTAL PENGELUARAN:':<32} Rp {self.total_pengeluaran:>10,.0f}\n"
        faktur += "="*55 + "\n"
        return faktur


class TransaksiPenjualan:
    """Class untuk merepresentasikan transaksi penjualan mangga ke Pelanggan"""
    
    def __init__(self, no_transaksi: str, pelanggan: Pelanggan):
        self.no_transaksi = no_transaksi
        self.pelanggan = pelanggan
        self.tanggal = datetime.now()
        self.detail_barang: List[Dict] = []
        self.subtotal = 0
        self.diskon_amount = 0
        self.total_bayar = 0
        self.status = "PENDING"
        
    def tambah_barang(self, mangga: Mangga, jumlah: int) -> bool:
        """Menambahkan mangga yang dibeli pelanggan jika stok mencukupi"""
        if mangga.kurangi_stok(jumlah):
            subtotal_item = mangga.harga_jual * jumlah
            self.detail_barang.append({
                'mangga': mangga,
                'jumlah': jumlah,
                'harga_jual': mangga.harga_jual,
                'subtotal': subtotal_item
            })
            self.subtotal += subtotal_item
            return True
        return False
        
    def hitung_total(self):
        """Menghitung total akhir setelah diskon member"""
        diskon_persen = self.pelanggan.get_diskon_persen()
        self.diskon_amount = self.subtotal * diskon_persen
        self.total_bayar = self.subtotal - self.diskon_amount
        self.status = "SUCCESS"
        
    def cetak_struk(self) -> str:
        """Mencetak struk belanja untuk pelanggan"""
        struk = "\n" + "="*55 + "\n"
        struk += "              NOTA PENJUALAN MANGGA\n"
        struk += "="*55 + "\n"
        struk += f"No Transaksi : {self.no_transaksi}\n"
        struk += f"Tanggal      : {self.tanggal.strftime('%d-%m-%Y %H:%M:%S')}\n"
        struk += f"Pelanggan    : {self.pelanggan.nama}\n"
        struk += "-"*55 + "\n"
        struk += f"{'Jenis Mangga':<20} {'Qty (kg)':<10} {'Harga Jual':<12} {'Subtotal':<10}\n"
        struk += "-"*55 + "\n"
        for item in self.detail_barang:
            m = item['mangga']
            struk += f"{m.jenis:<20} {item['jumlah']:<10} Rp {item['harga_jual']:>8,.0f} Rp {item['subtotal']:>8,.0f}\n"
        struk += "-"*55 + "\n"
        struk += f"{'Subtotal:':<32} Rp {self.subtotal:>10,.0f}\n"
        if self.diskon_amount > 0:
            diskon_p = int(self.pelanggan.get_diskon_persen() * 100)
            struk += f"{f'Diskon Member ({diskon_p}%):':<32} -Rp {self.diskon_amount:>9,.0f}\n"
        struk += "-"*55 + "\n"
        struk += f"{'TOTAL BAYAR:':<32} Rp {self.total_bayar:>10,.0f}\n"
        struk += "="*55 + "\n"
        return struk


class TokoMangga:
    """Class utama untuk mengelola bisnis Toko Mangga"""
    
    def __init__(self, nama_toko: str, modal_awal: float):
        self.nama_toko = nama_toko
        self.kas = modal_awal
        self.daftar_mangga: Dict[str, Mangga] = {}
        self.daftar_supplier: Dict[str, Supplier] = {}
        self.daftar_pelanggan: Dict[str, Pelanggan] = {}
        self.riwayat_pembelian: List[TransaksiPembelian] = []
        self.riwayat_penjualan: List[TransaksiPenjualan] = []
        self.trx_pembelian_counter = 0
        self.trx_penjualan_counter = 0
        
    def tambah_mangga(self, mangga: Mangga):
        self.daftar_mangga[mangga.kode] = mangga
        
    def tambah_supplier(self, supplier: Supplier):
        self.daftar_supplier[supplier.id_supplier] = supplier
        
    def tambah_pelanggan(self, pelanggan: Pelanggan):
        self.daftar_pelanggan[pelanggan.id_pelanggan] = pelanggan
        
    def beli_mangga(self, id_supplier: str, item_list: List[Dict[str, int]]) -> bool:
        """
        Melakukan pembelian/restok mangga dari supplier
        item_list format: [{'kode_mangga': 'M001', 'jumlah': 20}]
        """
        supplier = self.daftar_supplier.get(id_supplier)
        if not supplier:
            print("✗ Supplier tidak ditemukan!")
            return False
            
        self.trx_pembelian_counter += 1
        no_trx = f"BUY-{self.trx_pembelian_counter:05d}"
        transaksi = TransaksiPembelian(no_trx, supplier)
        
        # Hitung total pengeluaran sementara untuk cek kecukupan KAS
        total_sementara = 0
        for item in item_list:
            mangga = self.daftar_mangga.get(item['kode_mangga'])
            if mangga:
                total_sementara += mangga.harga_beli * item['jumlah']
                
        if total_sementara > self.kas:
            print(f"✗ Gagal Restok! Kas Toko tidak cukup. Dibutuhkan: Rp {total_sementara:,.0f}, Kas saat ini: Rp {self.kas:,.0f}")
            return False
            
        # Jalankan restok
        for item in item_list:
            mangga = self.daftar_mangga.get(item['kode_mangga'])
            if mangga:
                transaksi.tambah_barang(mangga, item['jumlah'])
                
        self.kas -= transaksi.total_pengeluaran
        self.riwayat_pembelian.append(transaksi)
        print(transaksi.cetak_faktur())
        return True
        
    def jual_mangga(self, id_pelanggan: str, item_list: List[Dict[str, int]]) -> bool:
        """
        Melakukan penjualan mangga ke pelanggan
        item_list format: [{'kode_mangga': 'M001', 'jumlah': 5}]
        """
        pelanggan = self.daftar_pelanggan.get(id_pelanggan)
        if not pelanggan:
            print("✗ Pelanggan tidak ditemukan!")
            return False
            
        self.trx_penjualan_counter += 1
        no_trx = f"SELL-{self.trx_penjualan_counter:05d}"
        transaksi = TransaksiPenjualan(no_trx, pelanggan)
        
        # Coba tambahkan semua item ke keranjang
        item_berhasil = 0
        for item in item_list:
            mangga = self.daftar_mangga.get(item['kode_mangga'])
            if mangga:
                if transaksi.tambah_barang(mangga, item['jumlah']):
                    item_berhasil += 1
                else:
                    print(f"✗ Gagal menjual {item['jumlah']} kg Mangga {mangga.jenis}. Stok tidak cukup (Sisa: {mangga.stok} kg)")
                    
        if item_berhasil == 0:
            print("✗ Transaksi dibatalkan karena tidak ada item yang mencukupi stok.")
            return False
            
        transaksi.hitung_total()
        self.kas += transaksi.total_bayar
        pelanggan.tambah_belanja(transaksi.total_bayar)
        self.riwayat_penjualan.append(transaksi)
        print(transaksi.cetak_struk())
        return True
        
    def cetak_laporan_keuangan(self):
        """Menampilkan ringkasan keuangan toko"""
        total_pembelian = sum(t.total_pengeluaran for t in self.riwayat_pembelian)
        total_penjualan = sum(t.total_bayar for t in self.riwayat_penjualan)
        # Menghitung keuntungan kotor (berdasarkan HPP barang terjual)
        keuntungan_kotor = 0
        for trx in self.riwayat_penjualan:
            for item in trx.detail_barang:
                mangga = item['mangga']
                keuntungan_kotor += (mangga.harga_jual - mangga.harga_beli) * item['jumlah']
                
        print("\n" + "="*55)
        print(f"       LAPORAN KEUANGAN & KAS - {self.nama_toko}")
        print("="*55)
        print(f"Saldo Kas Toko Saat Ini : Rp {self.kas:>12,.0f}")
        print(f"Total Belanja Supplier  : Rp {total_pembelian:>12,.0f}")
        print(f"Total Penjualan         : Rp {total_penjualan:>12,.0f}")
        print(f"Keuntungan Kotor (Est)  : Rp {keuntungan_kotor:>12,.0f}")
        print("="*55 + "\n")
        
    def cetak_laporan_stok(self):
        """Menampilkan status stok barang saat ini"""
        print("\n" + "="*55)
        print(f"          LAPORAN STOK BARANG - {self.nama_toko}")
        print("="*55)
        print(f"{'Kode':<8} {'Jenis Mangga':<22} {'Stok (kg)':<12} {'Status':<10}")
        print("-"*55)
        for mangga in self.daftar_mangga.values():
            status = "✓ READY" if mangga.stok > 10 else ("⚠ MINIMAL" if mangga.stok > 0 else "✗ HABIS")
            print(f"{mangga.kode:<8} {mangga.jenis:<22} {mangga.stok:<12} {status:<10}")
        print("="*55 + "\n")


# ==================== SIMULASI PROGRAM ====================

if __name__ == "__main__":
    print("=======================================================")
    print("      MEMULAI SIMULASI SISTEM POS TOKO MANGGA OOP      ")
    print("=======================================================")
    
    # 1. Inisialisasi Toko dengan Modal Kas Awal Rp 5.000.000
    toko = TokoMangga("Toko Mangga Segar Jaya", modal_awal=5000000)
    
    # 2. Daftarkan Master Data Jenis Mangga
    # (Stok awal diatur 0, nanti akan di-restok dari supplier)
    toko.tambah_mangga(Mangga("M001", "Harum Manis", harga_beli=18000, harga_jual=25000, stok=0))
    toko.tambah_mangga(Mangga("M002", "Indramayu", harga_beli=12000, harga_jual=18000, stok=0))
    toko.tambah_mangga(Mangga("M003", "Gedong Gincu", harga_beli=25000, harga_jual=35000, stok=0))
    toko.tambah_mangga(Mangga("M004", "Manalagi", harga_beli=14000, harga_jual=20000, stok=0))
    
    # 3. Daftarkan Supplier
    toko.tambah_supplier(Supplier("S001", "Tani Makmur Cirebon", "0812-3456-7890"))
    toko.tambah_supplier(Supplier("S002", "Grosir Buah Indramayu", "0877-6543-2109"))
    
    # 4. Daftarkan Pelanggan
    toko.tambah_pelanggan(Pelanggan("C001", "Farhan Assegaf", "0899-1111-2222"))
    toko.tambah_pelanggan(Pelanggan("C002", "Budi Santoso", "0813-8888-9999"))
    
    # --- PROSES SIMULASI ---
    
    # A. Cek Stok Awal
    toko.cetak_laporan_stok()
    
    # B. Lakukan Restok/Pembelian dari Supplier S001 (Tani Makmur Cirebon)
    print("\n>>> Melakukan restok mangga dari Supplier Tani Makmur...")
    toko.beli_mangga("S001", [
        {'kode_mangga': 'M001', 'jumlah': 100}, # Beli 100kg Harum Manis
        {'kode_mangga': 'M003', 'jumlah': 50},  # Beli 50kg Gedong Gincu
    ])
    
    # C. Lakukan Restok/Pembelian dari Supplier S002
    print("\n>>> Melakukan restok mangga dari Supplier Grosir Buah Indramayu...")
    toko.beli_mangga("S002", [
        {'kode_mangga': 'M002', 'jumlah': 80},  # Beli 80kg Indramayu
        {'kode_mangga': 'M004', 'jumlah': 60},  # Beli 60kg Manalagi
    ])
    
    # Cek Stok & Kas Toko Setelah Restok
    toko.cetak_laporan_stok()
    toko.cetak_laporan_keuangan()
    
    # D. Penjualan ke Pelanggan Pertama (Farhan Assegaf)
    print("\n>>> Transaksi Penjualan ke Farhan Assegaf...")
    toko.jual_mangga("C001", [
        {'kode_mangga': 'M001', 'jumlah': 10}, # Beli 10kg Harum Manis
        {'kode_mangga': 'M003', 'jumlah': 5},  # Beli 5kg Gedong Gincu
    ])
    
    # E. Penjualan ke Pelanggan Kedua (Budi Santoso)
    print("\n>>> Transaksi Penjualan ke Budi Santoso...")
    toko.jual_mangga("C002", [
        {'kode_mangga': 'M002', 'jumlah': 15}, # Beli 15kg Indramayu
        {'kode_mangga': 'M004', 'jumlah': 20}, # Beli 20kg Manalagi
    ])
    
    # F. Penjualan Kedua ke Farhan Assegaf (Sekarang dia punya riwayat loyalitas belanja dan berhak dapat diskon)
    print("\n>>> Transaksi Penjualan Kedua ke Farhan Assegaf (Mendapatkan Diskon Member)...")
    # Cek status loyalitas Farhan sebelum belanja
    print(toko.daftar_pelanggan["C001"])
    toko.jual_mangga("C001", [
        {'kode_mangga': 'M001', 'jumlah': 15}, # Beli 15kg Harum Manis
        {'kode_mangga': 'M003', 'jumlah': 10}, # Beli 10kg Gedong Gincu
    ])
    
    # G. Laporan Akhir
    toko.cetak_laporan_stok()
    toko.cetak_laporan_keuangan()
