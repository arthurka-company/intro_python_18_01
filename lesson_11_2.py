# requests
'''
1. Получаем список альбомов. Слайсом берем нужное количество
2. Создаем папки для альбомов
3. Получаем фото с фильтром по ид альбома
4. Сохраняем фото в нужные папки
'''
import requests
import os
import random


ALBUM_URL = 'https://jsonplaceholder.typicode.com/albums'
PHOTO_URL = 'https://jsonplaceholder.typicode.com/photos'
RESULT_FOLDER = 'result'


def get_ablums(number: int) -> list:
    response = requests.get(ALBUM_URL)
    response_data = response.json()
    albums = random.choices(response_data, k=number)
    return albums


def create_folder(folder_name: str) -> None:
    os.makedirs(folder_name, exist_ok=True)


def get_photos_by_album_id(pk: int, photos_number: int) -> list:
    response = requests.get(
        PHOTO_URL,
        params={
            'albumId': pk
        }
    )
    response_data = response.json()
    return response_data[:photos_number]


def save_photos_to_the_folder(photos: list, folder: str) -> None:
    for idx, photo in enumerate(photos):
        response = requests.get(photo['url'])
        with open(os.path.join(folder, f'{photo["title"]}.jpg'), 'bw') as f:
            f.write(response.content)
        if idx % 2 == 0:
            print('Processed:', idx, 'photos')


def main(n: int, photos_number: int) -> None:
    albums = get_ablums(n)
    for album in albums:
        print('Processing album name:', album['title'])
        album_folder = os.path.join(RESULT_FOLDER, f'{album["id"]} - {album["title"]}')
        create_folder(album_folder)
        photos = get_photos_by_album_id(album['id'], photos_number)
        save_photos_to_the_folder(photos, album_folder)


if __name__ == '__main__':
    n = 2
    photos_number = 10
    main(n, photos_number)
