#!/usr/bin/env  python
# -*- coding:utf8  -*-

# 三元表达式
name = 'deanywang'
res = ('SB' if name == 'deany' else 'NB')
print(res)

# 只能用if不能用else
li = ['python%s' % i for i in range(10) if i > 5]
print(li)

# 1.生成器表现形式1，把列表解析的[]换成()得到的就是生成器表达式
chicken = ('小鸡%s' % i for i in range(10))  # 生成器表达器
print(chicken.__next__())
print(next(chicken))
print(next(chicken))
print(next(chicken))
print(next(chicken))
print(next(chicken))


# 2.生成器表现形式2
def test():
    yield 1
    yield 2
    yield 3


res1 = test()
print(res1)
print(res1.__next__())
print(next(res1))
print(res1.__next__())


# 缺点 1：占空间大
#     2.效率低
def xiadan():
    ret = []
    for i in range(100):
        ret.append('鸡蛋%s' % i)
    return ret


print(xiadan())


# 生成器函数
def xiadan1():
    for y in range(100):
        yield '鸡蛋%s' % y


ff = xiadan1()
print(ff)  # 迭代器对象
for k in range(100):
    chidan1 = ff.__next__()
    print('吃鸡蛋', chidan1)
# chidan2 = ff.__next__()
# print('吃鸡蛋', chidan2)
# chidan3 = ff.__next__()
# print('吃鸡蛋', chidan3)
# chidan4 = xiadan1().__next__()
# print('吃鸡蛋', chidan4)

# for z in ff:
#     print(z)