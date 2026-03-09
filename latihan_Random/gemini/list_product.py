import pandas as pd

# baca file CSV
csv_path = r'A:\pythonDasar\latihan_Random\CSV\list_product.csv'
df = pd.read_csv(csv_path)

print(df[['nama_produk', 'harga']].head())

# hitung total stok
total_stok = df['stok'].sum()
print("Total stok:", total_stok)

# cari product dengan harga tertinggi
product_termahal = df[df['harga'] == df["harga"].max()]
print("Product termahal:", product_termahal)
grouped_data = df.groupby('kategori')[['harga', 'stok']].sum()
print(grouped_data)
# cari product dengan stok paling sedikit dalam kategori elektronik
product_paling_sedikit = df[df['kategori'] == 'elektronik'].sort_values('stok').head(1)
print(product_paling_sedikit)