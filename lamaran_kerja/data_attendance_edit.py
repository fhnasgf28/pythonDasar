import json


def is_complete(entries):
    return ('in' in entries and 'out' not in entries) or ('out' in entries and 'in' not in entries)

with open('data_attendance.txt', 'r') as file:
    data = file.read()
    attendance_data = json.loads(data)
    print(attendance_data, 'nama saya farhnassegaf')