def read_attendance(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data

def analyze_attendance(data):
    present_count = 0
    absent_count = 0
    attendance_dict = {}

    for line in data:
        name, status = line.strip().split(',')
        attendance_dict[name] = status

        if status == 'Present':
            present_count += 1
        elif status == 'Absent':
            absent_count += 1
    
    return attendance_dict, present_count, absent_count

def print_attendance_summary(attendance_dict, present_count, absent_count):
    print("Attendance Summary:")
    for name, status in attendance_dict.items():
        print(f"{name}: {status}")
    print(f"Present: {present_count}")
    print(f"Absent: {absent_count}")

def main():
    file_name = '/Users/farhan/pythonDasar/latihan_Random/copilot/attendance.txt'
    data = read_attendance(file_name)
    attendance_dict, present_count, absent_count = analyze_attendance(data)
    print_attendance_summary(attendance_dict, present_count, absent_count)

if __name__ == "__main__":
    main()