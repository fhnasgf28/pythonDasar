# baca file txt
def baca_file_attendance(file_path):
    data =[]
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                tanggal, karyawan_id, status = line.strip().split(',')
                data.append({'Tanggal': tanggal, 'Karyawan_ID': karyawan_id, 'Status': status})
    return data
# proses data untuk menghitung total kehadiran per karyawan
file_path = 'attendance.txt'
attendance_data = baca_file_attendance(file_path)
total_attendance = {}
for entry in attendance_data:
    karyawan_id = entry['Karyawan_ID']
    status = entry['Status']
    if status == 'Hadir':
        # kehadiran
        if karyawan_id in total_attendance:
            total_attendance[karyawan_id] += 1
        else:
            total_attendance[karyawan_id] = 1
print(total_attendance)
for name, total in total_attendance.items():
    print(f"{name}: {total}")