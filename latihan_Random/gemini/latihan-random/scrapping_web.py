import requests
from bs4 import BeautifulSoup

from auth.test_auth import response

url = 'https://www.detik.com/'

try:
    response = requests.get(url)
    response.raise_for_status()

    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    judul_artikel = soup.find_all("h2", class_="berita-utama")
    if judul_artikel:
        print("Judul Artikel:")
        for judul in judul_artikel:
            print(judul.text.strip())
    else:
        print("Tidak ada judul artikel yang ditemukan.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")