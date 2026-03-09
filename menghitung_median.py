def hitung_rata_median(angkalist):
    rata_rata = sum(angkalist) / len(angkalist)
    angkalist.sort()
    if len(angkalist) % 2 == 0:
        median = (angkalist[len(angkalist) // 2 - 1] + angkalist[len(angkalist) // 2]) / 2
    else:
        median = angkalist[len(angkalist) // 2]
    return rata_rata, median

angka_list = [10,21,24,26,5,77,85]
rata_rata, median = hitung_rata_median(angka_list)
print(f'angka List {angka_list} \nRata-rata: {rata_rata: .2f}, median:{median: .2f}')

