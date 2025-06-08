def hitung_kebebasan_finansial(pengeluaran_bulanan, faktor=25):
    pengeluaran_tahunan = pengeluaran_bulanan * 12
    target_kebebasan_finansial = pengeluaran_tahunan * faktor

    return target_kebebasan_finansial


# Contoh penggunaan
pengeluaran_bulanan = float(input("Masukkan pengeluaran bulanan: "))
target_kebebasan_finansial = hitung_kebebasan_finansial(pengeluaran_bulanan)
print(f"Target kebebasan finansial: Rp {target_kebebasan_finansial:,.0f}")