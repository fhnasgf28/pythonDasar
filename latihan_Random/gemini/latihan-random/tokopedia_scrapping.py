import requests
from bs4 import BeautifulSoup

def scrape_tokopedia(url):
    print("Scraping Tokopedia...")
    try:
        print(f"URL: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Memeriksa apakah permintaan berhasil

        soup = BeautifulSoup(response.content, "html.parser")

        # Sesuaikan selector CSS ini berdasarkan struktur HTML Tokopedia
        produk_elements = soup.find_all("div", class_="css-1f4mp12")

        for produk in produk_elements:
            nama_produk = produk.find("div", class_="css-1g3r1p9").text.strip()
            harga_produk = produk.find("div", class_="css-1ksb1pend").text.strip()

            print(f"Nama Produk: {nama_produk}")
            print(f"Harga: {harga_produk}")
            print("-" * 20)

    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")
    except AttributeError:
        print("Struktur HTML Tokopedia mungkin telah berubah.")

# Contoh penggunaan
url = "https://www.tokopedia.com" # Ganti "laptop" dengan kata kunci pencarian Anda
scrape_tokopedia(url)