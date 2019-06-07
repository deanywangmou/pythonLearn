#!/usr/bin/env python
# -*- coding:utf8 -*-

# 内置函数map
tem = [2, 5, 12, 8, 99, 122, 55]


def add_one(x):  # lambda x:x+1
    return x + 1


def demo(func, array):
    methon = []
    for i in array:
        res = func(i)
        methon.append(res)
    return methon


print(demo(add_one, tem))  # [3, 6, 13, 9, 100, 123, 56]
print(demo(lambda x: x + 1, tem))  # [3, 6, 13, 9, 100, 123, 56]
print('内置函数map：', list(map(add_one, tem)))  # 内置函数map： [3, 6, 13, 9, 100, 123, 56]
print('内置函数map：', set(map(add_one, tem)))  # 内置函数map： {3, 100, 6, 9, 13, 56, 123}
