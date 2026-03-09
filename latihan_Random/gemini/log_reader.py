import re

def rad_log_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
                return None
            return None
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def parse_common_log(log_line):
    pattern = r'^(\S+) - - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+\d{4})\] "(\S+)" (\d+) (\d+) "(\S+)" "([^"]+)"'
    if pattern:
        timestamp, level, message = pattern.groups()
        return {
            'timestamp': timestamp,
            'level': level,
            'message': message
        }
    return None

if __name__ == "__main__":
    log_file = 'sample.log'
    with open(log_file, 'r') as f:
        f.write("2025-04-17 07:30:00,123 INFO - Aplikasi dimulai.\n")
        f.write("2025-04-17 07:30:05,456 DEBUG - Memproses data: X=10, Y=20\n")
        f.write("2025-04-17 07:30:10,789 ERROR - Terjadi kesalahan: Koneksi database gagal.\n")
    print("membaca log dari file", log_file)
    for line in rad_log_file(log_file):
        print(f"Line: {line}")
    print("parsing log")

    for line in rad_log_file(log_file):
        parsed_log = parse_common_log(line)
        if parsed_log:
            print(f"Timestamp: {parsed_log['timestamp']}")
            print(f"Level: {parsed_log['level']}")
            print(f"Message: {parsed_log['message']}")
            print()