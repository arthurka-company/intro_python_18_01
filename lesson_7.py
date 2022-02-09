# Функции


# print('Ok')
# value = int('999')
# # int('100g')
#
# print(value)

# type()
# dir()
# float, str, list, dict ...
# len()
# range()
# sorted()
# min()
# max()

import random
from random import randint, choice
import string
import os
from os.path import isfile

# import numpy

# print(random.randint(1, 4))
# print(randint(1, 8))
# print(choice([2, 3]))
#
# print(dir(random))
# random.seed(100)

# l = [1, 2, 3, 4, 5]
# result = random.shuffle(l)  # изменяет объект
# print(l)
# print(result)
#
# print(string.ascii_letters)


import os

# os.makedirs('test_dir', exist_ok=True)
#
# print(os.getcwd())
#
# print(os.path.isdir('test_dir'))
# print(os.path.isdir('test_dir0'))
# print(os.path.isfile('test_dir/test.txt'))
# os.remove('test_dir/test.txt')
# os.rmdir('test_dir')

print(os.path.join('home/tarchanskyj', 'test', 'dir', 'file.py'))

print(os.listdir())
print(os.path.splitext(os.path.join('home/tarchanskyj', 'test', 'dir', 'file.py')))

