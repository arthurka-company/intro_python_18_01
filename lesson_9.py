from typing import Any


def foo() -> int:
    print('ok')
    return 100

#
# d = 45
# s = '333'
# # s = foo()
# f = foo
# print(d, s, f)
# f()
#
# # print(foo())
# print(foo)


def test_func(value: Any) -> None:
    value()
    print(value())

import os
test_func(foo)
test_func(os.getcwd)


def runner(list_to_execute, image):
    for func in list_to_execute:
        image = func(image)
    return image

flow = {
    '1': [flip, blend, blur],
    '2': [flip],
}

res = runner(flow['1'], image)