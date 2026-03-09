# looping dari list
# for loop

print("For Loop")

kumpulan_angka = [4, 3, 2, 1, 5, 6, 7]

for angka in kumpulan_angka:
    print(f'angka sekarang --> {angka}')

print('\n=========================')
peserta = ["otong", "uca", "joko", "joko", "wati", "joko"]
for nama in peserta:
    print(f'peserta sekarang --> {nama}')

# for loop dan range
print("\nFor Loop dan Range")

kumpulan_angka = [10, 23, 15, 66, 74, 33, 25]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')

# while loop
print("\nWhile Loop")
kumpulan_angka = [10, 23, 15, 16, 42, 25, 66, 74, 33, 25]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

# list komprehension
print("\nList Comprehension")
data = ['ucup', 'otong', 'joko', 'wati', 44, 66, 22, 'Romusha']

[print(f'data = {i}') for i in data]

# enumerate
print("\nEnumerate")

data_list = ['ucup', 'otong', 'joko', 'wati', 44, 66, 22, 'Romusha']

for index, data in enumerate(data_list):
    print(f'index = {index}, data = {data}')
