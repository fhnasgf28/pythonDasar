data_pelanggan = {
    "P001": {"nama": "Budi Santoso", "konsumsi_m3": 15},
    "P002": {"nama": "Ani Lestari", "konsumsi_m3": 25},
    "P003": {"nama": "Joko Widodo", "konsumsi_m3": 10},
    "P004": {"nama": "Siti Aminah", "konsumsi_m3": 30}
}

def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None

def hitung_konsumsi_total():
    total_m3 = sum(pelanggan["konsumsi_m3"] for pelanggan in data_pelanggan.values())
    total_km3 = total_m3 / 1000
    return total_m3, total_km3


def main():
    print("=== Sistem Manajemen PDAM ===")
    print("1. Cari Pelanggan")
    print("2. Hitung Total Konsumsi")
    pilihan = input("Pilih opsi (1/2): ")

    if pilihan == "1":
        id_cari = input("Masukkan ID Pelanggan (contoh: P001): ")
        pelanggan = cari_pelanggan(id_cari)
        if pelanggan:
            print(f"Nama: {pelanggan['nama']}")
            print(f"Konsumsi Air: {pelanggan['konsumsi_m3']} m³")
        else:
            print("Pelanggan tidak ditemukan!")

    elif pilihan == "2":
        total_m3, total_km3 = hitung_konsumsi_total()
        print(f"Total Konsumsi Air: {total_m3} m³")
        print(f"Total Konsumsi Air dalam km³: {total_km3:.10f} km³")
    else:
        print("Pilihan tidak valid!")


# Jalankan program
if __name__ == "__main__":
    main()