# coding=utf-8

def fun1(*args, **kw):
    print(args)
    print('fun1-->', kw)


def fun2(*args, **kw):
    print(args)
    print('fun2-->', kw)


def fun3(*args, **kw):
    print(args)
    print('fun3-->', kw)


fun1(1, 2, 3, 4, name='wang')
fun2([1, 2, 3, 4], name='wang')
fun3((1, 2, 3, 4), name='wang')
fun3(*(1, 2, 3, 4), **{'name': 'wang'})
fun3(*[1, 2, 3, 4], **{'name': 'wang'})


def fun4(x, y, **kw):
    print(x, y)
    print('fun4-->', kw)


fun4(*(1, 2,), **{'name1': 'wang1'})

print('------------')
f1 = 2
f2 = 3
f1, f2 = f2, f1
print(f1, f2)

print('------------')
l = [12, 4, 6, 3, 5, 88, 9, 56]
a, *e, b = l
print(a)
print(*e)
print(b)


def foo(x, y, z):
    print(x, y, z)  # 1 2 3


foo(*[1, 2, 3])
