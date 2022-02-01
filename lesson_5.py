# values = [1, 2, 3]
# new_values = values.copy()
# new_values.append(50)
# values[0] = 100
# print(values)
# print(new_values)
# print(id(values), id(new_values))


# values = (1, 2, 3)
# new_values = values
# new_values += (23,)
# # values[0] = 100
# print(values)
# print(new_values)
# print(id(values), id(new_values))

# list, int, tuple

# import random
# from random import randint
# #
# # print(random.randint(1, 100))
# # values = [random.randint(0, 200) for _ in range(20)]
# # print(values)
# # print(len(values))
#
# print(random.choice('qwertty'))
# print(random.choices('qwertty', k=3))

'''
У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
'''

# a, b = [1, 2]
# print(a, b)
# # # my_str, my_symbol = "blablacar", "bla"
# my_str = "blablacar"
# my_symbol = "bla"
# print(my_str.count(my_symbol))
# count = 0
# for idx in range(len(my_str)):
# # for idx, _ in enumerate(my_str):
#     if my_symbol == my_str[idx + 10:idx + 10 + len(my_symbol)]:
#         count += 1
# print(count)

# print([1, 2, 3][:100])


'''
У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать столько раз my_symbol, сколько он встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
'''
# my_str = "blablacar"
# my_symbol = "bla"
# for _ in range(my_str.count(my_symbol)):
#     print(my_symbol)
#
# result = f'{my_symbol}\n' * my_str.count(my_symbol)
# print(result)


'''
У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько
РАЗНЫХ символов встречается в my_str.
Большая и маленькая буква считается как одинаковый символ.
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car".
Вывод на экран:
'''
# my_str = "bla BLA car"
# my_str_lower = my_str.lower()
# result = []
#
# for i in my_str_lower:
#     if i not in result:
#         result.append(i)
# print(len(result))
#
# # set()
# print(len(set(list(my_str_lower))))
# str_to_list = list(my_str_lower)
# list_to_set = set(str_to_list)
# print(len(list_to_set))
# print(set(my_str_lower))
#
# unique_list = list(set(str_to_list))


'''
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str,
которые стоят на четных местах в строке (считаем с 0)
'''
# my_str = 'wofjiefjowqeifjofj'
# my_list = []
# for i in range(len(my_str)):
#     if i % 2 == 0:
#         my_list.append(my_str[i])
# print(my_list)
#
# my_list = list(my_str[::2])
# print(my_list)


'''
Дана строка my_str, список str_index целых чисел в диапазоне от
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с
индексами из str_index
'''
# my_str = "qwerty"
# my_list = []
# str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
#
# for idx in str_index:
#     my_list.append(my_str[idx])
# print(my_list)
#
# my_list = [my_str[idx] for idx in str_index]
# print(my_list)
#

"""
Есть целое число. Посчитать количество цифр
"""
# my_number = 1241234982394812948
# int_to_str = str(my_number)
# print(len(int_to_str))
# print(len(my_number))

'''
Дано целое число. Определить наибольшую цифру в этом числе
'''
# my_number = 1241234823481248
# my_str = str(my_number)
# my_list = [int(i) for i in my_str]
# # max, min
# print(max(my_list))
#
# print('0' > '9')
# print(ord('D'), ord('9'))
# print(chr(68), chr(57))
# print(max(str(my_number)))

'''
Дано целое число. Составить число (int) с цифрами в обратном порядке.
'''

# my_number = 1241234823481248
# print(int(str(my_number)[::-1]))


'''
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
'''
# my_number = 1241234823481248
# my_str = str(my_number)
# sorted_list = sorted(my_str, reverse=False)
# print(type(str(sorted_list)))
# print(''.join(sorted_list))
#
# n_list = [123, 33, 3, 232]
# n_list.sort(reverse=True)
# print(n_list)


# Множества

# set, frozenset


# my_list = [1, 3, 34, 44, 34, 3]
#
# my_set = set(my_list)
# my_set_2 = {1, 3, 34, 44, 34, 3}
# # my_set_3 = {}  # dict
# my_set_3 = set()  # set
#
# print(set([23, 3]))
# print(set((23, 3)))
# print(set('wefwewf'))
#
# print(type(my_set_3))
# print(my_set)
# print(my_set_2)

import random
# Уникализация списка
# my_list = [1, 3, 34, 44, 34, 3]
# unique_list = list(set(my_list))
#
# my_set_1 = {random.randint(10, 50) for _ in range(20)}
# my_set_2 = {random.randint(10, 50) for _ in range(20)}
# print(my_set_1)
# print(my_set_2)
#
# print(my_set_1.intersection(my_set_2), 'intersection')
# print(my_set_1.difference(my_set_2), 'difference')
# print(my_set_2.difference(my_set_1), 'difference')
# my_list = [1, 3, 34, 44, 34, 3]
# unique_set = set(my_list)
#
# print(unique_set)
#
# unique_set.add(44)
# print(unique_set)
#
# print(33 in unique_set)
# print(44 in unique_set)
# print(unique_set.pop())
# unique_set.remove(44)
# unique_set.clear()
# print(unique_set)

my_list = [1, 3, 34, 44, 34, 3]
unique_set = frozenset(my_list)
