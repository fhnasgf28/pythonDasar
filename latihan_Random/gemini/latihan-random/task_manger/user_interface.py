def tampilkan_menu():
    print("\n--- Manajemen Tugas ---")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Edit Tugas")
    print("6. Keluar")
    print("----------------------")

def dapatkan_input(pesan):
    return input(pesan + ":").strip()

def dapatkan_pilihan():
    return input("Pilih menu (1-6): ").strip()

def dapatkan_index_tugas():
    return input("Masukkan index tugas yang ingin diubah: ").strip()

def dapatkan_deskripsi_tugas():
    return input("Masukkan deskripsi tugas baru: ").strip()

def dapatkan_prioritas_tugas():
    prioritas = input("Masukkan prioritas tugas (tinggi/sedang/rendah): ").strip().lower()
    if prioritas not in ["tinggi", "sedang", "rendah"]:
        print("Prioritas tidak valid. Menggunakan 'sedang' sebagai default.")
        prioritas = "sedang"
    return prioritas

def dapatkan_status_edit():
    status = input("Masukkan status tugas (selesai/belum selesai): ").strip().lower()
    if status not in ["selesai", "belum selesai"]:
        print("Status tidak valid. Menggunakan 'belum selesai' sebagai default.")
        status = "belum selesai"
    return status

def dapatkan_deskripsi_edit():
    return input("Masukkan deskripsi tugas yang ingin diedit: ").strip()

def dapatkan_prioritas_edit():
    prioritas = input("Masukkan prioritas tugas (tinggi/sedang/rendah): ").strip().lower()
    if prioritas not in ["tinggi", "sedang", "rendah"]:
        print("Prioritas tidak valid. Menggunakan 'sedang' sebagai default.")
        prioritas = "sedang"
    return prioritas

if __name__ == "__main__":
    tampilkan_menu()

