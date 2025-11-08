def hitung_kalori_badminton(berat_badan_kg: float, durasi_jam: float = 1.0) -> float:
    """
    Menghitung kalori yang terbakar saat bermain badminton.
    berat_badan_kg: berat badan dalam kilogram
    durasi_jam: durasi bermain dalam jam (default 1 jam)
    """
    MET_badminton = 7  # nilai MET untuk bermain badminton
    kalori = MET_badminton * berat_badan_kg * durasi_jam
    return kalori

# Contoh penggunaan:
berat_badan = float(input("Masukkan berat badan Anda (kg): "))
durasi = float(input("Masukkan durasi bermain badminton (jam): "))
kalori_terbakar = hitung_kalori_badminton(berat_badan, durasi)
print(f"Kalori yang terbakar: {kalori_terbakar:.2f} kkal")
