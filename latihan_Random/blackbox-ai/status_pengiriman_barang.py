status_pengiriman = {
    "1": "Pengiriman sedang diproses",
    "2": "Pengiriman sedang dalam perjalanan",
    "3": "Pengiriman telah samapi",
    "4": "Pengiriman gagal",
}

data_pengiriman = {}


def cek_status(no_resi):
    # simulasikan status pengiriman berdasarkan no resi
    if no_resi == '1234567':
        return status_pengiriman['2']
    elif no_resi == "780909":
        return status_pengiriman['3']
    else:
        return status_pengiriman['1']


def tambah_pengiriman(no_resi, tanggal_pengiriman, estimasi_pengiriman, ):
    #tambahkan data pengiriman ke kamus
    data_pengiriman[no_resi] = {
        "tanggal_pengiriman": tanggal_pengiriman,
        "estimasi_waktu": estimasi_pengiriman,
        "status_pengiriman": cek_status(no_resi)
    }

def tampilkan_pengiriman(no_resi):
    #tampilkan data pengiriman
    if no_resi in data_pengiriman:
        print(f"No, Resi: {no_resi}")
        print(f"Tanggal Pengiriman: {data_pengiriman[no_resi]['tanggal_pengiriman']}")
        print(f"Estimasi Waktu Pengiriman: {data_pengiriman[no_resi]['estimasi_waktu']}")
        print(f"Status Pengiriman: {data_pengiriman[no_resi]['status_pengiriman']}")
    else:
        print("No Resi tidak ditemukan")


def main():
    print("Selamat datang di sistem pelacakan pengiriman")
    while True:
        print("1. Tambah pengiriman")
        print("2. Tampilkan pengiriman")
        print("3. Keluar")
        pilihan = input("Pilih Menu:/t")
        if pilihan =='1':
            no_resi = input("Masukkan nomor resi pengirimn: ")
            tanggal_pengiriman = input("Masukkan tanggal pengiriman (YYY-MM-DD): ")
            estimasi_pengiriman = input("Masukan estimasi waktu pengiriman (hari):")
            tambah_pengiriman(no_resi, tanggal_pengiriman, estimasi_pengiriman)
        elif pilihan =='2':
            no_resi = input("Masukkan nomor resi pengiriman: ")
            tampilkan_pengiriman(no_resi)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
