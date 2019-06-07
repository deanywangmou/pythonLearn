#!/usr/bin/env  python
# -*-  coding:utf8  -*-

# 元组tuple，元素不可被修改，并且元组不能被增加或者删除，可以查看
# 一般写元组的时候，后面加个,号不报错
# 1.获取元组值，可通过索引和切片方法
tu1 = ('abc', 11, 22, 33, [11, 22, 33, 44], (1, 2, 3,), True,)
s1 = tu1[0]  # 通过索引值获取值
print(s1)  # abc
s2 = tu1[1:4]  # 通过切片获取值
print(s2)  # (11, 22, 33)

for i in tu1:
    print(i)

# 2.字符串和列表转换成元组
ss = "abcdefghijklmn"
li = [12, 13, True, 'abc', 110, ]
s3 = tuple(ss)
print(s3)  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n')
s4 = tuple(li)
print(s4)  # (12, 13, True, 'abc', 110)

# 3.元组转换成列表
tu2 = ('abc', 11, 22, 33, [11, 22, 33, 44], (1, 2, 3,), True,)
s5 = list(tu2)  # ['abc', 11, 22, 33, [11, 22, 33, 44], (1, 2, 3), True]
print(s5)

# 4.当元组中只有字符串时，将元组转换成字符串可以使用join方法
tu3 = ("wang", "mou",)
s6 = '_'.join(tu3)  # wang_mou
print(s6)

# 当元组中有数字时，只能通过for循环转换成字符
tu4 = (12, 123, 'sds', 'waeefwe',)
sss = ''
for m in tu4:
    sss += str(m)
print(sss)

# 5.extend是扩展源列表,如果extend一个字符串，则会把每个字符串拆分元素加入到列表中
li = [12, 123, 'sds', 'waeefwe']
li.extend((11, 22, 33,))
print(li)  # [12, 123, 'sds', 'waeefwe', 11, 22, 33]
li.extend("deany")
print(li)

# 修改元组中列表元素
tu6 = [12, 123, 'sds', [(34, 55)], 'waeefwe', ]
tu6[3][0] = (23, 22, 44,)
print(tu6)  # [12, 123, 'sds', [(23, 22, 44)], 'waeefwe']

tu7 = (13, 32, 44, 55, 66, 88, 44, 11,)
s7 = tu7.count(44)  # 统计元组中某个元素的个数
print(s7)  # 2
s8 = tu7.index(44, 3, 8)  # 可以指定列表首位位置li7.index(33，2，5)，不加首位位置只查找元素第一次出现的索引值
print(s8)  # 6


