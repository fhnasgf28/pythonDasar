import json
import os

file_pengiriman = "pengiriman_barang.json"

def load_data():
    if os.path.exists(file_pengiriman):
        with open(file_pengiriman, 'r') as file:
            return json.load(file)
    return[]

# simpan data pengiriman ke file json 
def save_data(data):
    with open(file_pengiriman, 'w') as file:
        json.dump(data, file, indent=4)

# data pengiriman
pengiriman = load_data()
def tambah_pengiriman():
    id_pengiriman = input("Masukkan ID Pengiriman: ")
    nama_penerima = input("Masukkan Nama Penerima: ")
    alamat = input("Masukkan Alamat: ")
    status = "Dalam Perjalanan"

    data_baru = {
        "id": id_pengiriman,
        "penerima": nama_penerima,
        "alamat": alamat,
        "status": status
    }

    pengiriman.append(data_baru)
    save_data(pengiriman)
    print("Pengiriman berhasil ditambahkan.")

def perbaharui_status():
    id_pengiriman = input("Masukkan id pengiriman yang ingin diperbaharui: ")
    for p in pengiriman:
        if p["id"] == id_pengiriman:
            status_baru = input("Masukkan status pengiriman baru: ")
            p["status"] = status_baru
            save_data(pengiriman)
            print("Status pengiriman berhasil diperbaharui.")
            return
    print("ID pengiriman tidak ditemukan.")

def lihat_pengiriman():
    print("Daftar Pengiriman:")
    if not pengiriman:
        print("Belum ada pengiriman.")
        return
    for p in pengiriman:
        print(f"ID: {p['id']} | Penerima: {p['penerima']} | Status: {p['status']}")
    print()
    
def cari_pengiriman():
    id_pengiriman = input("Masukkan id pengiriman yang ingin dicari: ")
    for p in pengiriman:
        if p["id"] == id_pengiriman:
            print(f"ID Pengiriman: {p['id']}")
            print(f"Penerima: {p['penerima']}")
            print(f"Alamat: {p['alamat']}")
            print(f"Status: {p['status']}")
            return
    print("ID pengiriman tidak ditemukan.")

def main():
    while True:
        print("📦 Sistem Pelacakan Pengiriman 📦")
        print("1. Tambah Pengiriman")
        print("2. Perbarui Status Pengiriman")
        print("3. Lihat Semua Pengiriman")
        print("4. Cari Pengiriman Berdasarkan ID")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_pengiriman()
        elif pilihan == "2":
            perbaharui_status()
        elif pilihan == "3":
            lihat_pengiriman()
        elif pilihan == "4":
            cari_pengiriman()
        elif pilihan == "5":
            print("🚀 Terima kasih! Sampai jumpa.")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.\n")

if __name__ == "__main__":
    main()