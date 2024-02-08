# kalkulator sederhana

angka_1 = float(input("Masukan Angka pertama \t:"))
operator = input("Operator (+,/,-, X)")
angka_2 = float(input("Masukan Angka kedua \t:"))

# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("Operator yang anda masukan salah")

print("Terimakasih sudah menggunakan operator sederhana ini")