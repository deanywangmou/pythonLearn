# coding=utf-8
def foo1(x, y, *args):
    print(x, y)  # 1 2
    print('foo1-->', args)  # (3, 4, 5)


foo1(1, 2, 3, 4, 5)


def foo2(x, y, *args):
    print(x, y)  # 1 2
    print('foo2-->', args)  # (3, 4, 5)


foo2(1, 2, *[3, 4, 5])


def foo3(x, y, z):
    print('foo3-->', x, y, z)  # 1 2 3


foo3(*[1, 2, 3])


# ===========**kwargs===========
def foo4(x, y, **kwargs):
    print(x, y)  # 1 2
    print('foo4-->', kwargs)  # {'a': 1, 'b': 2, 'c': 3}


foo4(1, y=2, a=1, b=2, c=3)


def foo5(x, y, **kwargs):
    print(x, y)  # 1 2
    print('foo5-->', kwargs)  # {'a': 1, 'b': 2, 'c': 3}


foo5(1, y=2, **{'a': 1, 'b': 2, 'c': 3})


def foo6(x, y, z):
    print('foo6-->', x, y, z)  # 2 3 1


foo6(**{'z': 1, 'x': 2, 'y': 3})


# 5、命名关键字参数：*后定义的参数，必须被传值（有默认值的除外），且必须按照关键字实参的形式传递
# 可以保证，传入的参数中一定包含某些关键字
def foo7(x, y, *args, a=1, b, **kwargs):
    print(x, y)  # 1 2
    print(args)  # (3, 4, 5)
    print(a)  # 1
    print(b)  # 3
    print(kwargs)  # {'c': 4, 'd': 5}


foo7(1, 2, 3, 4, 5, b=3, c=4, d=5)
