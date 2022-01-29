# for
# list and tuple, список и кортеж


########################  list and tuple ###################################
# my_list = list()
# my_tuple = tuple()
# my_list_1 = []
# my_list_2 = [12, 34, 45.23, 'hrtgrg', 'rtgrtg', None, [], [34, 44], my_tuple]
# print(my_list_1, my_list, my_list_2)
# my_tuple = tuple()
# print(type(my_list), type(my_tuple))
# 'sdfsdf'[3]
# [23, 34, 45][2]

################### проход по элементам списка
# i = 0
# while i < len(my_list_2):
#     print(my_list_2[i], type(my_list_2[i]))
#     i += 1
# #
# #
# # points = [[0, 0], [3, 4]]
#
#
# my_tuple = tuple()
# my_tuple_1 = ()
# my_tuple_2 = (1,)
# my_tuple_3 = (1, 56, 'wefefw', None, [], (34, 3434))
# l = [3]
# print(type((32,)))
# print(my_tuple_3, type(my_tuple_3))
# print(my_tuple_3[2:])
# print(my_tuple_3[2])
# print(my_tuple_3[::-1])
# print('')
# print(my_list_2)
# print(my_list_2[::-1])
#
# my_list = [12, 34, 45.23, 'hrtgrg', 'rtgrtg', None, [], [34, 44, 333]]  # изменяемый
# my_tuple = (1, 56, 'wefefw', None, [], (34, 3434))  # неизменяемый
#
# # 1
# print(id(my_list), id(my_tuple))
# my_list.append(55)
# my_tuple = my_tuple + (34,)
# print(my_list)
# print(my_tuple)
# print(id(my_list), id(my_tuple))
#
# # 2
# my_str = 'test'
# # my_str[2] = '3'
# my_list[0] = 1000
# print(my_list[-2][1])
# print(my_tuple[-2][1], '**')
# # my_tuple[0] = 1000
# print(my_list, my_tuple, my_str)

#
# matrix = [
#     [1, 2, 4],
#     [2, 4, 5]
# ]

##################### создание списка или кортежа из строки
# n = str(23424)
# my_list = list('my test string for list creation')
# my_tuple = tuple('my test string for list creation')
# print(my_list)
# print(my_tuple)
#
# # words = 'my    test string for list creation'.split()
# # words = 'my    test string for list creation'.split(' ')
# # words = 'my    test string for list creation'.split('test')
# words = 'my     test string for list creation'.split()
# my_str = ' '.join(words)
# my_str = '/'.join(['', 'home', 'user', 'project'])
# print(words)
# print(my_str)


############################# чтение элементов массива несколькими способами: индек и while, pop and while, for
# words = 'my    test string for list creation'.split()
# i = 0
# while i < len(words):
#     print(words[i])
#     i += 1
#
# print(words.pop())
# print(words.pop())
# print(words)

# words = words[::-1]
# while len(words) > 0:
#     print(words.pop())
#     print(words[::-1].pop())

# for value in words:
#     print(value)

# for value in 'words':
#     print(value)
#
# for page in range(1, 4):
#     print(page)

#
# if False:
#     print('1')
# elif False:
#     print('2')
# else:
#     print('3')
# print('End')

###################### len, range
# for page in [1, 2, 3]:
#     print(page)
#
# for page in range(0, 4):
#     print(page)

# for idx in range(len(words)):
#     print(idx, words[idx])

################################ break continue

# for i in range(200):
#     if i % 10 == 0:
#         print('10')
#     elif i > 100:
#         break
#     else:
#         continue
#     print(i, '//////////')
# print('end')


# Получить строку, в которой все слова будут развернуты, но порядок слов остается прежним
# text = 'my    test string for   list creation trim'
# # ym     tset ...
# new_list = []
# words = text.split()
# print(words)
#
# for word in words:
#     if word[0].lower() == 't':
#         new_list.append(word)
# print(new_list)

# in_text = 'my    test string for list creation'
# words = in_text.split(' ')
# new_list = []
# print(words)
# for word in words:
    # reversed_word = word[::-1]
    # new_list.append(reversed_word)
    # new_list.append(word[::-1])
# print(new_list)
# out_text = ' '.join(new_list)
# print(in_text)
# print(out_text)


##############################  создание списка через цикл for, решение задачи в одну строчку
# my_list = [i ** 2 for i in range(10) if i % 2 == 0]
# my_list = [i[::-1] for i in words]
# my_str = ' '.join([i[::-1] for i in words])
in_text = 'my    test string for list creation'
my_str = ' '.join([i[::-1] for i in in_text.split(' ')])
# print(my_list)
print(my_str)
