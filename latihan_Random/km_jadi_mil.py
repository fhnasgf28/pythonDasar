# menginput jarak dalam satuan kilometer
kilometer = float(input("Tuliskan jarak dalam Kilomter :"))

# nilai faktorial konversi
faktor_konversi = 0.621371

# menghitung jarak dalam satuan Mil
mil = kilometer * faktor_konversi

# menampilkan hasil konversi jarak
print('%0.2f kilometer sama dengan %0.2f Mil' %(kilometer, mil))