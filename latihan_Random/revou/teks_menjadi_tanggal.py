from datetime import datetime

hari = str(input("Masukan tanggal: "))
bulan = str(input("Masukan bulan (angka): "))
tahun = str(input("Masukan tahun (lengkap): "))
jam = str(input("Masukan Jam: "))
menit = str(input('Masukan Menit: '))

tanggal = hari + ' ' + bulan + ' ' + tahun + ' ' + jam + ':' + menit
datetime_object = datetime.strptime(tanggal, "%d %m %Y %H:%M")
datetime_object = datetime.strptime(tanggal, "%d %m %Y %H:%M")

print(type(datetime_object))
print(datetime_object)