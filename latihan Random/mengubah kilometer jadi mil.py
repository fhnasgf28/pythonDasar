# menginput jarak dalam satuan kilomter

kilometer = float(input("Tuliskan jarak dalam kilomter"))

# nilai faktor konversi
# faktor_konversi

faktor_konversi = 0.621371

# menghitung jarak dalam satuan mil
mil = kilometer * faktor_konversi

# menampilkan hasil konversi jarak
print('%0.2f kilometer sama dengan %0.2f Mil'%(kilometer, mil))