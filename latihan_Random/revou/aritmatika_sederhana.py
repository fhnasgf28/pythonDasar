# program simple calculator

operator = str(input("Pilih Operator 'penambahan', 'pengurangan', 'perkalian', atau 'pembagian'"))
number1 = int(input("Masukan Angka Pertama:"))
number2 = int(input("Masukan angka kedua:"))

if operator == 'penambahan':
    res = number1 + number2
elif operator == 'pengurangan':
    res = number1 - number2
elif operator == 'perkalian':
    res = number1 * number2
elif operator == 'pembagian':
    res = number1 / number2

print(f'{operator} dari {number1} dan {number2} adalah {res}')