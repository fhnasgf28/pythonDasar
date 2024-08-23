import csv

pengeluaran = {
    "makan": [],
    "transportasi": [],
    "hiburan": [],
    "lainnya": []
}


def tambah_pengeluaran(pengeluaran):
    while True:
        kategori = input(
            "Masukan Kategori (makan, transportasi, hiburan, lainnya atau 'selesai' untuk berhenti)").lower()
        if kategori == 'selesai':
            break
        if kategori not in pengeluaran:
            print("Kategori tidak valid")
            continue
        jumlah = float(input(f"Masukan jumlah pengeluaran untuk {kategori}:"))
        pengeluaran[kategori].append(jumlah)


def hitung_total(pengeluaran):
    total = {}
    for kategori, list_pengeluaran in pengeluaran.items():
        total[kategori] = sum(list_pengeluaran)
    return total


def simpan_ke_csv(pengeluaran, nama_file="pengeluaran.csv"):
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Kategori", "Total Pengeluaran"])
        for kategori, total in pengeluaran.items():
            writer.writerow([kategori, total])
    print(f"Data pengeluaran berhasil disimpan di {nama_file}")


def saran_penghematan(pengeluaran_total, rata_rata_harian):
    print("\nSaran Penghematan:")
    for kategori, total in pengeluaran_total.items():
        rata_rata = total / 30
        if rata_rata > rata_rata_harian[kategori]:
            print(f"Pertimbangkan untuk mengurangi pengeluaran di kategori {kategori}.")


# menjalankan program
def main():
    pengeluaran = {
        'makan': [],
        'transportasi': [],
        'hiburan': [],
        'lainnya': []
    }

    print("Selamat datang di Manajemen Keuangan Pribadi")

    tambah_pengeluaran(pengeluaran)
    pengeluaran_total = hitung_total(pengeluaran)
    print("\nRingkasan Pengeluaran Bulanan:")
    for kategori, total in pengeluaran_total.items():
        print(f"{kategori.capitalize()}: Rp{total:.2f}")

    simpan_ke_csv(pengeluaran_total)

    rata_rata_harian = {
        'makan': 100000,  # Sesuaikan dengan anggaran harian Anda
        'transportasi': 50000,
        'hiburan': 75000,
        'lainnya': 50000
    }

    saran_penghematan(pengeluaran_total, rata_rata_harian)


if __name__ == "__main__":
    main()