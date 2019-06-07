#!/user/bin/env  python
# -*- coding:utf-8 -*-
msg = 'i am   %s, my hobby is %s' % ('deany', 'coding')
print(msg)

# 打印浮点数
s1 = 'percent %.2f' % 99.92878876876
print(s1)

# 打印百分比
s2 = 'percent %.2f%%' % 99.92878876876
print(s2)

s3 = 'i am   %(name)s, my age is %(age)d' % {'name': 'deany', 'age': 20}
print(s3)

s4 = 'i am {2},age {1},i like {0}'.format('joke', 20, 'deany')
print(s4)

s5 = 'i am   {name}, my age is {age}'.format(name='deany', age=20)
print(s5)

s6 = 'i am   {name}, my age is {age}'.format(**{'name': 'deany', 'age': 20})
print(s6)

s7 = 'i am   {}, my age is {}'.format(*['deany', 20])
print(s7)


def test(x):
    '''
    :param x:
    :return:
    '''
    y = 2 * x + 1
    return y


print(test(2))


# 位置参数缺一不行多一也不行
# 关键字参数必须在位置参数后面
def handle(x, *args,**kwargs):
    print(x)
    print(args)


handle(1, 1, 2, 3, 4)  # print(args)    #(1, 2, 3, 4)
handle(1, [1, 2, 3, 4])  # print(args)  #([1, 2, 3, 4],)
handle(1, *[1, 2, 3, 4])  # print(args) #(1, 2, 3, 4)
handle(1, {'name': 'deany'})  # print(args) #({'name': 'deany'},)


def handle1(m, **kwargs):
    print(m)
    print(kwargs)
    print(type(kwargs))


handle1(1, x=2, y=3)  # print(kwargs)   #{'x': 2, 'y': 3}
handle1(1, **{'name': 'deany'})  # print(kwargs)    #{'name': 'deany'}

print('------------------------------------------------------')

name = 'abscc'


def fun():
    global name
    name = 'ffff'


fun()
print(name)

tt = 12


def test():
    print(tt)


test()
zz = test()
print(zz)

print('------------------------------------------------------')

mm = '老师'


def outer():
    mm = '学生'

    def inner():
        print(mm)

    return inner


ret = outer()
ret()  # 学生
print(ret)  # inner地址
result = ret()  # 学生
print(result)  # None

print('------------------------------------------------------')


# 利用递归实现1*2*3*4*5*6*7=5040
def digui(w):
    if w == 1:
        return 1

    return w * digui(w - 1)


s = digui(7)
print(s)
