# Создание объекта в памяти и присваивание переменной ссылки на объект
# n = 300
#
# print(n)
#
# n = 400
#
# print(500)
#
# print(id(n), '*')
# m = n
#
# n = 350
#
# print(n, m)
# print(id(n), id(m))

# n = 3000000.6
# m = 3000000.6
# n += 5

# Проверка идентификатора объекта в памяти через id
# n = []
# print(id(n))
# m = []
# n.append(3)
#
# print(id(n), id(m))

# Программа выполняется последовательно (построчно), если в коде ошибка, то все, что до ошибки выполнится.
# n = 350
# print(id(n))
# n = 400
# print('100')
# 3 / 0 - ошибка
# print()

# str = 20
# print(str, type(str))
# s = str(23)
#
# s = str(100)
# print(s, type(s))

# value = 100
# print(value, type(value))
# value = '100'
# print(value, type(value))
# type = 300
# print(type, type(type))


# Слова, которые нельзя использовать для имен переменных
# id = 100

# for = 100

# bool
# print(True, False)
# True = 100


# Строки -------------------------------------
# value = str()
# print(value, type(value))
# value = str(345)
# print(value, type(value))
# value = str(345.44)
# print(value, type(value))

# value = 'ssdfgg er er ege '
# print(value, type(value))

# print('one' + 'two')
# print('one' + ' two')
# print('one', 'two', sep='\n')
# print('one', 'two', sep='|')

# print('one' + ' two')
# print('one ' * 3)


# Bool и сравнения   ---------------------------------------
# flag = True
# print(flag, type(flag))
# value = 2 > 5
# print(value, type(value))
# value = 2 >= 5
# print(value, type(value))
# print(44 == 444)
# print(44 != 444)
# print(44 > 444)
# print(44 >= 444)
# print(44 < 444)
# print(44 <= 444)
# value = 300
# print(44 < value < 444)

# print('a' < 'b454')
# print(ord('a'), ord('b'))

# print('a' in 'qwearty')
# print('asdfdf' in 'qwearasdfdfty')
# print('asd' == 'asd')
# print('asd' != 'asds')
# print('asd' != 'asd')
# print('asd' not in 'fwefwef')

# ==  - сравнение значения переменных
# is  - сравнение ссылок на объекты в памяти

# n = 1000
# m = 1000
#
# print(n == m)
# print(n is m)
# print(n is not m)
#
# k = n
#
# print(k == m)
# print(k is m)


# and  И
# or  ИЛИ

# print(12 == 12 and 45 == 45 and 34 == 34)
# print(12 != 12 or 45 == 45 or 34 != 34)
#
# # value = 12 <= 12 and 45 == 45 and 34 == 34
# # value = (12 + 100) * 45 > 100
# # n = 1000
# # value = (n + 100) * 45 == 100
# n = '1000'
# value = (int(n) + 100) * 45 == 100 and 1 == 1
# print(value, '**')


# Ввод значений через консоль
# print('100')
# input('Ok:')


# value = input('Type some int: ')
# print('You typed:', value, type(value))
# new_value = int(value)
# print(new_value)


# print('Площадь прямоугольника:')
# a = input('Введите первую сторону: ')
# b = input('Введите первую сторону: ')
# # a = int(a)
# # b = int(b)
# a, b = int(a), int(b)
# s = a * b
# print('Площадь прямоугольника равна:', a * b)
# print('Площадь прямоугольника равна:', s)

# n = m = k = 520 + 66
# print(n, m, k)
# print(n is m is k)


# Конкатенация строк
a = 'one'
b = 'two'
c = f'three'
print(a + b)
print(c)

# print(f'Value 1 is: {4000}')
print(f'Value 1 is: {a}, value 2 is: {b} and value 3 is: {c}')
print('Value 1 is: ' + a + ', value 2 is: ' + b + ' and value 3 is: ' + c)
print('Value 1 is: {}, value 2 is: {} and value 3 is: {three}'.format(a, b, three=c))
print('Value 1 is: %s, value 2 is: %s and value 3 is: %s' % (a, b, c))
print('Value 1 is: %s, value 2 is: %s and value 3 is: %d' % (a, b, 100))
# print('Value 1 is: ' + 4000)



