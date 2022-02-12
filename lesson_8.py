'''
Even the Last
 Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить
  эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).

'''
#
# def even_the_last(input_array):
#     # if len(input_array) == 0:
#     if not input_array:
#         result = 0
#     else:
#         result = sum(input_array[::2])
#         result = result * input_array[-1]
#     return result
#
#
# print(even_the_last([1, 33, 43, 2323, 44, 5, 0, 4]))
# print(even_the_last([4]))
# print(even_the_last([]))


'''
Three Words
 Давайте научим наших роботов отличать слова от чисел.
Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд .
Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False.
'''

# def is_all_elements_words(input_array):
#     for item in input_array:
#         if not item.isalpha():
#             return False
#     return True
#
#
# def three_word(text):
#     # print(words)  # error
#     words = text.split()
#     print(words)
#     for i in range(len(words) - 2):
#         print(words[i:i + 3])
#         if is_all_elements_words(words[i:i + 3]):
#             # words[0:3]
#             return True
#     return False
#
#
# print(three_word('start 5 one two three 7 end'))
# print(three_word('start 5 one two'))

'''
First Word
 Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:
    В строке могут встречатся точки и запятые
    Строка может начинаться с буквы или, к примеру, с пробела или точки
    В слове может быть апостроф и он является частью слова
    Весь текст может быть представлен только одним словом и все

Входные параметры: Строка.
Выходные параметры: Строка.
'''

# def first_word(text):
#     # words = text.split()
#     # print(words)
#     # result = words[0]
#     # print(result.isalpha())
#     result = ''
#     for i in text:
#         if i.isalpha():
#             result += i
#         else:
#             if result == '':
#                 continue
#             elif i == "'" or i == '-':
#                 result += i
#             else:
#                 break
#
#     return result
#
#
# print(first_word("greet'ings, friends word"))
# print(first_word(". , - ' greet-word, friends word"))


'''
Bigger Price
 Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано в
первом аргументе, а сами данные по товарам будут переданы вторым аргументом.

Вх. данные: Число и список словарей (int and list of dicts). Каждый словарь имеет 2 ключа "name" и "price".
Вых. данные: Такой же как и второй аргумент.

Примеры:
bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]
'''
# import random
#
# def sort_by_price(item):
#     order = {
#         "bread": 0,
#         "wine": 1,
#         "meat": 2,
#         "water": 3
#     }
#     # return item['price'] * random.randint(1, 100)
#     return order[item['name']]
#
#
# def bigger_price(amount, products):
#     # return sorted(products, key=lambda item: item['price'], reverse=True)[:amount]
#     return sorted(products, key=sort_by_price, reverse=True)[:amount]
#
#
# print(bigger_price(2, [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ])
# )

'''
Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.

Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims".
 Если бы нам надо было найти ее первое вхождение, то тут все просто: с помощью
  функции index или find мы можем узнать, что "s" – это самый первый символ в слове
   "sims", а значит индекс первого вхождения равен 0. Но нам необходимо найти вторую
    "s", а она 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.

Input: Две строки (String).

Output: Int or None

Примеры:
second_index("sims", "s") == 3
second_index("find the river and another river", "e") == 12
second_index("hi", " ") is None
'''

# def second_index(main_string, substring):
#     count = 0
#     for idx in range(len(main_string) - len(substring) + 1):
#         if main_string[idx:idx + len(substring)] == substring:
#             count += 1
#         if count == 2:
#             return idx
#     return None
#
# def second_index(main_string, substring):
#     first_in = main_string.find(substring)
#     print(first_in)
#     second_in = main_string.find(substring, first_in + 1)
#     print(second_in)
#     return second_in if second_in > -1 else None
#
# print(second_index("find the river and another river", "w "))


'''
Sort Array by Element Frequency

 Отсортируйте данный итератор таким образом, чтобы его элементы оказались в
 порядке убывания частоты их появления, то есть по количеству раз, которое они появляются в
 элементах. Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в
 котором стояли изначально в итераторе.

Входные данные: Итератор

Выходные данные: Итератор

Пример:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
'''
import collections

def frequency_sort(input_array):
    counter = collections.defaultdict(int)
    for item in input_array:
        counter[item] += 1
    print(counter)
    print(counter.items())
    sorted_array = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    print(sorted_array)
    result = []
    for item in sorted_array:
        result += [item[0]] * item[1]
    return result


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))