def hitung_bmr(jenis_kelamin, berat_kg, tinggi_cm, usia):
    if jenis_kelamin.lower() == "pria":
        bmr = 10 * berat_kg + 6.25 * tinggi_cm - 5 * usia + 5
    elif jenis_kelamin.lower() == "wanita":
        bmr = 10 * berat_kg + 6.25 * tinggi_cm - 5 * usia - 161
    else:
        raise ValueError("Jenis kelamin harus 'pria' atau 'wanita'")
    
    return round(bmr, 2)


# Contoh
print(hitung_bmr("pria", 70, 170, 30))
