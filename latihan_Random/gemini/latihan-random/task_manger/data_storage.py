import json
import os

nama_file = "task_data.json"

def simpan_tugas(tugas):
    daftar_tugas = ambil_semua_tugas()
    daftar_tugas.append(tugas)
    simpan_semua_tugas(daftar_tugas)

def ambil_semua_tugas():
    if not os.path.exists(nama_file):
        return []
    try:
        with open(nama_file, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: File JSON rusak. Menggunakan daftar tugas kosong.")
        return []

def simpan_semua_tugas(daftar_tugas):
    with open(nama_file, "w") as file:
        json.dump(daftar_tugas, file, indent=4)

def perbaiki_data():
    daftar_tugas = ambil_semua_tugas()
    updated_tasks = []
    for tugas in daftar_tugas:
        if 'prioritas' not in tugas:
            tugas['prioritas'] = 'normal'
        if 'status' not in tugas:
            tugas['status'] = 'belum selesai'
        updated_tasks.append(tugas)
    simpan_semua_tugas(updated_tasks)
    print("Data telah diperbaiki dan disimpan kembali.")

    
if __name__ == "__main__":
    print("Contoh penggunaan:")
    # Simpan tugas baru
    tugas_baru = {
        "id": 1,
        "judul": "Belajar Python",
        "deskripsi": "Mempelajari dasar-dasar Python.",
        "status": "belum selesai"
    }
    simpan_tugas(tugas_baru)
    # Ambil semua tugas
    semua_tugas = ambil_semua_tugas()
    print("Daftar Tugas:")
    for tugas in semua_tugas:
        print(f"ID: {tugas['id']}, Judul: {tugas['judul']}, Deskripsi: {tugas['deskripsi']}, Status: {tugas['status']}")
# This code is a simple task manager that allows you to save and retrieve tasks from a JSON file.
# It includes functions to save a new task, retrieve all tasks, and save all tasks to the file.
        
        