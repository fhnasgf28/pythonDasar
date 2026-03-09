# import modul datetime untuk memanipulasi tanggal dan waktu
from datetime import datetime
import json

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
    datetime_str = entry["checktime"]
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    #     menambahkan data absensi ke dalam attendance_entries{} jika dalam bulan januari 2021
    if datetime_obj.year == 2021 and datetime_obj.month == 1:
        if name in attendance_entries:
            attendance_entries[name].append((datetime_obj, entry["check_status"]))
        else:
            attendance_entries[name] = [(datetime_obj, entry["check_status"])]

#  inisialisasi variable untuk menyimpan jumlh jam kerja karywan
total_hours_worked = {}
# iterasi melalui data absensi yang terjadi pada bulan Januari 2021

for name, entries in attendance_entries.items():
    #    inisialisasi variabel untuk menyimpan waktu check-in dan check-out
    check_in_time = None
    check_out_ime = None
    # inisialisasi variabel untuk menyimpan jumlah jam kerja Karyawan
    total_hours = 0

    # iterasi melalui entri absensi karyawn
    for entry in entries:
        if entry[1] == 'in':
            check_in_time = entry[0]
        elif entry[1] == 'out' and check_in_time is not None:
            check_out_time = entry[0]
            #hitung selisih waktu antara check-in dan check-out
            hours_worked = (check_out_time - check_in_time).total_seconds() / 3600
            #             tambahkan jumlah jam kerja ke total_hours
            total_hours += hours_worked
            #reset waktu check-in dan check-out untuk karyawan berikutnya
            check_in_time = None
            check_out_time = None

            #simpan jumlah jam kerja karyawan ke dalam variabel total_hours_worked
    total_hours_worked[name] = total_hours

#tampilkan jumlah jam kerja karyawan dalam bulan januari 2021
for name, total_hours in total_hours_worked.items():
    formated_total_hours = round(total_hours, 2)
    print(f'{name} = {formated_total_hours: .2f} jam')
