asupan_harian = []


def tambah_asupan(asupan_harian):
    while True:
        makanan = input("Masukkan Nama Makanan ('selesai' untuk berhenti): ").lower()
        if makanan == 'selesai':
            break
        kalori = float(input(f"Masukkan jumlah kalori untuk {makanan}"))
        asupan_harian.append((makanan, kalori))


def hitung_total_kalori(asupan_kalori):
    total_kalori = sum(kalori for makanan, kalori in asupan_kalori)
    return total_kalori


def bandingkan_dengan_target(total_kalori, target_kalori):
    if total_kalori > target_kalori:
        print(f"Anda telah melebihi target kalori harian Anda sebesar {total_kalori - target_kalori:.2f} kalori.")
    elif total_kalori < target_kalori:
        print(f"Anda masih bisa mengkonsumsi {target_kalori - total_kalori:.2f} kalori.")
    else:
        print("Anda telah mencapai target kalori harian Anda.")


def simpan_asupan_ke_file(asupan_harian, nama_file="Asupan_kalori.txt"):
    with open(nama_file, mode='w') as file:
        for makanan, kalori in asupan_harian:
            file.write(f"{makanan}: {kalori} kalori\n")
        total_kalori = hitung_total_kalori(asupan_harian)
        file.write(f"\nTotal kalori: {total_kalori:.2f} kalori\n")
    print(f"Data asupan kalori berhasil disimpan di {nama_file}")

# menjalankan program
def main():
    asupan_harian = []
    target_kalori = float(input("Masukan target kalori harian anda: "))

    print("Penghitung Kalori Harian")
    tambah_asupan(asupan_harian)

    total_kalori = hitung_total_kalori(asupan_harian)
    print(f"\nTotal kalori yang dikonsumsi hari ini: {total_kalori:.2f} kalori")

    bandingkan_dengan_target(total_kalori, target_kalori)

    simpan_asupan_ke_file(asupan_harian)


if __name__ == "__main__":
    main()