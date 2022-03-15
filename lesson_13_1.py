# ООП - объектно-ориентированное программирование
# класс
# атрибут класса
# экземпляр (объект) класса
# метод класса

# __new__ -> __init__

class Rectangle:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.additional_arg = 'Ok'
        self.p = self.get_perimeter()

    def __repr__(self):
        # print('repr')
        return f'Class Rectangle, params: {self.a}, {self.b}'

    def __str__(self):
        # print('str')
        return f'Rectangle: [{self.a}, {self.b}]'

    def get_perimeter(self, test=None):
        print('Perimetr')
        return (self.a + self.b) * 2

rect = Rectangle(a=12, b=22)

print(rect.b, rect.a, rect.additional_arg, rect.p)

print(repr(rect))
print(rect)

number = 100
print(number)
int()




