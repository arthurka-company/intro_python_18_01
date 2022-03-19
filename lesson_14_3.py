# Наследование
from lesson_14_2 import SafeRectangleWithProperty


class Rectangle(SafeRectangleWithProperty):
    pass


class MyClass:
# class MyClass(object):
    pass


# rect = Rectangle(12, 14)
# print(rect.__dict__)
# print(rect.a, rect.b)
# rect.a = 15
# print(rect.__dict__)


class Square(SafeRectangleWithProperty):
    def __init__(self, a, b):
        self.validate_params(a, b)
        self._SafeRectangleWithProperty__a = a
        self._SafeRectangleWithProperty__b = b
        self._SafeRectangleWithProperty__update_params()

    def validate_params(self, a, b):
        if a != b:
            raise ValueError('Sides must be equal')


# square = Square(12, 2)
# print(square.a, square.b, square.perimetr)


class NewStr(str):
    def __gt__(self, other):
        # print('0000okok', type(other))
        if isinstance(other, int) or isinstance(other, float):
            # print(other)
            return self > str(other)
        return super().__gt__(other)


# value = NewStr('5')
# print(value)
# print(value < 344.4)



#
#
# from django.views import ListView
# from braces.views import LoginRequiredView
# from some_packege import some_func
#
#
# class ProductListView(LoginRequiredView, ListView):
#     model = Product
#     template_name = 'templates/product_list.html'
#     html_objects_name = 'products'
#     redirect_url = ''
#
#
# class CategoryListView(ListView):
#     model = Category
#     template_name = 'templates/category_list.html'
#     html_objects_name = 'categories'
#
#
# urls = ['name/products', ProductListView.as_view(), name='products']


class Class1:
    atr_1 = 100
    atr = 30
    def foo_1(self):
        print('1')


class Class2:
    atr_2 = 200
    atr = 40
    def foo_2(self):
        print('2')


# class Class3(Class1, Class2):
class Class3(Class2, Class1):  # for python 3 <-.  for python 2 ->  порядок наследования классов
    pass


obj = Class3()
print(dir(obj))
print(obj.atr_1, obj.atr_2, obj.atr)

# print 1000  # python 2
print(1000)

# dict_1.update(dict_2)