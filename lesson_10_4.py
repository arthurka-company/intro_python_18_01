'''
Задание

У нас есть интернет магазин. Это стартап, потому до проверки ниши много действий делаются руками.
Поставщик прислал архив, в котором есть прайс и папка с картинками.
Прайс: id, name, brand, price
Картинки: имя файла начинается с id товара

Есть правило установки цены:
Для бренда Matchbox скидка от поставщика 40%
Для остальных 30%
Продажная цена = цена закупки * 2

Задача: подготовить папку для выгрузки на сайт интернет магазина

файл выгрузки: sku (=id), name, brand, price (продажная цена), image. Формат json

Картинка должна лежать в папке: catalog/products

'''
import csv
import json
import os
import shutil


DEFAULT_DISCOUNT = 0.3
IMAGE_OUTPUT = 'ls10/catalog/products'
IMAGE_INPUT = 'ls10/images'


def read_products_from_csv(file_path: str) -> list:
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [dict(row) for row in reader]
    return data


def get_product_price(product: dict, brand_discounts: dict) -> float:
    discount = brand_discounts[product['brand']] if product['brand'] in brand_discounts else DEFAULT_DISCOUNT
    price = float(product['price']) * (1 - discount) * 2
    return round(price, 2)


def get_image_path(product: dict, images: list) -> str:
    product_id = product['id']
    for image in images:
        if image.startswith(product_id) and not image[len(product_id)].isdigit():
            result_image_name = os.path.join(IMAGE_OUTPUT, image)
            shutil.copy(
                os.path.join(os.getcwd(), IMAGE_INPUT, image),
                os.path.join(os.getcwd(), result_image_name)
            )
            return result_image_name
    return ''


def prepare_products_for_export(data: list, brand_discounts: dict, images: list) -> list:
    result = []
    for product in data:
        result.append({
            'sku': product['id'],
            'name': product['name'],
            'brand': product['brand'],
            'price': get_product_price(product, brand_discounts),
            'image': get_image_path(product, images)
        })
    return result


if __name__ == '__main__':
    file_path = 'ls10/price.csv'
    brand_discounts = {
        'Matchbox': 0.4
    }
    os.makedirs(IMAGE_OUTPUT, exist_ok=True)

    images = os.listdir(IMAGE_INPUT)
    products = read_products_from_csv(file_path)
    out_products = prepare_products_for_export(products, brand_discounts, images)
    json.dump(out_products, open('ls10/products.json', 'w'))
    print(products)
    print(out_products)

