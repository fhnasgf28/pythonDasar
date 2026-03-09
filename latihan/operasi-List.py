# operasi List
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 5, 5, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20]

print(f"Data Angka :\n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(2)
jumlah_data_5 = data_angka.count(3)

print(f"Jumlah Data 2 : {jumlah_data_4}")
print(f"Jumlah Data 3 : {jumlah_data_5}")

# ambil posisi data (index)

data = ["Ucup", "Otong", "Dudung", "Otong", "Ucup2"]
print(f"Data : {data}")

index_dudung = data.index("Dudung")
index_ujang  = data.index("Ucup2")

print(f"Index Dudung : {index_dudung}")
print(f"Index Ucup2 : {index_ujang}")

# mengurutkan List
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka setelah sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# membalikan list
data_angka.reverse()
data.reverse()

print(f"data angka = \n{data_angka}")
print(f"data = \n{data}")
