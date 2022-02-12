global_number = 100


def some_func(a):
    global global_number
    print(a)
    print(global_number)
    global_number = 20
    b = 200
    print(b)


print(global_number)
b = 33
print(b)
some_func(10000)
print(b)
print(global_number)