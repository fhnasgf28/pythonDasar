import task_manager
import user_interface

def main():
    while True:
        user_interface.tampilkan_menu()
        pilihan = user_interface.dapatkan_pilihan()

        if pilihan == "1":
            deskripsi = user_interface.dapatkan_input("Masukkan deskripsi tugas")
            prioritas = user_interface.dapatkan_prioritas_tugas()
            task_manager.tambah_tugas(deskripsi, prioritas)
        elif pilihan == "2":
            # tambahkan 2 argumen
            # untuk menampilkan tugas
            # dan menampilkan status
            task_manager.tampilkan_tugas(user_interface.dapatkan_filter_status(), user_interface.dapatkan_filter_prioritas())
        elif pilihan == "3":
            index_tugas = user_interface.dapatkan_index_tugas()
            task_manager.tandai_selesai(index_tugas)
        elif pilihan == "4":
            index_tugas = user_interface.dapatkan_index_tugas()
            task_manager.hapus_tugas(index_tugas)
        elif pilihan == "5":
            index_tugas = user_interface.dapatkan_index_tugas()
            deskripsi_baru = user_interface.dapatkan_deskripsi_edit()
            prioritas_baru = user_interface.dapatkan_prioritas_edit()
            status_baru = user_interface.dapatkan_status_edit()
            task_manager.edit_tugas(index_tugas, deskripsi_baru, prioritas_baru, status_baru)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()