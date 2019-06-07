# ！/usr/bin/env python
# -*- coding:utf8 -*-
from functools import reduce


def mutl(x, y):  # lamdba x,y:x*y
    return x * y


temp = [1, 2, 3, 100]


def reduce_test(func, array, init=None):
    if init is None:
        res = temp.pop(0)
    else:
        res = init
    for i in array:
        res = func(i, res)
    return res


print(reduce_test(mutl, temp, 1))  # 600
print(reduce_test(mutl, temp, 100))  # 60000
print(reduce(lambda x, y: x * y, temp, 10))  # 6000
