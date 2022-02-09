# def func_name(argument_1, argument_2, argument_3=5):
#     print(argument_1, argument_2, argument_3)
#     return True
#
#
# func_name(1, 2)
# func_name(10, 2, 22)
# # func_name()  # error
# func_name(argument_2=2, argument_1=23)
# func_name(2, argument_2=2)
# # func_name(argument_1=2, 300)  # error

from random import randint

# point_A = {
#     'x': randint(-50, 50),
#     'y': randint(-50, 50),
# }
# point_B = {
#     'x': randint(-50, 50),
#     'y': randint(-50, 50),
# }
# point_C = {
#     'x': randint(-50, 50),
#     'y': randint(-50, 50),
# }
#
# triangle_ABC = {
#     'A': point_A,
#     'B': point_B,
#     'C': point_C
# }
# # triangle_KLM = {}
# print(triangle_ABC)


def create_point(min_limit, max_limit):
    point = {
        'x': randint(min_limit, max_limit),
        'y': randint(min_limit, max_limit),
    }
    return point


def create_triangle(name, min_limit, max_limit):
    tringle = {}
    for point in name:
        tringle[point] = create_point(min_limit, max_limit)
    return tringle

# print(create_point(-50, 50))
# print(create_point(-50, 50))
# print(create_point(-50, 50))
# print(create_point(-50, 50))

print(create_triangle('abc', -10, 10))
print(create_triangle('abc', -10, 10))
print(create_triangle('abc', -10, 10))

# валидация названия треугольника
# совпадение координат точек
# Задать значения по-умолчанию для лимитов координат



