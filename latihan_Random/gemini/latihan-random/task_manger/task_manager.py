import data_storage

def tambah_tugas(deskripsi, prioritas="sedang", status="belum selesai"):
    tugas = {
        "deskripsi": deskripsi,
        "prioritas": prioritas,
        "status": status
    }
    data_storage.simpan_tugas(tugas)
    print(f"Tugas '{deskripsi}' telah ditambahkan dengan prioritas '{prioritas}' dan status '{status}'.")

def lihat_tugas(filter_status=None, filter_prioritas=None):
    daftar_tugas = data_storage.ambil_semua_tugas()
    if not daftar_tugas:
        print("Tidak ada tugas yang ditemukan.")
        return
    print("Daftar Tugas:")
    for index, tugas in enumerate(daftar_tugas):
        tampilkan_tugas(index, tugas)

def tandai_selesai(index_tugas):
    daftar_tugas = data_storage.ambil_semua_tugas()
    try:
        index = int(index_tugas)
        if 0 <= index < len(daftar_tugas):
            daftar_tugas[index]["status"] = "selesai"
            data_storage.simpan_semua_tugas(daftar_tugas)
            print(f"Tugas '{daftar_tugas[index]['deskripsi']}' telah ditandai sebagai selesai.")
        else:
            print("Index tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def tampilkan_tugas(index, tugas):
    """Menampilkan detail satu tugas."""
    print(f"{index + 1}. Deskripsi: {tugas['deskripsi']}")
    print(f"   Prioritas: {tugas['prioritas']}")
    print(f"   Status: {tugas['status']}")
    print("-" * 20)

def edit_tugas(index_tugas, deskripsi_baru=None, prioritas_baru=None, status_baru=None):
    daftar_tugas = data_storage.ambil_semua_tugas()
    try:
        index = int(index_tugas)
        if 0 <= index < len(daftar_tugas):
            if deskripsi_baru:
                daftar_tugas[index]["deskripsi"] = deskripsi_baru
            if prioritas_baru:
                daftar_tugas[index]["prioritas"] = prioritas_baru
            if status_baru:
                daftar_tugas[index]["status"] = status_baru
            data_storage.simpan_semua_tugas(daftar_tugas)
            print(f"Tugas '{index}' telah diperbarui.")
        else:
            print("Index tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def hapus_tugas(index_tugas):
    daftar_tugas = data_storage.ambil_semua_tugas()
    try:
        index = int(index_tugas)
        if 0 <= index < len(daftar_tugas):
            del daftar_tugas[index]
            data_storage.simpan_semua_tugas(daftar_tugas)
            print(f"Tugas '{index}' telah dihapus.")
        else:
            print("Index tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Tandai Selesai")
        print("4. Edit Tugas")
        print("5. Hapus Tugas")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            deskripsi = input("Masukkan deskripsi tugas: ")
            prioritas = input("Masukkan prioritas tugas (sedang, rendah, tinggi): ")
            tambah_tugas(deskripsi, prioritas)
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            index_tugas = input("Masukkan index tugas yang akan ditandai sebagai selesai: ")
            tandai_selesai(index_tugas)
        elif pilihan == "4":
            index_tugas = input("Masukkan index tugas yang akan diperbarui: ")
            deskripsi_baru = input("Masukkan deskripsi baru (opsional): ")
            prioritas_baru = input("Masukkan prioritas baru (opsional): ")
            status_baru = input("Masukkan status baru (opsional): ")
            edit_tugas(index_tugas, deskripsi_baru, prioritas_baru, status_baru)
        elif pilihan == "5":
            index_tugas = input("Masukkan index tugas yang akan dihapus: ")
            hapus_tugas(index_tugas)
        elif pilihan == "6":
            print("Keluar dari program.")
            break

#         else: 
