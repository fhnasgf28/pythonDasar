import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data = {
    'tahun': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Beras (Rp / kg)': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000],
    'Gula (Rp / kg)': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],
    'Telur (Rp / doz)': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],
    'Daging Ayam (Rp /kg)': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000],
    'inflasi (%)': [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
}

df = pd.DataFrame(data)
print("Data Harga Komoditas dan Inflasi:")
print(df)

# visualisasi trend harga
plt.figure(figsize=(10, 6))
for komoditas in ['Beras (Rp / kg)', 'Gula (Rp / kg)', 'Telur (Rp / doz)', 'Daging Ayam (Rp /kg)']:
    plt.plot(df['tahun'], df[komoditas], label=komoditas)
    plt.scatter(df[komoditas], df['inflasi (%)'], label='Inflasi (%)')
    plt.xlabel('Tahun')
    plt.ylabel('Harga Komoditas')
    plt.title('Trend Harga Komoditas dan Inflasi')
    plt.legend()
    plt.grid(True)
    plt.show()

def prediksi_harga(komoditas):
    x = df['Tahun'].values.reshape(-1, 1)
    y = df[komoditas].values

    model = LinearRegression()
    model.fit(x, y)

    tahun_prediksi = np.array([2014, 2015, 2016, 2017, 2018, 2019]).reshape(-1, 1)
    prediksi = model.predict(tahun_prediksi)
    print(f"Prediksi harga {komoditas} pada tahun 2014-2019:")
    for tahun, harga in zip(tahun_prediksi, prediksi):
        print(f"Tahun {tahun}: Rp {harga:.2f}")

# PREDIKSI UNTUK SEMUA KOMODITAS
for komoditas in ['Beras (Rp / kg)', 'Gula (Rp / kg)', 'Telur (Rp / doz)', 'Daging Ayam (Rp /kg)']:
    prediksi_harga(komoditas)