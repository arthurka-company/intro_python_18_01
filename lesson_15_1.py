# Полиморфизм

print(12 + 12)
print('12' + '12')
print(['12'] + [23])

# print({'test': 33} + {'test_2': 34})


class MyDict(dict):
    def __add__(self, other):
        self.update(other)
        return self


print(MyDict({'test': 33}) + MyDict({'test_2': 34}))

obj.calcualte_square()

class Rectangle:
    pass

class Circle:
    pass


def return_square(obj):
    if isinstance(obj, Rectangle):
        value = 100
    elif isinstance(obj, Circle):
        value = 200
    return value


def return_square(obj):
    return obj.calcualte_square()


class Auto:
    pass

class Velo:
    pass


def fabric(obj_type=''):
    if obj_type = 'auto':
        return Auto()
    if obj_type = 'velo':
        return Velo()

