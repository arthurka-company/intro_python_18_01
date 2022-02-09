# валидация названия треугольника
# совпадение координат точек
# Задать значения по-умолчанию для лимитов координат
from random import randint

MIN_LIMIT = -50
MAX_LIMIT = 50


def create_point(min_limit, max_limit):
    point = {
        'x': randint(min_limit, max_limit),
        'y': randint(min_limit, max_limit),
    }
    return point


def create_triangle(name, min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    assert isinstance(name, str)
    assert len(name) == 3
    assert len(set(name)) == 3
    flag = False
    while not flag:
        tringle = {key: create_point(min_limit, max_limit) for key in name}
        flag = validate_triangle(tringle)
    return tringle


def validate_triangle(triangle):
    # print('111111')
    if len(set([i['x'] for i in triangle.values()])) != 3:
        return False
    if len(set([i['y'] for i in triangle.values()])) != 3:
        return False
    return True


# []
# {}
# set()
# {1, 3, 5}

# assert isinstance(3345, int)
# print(create_triangle('abc', -10, 10))
# print(create_triangle('klm'))

my_list = ['abc', 'klm', 'dug']
for name in my_list:
    print(create_triangle(name))


# d = {'a': {'x': 42, 'y': -49}, 'b': {'x': 42, 'y': -30}, 'c': {'x': -17, 'y': -44}}
# # for i in d.values():
# #     print(i)
# #     print(i['x'])
#
# my_list = [i['x'] for i in d.values()]
# print(my_list)
# my_set = set(my_list)
# print(my_set)