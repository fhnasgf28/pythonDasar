def tambah_kegiatan(kegiatan_list):
    while True:
        kegiatan = input("Masukkan nama kegiatan (atau ketik 'selesai' untuk mengakhiri)")
        if kegiatan.lower() == 'selesai':
            break
        try:
            durasi = float(input((f"Masukkan durasi kegiatan '{kegiatan}' dalam jam : ")))
            if durasi < 0:
                print("Durasi tidak boleh negatif. Silakan masukkan nilai yang valid.")
                continue
            kegiatan_list.append((kegiatan, durasi))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar untuk durasi")


def hitung_total_durasi(kegiatan_list):
    total = sum(durasi for _, durasi in kegiatan_list)
    return total

def hitung_persentase(kegiatan_list, total_durasi):
    persentase_list = []
    for kegiatan, durasi in kegiatan_list:
        persentase = (durasi / total_durasi) * 100
        persentase_list.append((kegiatan, persentase))
    return persentase_list

def main():
    kegiatan_list = []
    tambah_kegiatan(kegiatan_list)

    if not kegiatan_list:
        print('Tidak ada kegiatan yang dimasukkan')
        return

    total_durasi = hitung_total_durasi(kegiatan_list)

    print("\nRincian Kegiatan")
    for kegiatan, durasi in kegiatan_list:
        print(f"{kegiatan} : {durasi:.2f} jam")
    print(f"\nTotal Durasi Kegiatan: {total_durasi:.2f} jam")

    print("\nPersentase Kegiatan:")
    for kegiatan, persentase in hitung_persentase(kegiatan_list, total_durasi):
        print(f"{kegiatan}: {persentase:.2f}%")


if __name__ == "__main__":
    main()
