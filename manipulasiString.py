alay = "AkU KECe abIIz"
print("normal", ''+ alay)

alay = alay.lower()
print("normal", '' + alay)

#pengecekan dengan isX method
# contoh pengecekan lower case

salam = "FARHAN"
apakah_lower = salam.islower() #hasilnya bool
print(salam + "is Lower = " + str(apakah_lower))

apakah_upper = salam.isupper() #hasilnya bool
print(salam, "is Upper = " + str(apakah_upper))

# istitle()
judul = "Its okay not to Be Okay"
cek_judul = judul.istitle()
print(judul, "is title = " + str(cek_judul))

# startswith()
cek = "farhan".startswith("far")
print(cek)
#  endswith()
cek1 = "farhanassegaf".endswith("gaf")
print(cek1, "is title = " + str(cek1))

# penggabungan join()

list = ["farhan", "far","assegaf","han2"]
print(",".join(list))

# split()
print("farhan, far, assegaf, han2".split(","))

# alokasi karakter rjust, ljust, center

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(10)
print("'" + tengah + "'")