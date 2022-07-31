"""
@Time:2021/7/18 19:30
@Author:deanywang
@File:斐波那契数列.py
@return:""
"""


# 0 1 1 2 3  5 8 13 21 35
def feiBo(k):
    sum = 0
    sumList = []
    for i in range(k + 1):
        sum = sum + i
        if i <= 1:
            sum = i
            sumList.append(sum)
            # print("斐波那契数列"+str(sumList))
        elif i == 2:
            sum = 1
            sumList.append(sum)
        else:
            sum = sumList[-1] + sumList[-2]
            sumList.append(sum)
            # return sum
    print("斐波那契数列" ,sumList)


k = int(input("请输入参数："))
feiBo(k)


# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 斐波那契数列

# def fib(n):
#     a, b = 1, 1
#     for i in range(n-1):
#         a, b = b, a+b
#     return a
#
# # 输出了第10个斐波那契数列
# print(fib(10))



# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
