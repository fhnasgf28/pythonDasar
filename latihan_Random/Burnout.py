import pandas as pd
import numpy as np

# Membuat data contoh (Anda bisa mengganti dengan data Anda sendiri)
data = {'Jam Kerja': [40, 50, 60, 45, 55, 70, 42, 62, 58, 48],
        'Tingkat Stres': [2, 4, 5, 3, 4, 5, 2, 4, 3, 3],
        'Kualitas Tidur': [4, 2, 1, 3, 2, 1, 4, 2, 3, 3],
        'Kepuasan Kerja': [4, 3, 2, 4, 3, 1, 4, 2, 3, 4]}

df = pd.DataFrame(data)

# Menghitung skor burnout (contoh sederhana)
df['Skor Burnout'] = (df['Jam Kerja'] / 40 + df['Tingkat Stres'] + (6 - df['Kualitas Tidur']) + (6 - df['Kepuasan Kerja'])) / 4

# Membuat kategori burnout
def kategori_burnout(skor):
    if skor >= 4:
        return 'Tinggi'
    elif skor >= 2.5:
        return 'Sedang'
    else:
        return 'Rendah'

df['Kategori Burnout'] = df['Skor Burnout'].apply(kategori_burnout)

# Menampilkan statistik deskriptif
print("Statistik Deskriptif:")
print(df.describe())

# Menampilkan jumlah orang di setiap kategori burnout
print("\nJumlah Orang per Kategori Burnout:")
print(df['Kategori Burnout'].value_counts())

# Menampilkan data dengan kategori burnout
print("\nData dengan Kategori Burnout:")
print(df)

# Contoh visualisasi sederhana (membutuhkan matplotlib)
import matplotlib.pyplot as plt

df['Kategori Burnout'].value_counts().plot(kind='bar')
plt.title('Distribusi Kategori Burnout')
plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.show()

# Contoh visualisasi scatter plot untuk melihat korelasi antara jam kerja dan tingkat stres
plt.scatter(df['Jam Kerja'], df['Tingkat Stres'])
plt.title('Korelasi antara Jam Kerja dan Tingkat Stres')
plt.xlabel('Jam Kerja')
plt.ylabel('Tingkat Stres')
plt.show()

