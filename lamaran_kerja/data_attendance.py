# import modul datetime untuk memanipulasi tanggal dan waktu
from datetime import datetime
import json

# fungsi untuk memeriksa apakah entri absensi dalam satu hari lengkap atau tidak

def is_incomplete(entries):
    return ('in' in entries and 'out' not in entries) or ('out' in entries and 'in' not in entries)

# buka file data attendance_.txt
with open('data_attendance.txt', 'r') as file:
    # membaca isi data_attendance.txt
    data = file.read()
    # memparsing data sebagai objek JSON
    attendance_data = json.loads(data)

    # inisialisasi struktur data untuk menyimpan data absensi
attendance_entries = {}

# iterasi melalui data absensi dan identifikasi absensi yang tidak lengkap
for entry in attendance_data["resultdata"]:
    name = entry["employee"]
    action = entry["check_status"]
    datetime_str = entry["checktime"]
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

#     menambahkan data absensi ke dalam attendance_entries{} jika dalam bulan januari 2021
    if datetime_obj.year == 2021 and datetime_obj.month == 1:
        if name in attendance_entries:
            attendance_entries[name].append((action, datetime_obj))
        else:
            attendance_entries[name] = [(action, datetime_obj)]

# lakukan perulangan melalui data absensi yang hanya terjadi pada bulan Jnauari 2021 dan identifikasi absensi yang tidak lengkap
for name, entries in attendance_entries.items():
    # cekapakah entri absensi dalam satu hari lengkap atau tidak
    incomplete_entries = [entry for entry in entries if is_incomplete(entry)]

#     jika ada entri absensi yang tidak lengkap, tampilkan informasi
    if incomplete_entries:
        print(f'{name} =', ', '.join(
            [f'{action}: {datetime_obj.strftime("%Y-%m-%d %H:%M:%S")}' for action, datetime_obj in incomplete_entries]))

