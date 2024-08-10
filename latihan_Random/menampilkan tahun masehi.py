# mengimpor modul calendar
import calendar

# menginput tahun dan bulan
year = int(input("Masukan Tahun\t:"))
month = int(input("Masukan Bulan\t:"))

# menampilkan calendar bulanan
print(calendar.month(year, month))