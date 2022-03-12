import requests
from bs4 import BeautifulSoup
import pickle


url = 'https://teploradost.com.ua'


if __name__ == '__main__':
    # response = requests.get(url, headers={})
    session = requests.Session()
    session.headers.update({})

    with open('categories.pkl', 'rb') as f:
        categories = pickle.load(f)

    response = session.get(f'{url}{categories[0]}')
    soup = BeautifulSoup(response.text, 'html.parser')

    pages = soup.find_all('p', class_='result-value')[0]
    print(soup.find_all('p', class_='result-value'))
    print(pages.get_text().split('(')[-1].split()[1])

    # print(len(categories))


