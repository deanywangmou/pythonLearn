#!/usr/bin/env  python
# -*- coding:utf8 -*-
# 高阶函数：1.函数接收的参数是一个函数名  2.返回的值包括函数
def test1():
    print('from  test1')


def test2():
    print('from test2')
    return test1()


test2()
