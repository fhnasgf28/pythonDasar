
# program untuk memeriksa daftar belanjaan
# daftar barang yang harus di beli
daftar_belanjaan = ["baju", "celana", "sepatu", "topi", "kaos"]
#masukkan daftar belanjaan
input_belanjaan = input("Masukkan daftar belanjaan (pisahkan dengan koma): ")
daftar_belanjaan2 = input_belanjaan.replace(",", " ").split()

#periksa daftar belanjaan
barang_tidak_ada = [barang for barang in daftar_belanjaan if barang not in daftar_belanjaan2]
if not barang_tidak_ada:
    print("Semua barang telah dibeli.")
else:
    print("Barang yang belum dibeli:", ", ".join(barang_tidak_ada))
print("Barang yang belum dibeli:", ", ".join(barang_tidak_ada))