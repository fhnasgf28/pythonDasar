import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.title.text
print(title)