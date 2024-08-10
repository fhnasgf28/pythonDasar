# memnginput kalimat
kalimat = input("Tulis Sebuah kalimat\t:")
# memecah kalimat menjadi kata kata
kata = kalimat.split()

# mengurutkan kata kata
kata.sort()
# menampilkan kata-kata yang telah diurutkan
print("Berikut Urutan kata-kata\t:")
for urut in kata:
    print(urut)