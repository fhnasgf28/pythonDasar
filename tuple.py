cara_standar = ('farhan', 21, 'jakarta')

# untuk mendefinisikan tuple yang hanya berisi satu item, kita tetap harus menulis tnada koma

# mengakses nilai tuple

tuple_jenis_kelamin = ('laki-laki','perempuan')

print(tuple_jenis_kelamin[1])
print(tuple_jenis_kelamin[0])

# slicing Tuple
tuple_buah = ('Mangga','Nanas','Madu','biawak','anggur','melon','durian','pisang')

print(tuple_buah[1:4])

print(tuple_buah[1:])

# data tuple tidak bisa diubah

# contoh list

list_jenis_kelamin = ['laki-laki','perempuan']

print(list_jenis_kelamin[1])
print(list_jenis_kelamin[0])

# mengubah data list

list_buah = ['Mangga','Nanas','Madu','biawak','anggur','melon','durian','pisang']

print(list_buah[1:4])

print(list_buah[1:])

list_buah[0] = 'Kucing'
print(list_buah)
