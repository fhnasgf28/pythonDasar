import matplotlib.pyplot as plt
from networkx.algorithms.bipartite.basic import color

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
    "Noah": [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    "Olivia": [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    "Parker": [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    "Quinn": [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
}

# menghitung total kehadiran untuk setiap karyawan
total_attendance = {name: sum(days) for name, days in attendance_data.items()}

# menampilkan data kehadiran di terminal
print("Total Attendance per Employee:")
for name, total in total_attendance.items():
    print(f"{name}: {total}")

# visualisasi data menggunakan Mathplotlib
names = list(total_attendance.keys())
totals = list(total_attendance.values())

plt.figure(figsize=(10, 6))
plt.bar(names, totals, color="skyblue")
plt.title("Total Attendance per Employee", fontsize=16)
plt.xlabel("Employee", fontsize=14)
plt.ylabel("Total Attendance (Days)", fontsize=14)
plt.ylim(0, 10) #total hari dalam seminggu
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()