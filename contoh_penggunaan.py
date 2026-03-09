#!/usr/bin/env python3
"""
Contoh Penggunaan Class KeuanganManager
Demonstrasi cara menggunakan fitur-fitur pengelola keuangan
"""

from keuangan import KeuanganManager

def demo_penggunaan():
    """Contoh penggunaan aplikasi keuangan"""
    print("🎯 Demo Penggunaan Aplikasi Keuangan\n")
    
    # Membuat instance KeuanganManager
    keuangan = KeuanganManager("demo_keuangan.json")
    
    # Menambahkan beberapa transaksi pemasukan
    print("📈 Menambahkan Pemasukan...")
    keuangan.tambah_pemasukan(5000000, "Gaji", "Gaji bulan Januari")
    keuangan.tambah_pemasukan(1500000, "Freelance", "Proyek website")
    keuangan.tambah_pemasukan(500000, "Bonus", "Bonus kinerja")
    
    # Menambahkan beberapa transaksi pengeluaran
    print("\n📉 Menambahkan Pengeluaran...")
    keuangan.tambah_pengeluaran(1200000, "Sewa", "Sewa rumah bulanan")
    keuangan.tambah_pengeluaran(800000, "Makanan", "Belanja groceries")
    keuangan.tambah_pengeluaran(300000, "Transport", "Bensin dan parkir")
    keuangan.tambah_pengeluaran(150000, "Hiburan", "Nonton film dan makan")
    
    # Menampilkan ringkasan
    keuangan.tampilkan_ringkasan()
    
    # Menampilkan riwayat transaksi
    keuangan.tampilkan_transaksi()
    
    # Menampilkan laporan per kategori
    keuangan.laporan_kategori()

def contoh_perhitungan_manual():
    """Contoh perhitungan keuangan manual menggunakan fungsi terpisah"""
    print("\n" + "="*50)
    print("🧮 CONTOH PERHITUNGAN MANUAL")
    print("="*50)
    
    # Data contoh
    pemasukan = [
        {"nama": "Gaji", "jumlah": 5000000},
        {"nama": "Freelance", "jumlah": 2000000},
        {"nama": "Investasi", "jumlah": 500000}
    ]
    
    pengeluaran = [
        {"nama": "Sewa", "jumlah": 1500000},
        {"nama": "Makanan", "jumlah": 1000000},
        {"nama": "Transport", "jumlah": 400000},
        {"nama": "Hiburan", "jumlah": 300000}
    ]
    
    # Perhitungan
    total_pemasukan = sum(item["jumlah"] for item in pemasukan)
    total_pengeluaran = sum(item["jumlah"] for item in pengeluaran)
    saldo = total_pemasukan - total_pengeluaran
    
    # Menampilkan hasil
    print("💰 PEMASUKAN:")
    for item in pemasukan:
        print(f"   • {item['nama']:<15}: Rp {item['jumlah']:,.0f}")
    print(f"   {'TOTAL PEMASUKAN':<15}: Rp {total_pemasukan:,.0f}")
    
    print("\n💸 PENGELUARAN:")
    for item in pengeluaran:
        print(f"   • {item['nama']:<15}: Rp {item['jumlah']:,.0f}")
    print(f"   {'TOTAL PENGELUARAN':<15}: Rp {total_pengeluaran:,.0f}")
    
    print(f"\n💳 SALDO AKHIR: Rp {saldo:,.0f}")
    
    # Analisis persentase
    print(f"\n📊 ANALISIS:")
    print(f"   • Tingkat Tabungan: {(saldo/total_pemasukan)*100:.1f}%")
    
    # Rekomendasi
    if saldo > 0:
        if (saldo/total_pemasukan) >= 0.2:
            print("   ✅ Keuangan sangat sehat! Tingkat tabungan di atas 20%")
        elif (saldo/total_pemasukan) >= 0.1:
            print("   ✅ Keuangan sehat! Tingkat tabungan di atas 10%")
        else:
            print("   ⚠️ Keuangan cukup sehat, tapi bisa ditingkatkan")
    else:
        print("   🚨 Defisit! Perlu mengurangi pengeluaran atau menambah pemasukan")

def tips_keuangan():
    """Tips mengelola keuangan"""
    print("\n" + "="*50)
    print("💡 TIPS MENGELOLA KEUANGAN")
    print("="*50)
    
    tips = [
        "📝 Catat semua pemasukan dan pengeluaran secara rutin",
        "🎯 Buat anggaran bulanan dan patuhi batas yang ditetapkan", 
        "💰 Terapkan aturan 50-30-20: 50% kebutuhan, 30% keinginan, 20% tabungan",
        "🔍 Review pengeluaran bulanan untuk menemukan area penghematan",
        "💳 Hindari utang konsumtif dan prioritaskan melunasi utang",
        "📈 Mulai investasi meskipun dengan nominal kecil",
        "🎯 Tetapkan tujuan keuangan jangka pendek dan panjang",
        "🆘 Siapkan dana darurat minimal 3-6 bulan pengeluaran"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")
    
    print("="*50)

if __name__ == "__main__":
    # Jalankan demo
    demo_penggunaan()
    
    # Contoh perhitungan manual
    contoh_perhitungan_manual()
    
    # Tips keuangan
    tips_keuangan()
    
    print("\n🎉 Demo selesai! Anda bisa menjalankan 'python keuangan.py' untuk menggunakan aplikasi interaktif.")