# Декораторы

#
# def decorator_func(func):
#     print('In decorator')
#
#     def wrapper():
#         print('Before main func run')
#         func()
#         print('After main func run')
#     return wrapper
#
#
# @decorator_func
# def my_func():
#     print('My func')
#
#
# my_func()

import time


def time_decorator(func):
    def wrapper(*args):
        print(args)
        start_time = time.time()
        res = func(*args)
        print('Time:', time.time() - start_time)
        return res
    return wrapper


@time_decorator
def factorial(number):
    res = 1
    for i in range(1, number):
        res *= i
    return res


@time_decorator
def factorial_of_sum(value_1, value_2):
    res = 1
    for i in range(1, value_1 + value_2):
        res *= i
    return res


# print(factorial(number=4000))
# factorial(400000)

# for i in [10, 100, 1000]:
#     factorial(i)

factorial_of_sum(12, 22)
factorial_of_sum(12, 220)