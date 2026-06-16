# Contoh 1: Mencari di list
def cari_di_list(data, keyword):
    hasil = [item for item in data if keyword.lower() in str(item).lower()]
    return hasil

# Contoh 2: Mencari di file CSV
import csv

def cari_di_csv(nama_file, kolom, keyword):
    hasil = []
    with open(nama_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if keyword.lower() in row[kolom].lower():
                hasil.append(row)
    return hasil

# Contoh 3: Mencari di JSON
import json

def cari_di_json(nama_file, key, keyword):
    with open(nama_file, 'r') as file:
        data = json.load(file)
    hasil = [item for item in data if keyword.lower() in str(item.get(key, '')).lower()]
    return hasil
