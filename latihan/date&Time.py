from datetime import datetime

def hitung_usia(tanggal_lahir):
    # ambil tanggal hari ini
    tanggal_hari_ini = datetime.now()

    # ubah tanggal lahir menjadi objek datetime
    tanggal_lahir = datetime.strptime(tanggal_lahir, "%d %B %Y")

    # hitung selisih waktu antara tanggal hari ini dan tanggal lahir
    selisih_waktu = tanggal_hari_ini - tanggal_lahir

    # ekstrak tahun dari selisih waktu antara tanggal hari ini dan tanggal lahir
    usia_tahun = selisih_waktu.days // 365

    return usia_tahun, selisih_waktu

def main():
    print ("======selamat datang diperhitungan usia======")
    tanggal_lahir = input("Masukan Tanggal lahir anda dengan Format (dd-mm-yyyy) : ")

    # hitung_usia
    usia_tahun, selisih_waktu = hitung_usia(tanggal_lahir)

    print(f"\nUsia Anda saat ini adalah {usia_tahun} tahun, {selisih_waktu.days % 365 // 30} Bulan, dan {selisih_waktu.days %365 % 30} Hari")

if __name__ == "__main__":
    main()