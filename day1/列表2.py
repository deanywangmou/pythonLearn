#!/usr/bin/env   python
# -*_  coding:utf8  -*-
test1 = 'wangmou'
t1 = test1[1]  # 获取字符对应下表的某一个字符
print(t1)  # a

t2 = test1[0:2]  # 获取字符某一个范围内对应的字符串，范围位左开右闭，-1为最后一个位置
print(t2)  # wa

t3 = len(test1)  # 获取字符的长度
print(t3)  # 7

for x in test1:
    print(x)

t4 = test1.replace('wa', 'De')  # 替换，test1.replace（'wa','De'，1）只替换第一个值
print(t4)  # Dengmou

v = range(0, 100, 5)
for q in v:
    print(q)

for i in range(100, 0, -5):
    print(i)

# aa=input()
# l=len(aa)
# yy=range(0,l)
# for n in yy:
#     print(n,aa[n])
#
# for n in  range(0,len(aa)):
#     print(n,aa[n])

