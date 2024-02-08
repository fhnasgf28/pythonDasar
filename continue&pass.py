angka = 0

print(f"angka sekarang --> {angka}")

while angka < 10:
    angka += 1
    print(f"angka sekarang --> {angka}")
    print("otong ganteng maksimal")

    if angka == 3:
        print("Mantap Bro")
        continue  # continue akan membuat loop meloncat dan tidak eksekusi ke bawah
        print("OK Bro sip") #aksi dua

    print("OK Bro") #aksi dua