import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# print(r.text)
# print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='entry-content')
content = soup.find_all('p')
print(content)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)