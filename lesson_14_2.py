# from lesson_14_1 import *
#
#
# t = Test()
#
# t._protected()


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimetr = self.get_perimeter()
        self.square = self.get_square()

    def __repr__(self):
        return f'Class Rectangle, params: {self.a}, {self.b}'

    def __str__(self):
        return f'Rectangle: [{self.a}, {self.b}]'

    def get_perimeter(self):
        return (self.a + self.b) * 2

    def get_square(self):
        return self.a * self.b

    def update_params(self):
        self.perimetr = self.get_perimeter()
        self.square = self.get_square()


# recrangle = Rectangle(10, 15)
# print(recrangle.a, recrangle.b, recrangle.perimetr, recrangle.square)
# recrangle.a = 30
# print(recrangle.a, recrangle.b, recrangle.perimetr, recrangle.square)
# # recrangle.perimetr = recrangle.get_perimeter()
# recrangle.square = recrangle.get_square()
# print(recrangle.a, recrangle.b, recrangle.perimetr, recrangle.square)
# recrangle.update_params()


class SafeRectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.perimetr = self.get_perimeter()
        self.square = self.get_square()

    def get_sides(self):
        return [self.__a, self.__b]

    def set_sides(self, a, b):
        self.__a = a
        self.__b = b
        self.update_params()

    def get_perimeter(self):
        return (self.__a + self.__b) * 2

    def get_square(self):
        return self.__a * self.__b

    def update_params(self):
        self.perimetr = self.get_perimeter()
        self.square = self.get_square()


# s_rect = SafeRectangle(10, 15)
# print(s_rect.__dict__)
# print(s_rect.get_sides())
# # print(s_rect._SafeRectangle__a)
# # s_rect.__a = 30
# s_rect.set_sides(30, 40)
# print(s_rect.__dict__)


class SafeRectangleWithProperty:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.__update_params()

    def __update_params(self):
        self.perimetr = (self.__a + self.__b) * 2
        self.square = self.__a * self.__b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        print('Update rectangle')
        self.__a = value
        self.__update_params()

    @a.deleter
    def a(self):
        print('DELETE')

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        print('Update rectangle')
        self.__b = value
        self.__update_params()


# s_rect = SafeRectangleWithProperty(10, 15)
# print(s_rect.__dict__)
# print(s_rect.a, s_rect.b, s_rect.perimetr, s_rect.square)
# s_rect.a = 100
# s_rect.b = 30
# print(s_rect.__dict__)
# del s_rect.a
