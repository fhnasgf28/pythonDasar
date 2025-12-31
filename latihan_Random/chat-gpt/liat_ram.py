import os

def get_ram_info():
    with open("/proc/meminfo", "r") as f:
        meminfo = f.readlines()

    mem_total = 0
    mem_available = 0

    for line in meminfo:
        if line.startswith("MemTotal"):
            mem_total = int(line.split()[1]) // 1024
        elif line.startswith("MemAvailable"):
            mem_available = int(line.split()[1]) // 1024

    return mem_total, mem_available

total, available = get_ram_info()

print(f"Total RAM      : {total} MB")
print(f"Sisa RAM       : {available} MB")
print(f"RAM Terpakai   : {total - available} MB")