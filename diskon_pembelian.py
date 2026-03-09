def hitung_diskon(total_harga, persentase_diskon):
    diskon = total_harga * (persentase_diskon / 100)
    harga_setelah_diskon = total_harga - diskon
    return harga_setelah_diskon


total_harga_barang = 100000
persentase_diskon = 20
harga_setelah_diskon = hitung_diskon(total_harga_barang, persentase_diskon)
print(f"Harga setelah diskon: Rp.{harga_setelah_diskon:.2f}")


def hitung_jenis_diskon(jenis_barang, total_harga):
    if jenis_barang == 'Elektronik':
        persentase_diskon = 10
    elif jenis_barang == 'Pakaian':
        persentase_diskon = 20
    else:
        persentase_diskon = 5

    diskon = total_harga * (persentase_diskon / 100)
    harga_setelah_diskon = total_harga - diskon
    return harga_setelah_diskon


total_harga_barang = 200
jenis_barang = 'Elektronik'
harga_setelah_diskon = hitung_jenis_diskon(jenis_barang, total_harga_barang)
print(f'Harga {jenis_barang} setelah diskon: RP.{harga_setelah_diskon:.2f}')

# menghitung diskon berdasarkan Jumlah barang:
def hitung_diskon_jumlah_barang(jumlah_barang, harga_per_barang):
    if jumlah_barang >= 10:
        persentase_diskon = 15
    else:
        persentase_diskon = 5

    total_harga = jumlah_barang * harga_per_barang
    diskon = total_harga * (persentase_diskon / 100)
    harga_sebelum_diskon = total_harga + diskon
    harga_setelah_diskon = total_harga - diskon
    return harga_setelah_diskon, harga_sebelum_diskon

harga_per_barang = 100000
jumlah_barang = 12
harga_setelah_diskon, harga_sebelum_diskon = hitung_diskon_jumlah_barang(jumlah_barang, harga_per_barang)
print(f"Harga {jumlah_barang} barang setelah diskon: ${harga_setelah_diskon:.2f}")
print(f"Harga {jumlah_barang} barang sebelum diskon: ${harga_sebelum_diskon:.2f}")

