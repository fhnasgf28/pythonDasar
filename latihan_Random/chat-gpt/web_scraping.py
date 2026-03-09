import requests
from bs4 import BeautifulSoup
import csv

from auth.test_auth import response

# URL halaman web
# URL target
url = 'http://books.toscrape.com/catalogue/page-1.html'

# Kirim permintaan GET ke URL
response = requests.get(url)

# Periksa apakah permintaan berhasil
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # ambil semua elment buku
    books = soup.find_all('article', class_='product_pod')

    # siapkan file csv
    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Judul Buku', 'Harga', 'Stok'])

        for book in books:
            title = book.find('h3').text
            price = book.find('p', class_='price_color').text
            stock = book.find('p', class_='instock availability').text.strip()

            writer.writerow([title, price, stock])

    print("Data buku berhasil disimpan ke file CSV.")
else:
    print("Gagal mengambil data buku.")