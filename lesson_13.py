# ООП - объектно-ориентированное программирование
# класс
# атрибут класса
# экземпляр (объект) класса
# метод класса

# def make_lower_symbol(symbol: str) -> str:
#     mapping = {
#         'W': 'w'
#     }
#     return mapping[symbol]
#
# 'WWWord'.lower()
# value = 'WWWord'
# new_value = ''
# for i in value:
#     if i in 'QWEQREWWETT':
#         new_value += make_lower_symbol(i)
#     else:
#         new_value += i
#
# print(new_value)
#
# print(value.lower())


class Student:
    pass

obj = Student()
# print(type(obj))


class Rectangle:
    a = 0
    b = 0

    def get_perimeter(self, test=None):
        return (self.a + self.b) * 2

rect = Rectangle()

print(rect)
print(type(rect))


def create_class_obj(class_type):
    return class_type()

rect_2 = create_class_obj(Rectangle)
# rect_2 = create_class_obj(Student)
print(rect_2, type(rect_2))

print(rect_2.b, rect_2.a)
rect_2.a = 23
print(rect_2.b, rect_2.a, rect_2.get_perimeter())
print(rect.b, rect.a)


