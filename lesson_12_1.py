import requests
from bs4 import BeautifulSoup
import pickle


url = 'https://teploradost.com.ua/'


if __name__ == '__main__':
    # response = requests.get(url, headers={})
    session = requests.Session()
    session.headers.update({})

    response = session.get(url)
    categories = []
    done = []
    soup = BeautifulSoup(response.text, 'html.parser')
    for img in soup.find_all('img', class_='lazyloads'):
        # print(img)
        # print(img.parent['href'])
        categories.append(img.parent['href'])
        # print(img.parent['href'])

    print(len(categories))
    with open('categories.pkl', 'wb') as f:
        pickle.dump(categories, f)

