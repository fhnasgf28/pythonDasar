data_0 = [1, 2]
data_1 = [3, 4, 5, 5, 7]

data_list_biasa = [1, 2, 3, 4, 5, 6, 7, 8, ]
print(f"list biasa\t: {data_list_biasa}")

list_2D = [data_0, data_1, 6, 7]
print(f'list 2D\t: {list_2D}')

# contoh penggunaan

peserta_0 = ["ucup", 23, "Laki-laki"]
peserta_1 = ["otong", 22, "aki-aki"]
peserta_2 = ["dudung", 21, "awewe"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"list peserta\t: {list_peserta}")

for peserta in list_peserta:
    print(f'nama peserta\t: {peserta[0]}')
    print(f'umur peserta\t: {peserta[1]}')
    print(f'gender peserta\t: {peserta[2]}\n')

#     dengan reference

list_copy = list_peserta.copy();
print(f'peserta = {list_copy}')
peserta_0[0] = "michael"
print(f'peserta = {list_copy}')
print(f'peserta = {list_peserta}')

