#!/usr/bin/env python3
"""
Aplikasi Pengelola Keuangan Sederhana
Untuk mencatat pemasukan, pengeluaran, dan membuat laporan keuangan
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any


class KeuanganManager:
    def __init__(self, filename: str = "data_keuangan.json"):
        self.filename = filename
        self.transaksi = self.load_data()
    
    def load_data(self) -> List[Dict[str, Any]]:
        """Memuat data keuangan dari file JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_data(self):
        """Menyimpan data keuangan ke file JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.transaksi, f, ensure_ascii=False, indent=2)
    
    def tambah_pemasukan(self, jumlah: float, kategori: str, deskripsi: str = ""):
        """Menambahkan transaksi pemasukan"""
        transaksi = {
            'id': len(self.transaksi) + 1,
            'tanggal': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'tipe': 'pemasukan',
            'jumlah': abs(jumlah),  # Pastikan positif
            'kategori': kategori,
            'deskripsi': deskripsi
        }
        self.transaksi.append(transaksi)
        self.save_data()
        print(f"✅ Pemasukan Rp {jumlah:,.0f} berhasil ditambahkan!")
    
    def tambah_pengeluaran(self, jumlah: float, kategori: str, deskripsi: str = ""):
        """Menambahkan transaksi pengeluaran"""
        transaksi = {
            'id': len(self.transaksi) + 1,
            'tanggal': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'tipe': 'pengeluaran',
            'jumlah': abs(jumlah),  # Pastikan positif
            'kategori': kategori,
            'deskripsi': deskripsi
        }
        self.transaksi.append(transaksi)
        self.save_data()
        print(f"✅ Pengeluaran Rp {jumlah:,.0f} berhasil ditambahkan!")
    
    def hitung_saldo(self) -> float:
        """Menghitung total saldo"""
        total_pemasukan = sum(t['jumlah'] for t in self.transaksi if t['tipe'] == 'pemasukan')
        total_pengeluaran = sum(t['jumlah'] for t in self.transaksi if t['tipe'] == 'pengeluaran')
        return total_pemasukan - total_pengeluaran
    
    def tampilkan_ringkasan(self):
        """Menampilkan ringkasan keuangan"""
        total_pemasukan = sum(t['jumlah'] for t in self.transaksi if t['tipe'] == 'pemasukan')
        total_pengeluaran = sum(t['jumlah'] for t in self.transaksi if t['tipe'] == 'pengeluaran')
        saldo = self.hitung_saldo()
        
        print("\n" + "="*50)
        print("📊 RINGKASAN KEUANGAN")
        print("="*50)
        print(f"💰 Total Pemasukan  : Rp {total_pemasukan:,.0f}")
        print(f"💸 Total Pengeluaran: Rp {total_pengeluaran:,.0f}")
        print(f"💳 Saldo Akhir      : Rp {saldo:,.0f}")
        
        if saldo >= 0:
            print("✅ Status: Keuangan Sehat")
        else:
            print("⚠️ Status: Defisit - Perlu Perhatian!")
        print("="*50)
    
    def tampilkan_transaksi(self, limit: int = 10):
        """Menampilkan riwayat transaksi terakhir"""
        if not self.transaksi:
            print("❌ Belum ada transaksi yang tercatat")
            return
        
        print(f"\n📝 RIWAYAT TRANSAKSI (Terakhir {limit})")
        print("-" * 80)
        
        # Ambil transaksi terakhir
        transaksi_terakhir = self.transaksi[-limit:] if len(self.transaksi) > limit else self.transaksi
        
        for t in reversed(transaksi_terakhir):
            icon = "💰" if t['tipe'] == 'pemasukan' else "💸"
            jumlah_str = f"+Rp {t['jumlah']:,.0f}" if t['tipe'] == 'pemasukan' else f"-Rp {t['jumlah']:,.0f}"
            
            print(f"{icon} {t['tanggal']} | {jumlah_str:>15} | {t['kategori']}")
            if t['deskripsi']:
                print(f"     └─ {t['deskripsi']}")
        print("-" * 80)
    
    def laporan_kategori(self):
        """Membuat laporan berdasarkan kategori"""
        if not self.transaksi:
            print("❌ Belum ada data untuk membuat laporan")
            return
        
        # Kelompokkan berdasarkan kategori dan tipe
        kategori_pemasukan = {}
        kategori_pengeluaran = {}
        
        for t in self.transaksi:
            if t['tipe'] == 'pemasukan':
                kategori_pemasukan[t['kategori']] = kategori_pemasukan.get(t['kategori'], 0) + t['jumlah']
            else:
                kategori_pengeluaran[t['kategori']] = kategori_pengeluaran.get(t['kategori'], 0) + t['jumlah']
        
        print("\n" + "="*50)
        print("📊 LAPORAN PER KATEGORI")
        print("="*50)
        
        if kategori_pemasukan:
            print("💰 PEMASUKAN:")
            for kategori, jumlah in sorted(kategori_pemasukan.items(), key=lambda x: x[1], reverse=True):
                print(f"   • {kategori:<20}: Rp {jumlah:,.0f}")
        
        if kategori_pengeluaran:
            print("\n💸 PENGELUARAN:")
            for kategori, jumlah in sorted(kategori_pengeluaran.items(), key=lambda x: x[1], reverse=True):
                print(f"   • {kategori:<20}: Rp {jumlah:,.0f}")
        
        print("="*50)
    
    def hapus_transaksi(self, id_transaksi: int):
        """Menghapus transaksi berdasarkan ID"""
        for i, t in enumerate(self.transaksi):
            if t['id'] == id_transaksi:
                transaksi_terhapus = self.transaksi.pop(i)
                self.save_data()
                print(f"✅ Transaksi ID {id_transaksi} berhasil dihapus!")
                return
        print(f"❌ Transaksi dengan ID {id_transaksi} tidak ditemukan")


def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\n" + "="*50)
    print("💰 APLIKASI PENGELOLA KEUANGAN")
    print("="*50)
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran") 
    print("3. Lihat Ringkasan Keuangan")
    print("4. Lihat Riwayat Transaksi")
    print("5. Laporan per Kategori")
    print("6. Hapus Transaksi")
    print("0. Keluar")
    print("="*50)


def main():
    """Fungsi utama aplikasi"""
    keuangan = KeuanganManager()
    
    print("🎉 Selamat datang di Aplikasi Pengelola Keuangan!")
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("Pilih menu (0-6): ").strip()
            
            if pilihan == "1":
                # Tambah pemasukan
                jumlah = float(input("Masukkan jumlah pemasukan: Rp "))
                kategori = input("Masukkan kategori (misal: Gaji, Bonus, Freelance): ")
                deskripsi = input("Masukkan deskripsi (opsional): ")
                keuangan.tambah_pemasukan(jumlah, kategori, deskripsi)
                
            elif pilihan == "2":
                # Tambah pengeluaran
                jumlah = float(input("Masukkan jumlah pengeluaran: Rp "))
                kategori = input("Masukkan kategori (misal: Makanan, Transport, Tagihan): ")
                deskripsi = input("Masukkan deskripsi (opsional): ")
                keuangan.tambah_pengeluaran(jumlah, kategori, deskripsi)
                
            elif pilihan == "3":
                # Lihat ringkasan
                keuangan.tampilkan_ringkasan()
                
            elif pilihan == "4":
                # Lihat riwayat transaksi
                try:
                    limit = int(input("Berapa transaksi terakhir yang ingin ditampilkan? (default: 10): ") or "10")
                    keuangan.tampilkan_transaksi(limit)
                except ValueError:
                    keuangan.tampilkan_transaksi()
                    
            elif pilihan == "5":
                # Laporan kategori
                keuangan.laporan_kategori()
                
            elif pilihan == "6":
                # Hapus transaksi
                keuangan.tampilkan_transaksi()
                try:
                    id_transaksi = int(input("Masukkan ID transaksi yang ingin dihapus: "))
                    keuangan.hapus_transaksi(id_transaksi)
                except ValueError:
                    print("❌ ID transaksi harus berupa angka")
                    
            elif pilihan == "0":
                print("👋 Terima kasih telah menggunakan Aplikasi Pengelola Keuangan!")
                break
                
            else:
                print("❌ Pilihan tidak valid! Silakan pilih 0-6")
                
        except ValueError:
            print("❌ Input tidak valid! Pastikan memasukkan angka yang benar")
        except KeyboardInterrupt:
            print("\n👋 Aplikasi dihentikan oleh pengguna")
            break
        except Exception as e:
            print(f"❌ Terjadi error: {e}")


if __name__ == "__main__":
    main()