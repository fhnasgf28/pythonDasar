import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data harga komoditas pokok (contoh sederhana)
data = {
    'Tahun': [2019, 2020, 2021, 2022, 2023],
    'Beras (Rp/kg)': [12000, 12500, 13500, 15000, 16500],
    'Minyak Goreng (Rp/liter)': [15000, 16000, 18000, 25000, 22000],
    'Daging Ayam (Rp/kg)': [35000, 37000, 40000, 42000, 45000],
    'Inflasi (%)': [2.7, 2.0, 1.6, 5.5, 4.2]
}

# Membuat DataFrame
df = pd.DataFrame(data)
print("Data Harga Komoditas dan Inflasi:")
print(df)

# Visualisasi trend harga
plt.figure(figsize=(12, 6))
for komoditas in ['Beras (Rp/kg)', 'Minyak Goreng (Rp/liter)', 'Daging Ayam (Rp/kg)']:
    plt.plot(df['Tahun'], df[komoditas], marker='o', label=komoditas)

plt.title('Trend Harga Komoditas Pokok (2019-2023)')
plt.xlabel('Tahun')
plt.ylabel('Harga (Rp)')
plt.legend()
plt.grid(True)
plt.show()

# Analisis korelasi dengan inflasi
plt.figure(figsize=(10, 5))
for komoditas in ['Beras (Rp/kg)', 'Minyak Goreng (Rp/liter)', 'Daging Ayam (Rp/kg)']:
    plt.scatter(df[komoditas], df['Inflasi (%)'], label=komoditas)

plt.title('Korelasi Harga Komoditas dengan Inflasi')
plt.xlabel('Harga Komoditas (Rp)')
plt.ylabel('Inflasi (%)')
plt.legend()
plt.grid(True)
plt.show()


# Prediksi harga menggunakan regresi linear
def prediksi_harga(komoditas):
    X = df['Tahun'].values.reshape(-1, 1)
    y = df[komoditas].values

    model = LinearRegression()
    model.fit(X, y)

    tahun_prediksi = np.array([2024, 2025]).reshape(-1, 1)
    prediksi = model.predict(tahun_prediksi)

    print(f"\nPrediksi harga {komoditas}:")
    for tahun, harga in zip([2024, 2025], prediksi):
        print(f"Tahun {tahun}: Rp {harga:,.0f}")


# Prediksi untuk semua komoditas
for komoditas in ['Beras (Rp/kg)', 'Minyak Goreng (Rp/liter)', 'Daging Ayam (Rp/kg)']:
    prediksi_harga(komoditas)