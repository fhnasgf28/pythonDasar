import json 
from datetime import datetime

# data sample kehadiran karyawan 

attendance_data = [
    {"employee_id": 1, "name": "Alice", "attendance": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-06", "2024-11-07"]},
    {"employee_id": 2, "name": "Bob", "attendance": ["2024-11-01", "2024-11-02", "2024-11-06", "2024-11-08"]},
    {"employee_id": 3, "name": "Charlie", "attendance": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-04", "2024-11-05", "2024-11-07", "2024-11-08", "2024-11-10"]}
]

# konfigurasi jumlah hari kerja minimum dalam satu bulan 
min_working_days = 20 

# fungsi untuk menghitung kehadiran karyawan 
def calculate_attendance(attendance_data, min_working_days):
    attendance_summary = []
    for data in attendance_data:
        total_days_present = len(data["attendance"])
        meets_requirement = total_days_present >= min_working_days
        attendance_summary.append({
            "employee_id": data["employee_id"],
            "name": data["name"],
            "total_days_present": total_days_present,
            "meets_requirement": meets_requirement
        })

# fungsi untuk menyimpan data ke file JSON 
def save_to_json(data, filename="attendance_summary.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data kehadiran karyawan telah disimpan dalam {filename}.")

# menghitung kehadiran dan menyimpan hasilnya ke JSON
attendance_summary = calculate_attendance(attendance_data, min_working_days)
save_to_json(attendance_summary)