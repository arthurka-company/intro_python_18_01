# Методы строк и списков

# print('|'.join(['12', '23', '34']))
# print('asdfdf, sdfsdf,fsd,ffd,fff  dfdf df '.split(','))
# print('sfsdfdsFDFSDFsdfsfsf '.lower())
# print('sfsdfdsFDFSDFsdfsfsf '.upper())
# print('sfsd,sdfsd,f-thf,fgbfgh '.title())
# print('asdf sd FFFsf sdf '.capitalize())
#
# print('ertyuioo'.find('io'))
# print('ertyuioo'.replace('t', '|||'))
# print('ertyuioo'.replace('o', '11212', 1))
#
# print('asdffd sf sd'.index('ff'))
# print('asdffd sff sd'.rindex('ff'))
# print('asdffd sf sd'.rfind('ff'))

# print('qWertyuiop'.lower().startswith('qwer'))
# print('qwertyuiop'.startswith('qWer'))
# print('qwertyuiop'.endswith('qWer'))
#
# print('qwertewq'.count('er'))
#
# my_str = 'test'
# my_str = my_str.capitalize()
# print(my_str)

# ''.startswith('t')
#
# print('234342'.isdigit())
# print('234342'.isalpha())

# print(dir(''))

# my_list = []
#
# my_list.append('123')
# my_list.append('55')
# my_list.append(345)
# my_list.append([345, 2344])
# my_list = my_list + [345, 2344]
# my_list.extend([44, 55, 66])
# print(my_list)
# my_list.insert(1, 333333)
# my_list.remove(345)
# print(my_list.remove(345))
# print(my_list.pop())
#
# print(my_list)
# print(my_list.count('1234'))
# a = [34, 44, 3, 33]
# a.sort()
# print(a)
# print(my_list.reverse())
# print(my_list.copy())
# my_list.clear()
# print(my_list)


'''
Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
 Если число является частью слова, то его суммировать не нужно.
'''

# text = 'asdff fwef wef 234 fs32 323 sffd 33 sfsf'
# my_list = text.split()
# result = 0
# for word in my_list:
#     if word.isdigit():
#         print(word)
#         result += int(word)
# print(result)
# result = sum([int(word) for word in text.split() if word.isdigit()])
# print(result)


'''
Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив 
изначальные строки запятыми.
 В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова 
 "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре. 
 
 ("brightness wright",)
 
 ("bright aright", "ok")
#  '''
# input_phrase = ("bright aright", "ok", 'right')
# print(','.join(input_phrase).replace('right', 'left'))
#
