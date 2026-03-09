def tambah(a,b):
    return a + b
def kurang(a,b):
    return a - b

def kali(a, b):
    return a * b
def bagi(a, b):
    a / b

def main():
    '''' fungsi utama program'''
    # mendapatkan input operasi
    operasi = input("Masukan Operasi (+ , -, /, x)")

    # mendapatkan inputnilai
    a = float(input('Masukan nilai pertama'))
    b = float(input('Masukan nilai kedua'))

    if operasi == "+":
        hasil  = tambah(a, b)
    elif operasi == "-":
        hasil = kurang(a, b)
    elif operasi == "/":
        hasil = bagi(a, b)
    elif operasi == "x":
        hasil = kali(a, b)
    else:
        print("operasi tidak valid")
        return

    # menampilkan hasil
    print("hasil: {} ".format(hasil))
if __name__ == "__main__":
    main()