teks = input("masukan teks : ")
pengganti = input('Masukan huruf pengganti huruf vokal : ')

for huruf in 'aiueoAIUEOfF':
    teks = teks.replace(huruf, pengganti)

print(teks)