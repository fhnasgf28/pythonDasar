def nilai_laptop(prosesor, ram, penyimpanan, grafis, harga):
    score = 0

    # Penilaian prosesor
    if prosesor >= 3.5:
        score += 3
    elif prosesor >= 2.5:
        score += 2
    else:
        score += 1

    # Penilaian RAM
    if ram >= 16:
        score += 3
    elif ram >= 8:
        score += 2
    else:
        score += 1

    # Penilaian penyimpanan
    if penyimpanan == "SSD":
        score += 3
    elif penyimpanan == "HDD" and ram >= 8:
        score += 2
    else:
        score += 1

    # Penilaian grafis
    if grafis == "dedicated":
        score += 3
    else:
        score += 2

    # Penilaian harga (terkait dengan kualitas)
    if harga <= 500:
        score += 1
    elif harga <= 1000:
        score += 2
    else:
        score += 3

    # Memberikan penilaian kualitas berdasarkan score
    if score >= 12:
        return "Laptop ini sangat baik"
    elif score >= 8:
        return "Laptop ini cukup baik"
    else:
        return "Laptop ini buruk"

# Input data laptop
prosesor = float(input("Masukkan kecepatan prosesor (GHz): "))
ram = int(input("Masukkan kapasitas RAM (GB): "))
penyimpanan = input("Masukkan jenis penyimpanan (SSD/HDD): ")
grafis = input("Apakah laptop memiliki grafis terpisah? (yes/no): ").lower()
grafis = "dedicated" if grafis == "yes" else "integrated"
harga = float(input("Masukkan harga laptop (USD): "))

# Output hasil penilaian
hasil = nilai_laptop(prosesor, ram, penyimpanan, grafis, harga)
print(hasil)
