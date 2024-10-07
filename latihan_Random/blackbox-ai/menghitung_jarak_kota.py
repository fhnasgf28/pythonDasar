import math

def hitung_jarak():
    nama_kota1 = input("Masukkan nama kota 1: ")
    lintang1 = float(input("Masukkan lintang kota 1 (dalam derajat): "))
    bujur1 = float(input("Masukkan bujur kota 1 (dalam derajat): "))

    nama_kota2 = input("Masukkan nama kota 2: ")
    lintang2 = float(input("Masukkan lintang kota 2 (dalam derajat): "))
    bujur2 = float(input("Masukkan bujur kota 2 (dalam derajat): "))

    # Konversi derajat ke radian
    lintang1_rad = math.radians(lintang1)
    bujur1_rad = math.radians(bujur1)
    lintang2_rad = math.radians(lintang2)
    bujur2_rad = math.radians(bujur2)

    # Hitung jarak
    delta_lat = lintang2_rad - lintang1_rad
    delta_long = bujur2_rad - bujur1_rad
    haversin_lat = math.sin(delta_lat/2)**2
    haversin_long = math.sin(delta_long/2)**2
    jarak = 2 * math.asin(math.sqrt(haversin_lat + math.cos(lintang1_rad) * math.cos(lintang2_rad) * haversin_long))

    # Konversi radian ke kilometer
    jarak_km = jarak * 6371

    print("Jarak antar {} dan {} adalah: {:.2f} km".format(nama_kota1, nama_kota2, jarak_km))

hitung_jarak()