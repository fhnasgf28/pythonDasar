# fungsi untuk menghitung total biaya anggaran
def hitung_anggaran(sewa_lokasi, katering_per_orang, jumlah_orang, dekorasi, hiburan, transportasi, biaya_tak_terduga):
    # menghitung biaya katering
    total_katering = katering_per_orang * jumlah_orang
    # menghitung total anggaran
    total_anggaran = sewa_lokasi + total_katering + dekorasi + hiburan + transportasi + biaya_tak_terduga
    return total_anggaran

def cetak_laporan_anggaran(sewa_lokasi, katering_per_orang, jumlah_orang, dekorasi, hiburan, transportasi, biaya_tak_terduga):
    total_katering = katering_per_orang * jumlah_orang
    total_anggaran = hitung_anggaran(sewa_lokasi, katering_per_orang, jumlah_orang, dekorasi, hiburan,transportasi,biaya_tak_terduga)

    print("====== Laporan Anggaran Acara ======")
    print(f"Sewa Lokasi          : Rp {sewa_lokasi:,}")
    print(f"Katering ({jumlah_orang} orang) : Rp {total_katering:,} (Rp {katering_per_orang:,} per orang)")
    print(f"Dekorasi             : Rp {dekorasi:,}")
    print(f"Hiburan              : Rp {hiburan:,}")
    print(f"Transportasi         : Rp {transportasi:,}")
    print(f"Biaya Tak Terduga    : Rp {biaya_tak_terduga:,}")
    print("------------------------------------")
    print(f"Total Anggaran       : Rp {total_anggaran:,}")

# input data anggaran dari user
sewa_lokasi = int(input("Masukkan biaya sewa lokasi: Rp "))
katering_per_orang = int(input("Masukkan biaya katering per orang: Rp "))
jumlah_orang = int(input("Masukkan jumlah peserta: "))
dekorasi = int(input("Masukkan biaya dekorasi: Rp "))
hiburan = int(input("Masukkan biaya hiburan: Rp: "))
transportasi = int(input("Masukkan biaya transportasi: Rp :"))
biaya_tak_terduga = int(input("Masukkan biaya tak terduga: "))

# cetak laporan anggaran
cetak_laporan_anggaran(sewa_lokasi, katering_per_orang, jumlah_orang, dekorasi, hiburan, transportasi, biaya_tak_terduga)