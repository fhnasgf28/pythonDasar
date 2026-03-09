import math

def hitung_jari_jari_diameter(diameter):
    """menghitung jari jari dari diameter"""
    if diameter < 0:
        return "Diameter tidak boleh negatif"
    return diameter / 2

def hitung_jari_jari_dari_keliling(keliling):
    if keliling < 0:
        return "Keliling tidak boleh negatif"
    return keliling / (2 * math.pi)

def hitung_jari_jari_dari_luas(luas):
    if luas < 0:
        return "Luas tidak boleh negatif"
    if luas == 0:
        return 0.0
    return math.sqrt(luas / math.pi)

def main():
    print("Selamat datang di kalkulator jari-jari lingkaran")
    print("anda memiliki informasi apa untuk menghitung jari jari")
    print("1.Diamter")
    print("2. Keliling (Circumference)")
    print("3. Luas (Area)")
    pilihan = input("Masukkan pilihan Anda(1/2/3)")

    if pilihan == 1:
        try:
            diameter_input = float(input("Masukkan nilai diamter"))
            jari_jari = hitung_jari_jari_diameter(diameter_input)
            if isinstance(jari_jari, str):
                print(f"error: {jari_jari}")
            else:
                print(f"jari-jari lingkaran adalah: {jari_jari:.4f}")
        except ValueError:
            print('Input tidak valid, harap masukkan angka untuk keliling')
            