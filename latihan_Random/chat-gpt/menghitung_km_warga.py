import json

# nama file untuk menyimpan data

file_data = "data_rumah.json"

def muat_data():
    try:
        with open(file_data, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def simpan_data(data):
    with open(file_data, "w") as file:
        json.dump(data, file, indent=4)

def hitung_penggunaan_km(pembacaan_sekarang, pembacaan_sebelumnya):
    return pembacaan_sekarang - pembacaan_sebelumnya

def tambah_data_rumah(data_rumah, nomor_rumah, pembacaan_sekarang, pembacaan_sebelumnya):
    data_rumah.append({
        "nomor_rumah": nomor_rumah,
        "pembacaan_sekarang": pembacaan_sekarang,
        "pembacaan_sebelumnya": pembacaan_sebelumnya
    })

def laporan_penggunaan_km(data_rumah):
    for rumah in data_rumah:
        penggunaan = hitung_penggunaan_km(rumah["pembacaan_sekarang"], rumah["pembacaan_sebelumnya"])
        print(f"Nomor Rumah: {rumah['nomor_rumah']}, Penggunaan: {penggunaan} KM")

def main():
    data_rumah = muat_data()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Rumah")
        print("2. Laporan Penggunaan KM")
        print("3. Keluar")

        pilihan = input("Pilihan: ")

        if pilihan == "1":
            nomor_rumah = input("Nomor Rumah: ")
            pembacaan_sekarang = int(input("Pembacaan Sekarang: "))
            pembacaan_sebelumnya = int(input("Pembacaan Sebelumnya: "))
            tambah_data_rumah(data_rumah, nomor_rumah, pembacaan_sekarang, pembacaan_sebelumnya)
            simpan_data(data_rumah)
            print("Data Rumah berhasil ditambahkan.")
        elif pilihan == "2":
            laporan_penggunaan_km(data_rumah)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()

