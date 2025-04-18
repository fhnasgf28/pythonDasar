import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/'
response = requests.get(url)
html_content = response.text

# parsing 
soup = BeautifulSoup(html_content, 'html.parser')

# mencari semua elemen dengan tag <a>
links = soup.find_all('a')
for link in links:
    # mencetak isi dari atribut href
    print(link.get('href'))
# mencetak isi dari teks link
    print(link.text)
# mencetak isi dari tag <a>
    print(link)
# mencetak isi dari tag <a> dengan class tertentu
    print(link.get('class'))
# mencetak isi dari tag <a> dengan id tertentu
    print(link.get('id'))
# mencetak isi dari tag <a> dengan atribut tertentu
    print(link.get('data-attr'))
# mencetak isi dari tag <a> dengan atribut tertentu
    print(link.get('data-attr2'))
# mencetak isi dari tag <a> dengan atribut tertentu
    print(link.get('data-attr3'))
# mencetak isi dari tag <a> dengan atribut tertentu
    print(link.get('data-attr4'))