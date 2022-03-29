# Декораторы
# from lesson_10 import *  # Bad practice
from lesson_10 import lesson_10_fuction_1, lesson_10_fuction_2, lesson_10_fuction_3
from lesson_10 import (
    lesson_10_fuction_1,
    lesson_10_fuction_2,
    lesson_10_fuction_3,
)
from lesson_10 import GeometryClass
import time
import math
import numpy


class MyClass:
    CONST = math.pi
    FIELDS = [
        'name',
        'id',
        'metadata',
    ]

    def __init__(self, args):
        self.args = args

    def get_args(self):
        return self.args

    def do_smth(self):
        print(self.args)

    @staticmethod
    def get_current_time():
        print(time.time())

    @classmethod
    def get_some_number(cls, value):
        return cls.CONST * value

    @classmethod
    def get_class_fields(cls):
        return cls.FIELDS


# MyClass
obj = MyClass(args=[34, 44])
obj.do_smth()
args = obj.get_args()
print(args, 'res')

obj.get_current_time()

MyClass.get_current_time()
print(obj.get_some_number(40), '**')
print(MyClass.get_some_number(40), '**')
print(MyClass.get_class_fields())
print(MyClass.FIELDS)
