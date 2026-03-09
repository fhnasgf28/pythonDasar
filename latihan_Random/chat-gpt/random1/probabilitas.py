import random 
import matplotlib.pyplot as plt

# Contoh data kehadiran karyawan
attendance_data = {
    "Alice": [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    "Bob": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Charlie": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "David": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Eve": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Frank": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Grace": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Henry": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Isabella": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Jack": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Kate": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Liam": [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    "Mia": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
}

# menghitung total kehadiran untuk setiap karyawan
total_attendance = {name: sum(days) for name, days in attendance_data.items()}
print(total_attendance)

# menampilkan data kehadiran di terminal
print("Total Attendance per Employee:")
for name, total in total_attendance.items():
    print(f"{name}: {total}")