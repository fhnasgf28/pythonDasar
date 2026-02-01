import random

def peluang_menikah(gaji, usia, faktor_sosial, tahun=2, simulasi=10000):
    """
    gaji: dalam juta
    usia: tahun
    faktor_sosial: skala 0-1 (dukungan keluarga, lingkungan, dll.)
    tahun: target waktu (default 2 tahun)
    simulasi: jumlah percobaan Monte Carlo
    """
    peluang_total = 0
    
    for _ in range(simulasi):
        # Asumsi dasar probabilitas
        base_prob = 0.2  # peluang dasar menikah dalam 2 tahun
        
        # Faktor gaji (semakin tinggi semakin besar peluang)
        if gaji >= 5:
            base_prob += 0.15
        else:
            base_prob += 0.05
        
        # Faktor usia (anggap ideal menikah di usia 25-35)
        if 25 <= usia <= 35:
            base_prob += 0.2
        else:
            base_prob -= 0.1
        
        # Faktor sosial
        base_prob += faktor_sosial * 0.3
        
        # Randomisasi (simulasi ketidakpastian)
        if random.random() < base_prob:
            peluang_total += 1
    
    return peluang_total / simulasi

# Contoh penggunaan
gaji = 5  # juta
usia = 27
faktor_sosial = 0.7  # cukup mendukung
hasil = peluang_menikah(gaji, usia, faktor_sosial)

print(f"Peluang menikah dalam 2 tahun dengan gaji {gaji} juta: {hasil*100:.2f}%")
