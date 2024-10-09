def estimasi_biaya_turing(jarak, konsumsi_bbm, harga_bbm, biaya_akomodasi, biaya_makan, jumlah_hari):
    # hitung total bahan bakar yang dibutuhkan (liter)
    total_bbm = jarak / konsumsi_bbm
    # hitung biaya bahan bakar (rupiah)
    biaya_bbm = total_bbm * harga_bbm
    # hitung biaya akomodasi total (rupiah)
    biaya_akomodasi_total = biaya_akomodasi * (jumlah_hari - 1)
    # hitung biaya makanan total (rupiah)
    biaya_makanan_total = biaya_makan * jumlah_hari
    # hitung estimasi biaya perjalanan total
    total_biaya = biaya_bbm + biaya_akomodasi_total + biaya_makanan_total

    return total_biaya

# Input dari user
jarak = float(input("Masukkan jarak perjalanan (km): "))
konsumsi_bbm = float(input("Masukkan konsumsi bahan bakar (km/liter): "))
harga_bbm = float(input("Masukkan harga bahan bakar per liter (Rp): "))
biaya_akomodasi = float(input("Masukkan biaya akomodasi per malam (Rp): "))
biaya_makanan = float(input("Masukkan biaya makanan per hari (Rp): "))
jumlah_hari = int(input("Masukkan jumlah hari perjalanan: "))

# hitung estimasi biaya
total_biaya = estimasi_biaya_turing(jarak,konsumsi_bbm, harga_bbm, biaya_akomodasi, biaya_makanan, jumlah_hari)

# tampilkan hasil estimasi
print(f"\nEstimasi total biaya perjalanan: Rp {total_biaya:,.0f}")