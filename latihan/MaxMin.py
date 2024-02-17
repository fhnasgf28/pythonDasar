# maksimum dan minimum

a = [10, 4, 30, 80, 90, 100, 800, 7098, 909090]

print("maksimum : ", max(a))
print("minimum : ", min(a))

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimum(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil

print(a)
print('Nilai Terbesar\t:', nilai_maksimal(a))
print('Nilai Terkecil\t:', nilai_minimum(a))