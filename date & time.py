import datetime as dt

print("silahkan masukan tangal, bulan dan tahun lahir anda")

tanggal = int(input("masukan tanggal lahir anda : "))
bulan = int(input("bulan lahir anda : "))
tahun = int(input("tahun lahir anda : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print("Tanggal lahir anda adalah : ", tanggal_lahir)

hari_ini = dt.date.today()
print(f"Hari ini tanggal \t: {hari_ini}")

print("=======Menghitung Umur=========")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"Umur anda adalah \t: {umur_tahun} tahun")
# umur_bulan_sisa = (umur_hari.days % 365) // 30	

# print(f"Harinya adalah \t: {tanggal_lahir:%A}")
# print(f"umur anda adalah \t: {umur_tahun} tahun, {umur_bulan_sisa} bulan")