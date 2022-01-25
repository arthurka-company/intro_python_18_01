# if else
# while


# if условие:
#     блок действий если ДА
# elif условие_2:
#     блок действий если ДА
# elif условие_2:
#     блок действий если ДА
# else:
#     блок действий если НЕТ

# exit()

# a = 100
#
# if a > 70:
#     print('70')
# elif a > 50:
#     print('50')
# else:
#     print('False')


a = 73

# if a > 70:
#     print('70')
#     if a == 73:
#         print('Ok')
#     else:
#         print('Not Ok')
# elif a > 50:
#     print('50')
# else:
#     print('False')


# if a > 100 and a < 1000:
#     print('ok')
# if 100 < a < 1000:
#     print('ok')

# 0, '', [], None - False
# 1 не пустое значение - True

# if []:
#     print('True')
# else:
#     print('False')

# value = input('Введите что-то:')
# if value.isdigit():
#     value = int(value)
#     print(f'Input: {value}. Result: {value * 2}')
# elif len(value) > 5:
#     print('Too long value')
# elif value[0] == 'a':
#     print('First symbol is \'a\'')


######################################################################################
# Работа со строками: срезы

value = 'qwerty'
# print(value[0])
# print(value[1:])
# print(value[1:4])
# print(value[-1])
# print(value[-2])
# print(value[:4])
# print(value[::2])
# print(value[1::2])
# print(value[::-1])
# print(value[::-2])

# value_2 = value[::-1]
# print(value, value_2)
# print(value[-2:])

# index = 1
# print(value[index])
# print(value[index:])

#########################################################################################
# тернарный оператор

# condition = 50
# # value
# if condition > 90:
#     value = condition * 2
# else:
#     value = condition / 2
#
# print(value)
#
# # value = значение_если_ДА if Условие else значение_если_НЕТ
#
# value = condition * 2 if condition > 90 else condition / 2
# print(value)

# func_result = ''
# func_result = '234'
# func_result = None
# # value = func_result or 'Bad value'
# value = func_result or 0
# print(value)


#####################################################################################3
# Цикл while

# while условие:
#     Если ДА

# number = 3
# i = 0
# while i < 10:
#     number *= 2  # number = number * 2
#     print(number, i)
#     i += 1
# print(number, i)
#
# while True:
#     # print('Ok')
#     value = input('Type int: ')
#     if value.isdigit():
#         print('Good!')
#         break
# print('Finish')


value = 'Input second input'
i = 0
word = ''
while i < len(value):
    element_of_the_string = value[i]
    if element_of_the_string != ' ':
        word += element_of_the_string
    else:
        print(word)
        word = ''
    i += 1
print(word)
