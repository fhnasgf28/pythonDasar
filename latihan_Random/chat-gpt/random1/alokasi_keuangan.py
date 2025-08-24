def alokasi_keuangan(gaji_bulanan):
    kebutuhan_pokok = gaji_bulanan * 0.5
    keinginan = gaji_bulanan * 0.3
    tabungan_investasi = gaji_bulanan * 0.2

    hasil = {
        "Kebutuhan Pokok": kebutuhan_pokok,
        "Keinginan": keinginan,
        "Tabungan & Investasi": tabungan_investasi,
    }

    return hasil

def simulasi_kekayaan(gaji_bulanan, tahun, bunga_tahunan=0.05):
    alokasi = alokasi_keuangan(gaji_bulanan)
    tabungan_bulanan = alokasi["Tabungan & Investasi"]

    total_tabungan = 0
    for i in range(tahun * 12):
        total_tabungan += tabungan_bulanan
        #menerapkan bunga manjemuk bulanan
        total_tabungan *= (1 + bunga_tahunan / 12)

    return total_tabungan
def tampilkan_alokasi(gaji_bulanan):
    alokasi = alokasi_keuangan(gaji_bulanan)
    print("\nHasil alokasi keuangan:")
    print(f"Gaji Bulanan: Rp {gaji_bulanan:.2f}")
    print(f"Kebutuhan Pokok: Rp {alokasi['Kebutuhan Pokok']:.2f}")
    print(f"Keinginan: Rp {alokasi['Keinginan']:.2f}")
    print(f"Tabungan & Investasi: Rp {alokasi['Tabungan & Investasi']:.2f}")
    for kategori, jumlah in alokasi.items():
        print(f"{kategori}: Rp {jumlah:.2f}")

if __name__ == "__main__":
    try:
        gaji_bulanan = float(input("Masukkan gaji bulanan Anda: Rp "))
        tampilkan_alokasi(gaji_bulanan)
        tahun_simulasi = 5
        bunga_tahunan = 0.08
        hasil_simulasi = simulasi_kekayaan(gaji_bulanan, tahun_simulasi, bunga_tahunan)
        print(f"\nPerkiraan total tabungan setelah {tahun_simulasi} tahun (bunga {bunga_tahunan*100:.0f}%): Rp{hasil_simulasi:,.0f}")
    except ValueError:
        print("Harap masukkan angka yang valid.")