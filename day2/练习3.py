#!/usr/bin/env  python
# -*- coding:utf8  -*-
# 1.找出两个列表中相同的元素
li1 = [11, 22, 33]
li2 = [44, 22, 33]
for i in li1:
    if i in li2:
        print(i)

# 找出两个列表中不同的元素
li1 = [11, 22, 33]
li2 = [44, 22, 33]
for i in li1:
    if i not in li2:
        print(i)
for i in li2:
    if i not in li1:
        print(i)
print('--------------------------------')

# 2.有12345678这8个数，能组成多少个互不相同且无重复的的两位数数字
li3 = [1, 2, 3, 4, 5, 6, 7, 8]
li4 = [1, 2, 3, 4, 5, 6, 7, 8]
for m in li3:
    for n in li4:
        if m != n:
            print(m, n)
        elif n == m:
            print(m, n)

count = 0
for m in range(1, 9):
    for n in range(1, 9):
        if m != n:
            count += 1
print(count)
print('------------------------------------')

# 3.输出一个九九乘法表
for m in range(1, 10):
    string = ''
    for n in range(1, m + 1):
        string += (str(n) + '*' + str(m) + '=' + str(m * n) + '\t')
    print(string)

# print用法
print('aaa', end='')
print('bbb')
print('abc', 'efg', 'higk', sep='-', end='')
print('-------------------------')

# 4.一个列表有有多个字符，选择两个字符两两组合，字符不重复，请问组合方式有哪些
li5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
l = len(li5)
count=0
for k in range(0, l - 1):
    for v in range(k + 1, l):
        print(li5[k], li5[v], sep='')
        count+=1
print()
print('组合的方式数量有：',count)

# 5.公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱卖100只鸡，其中公鸡、母鸡
# 小鸡必须要有，问公鸡、母鸡小鸡要买多少只刚好凑足100文钱
for x in range(1, 100 // 5):
    for y in range(1, 100 // 3):
        for z in range(1, 101):
            if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
                print(x, y, z)
# 6.请用代码实现，利用下划线将列表中的每一个元素拼接成字符串，li=['wang','mou','deany']
li = ['wang', 'mou', 'deany']
str1 = '_'.join(li)
print(str1)
print('-------------------------------------------------')

# 元组操作
tu = ('alex', 'eric', 'rain')
print(tu[1])
print(tu[0:2])
for w in range(len(tu)):
    print(w)
for idex in enumerate(tu, 10):
    print(idex)

# 8.有一列表nums=[2,7,11,15,1,8,7]，请找到列表中任意两个元素相加等于9的集合，如:[(4,5),(1,7)]
nums = [2, 7, 11, 15, 1, 8, 7]
aa = []
for u in nums:
    for v in nums:
        if u + v == 9:
            aa.append((u, v))
print(aa)

# 9.有一列表nums=[2,7,11,15,1,8,7]，请找到列表中任意两个元素相加等于9的集合的索引值，如:[(4,5),(1,7)]
nums = [2, 7, 11, 15, 1, 8, 7]
bb = []
for x in range(len(nums)):
    for y in range(x,len(nums)):
        if nums[x] + nums[y] == 9:
            bb.append((x, y))
print(bb)

# 10.页面分页
user_list = []
for i in range(1, 302):
    temp = {'name': "wang" + str(i), 'email': 'wang' + str(i) + '@qq.com', 'pwd': 'pwd' + str(i)}
    user_list.append(temp)
print(user_list)

page = input("请输入页面页码：")
page = int(page)
start = (page - 1) * 10
end = page * 10
result = user_list[start: end]
for m in result:
    print(m)



q=10
for  i  in range(0,10):
    m=q-i
    n=2*i+1
    print(' '*m,'*'*n)


