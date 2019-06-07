#!/user/bin/env  python
# -*- coding:utf-8 -*-
# 集合：1.不同元素组成
#       2.无序
#       3.集合中元素必须是不可变元素
s = set('hello')
print(s)  # {'l', 'e', 'h', 'o'}

s = set(['deany', 'deany', 'hello'])
print(s)  # {'hello', 'deany'}

# 1.添加，只能更新一个值
s = {1, 23, 4, 5, 6, 7}
s.add('4')
print(s)  # {1, 4, 5, 6, 7, 23, '4'}
s.add(4)
print(s)  # {1, 4, 5, 6, 7, 23, '4'}

# 2.清除
s.clear()
print(s)  # set()

# 3.拷贝
s = {1, 23, 4, 5, 6, 7}
s1 = s.copy()
print(s1)  # {1, 4, 5, 6, 7, 23}

# 4.删除
s = {1, 'sb', 23, 4, 5, 6, 7, 'pop', 'd'}
v = s.pop()  # 随机删
print(v, s)  # 1 {4, 5,'sb', 6, 7, 'd', 'pop', 23}无序删除
s.remove('d')  # 指定删除，不存在的元素会报错
print(s)  # {4, 5, 6, 7, 'sb', 23, 'pop'}
s.discard('sbbbb')  # 指定删除，不存在的元素不会报错
print(s)

#
python = ['sb', 'wangmou', 'deany', 'sb']
linux = ['sb', 'wangmou', 'diudiu']
p_s = set(python)
l_s = set(linux)
print(p_s, l_s)
print('求交集:', p_s.intersection(l_s))  # 求交集
print('求交集:', p_s & l_s)  # 求交集
print('求并集:', p_s.union(l_s))  # 求并集
print('求并集:', p_s | l_s)  # 求并集
print('求差集:', p_s - l_s)  # 求差集
print('求差集:', p_s.difference(l_s))  # 求差集
print('交叉补集：', p_s.symmetric_difference(l_s))  # 求交叉补集
print('交叉补集：', p_s ^ l_s)  # 求交叉补集
p_s.symmetric_difference_update(l_s)
print('交叉补集：', p_s)  # 求交叉补集

s1 = {1, 2}
s2 = {3, 4}
print(s1.isdisjoint(s2))  # 如果s1与s2没有元素相同则返回True，反之False

s3 = {2, 3}
s4 = {1, 2, 3, 4}
print(s3.issubset(s4))  # 判断s3是否是s4的子集
print(s3.issuperset(s4))  # 判断s3是否是s4的父集

s5 = {2, 3}
s6 = {1, 2, 3, 4}
s5.update(s6)
print(s5)  # 更新多个值

s = frozenset('hello')  # 不可变集合
print(s)
