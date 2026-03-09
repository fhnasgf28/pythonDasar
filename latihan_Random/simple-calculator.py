# program simple calcultor

operator = str(input('Pilih operator "penambahan", "pengurangan","perkalian" atau "pembagian"\t:'))

number1 = int(input("Masukan Angka Pertama \t:"))
number2 = int(input("Masukan angka kedua\t:"))

if operator == 'penambahan':
    res = number1 + number2
elif operator == 'pengurangan':
    res = number1 - number2
elif operator == 'perkalian':
    res = number1 * number2
elif operator == 'pembagian':
    res = number1 / number2
else:
    res = number1 + number2

print(f'{operator} dari {number1} dan {number2} adalah {res}')
