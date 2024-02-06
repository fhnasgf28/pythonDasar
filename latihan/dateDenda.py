from datetime import datetime

def hitung_denda(tanggal_jatuh_tempo, tanggal_pembayaran, denda_perHari):
    """
    =======Mengitung Jatuh Tempo
    """
    # hitung selisih antara waktu jatuh tempo dan Waktu pembayaran
    selisih_waktu = tanggal_pembayaran - tanggal_jatuh_tempo

    
    # hitung jumlah hari keterlambatan
    jumlah_hari = selisih_waktu.days
    
    # jika pembayaran tepat waktu, return 0
    if jumlah_hari <= 0:
        return 0
    
    # hitung denda
    denda = jumlah_hari * denda_perHari
    
    return denda

def main():
    print("======SELAMAT DATANG DI PROGRAM DENDA======")
    print("======MENGHITUNG JATUH TEMPO DAN DENDA=====")

    # masukan tanggal jatuh tempo
    tanggal_jatuh_tempo_str = input("Masukan tanggal jatuh tempo (dd-mm-yyyy) : ")
    tanggal_jatuh_tempo = datetime.strptime(tanggal_jatuh_tempo_str, "%d-%m-%Y")

    # masukan tanggal dan waktu pembayaran
    tanggal_pembayaran_str = input("Masukan tanggal dan waktu jatuh tempo (dd-mm-yyyy) : ")
    tanggal_pembayaran = datetime.strptime(tanggal_pembayaran_str, "%d-%m-%Y")

    # masukan tingkat denda perhari
    denda_perHari = float(input("Masukan tingkat denda perhari : "))

    # hitung denda 
    denda = hitung_denda(tanggal_jatuh_tempo, tanggal_pembayaran, denda_perHari)

    # tampilkan hasil
    print(f"Jumlah Denda yang harus dibayar : Rp{denda:,.2f}")

if __name__ == "__main__":
    main()