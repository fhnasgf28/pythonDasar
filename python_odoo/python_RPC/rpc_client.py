import xmlrpc.client

# membuat koneksi ke server
server = xmlrpc.client.ServerProxy("http://localhost:8000")
print(server.add_numbers(10, 20))

# memanggil metode yang diekspos oleh server
print(server.substract_numbers(10, 20))
result_add = server.add(10, 20)
result_subtract = server.subtract(10, 20)

print(f"Hasil penjumlahan: {result_add}")
print(f"Hasil pengurangan: {result_subtract}")