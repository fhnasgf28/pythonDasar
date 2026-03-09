# input data

modal_awal = float(input("Masukkan modal awal: "))
harga_beli = float(input("Masukkan harga beli: "))
harga_jual = float(input("Masukkan harga jual: "))
target_penjualan_per_hari = float(input("Masukkan target penjualan per hari: "))

# kalkulasi
keuntungan_per_tabung = harga_jual - harga_beli
jumlah_tabung = int(modal_awal // harga_beli)
total_keuntungan = jumlah_tabung * keuntungan_per_tabung
bep_tabung = modal_awal // keuntungan_per_tabung
hari_bep = bep_tabung / target_penjualan_per_hari

# output
print("Jumlah tabung yang dibeli:", jumlah_tabung)
print("Keuntungan per tabung:", keuntungan_per_tabung)
print("Total keuntungan:", total_keuntungan)
print("BEP per tabung:", bep_tabung)
print("Hari BEP:", hari_bep)
print("Total keuntungan per hari:", total_keuntungan / hari_bep)