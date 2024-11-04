
def format_rupiah(nilai):
    return f"Rp {nilai:,.0f}".replace(',', '.').replace('Rp ', 'Rp ')
def hitung_kekayaan():
    print("Selamat Datang di Program Menghitung Kekayaan")

    # mengambil input dari pengguna
    uang_tunai = float(input("Masukkan Jumlah Uang Tunai: "))
    property = float(input("Masukkan Jumlah Property: "))
    investasi = float(input("Masukkan Jumlah Investasi: "))
    kendaraan = float(input("Masukan nilai kendaraan: "))

#     menghitung total kekayaan
    total_kekayaan = uang_tunai + property + investasi + kendaraan
    print(f'Total Kekayaan: {format_rupiah(total_kekayaan)}')

# memanggil fungsi hitung_kekayaan
hitung_kekayaan()
