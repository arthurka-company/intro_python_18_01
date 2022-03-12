# sudo apt-get install python3-bs4
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://teploradost.com.ua/'

response = requests.get(url)
print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.title.parent.parent.name)
# print(soup.head.children)
# for i in soup.head.children:
# #     print(i.name)
# print(soup.h1)
# # print(soup.find_all('div', id='quickBuy'))
# divs = soup.find_all('div', id='quickBuy')
# # print(divs[0].label)
# # print(divs[0].find_all('label'))
#
# div = soup.find(id='quickBuy')
# # print(div.name)
# # print(div.)
#
# # print(soup.find_all('div', {'class': 'footer-column payment'}))
#
# objs = soup.find_all('div', {'class': 'footer-column payment'})
# for img in objs[0].find_all('img'):
#     print(img.get('alt'), img.get('src'))

print(len(soup.find_all('a', class_='child-name top-child-name')))
