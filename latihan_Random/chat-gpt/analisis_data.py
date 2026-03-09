import pandas as pd

# 1 muat data dari file csv
file_path = 'penjualan.csv'
data = pd.read_csv(file_path)

# 2. hitung total penjuallan untuk setiap produc
data['Total_Penjualan']= data['Jumlah'] * data['Harga_Satuan']
total_penjualan_per_produk = data.groupby('Produk')['Total_Penjualan'].sum().sort_values(ascending=False)

print("Total Penjualan untuk setiap produk:")
print(total_penjualan_per_produk)

# 3.cari produk terlaris
produk_terlaris = data.groupby('Produk')['Jumlah'].sum().idxmax()
print(f"\nProduk Terlaris berdasarkan jumlah terjual:{produk_terlaris}")

# 4. Analisis berdasarkan waktu
data['Tanggal'] = pd.to_datetime(data['Tanggal'])
data['Bulan'] = data['Tanggal'].dt.to_period('M')
penjualan_per_bulan = data.groupby('Bulan')['Total_Penjualan'].sum()

print("\nTotal penjualan per bulan:")
print(penjualan_per_bulan)